from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd 
from datetime import date 
import PyPDF2
import re
import tabula
import jpype
import fitz  # PyMuPDF
from tabula import read_pdf
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime



# Configuração do WebDriver
def inicializar_webdriver():
    driver = webdriver.Safari()
    driver.get('''https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/boletim-diario/boletim-diario-do-mercado/''')
    driver.maximize_window()
    return driver

# Navegar até a página e aguardar o iframe
def navegar_pagina(driver):
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "bvmf_iframe")))

# Selecionar a Data no Calendário
def selecionar_data(driver, data, xpaths_por_data):
    time.sleep(10)
    botaoCalendar = driver.find_element('xpath','//*[@id="root"]/div/div[1]/div/div/div[2]/div[3]/duet-date-picker/div/div[1]/button')
    driver.execute_script("arguments[0].click();", botaoCalendar)
    xpath_dia = xpaths_por_data.get(data)
    if xpath_dia:
        botaodia = driver.find_element('xpath', xpath_dia)
        driver.execute_script("arguments[0].click();", botaodia)
    else:
        print("Data não mapeada no dicionário.")
        driver.quit()
        raise ValueError("Data fornecida não está mapeada no dicionário de XPaths.")

# Expandir e Baixar o PDF
def expandir_baixar_pdf(driver):
    botoExpandir = driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div/div/div[3]/ul/li[2]/a')
    driver.execute_script("arguments[0].click();", botoExpandir)
    botaoPdf = driver.find_element('xpath','//*[@id="root"]/div/div[1]/div/div/div[3]/ul/li[2]/div/div[1]/div/div[2]/p/a')
    driver.execute_script("arguments[0].click();", botaoPdf)
    driver.implicitly_wait(10)
    time.sleep(5)

# Processar o PDF
def processar_pdf(data):
    caminho_jvm = '/Users/pontoapple/Library/Java/JavaVirtualMachines/openjdk-20.0.1/Contents/Home/lib/server/libjvm.dylib'
    if not jpype.isJVMStarted():
        jpype.startJVM(caminho_jvm)

    nome_arquivo = f'//Users/pontoapple/Downloads/BDI_00_{data}.pdf'
    tabelas_selecionadas = []  
    paginas_desejadas = [9, 10, 11]
    try:
        tabelas = tabula.read_pdf(nome_arquivo, pages=paginas_desejadas)
        for tabela in tabelas:
            if 'Ação.1' in tabela.columns:
                tabelas_selecionadas.append(tabela)
                # Remover a linha abaixo, ela não é mais necessária
                # tabelas_selecionadas = tabelas_selecionadas[0]
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    
    return tabelas_selecionadas
def processar_tabelas_altas_baixas(tabelas_selecionadas):
    index_to_split = tabelas_selecionadas.columns.get_loc('Ação.1')
    df_altas = tabelas_selecionadas.iloc[:, :index_to_split]
    df_baixas = tabelas_selecionadas.iloc[:, index_to_split:]
    
    # Formatar df_altas
    if len(df_altas.columns) == 5:
        df_altas.columns = ['Maiores Altas', 'Tipo', '', 'Preço R$', 'Osciação']
        df_altas = df_altas.drop('', axis=1)
    elif len(df_altas.columns) == 4:
        df_altas.columns = ['Maiores Altas', 'Tipo', 'Preço R$', 'Osciação']
    
    # Formatar df_baixas
    if len(df_baixas.columns) == 5:
        df_baixas.columns = ['Maiores baixas', 'Tipo', '', 'Preço R$', 'Osciação']
        df_baixas = df_baixas.drop('', axis=1)
    elif len(df_baixas.columns) == 4:
        df_baixas.columns = ['Maiores baixas', 'Tipo', 'Preço R$', 'Osciação']
    
    # Extrai as listas como antes
    lista_altas = df_altas['Maiores Altas']
    lista_baixas = df_baixas['Maiores baixas']
    
    # Usa pd.concat para juntar as duas listas
    lista_unida = pd.concat([lista_altas, lista_baixas], ignore_index=True)
    
    # Opcional: remove duplicatas se você deseja apenas valores únicos
    lista_unida = lista_unida.drop_duplicates()
    
    # Converte para uma lista Python (opcional, dependendo do que você precisa fazer com os dados)
    lista = lista_unida.tolist()
    print(lista)
    return lista, df_altas, df_baixas

def extrair_tabelas_por_texto(data, lista):
    # Abre o arquivo PDF
    pdf_document = fitz.open(f'//Users/pontoapple/Downloads/BDI_00_{data}.pdf')
    
    # Lista para armazenar as tabelas extraídas
    extracted_tables = []
    
    # Pesquisa cada texto da lista em cada página do PDF e extrai tabelas onde o texto é encontrado
    for search_text in lista:
        for current_page in range(96, 168):  # Assumindo que você quer verificar apenas essas páginas
            page = pdf_document.load_page(current_page)
            text_instances = page.search_for(search_text)
    
            # Se encontrou o texto na página, extrai as tabelas dessa página
            if text_instances:
                tables = read_pdf(f'//Users/pontoapple/Downloads/BDI_00_{data}.pdf', 
                                  pages=str(current_page + 1), 
                                  multiple_tables=True,
                                  silent=True)  # silent=True para evitar mensagens de log
    
                # Adiciona todas as tabelas encontradas na página ao resultado
                extracted_tables.extend(tables)  # Aqui foi corrigido de append para extend
    
    # Fecha o documento PDF
    pdf_document.close()
    
    return extracted_tables

def processar_resultados_busca(tabelas_extradas, lista):
    # Lista para armazenar os resultados
    results = []

    # Percorre cada tabela extraída
    for table_index, table in enumerate(tabelas_extradas):
        # Para cada elemento na lista
        for element in lista:
            # Usa isin para verificar se o elemento está em alguma das colunas da tabela
            mask = table.isin([element])
            # Verifica se alguma das linhas tem 'True' (ou seja, o elemento foi encontrado)
            if mask.any(axis=1).any():
                # Usa o mask para filtrar as linhas onde o elemento está presente
                rows_with_element = table[mask.any(axis=1)]
                result = {
                    'element': element,
                    'table_index': table_index,
                    'rows_with_element': rows_with_element
                }
                results.append(result)
    
    return results

def processar_dfs_encontrados(tabelas_extradas, lista):
    # Lista para armazenar os DataFrames de linhas onde os elementos foram encontrados
    dfs_with_element = []

    # Percorre cada tabela extraída
    for table_index, table in enumerate(tabelas_extradas):
        # Para cada elemento na lista
        for element in lista:
            # Usa isin para verificar se o elemento está em alguma das colunas da tabela
            mask = table.isin([element])
            # Verifica se alguma das linhas tem 'True' (ou seja, o elemento foi encontrado)
            if mask.any(axis=1).any():
                # Usa o mask para filtrar as linhas onde o elemento está presente
                # .copy() garante que você obtém uma cópia independente, não uma visualização
                rows_with_element = table[mask.any(axis=1)].copy()
                # Usa .loc para fazer atribuições de uma forma que evita o SettingWithCopyWarning
                rows_with_element.loc[:, 'element'] = element
                rows_with_element.loc[:, 'table_index'] = table_index
                # Armazena o DataFrame modificado
                dfs_with_element.append(rows_with_element)

    # Concatena todos os DataFrames encontrados em um único DataFrame
    results_df = pd.concat(dfs_with_element, ignore_index=True)
    results_df.columns = ['Código', 'Empresa/Ação','Tipo','NM', 'Abertura', 'Mínimo', 'Máximo', 'Médio', 'Fechamento', 'Oscilação (%)',
                          'Compra (R$)Venda (R$)' ,'Numero/Quantidade', '.','Index']# Exibe o Da
    return results_df
def salvar_dfs_no_banco(user, senha, banco_de_dados, host, porta, resultados_df, df_altas, df_baixas):
    # Estabelece a conexão com o banco de dados
    conexao = create_engine(f"mysql+pymysql://{user}:{senha}@{host}:{porta}/{banco_de_dados}")

    # Obter a hora atual para criar um nome de tabela único
    timestamp_atual = datetime.now().strftime('%Y%m%d%H%M%S')
    
    # Nome das tabelas com timestamp para torná-las únicas
    nome_tabela_resultados = f'auxiliar_destaque9_{timestamp_atual}'
    nome_tabela_altas = f'Altas9_{timestamp_atual}'
    nome_tabela_baixas = f'baixas9_{timestamp_atual}'

    # Salva os DataFrames no banco de dados com nomes de tabelas únicos
    resultados_df.to_sql(nome_tabela_resultados, conexao, if_exists='fail', index=False)
    df_altas.to_sql(nome_tabela_altas, conexao, if_exists='fail', index=False)
    df_baixas.to_sql(nome_tabela_baixas, conexao, if_exists='fail', index=False)
    print("Tabelas criadas com sucesso.")
# Função principal
def main(data):
    xpaths_por_data = {
    '20240102':'//*[@id="ui-datepicker-div"]/div/table/tbody/tr[1]/td[2]/button',
    '20240103':'//*[@id="ui-datepicker-div"]/div/table/tbody/tr[1]/td[3]/button',
    '20240104':'//*[@id="ui-datepicker-div"]/div/table/tbody/tr[1]/td[4]/button',
    '20240105':'//*[@id="ui-datepicker-div"]/div/table/tbody/tr[1]/td[5]/button',
    '20240108': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[2]/td[1]/button',
    '20240109': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[2]/td[2]/button',
    '20240110': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[2]/td[3]/button',
    '20240111': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[2]/td[4]/button',
    '20240112': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[2]/td[5]/button',
    '20240115': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[3]/td[1]/button',  
    '20240116': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[3]/td[2]/button',
    '20240117': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[3]/td[3]/button', 
    '20240118': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[3]/td[4]/button', 
    '20240119': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[3]/td[5]/button', 
    '20240122': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[4]/td[1]/button', 
    '20240123': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[4]/td[2]/button', 
    '20240124': '///*[@id="ui-datepicker-div"]/div/table/tbody/tr[4]/td[3]/button', 
    '20240125': '//*[@id="ui-datepicker-div"]/div/table/tbody/tr[4]/td[4]/button', 
    }
    
  

    driver = inicializar_webdriver()
    navegar_pagina(driver)
    selecionar_data(driver, data, xpaths_por_data)
    expandir_baixar_pdf(driver)
    driver.quit()
    
    tabelas_encontradas = processar_pdf(data)
    if tabelas_encontradas:  # Verifica se a lista não está vazia
        if len(tabelas_encontradas) > 0:  
            tabela_selecionada = tabelas_encontradas[0]
            lista, df_altas, df_baixas = processar_tabelas_altas_baixas(tabela_selecionada)

            
            # Extrai tabelas do PDF baseadas na lista de textos de busca
            tabelas_extradas = extrair_tabelas_por_texto(data, lista)
            
            # Processa os DataFrames onde os elementos foram encontrados e concatena em um único DataFrame
            resultados_df = processar_dfs_encontrados(tabelas_extradas, lista)
            
            # Chama a função para salvar os DataFrames no banco de dados
            salvar_dfs_no_banco('root', 'Vt644510', 'ghia', 'localhost', 3306, resultados_df, df_altas, df_baixas)

# Rodar o script
data = input("Digite a data no formato AAAAMMDD: ")
main(data)
