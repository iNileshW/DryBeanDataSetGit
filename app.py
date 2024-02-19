import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Output, Input
from dash import Patch, clientside_callback
#from dash_bootstrap_templates import load_figure_template
import plotly.io as pio

# df=pd.read_csv(r'C:\Users\Monicca2502\Documents\Nilesh\AI\Pandas\Projects\DryBeanDataSetProject\data\Dry_Bean_Dataset_csv.csv')
#BootstapCSS:
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#Cyborg CSS:
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


# Initialize the app with constructor
app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME]
           )
server = app.server
# App layout
app.layout=html.Div([
html.H1('Dry Bean Data Set Dashboard for Models'),
html.Div(
    [html.Div(
        dcc.Link(f"{page['name']}-{page['path']}",       
        href=page['relative_path'])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container,    
])

# Run the app
if __name__ == '__main__':
    app.run_server(port=8040,debug=True)    