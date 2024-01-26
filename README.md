# Documentação Desafio Ghia

Avaliação do Desafio Ghia.


## Funcionalidades

- **Extração Automatizada de Dados**: O programa acessa automaticamente o site da B3, seleciona e baixa o arquivo PDF do boletim diário do mercado para a data especificada pelo usuário.
- **Processamento e Análise de Dados**: Após o download do arquivo, o sistema processa e extrai as tabelas principais das maiores altas e baixas do dia.
- **Pesquisa Detalhada**: O programa então realiza uma busca detalhada por mais informações sobre essas empresas no PDF, especificamente entre as páginas 96 e 168.
- **Consolidação de Dados**: Todos os dados extraídos são consolidados em tabelas estruturadas para análise.
- **Integração com Banco de Dados**: As tabelas geradas são automaticamente carregadas em um banco de dados SQL, permitindo uma gestão eficiente e a realização de consultas complexas.

## Requisitos do Sistema

- **Python**: É necessário ter a última versão do Python instalada.
- **Bibliotecas**: As bibliotecas Selenium, Pandas, Tabula, SQLAlchemy e Datetime devem estar instaladas.
- **Navegador Safari**: O sistema foi desenvolvido para funcionar com o navegador Safari.
- **Caminho do PDF**: O usuário deve especificar o caminho base para o download e processamento do arquivo PDF.

## Instruções de Uso

1. **Preparação do Ambiente**:
   - Certifique-se de que todas as bibliotecas necessárias estão instaladas.
   - Verifique se a última versão do Python está instalada.
   - Configure o caminho base para o download do arquivo PDF.

2. **Execução do Programa**:
   - Execute o arquivo `main.py` para iniciar o processo.
   - Quando solicitado, escolha um dia útil do mês de janeiro para análise.
   - O sistema irá automaticamente acessar o site da B3, baixar o arquivo PDF do dia escolhido e iniciar o processamento dos dados.

3. **Análise dos Dados**:
   - Após o processamento, as tabelas geradas estarão disponíveis no banco de dados SQL conectado.

OBS: O Dash acho que está com uma pequena falha mas ainda esse final de semana consigo consertar, atualizo aqui 
  
Email: vitorpereirathomee@gmail.com



