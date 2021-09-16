from os import terminal_size
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_bootstrap_components import themes
from dash_bootstrap_components._components.Button import Button
from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.NavItem import NavItem
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import csv
from datetime import date
import dash_table
import pandas as pd
from datetime import datetime as dt
import plotly.express as px
import numpy as np
import plotly.graph_objs as go
from sklearn import datasets
import mysql.connector
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import math
import statistics
import pandas
from uncertainties import ufloat


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="SQC"
)
mycursor = mydb.cursor()


# Read data
iris_raw = datasets.load_iris()
iris = pd.DataFrame(iris_raw["data"], columns=iris_raw["feature_names"])
# df = pd.read_sql("SELECT analyzer_name, analyzer_code FROM Analyzer WHERE analyzer_output = 'output2'", mydb)

# Create random data
Sample1 = np.random.randint(15, 20, size=100)
Sample2 = np.random.randint(11, 17, size=100)


# Array of table attributes
# tableCols = ['Mean', 'SD', 'CV', 'MU measurments', 'EWMA',
#              'CUSUM', 'Target Mean', 'Actual Mean', 'Target SD', 'Actual SD']
tableCols = ['Mean', 'SD', 'CV', 'EWMA']
# tableCols = [df.analyzer_name[0],df.analyzer_name[1], df.analyzer_name[2]]

# Array of table values
tableValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Array of table rows
tableRows = [
    html.Tr([html.Td(i) for i in tableCols]), html.Tr(
        [html.Td(i) for i in tableValues])
]

# Main Application page
app = dash.Dash('Hello World', external_stylesheets=[
                dbc.themes.MINTY, dbc.themes.BOOTSTRAP])

# App Logo image
Logo = "https://icon-library.com/images/graphs-icon/graphs-icon-4.jpg"


# --------------------------------------------------------------Calculations---------------------------------------

# Computing mean for array of data 
def Data_Mean(dataArray):
    return statistics.mean(dataArray)


# Computing standard deviation for array of data
def Data_SD(dataArray):
    return round(statistics.stdev(dataArray),1) 


# calculate pooled standard deviation (SD)
def Booled_SD(dataArray1,dataArray2):
    n1, n2 = len(dataArray1),len(dataArray2)
    dataArray1_SD, dataArray2_SD = Data_SD(dataArray1) ,Data_SD(dataArray2)
    pooled_standard_deviation = math.sqrt(((n1 - 1)*dataArray1_SD * dataArray1_SD +(n2-1)*dataArray2_SD * dataArray2_SD) / (n1 + n2-2))
    return round(pooled_standard_deviation,1)

# Calculate Coefficient of Variation for data array(CV)
def Data_CV(dataArray):
    dataArray_Mean = Data_Mean(dataArray)
    dataArray_SD = Data_SD(dataArray)
    return round((dataArray_SD/dataArray_Mean)*100,1)

# Calculate Measurments Uncertainty (MU)
def Data_MU(dataArray):
    dataArray_Mean = Data_Mean(dataArray)
    return ufloat(dataArray_Mean,0.01)

# Compute the Calculate the Exponentially weighted moving average (EWMA)
def Data_EWMA(dataArray):
#   EWMA = pd.DataFrame.ewm(dataArray)
  return 1

# Calculate Cumulative Sum of data array (CUSUM)
def Data_CUSUM(dataArray):
    
    return np.cumsum(dataArray)


# Calculate all and return an array of all statistical calculations 
def Calculate_All(dataArray):
   dataArray_Mean = Data_Mean(dataArray)
   dataArray_SD = Data_SD(dataArray)
   dataArray_CV = Data_CV(dataArray)
#    dataArray_MU = Data_MU(dataArray)
   dataArray_EWMA = Data_EWMA(dataArray)
#    dataArray_CUSUM = Data_CUSUM(dataArray)
   Calculations_Array = [dataArray_Mean, dataArray_SD, dataArray_CV, dataArray_EWMA]
   return Calculations_Array



# ----------------------------------------------------------Page Components---------------------------------------------------

# Space components
space = dbc.Row("  ", style={"height": "10px"})

# Mini space
miniSpace = dbc.Row("  ", style={"height": "5px"})

# Cards shadow
cardShadow = ["shadow-sm p-3 mb-5 bg-white rounded", {"margin-top": "-2em"}]

# Card to select period of time for data to plot it
Duration = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Col([
                    dbc.Label('Priod Of Time'),
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        start_date_placeholder_text="Start Period",
                        end_date_placeholder_text="End Period",
                        calendar_orientation='vertical',

                    ),
                    dbc.Col(space),
                    html.Div(id='output-container-date-picker-range',)
                ]),
            ], row=True,
        ),
    ],
    body=True,
    className=cardShadow[0],

)

# Card to select Analyzer name and code of the data
Analyzer_control = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label('Analyzer'),
                dbc.Col(space),
                dcc.Dropdown(
                    id='Analyzer_Code',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="Analyzer_code",
                    multi=True,
                    placeholder='Select Analyzer Code'
                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='Analyzer_Name',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="Analyzer_Name",
                    multi=True,
                    placeholder='Select Analyzer Name'
                ),
            ],
        ),
    ],
    body=True,
    className=cardShadow[0],
    style=cardShadow[1]
)

# Card to select Test code , name and reagent lot number
Test_control = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label('Test'),
                dcc.Dropdown(
                    id='Test_Code',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="Test_code",
                    multi=True,
                    placeholder='Select Test Code'
                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='Test_Name',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="Test_Name",
                    multi=True,
                    placeholder='Select Test Name'
                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='CH_Num',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="CH_LOT",
                    multi=True,
                    placeholder='Select Reagent Ot Number'
                ),
            ],
        )
    ],
    body=True,
    className=cardShadow[0],
    style=cardShadow[1]
)

# Card to select quality control name and level
QC = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label('QC'),
                dcc.Dropdown(
                    id='QC_Num',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="QC_LOT",
                    multi=True,
                    placeholder='Select QC Lot Number'
                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='QC_Name',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="QC_name",
                    multi=True,
                    placeholder='Select QC Name'
                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='QC_Level',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    value="QC_level",
                    multi=True,
                    placeholder='Select QC Level'
                ),
            ],
        )
    ],
    body=True,
    className=cardShadow[0],
    style=cardShadow[1]
)

# Calculate Statistical calculations and plot control chart
plotButton = dbc.Button("Calculate and Plot", id='Plot_Button',n_clicks = 0, outline=True, color='secondary', block=True,
                        style={'background-color': '#2D4D61 !important',
                               "margin-top": "-1em"}
                        )

# Table of calculations
Calculations = dbc.Card(
    [
        dbc.Label(html.H4("Calculations", className="ml-2",
                          style={'font-weight': 'bold', 'color': '#caccce', })),
        dbc.Col(space),
        dbc.Table(id = 'Calcs_Table')
        # dbc.Table(html.Tbody(id = 'Calcs_Table'), bordered=True, striped=True, responsive=True,
        #           style={"text-align": "center"}
        #           )
        # dash_table.DataTable(
        #     id = "Calcs_Table",
        #     columns = (
        #     [{'id': c, 'name': c} for c in tableCols]
        #     ),
        #     # data = [{v for v in tableValues}],
            
        # )
        # 
    ],
    body=True,
    className=cardShadow[0],
    style={"width": "103.5%", "margin-left": "-1em"}

)


# --------------------------------------------------------------Nav Bar---------------------------------------

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink(
    'Home', href="#", style={"color": "#caccce"},))
nav_item2 = dbc.NavItem(dbc.NavLink(
    'Results', href="#", style={"color": "#caccce"},))

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            "more pages", header=True),
        dbc.DropdownMenuItem(
            "anything", href="#", style={'color': '#caccce', 'hover': {'color': '#2e4d61'}})
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)

NavBar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=Logo, height="50px")),
                        dbc.Col(dbc.NavbarBrand(html.H4("SQC Calculator", className="ml-2",
                                                        style={'font-weight': 'bold', 'color': '#caccce', }))),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="#",
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, nav_item2, dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
        fluid=True,
    ),
    color="#2e4d61",
    dark=True,
    className="mb-10",
)


# -----------------------------------------------------------Whole Page-------------------------------------------------------------

# Call app cards
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(NavBar, md=12)),
        dbc.Row(
            [
                # Filters card
                dbc.Col([
                    dbc.Card(
                        [
                            dbc.Col(space),
                            dbc.Col(Duration),
                            dbc.Col(Analyzer_control,),
                            dbc.Col(Test_control),
                            dbc.Col(QC),
                            dbc.Col(plotButton),
                            dbc.Col(space)
                        ],
                        body=True,
                        # style={"overflowY": "scroll"}
                        # className = "shadow-sm p-3 mb-5 bg-white rounded"
                    )
                ], md=4),

                # Calculations and plot card
                dbc.Col([
                    dbc.Col(Calculations),
                    dbc.Col(space),
                    dcc.Graph(id="cluster-graph",
                              style={"margin-top": "-3em"}),

                ], md=8),
            ],
            align="top",
            style={"margin-top": "1rem", "padding-bottom": "1rem"}
        ),
    ],
    style={"background-color": "#eaeaea", "height": "100%"},
    fluid=True,

)

# --------------------------------------------------------------------Functions------------------------------------------

# Navbar


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    # [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# Select period Function
@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_output(start_date, end_date):
    string_prefix = ''
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len(''):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix

# Calculate Button Function
@app.callback(Output('Calcs_Table', 'children'),
              Input('Plot_Button', 'n_clicks'))
def Calculate(n_clicks):
    table_Rows=[]
    if n_clicks > 0 :
        table_Values = Calculate_All(Sample1)
        table_Rows = [
        html.Tr([html.Td(i) for i in tableCols]), html.Tr(
        [html.Td(i) for i in table_Values])
        ]
    return html.Tbody(table_Rows)

if __name__ == '__main__':
    app.run_server(debug=True)
