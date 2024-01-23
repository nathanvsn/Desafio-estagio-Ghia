# Teste Prático para Estágio em Banco de Dados e SQL

## Objetivo: 
Extrair e analisar dados da base aberta da CETIP/B3, focando em maiores altas e baixas do mercado, e armazená-los em um servidor local usando SQL.

## Instruções Detalhadas:

### Utilização da Base de Dados Aberta da CETIP/B3:
Acesse a base aberta da CETIP/B3 https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/boletim-diario/boletim-diario-do-mercado/

### 1. Extração de Dados com Inputs Dinâmicos:
Implemente entrada de dados (data de início e fim) para o período de análise.
Extraia dados das "Ações do IBOVESPA - Maiores Altas e Baixas" da página 10.

### 2. Extração de Dados Detalhados:
Extraia dados detalhados apenas das ações de destaque(página 10) disponíveis nas páginas 96 a 506.

### 3. Desenvolvimento de Consultas SQL:
Crie uma consulta SQL para a tabela "Destaque", incorporando dados do passo 1.
Desenvolva uma consulta SQL para "auxiliar_destaque" com dados do passo 2.

### 4. Relacionamento entre Tabelas:
Elabore uma consulta SQL estabelecendo relacionamento entre "Destaque" e "auxiliar_destaque".

### 5. Visualização Integrada:
Crie um viewer para apresentar informações integradas das tabelas "Destaque" e "auxiliar_destaque".

## Entregáveis:

### 1.querys.sql 
#### Crie um arquivo querys.sql com os seguintes itens:
1. Consultas SQL para Criação de Tabelas:
2. Inclua scripts SQL para a criação das tabelas "Destaque" e "auxiliar_destaque".
3. Forneça a consulta SQL que relaciona as tabelas "Destaque" e "auxiliar_destaque".

### 2.Pasta_codigo
#### Crie uma pasta "Pasta_codigo" com os seguinte itens:
1. Codigos python separados ou não por modulos sendo o principal como "main.py"
Documentação de cada etapa do processo.


# Objetivo Geral:
Este desafio tem como finalidade avaliar e desenvolver competências cruciais para a função de estagiário em Banco de Dados e SQL, alinhadas às necessidades operacionais e estratégicas da nossa empresa. Os participantes serão desafiados a demonstrar habilidades em extração automática de dados e gerenciamento eficiente de bases de dados SQL, competências essenciais para o sucesso em nosso ambiente de trabalho dinâmico e orientado a dados.

# Escopo do Desafio:
O desafio consiste em uma série de tarefas que simulam cenários reais enfrentados em nossa operação diária, exigindo do candidato não apenas conhecimento técnico, mas também capacidade analítica e habilidade para resolver problemas. As tarefas abrangem desde a extração automatizada de dados de fontes abertas até o armazenamento, manipulação e visualização desses dados em um sistema de gerenciamento de banco de dados SQL.

# Especificações Técnicas:

## Extração de Dados:

Implementação de um sistema automatizado para extração de dados, enfatizando a eficiência e a precisão na captura de informações.
## Manuseio de Banco de Dados SQL:

Demonstração de proficiência no uso de SQL para armazenar, consultar e manipular dados, com um foco especial na integridade e segurança dos dados.
## Visualização e Análise de Dados:

Capacidade de criar visualizações claras e informativas, facilitando a análise e a tomada de decisão baseada em dados.
## Resultados Esperados:

### Competência Técnica: 
Demonstração clara de habilidades técnicas em SQL e em ferramentas de extração de dados.
### Resolução de Problemas: 
Habilidade para identificar e solucionar desafios práticos relacionados à gestão de dados.
### Inovação e Criatividade: 
Aplicação de abordagens inovadoras e criativas na manipulação e apresentação de dados.
### Documentação e Comunicação:
Capacidade de documentar o processo de forma clara e concisa, evidenciando o raciocínio por trás das escolhas técnicas.

# Processo de Avaliação:
Os candidatos serão avaliados com base na precisão técnica, eficiência, criatividade e clareza na documentação de suas soluções. A avaliação final considerará a adequação das soluções às necessidades operacionais da empresa e a capacidade do candidato de trabalhar de forma eficaz com dados complexos.
