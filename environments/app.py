from dash import Dash, dash_table, dcc, html, Input, Output, callback
import pandas as pd
import dash_bootstrap_components as dbc
# Need to use Python 3.8 or higher and Dash 2.2.0 or higher

# Read data
df =pd.read_csv("Sample Superstore.csv")

# Start app
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([
    dcc.Markdown('# Titel', style={'textAlign':'center'}),

    dbc.Label("Show number of rows"),
    row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),

    my_table := dash_table.DataTable(
        columns=[
            {'name': 'Long Name', 'id': 'Long Name', 'type': 'text'},
            {'name': 'Share of KPI', 'id': 'Share of KPI', 'type': 'numeric'},
            {'name': 'KPI', 'id': 'KPI', 'type': 'numeric'}
        ],
        data=df.to_dict('records'),
        filter_action='native',
        page_size=10,

        style_data={
            'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        }
    ),
    dbc.Row([
        dbc.Col([
            continent_drop := dcc.Dropdown([x for x in sorted(df.ACG.unique())])
        ], width=3),
        dbc.Col([
            country_drop := dcc.Dropdown([x for x in sorted(df.CG.unique())], multi=True)
        ], width=3)

    ], justify="between", className='mt-3 mb-4'),

])