import dash
from dash import Dash, dcc, html, callback, Output, Input
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from dash import dash_table

dash.register_page(__name__,order=5)
prediction_dt=pd.read_csv(r"C:\Users\Monicca2502\Documents\Nilesh\AI\Pandas\Projects\DryBeanDataSetGit\prediction_dt.csv")
prediction_rf=pd.read_csv(r"C:\Users\Monicca2502\Documents\Nilesh\AI\Pandas\Projects\DryBeanDataSetGit\prediction_rf.csv")
prediction_lgbm=pd.read_csv(r"C:\Users\Monicca2502\Documents\Nilesh\AI\Pandas\Projects\DryBeanDataSetGit\prediction_lgbm.csv")

# Define the app layout
layout = html.Div([
    #RF DataTable
    html.H1("Data and Classification Report Viewer For LGBM"),
    dash_table.DataTable(        
        id='data-table_rf',
        columns=[{'name': col, 'id': col} for col in prediction_rf.columns],
        #data=prediction.to_dict('records')

        data=prediction_dt.head(5).to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto', 'overflowX': 'auto'},   # Add horizontal scroll bar
        style_cell={'maxWidth': 0}  #
    ),
    # RF Classification Report
    html.Div([
        html.H1("Classification Report for LGBM"),
        html.Pre(
            children=classification_report(prediction_dt["Actual"], prediction_rf["prediction"]),
            style={'whiteSpace': 'pre-wrap'}
        )
    ]),

    html.H1("Data and Classification Report Viewer For Decision Table"),
    #DT DataTable
    # DataTable to display first few rows of the DataFrame
    dash_table.DataTable(
        style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'lineHeight': '15px'
    },     
        id='data-table_dt',
        columns=[{'name': col, 'id': col} for col in prediction_dt.columns],
        #data=prediction.to_dict('records')
        data=prediction_dt.head(5).to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto', 'overflowX': 'auto'},   # Add horizontal scroll bar
        style_cell={'maxWidth': 0}  #
    ),

    # DT Classification Report
    html.H1("Classification Report for Decision Table"),
    html.Div([        
        html.Pre(
            children=classification_report(prediction_dt["Actual"], prediction_dt["prediction"]),
            style={'whiteSpace': 'pre-wrap'}
        )
    ]),

    #RF DataTable
    html.H1("Data and Classification Report Viewer For Random Forester"),
    dash_table.DataTable(        
        id='data-table_rf',
        columns=[{'name': col, 'id': col} for col in prediction_rf.columns],
        #data=prediction.to_dict('records')

        data=prediction_dt.head(5).to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto', 'overflowX': 'auto'},   # Add horizontal scroll bar
        style_cell={'maxWidth': 0}  #
    ),
    # RF Classification Report
    html.Div([
        html.H1("Classification Report for Random Forester"),
        html.Pre(
            children=classification_report(prediction_dt["Actual"], prediction_rf["prediction"]),
            style={'whiteSpace': 'pre-wrap'}
        )
    ])
])

# Run the app
# if __name__ == '__main__':
#     app.run_server(port=8040,debug=True)
