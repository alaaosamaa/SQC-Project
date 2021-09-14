import mysql.connector
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database = "SQC"
)
mycursor = mydb.cursor()


df = pd.read_sql("SELECT analyzer_name, analyzer_code FROM Analyzer WHERE analyzer_output = 'output2'", mydb)
app_name = 'dash-mysqldataplot'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'MYSQL + Dash'
trace = go.Bar(x=df.analyzer_name, y=df.analyzer_code, name='analyzer_name')

app.layout = html.Div(children=[html.H1("MYSQL + Dash", style={'textAlign': 'center'}),
	dcc.Graph(
		id='example-graph',
		figure={
			'data': [trace],
			'layout':
			go.Layout(title='MySQL SQC', barmode='stack')
		})
], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)