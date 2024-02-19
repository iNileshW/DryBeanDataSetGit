import dash
from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from data import X_train, X_val, y_train, y_val, df

#Decision Tree
clf = DecisionTreeClassifier(random_state=42)
#fit
clf.fit(X_train, y_train)
#predict
y_pred = clf.predict(X_val)
X_val["Actual"]=y_val
X_val["prediction"]=y_pred
#Create Prediction File
X_val.to_csv(r"C:\Users\Monicca2502\Documents\Nilesh\AI\Pandas\Projects\DryBeanDataSetGit\prediction_dt.csv",index=False)

feature_importance = clf.feature_importances_
feature_importance_df = pd.DataFrame({"Feature": X_train.columns, "Importance": feature_importance})
feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=True)
columns=list(feature_importance_df.Feature.tail(20))

dash.register_page(__name__,order=2)
# Initialize the Dash app
# app = dash.Dash(__name__)

# Define the app layout
# app.
layout = html.Div([
    html.H1("Decision Table Histogram Viewer for Dry Bean Data Set"),    
    # Dropdown to select column for histogram
    dcc.Dropdown(
        id='column-dropdown_hist_dt',
        options=[{'label': col, 'value': col} for col in columns],
        value=columns[0],  # Default selected column
        style={'width': '50%'}
    ),
    #Histogram Graph Output   
    dcc.Graph(id='histogram-graph_dt'),
    # Dropdown to select column
    dcc.Dropdown(
        id='column-dropdown_box_dt',
        options=[{'label': col, 'value': col} for col in columns],
        value=columns[0],  # Default selected column
        style={'width': '50%'}
    ),   
    #Box Graph Output
    dcc.Graph(id='box-graph_dt'),
])

# Define callback to update the graph based on column selection
# @app.
@callback(
    Output('histogram-graph_dt', 'figure'),
    [Input('column-dropdown_hist_dt', 'value')]
)
def update_graph(selected_column):
    # Create histogram using Plotly Express
    fig = px.histogram(df, x=selected_column,color="Class", nbins=30)

    # Update layout
    fig.update_layout(
        title=f'Histogram for {selected_column}',
        xaxis_title=selected_column,
        yaxis_title='Frequency',
        bargap=0.1  # Set gap between bars
    )
    return fig

# Define callback to update the graph based on column selection
# @app.
@callback(
    Output('box-graph_dt', 'figure'),
    [Input('column-dropdown_box_dt', 'value')]
)

def update_graph(selected_column):
    # Create box plot with points using Plotly Express
    fig = px.box(df, x=selected_column, points='all', color="Class")
    # Update layout
    fig.update_layout(
        title=f'Box Plot with Points for {selected_column}',
        xaxis_title=selected_column,
        yaxis_title='Values',
        boxmode='group'  # Display boxes in groups
    )
    return fig

# Run the app
# if __name__ == '__main__':
#     app.run_server(port=8040,debug=True)
