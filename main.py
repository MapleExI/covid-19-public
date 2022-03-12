from src.bigquery_connection import bigquery_connector
from src.graph_builder import graph
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

#create the layout
app.layout = html.Div([
    html.H4('COVID-19 INFORMATION'),
    html.P("Select data type:"),
    dcc.Dropdown(["Confirmed", "Deceased", "Recovered"], "Confirmed", id='DataType'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("DataType", "value"))


def __main__(datatype):
    con = bigquery_connector() #create bigquery connection with credentials
    con.read_table() #read dataset from google open covid-19 information
    data = con.get_data()
    g = graph(data,datatype) #initialize graph class with datasets and chosen data type
    return g.create_figure() #create the graph

if __name__ == '__main__':
    app.server(host='0.0.0.0', port=8080, debug=True)

