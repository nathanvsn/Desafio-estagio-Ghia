# Teste Prático para Estágio em Banco de Dados e SQL

## Instruções:
- Faça um fork deste repositório;
- O conjunto mínimo de tecnologias a serem utilizadas são: SQL e Python
- Crie um passo a passo de como rodar a sua aplicação;
- Após finalizar, submeta um pull request com um comentário informando o seu e-mail de contato e aguarde nossa avaliação.

## Objetivo: 
Este desafio tem como finalidade avaliar e desenvolver competências cruciais para a função de estagiário em Banco de Dados e SQL, alinhadas às necessidades operacionais e estratégicas da nossa empresa. Os participantes serão desafiados a demonstrar habilidades em extração automática de dados e gerenciamento eficiente de bases de dados SQL, competências essenciais para o sucesso em nosso ambiente de trabalho dinâmico e orientado a dados.

## Instruções Detalhadas:

### Utilização da Base de Dados Aberta da CETIP/B3:
Acesse a base aberta da CETIP/B3 https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/boletim-diario/boletim-diario-do-mercado/

### 1. Extração de Dados com Inputs Dinâmicos:
- Implemente entrada de dados (data de início e fim) para o período de análise.
- Extraia dados das "Ações do IBOVESPA - Maiores Altas e Baixas" da página 10.

### 2. Extração de Dados Detalhados:
- Extraia dados detalhados apenas das ações de destaque (página 10) disponíveis nas páginas 96 a 162.

### 3. Desenvolvimento de Consultas SQL:
- Crie uma consulta SQL para a tabela "Destaque", incorporando dados do passo 1.
- Desenvolva uma consulta SQL para "auxiliar_destaque" com dados do passo 2.

### 4. Relacionamento entre Tabelas:
- Elabore uma consulta SQL estabelecendo relacionamento entre "Destaque" e "auxiliar_destaque".

### 5. Visualização Integrada:
- Crie um viewer para apresentar informações integradas das tabelas "Destaque" e "auxiliar_destaque".

### OBS:
- Todos os dados e operações relacionadas ao desafio devem ser implementados em um servidor PostgreSQL local. Utilize a seguinte configuração padrão para a conexão: postgresql://postgres:postgres@localhost:5432/postgres

## Entregáveis:

### 1.querys.sql 
#### Crie um arquivo querys.sql com os seguintes itens:
- Consultas SQL para Criação de Tabelas:
- Inclua scripts SQL para a criação das tabelas "Destaque" e "auxiliar_destaque".
- Forneça a consulta SQL que relaciona as tabelas "Destaque" e "auxiliar_destaque".

### 2.Pasta_codigo
#### Crie uma pasta "Pasta_codigo" com os seguinte itens:
- Codigos python, separados ou não por modulos sendo o principal como "main.py"
- Documentação de cada etapa do processo.

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
