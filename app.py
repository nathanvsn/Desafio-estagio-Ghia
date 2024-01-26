# Importar as bibliotecas necessárias
import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from main import processar_tabelas_altas_baixas  

# Coletar a data do usuário na linha de comando20
data_usuario = input("Insira a data (AAAAMMDD): ")

# Processar os dados usando a data inserida pelo usuário
resultados_df, df_altas, df_baixas = processar_tabelas_altas_baixas(data_usuario)

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definir o layout da aplicação
app.layout = dbc.Container(fluid=True, children=[
    html.H1("Dashboard "),
    
    html.H2("Resultados"),
    dash_table.DataTable(
        id='tabela-resultados',
        columns=[{"name": i, "id": i} for i in resultados_df.columns],
        data=resultados_df.to_dict('records'),
        style_table={'overflowX': 'auto'},
    ),
    
    html.H2("Maiores Altas"),
    dash_table.DataTable(
        id='tabela-altas',
        columns=[{"name": i, "id": i} for i in df_altas.columns],
        data=df_altas.to_dict('records'),
        style_table={'overflowX': 'auto'},
    ),
    
    html.H2("Maiores Baixas"),
    dash_table.DataTable(
        id='tabela-baixas',
        columns=[{"name": i, "id": i} for i in df_baixas.columns],
        data=df_baixas.to_dict('records'),
        style_table={'overflowX': 'auto'},
    ),
])

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
