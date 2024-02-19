import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
dash.register_page(__name__,path='/',order=1)
# Initialize the Dash app
# app = dash.Dash(__name__)

# Define the app layout
# app.
layout = html.Div([    
    # html.Div([
    #     html.Div(
    #         dcc.Link(f"{page['name']}-{page['path']}",
    #                  href=page["relative_path"])
    #     ) for page in dash.page_registry.values()
    # ]),
    # dash.page_container,
    dbc.Button("Primary", color="primary", className="me-1"),
        dbc.Button("Secondary", color="secondary", className="me-1"),
        dbc.Button("Success", color="success", className="me-1"),
        dbc.Button("Warning", color="warning", className="me-1"),
        dbc.Button("Danger", color="danger", className="me-1"),
        dbc.Button("Info", color="info", className="me-1"),
        dbc.Button("Light", color="light", className="me-1"),
        dbc.Button("Dark", color="dark", className="me-1"),
        dbc.Button("Link", color="link"),
         dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
])