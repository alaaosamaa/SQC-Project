from os import name, terminal_size
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
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
from numpy.core.fromnumeric import size
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
## Analyzer_df = pd.read_sql("SELECT analyzer_name, analyzer_code FROM Analyzer WHERE analyzer_output = 'output2'", mydb)
# Analyzer_df = pd.read_sql("SELECT * FROM Analyzer ", mydb)
Lab_df = pd.read_sql("SELECT DISTINCT lab_branch FROM Lab ", mydb)
QC_df = pd.read_sql("SELECT qc_lot_number,qc_name FROM QC_Parameters ", mydb)
# Plot_df = pd.read_sql("SELECT qc_result FROM test_qc_results ", mydb)
# Plot_Mean_SD_df = pd.read_sql("SELECT qc_result, qc_assigned_mean, qc_assigned_sd FROM test_qc_results JOIN Test ON test_code = t_code JOIN QC_Parameters ON qc_id = q_c_id WHERE test_name = %s AND test_code = %s AND qc_lot_number = %s AND qc_name =%s AND qc_level = %s", (name, i[1],) 



# Create random data
Sample1 = np.random.randint(15, 20, size=112)
Sample2 = np.random.randint(11, 17, size=112)


# Array of table attributes
# tableCols = ['Mean', 'SD', 'CV', 'MU measurments', 'EWMA',
#              'CUSUM', 'Target Mean', 'Actual Mean', 'Target SD', 'Actual SD']
Mean_Table_cols = ['Assigned Mean','Caculated Mean', 'Assigned SD',  'Calculated SD']
CV_Table_cols = ['CV %', 'MU Measurments']
# tableCols = [Analyzer_df.analyzer_name[0],Analyzer_df.analyzer_name[1], Analyzer_df.analyzer_name[2]]

# Array of table values
Mean_Table_values = [0,0,0,0]
CV_Table_values = [0,0]


# Array of table rows
Mean_Table_Data = [
    html.Tr([html.Td(Mean_Table_cols[0],className="table-active"),html.Td(Mean_Table_values[0]),html.Td(Mean_Table_cols[1],className="table-active"),html.Td(Mean_Table_values[1])]), 
    html.Tr([html.Td(Mean_Table_cols[2],className="table-active"),html.Td(Mean_Table_values[2]),html.Td(Mean_Table_cols[3],className="table-active"),html.Td(Mean_Table_values[3])])
]
CV_Table_Data = [
    html.Tr([html.Td(CV_Table_cols[0],className="table-active"),html.Td(CV_Table_values[0])]), 
    html.Tr([html.Td(CV_Table_cols[1],className="table-active"),html.Td(CV_Table_values[1])])
]

graph_calcs=[
                html.Tr( [html.Th('Assigned Mean'), html.Th(Mean_Table_values[0],style={'font-weight':'normal','border-right':'1px solid #B3B6B7'}),html.Th("Calculated Mean"), html.Th(Mean_Table_values[1],style={'font-weight':'normal'})], style={'font-size':'small','border-bottom':'1px solid #B3B6B7'} ),
                html.Tr( [html.Td('Assigned SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[2],style={'border-right':'1px solid #B3B6B7'}),html.Td('Calculated SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[3])]),
                
            ]

# function that updates table data
# def Updata_Calcs_Table_Data(MeanTableValuesArray,CVTableValuesArray):
#     Mean_Table_Data = [
#     html.Tr([html.Td(Mean_Table_cols[0],className="table-active"),html.Td(Mean_Table_values[0]),html.Td(Mean_Table_cols[1],className="table-active"),html.Td(MeanTableValuesArray[1])]), 
#     html.Tr([html.Td(Mean_Table_cols[2],className="table-active"),html.Td(Mean_Table_values[2]),html.Td(Mean_Table_cols[3],className="table-active"),html.Td(MeanTableValuesArray[3])])
#     ]
#     CV_Table_Data = [
#     html.Tr([html.Td(CV_Table_cols[0],className="table-active"),html.Td(CVTableValuesArray[0])]), 
#     html.Tr([html.Td(CV_Table_cols[1],className="table-active"),html.Td(CVTableValuesArray[1])])
# ]    
#     return Mean_Table_Data,CV_Table_Data
def Updata_Calcs_Table_Data(MeanTableValuesArray,CVTableValuesArray):
    graph_calcs=[
                html.Tr( [html.Th('Assigned Mean'), html.Th(Mean_Table_values[0],style={'font-weight':'normal','border-right':'1px solid #B3B6B7'}),html.Th("Calculated Mean"), html.Th(Mean_Table_values[1],style={'font-weight':'normal'})], style={'font-size':'small','border-bottom':'1px solid #B3B6B7'} ),
                html.Tr( [html.Td('Assigned SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[2],style={'border-right':'1px solid #B3B6B7'}),html.Td('Calculated SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[3])]),
                
            ]
    Mean_Table_Data = [
    html.Tr([html.Td(Mean_Table_cols[0],className="table-active"),html.Td(Mean_Table_values[0]),html.Td(Mean_Table_cols[1],className="table-active"),html.Td(MeanTableValuesArray[1])]), 
    html.Tr([html.Td(Mean_Table_cols[2],className="table-active"),html.Td(Mean_Table_values[2]),html.Td(Mean_Table_cols[3],className="table-active"),html.Td(MeanTableValuesArray[3])])
    ]
    CV_Table_Data = [
    html.Tr([html.Td(CV_Table_cols[0],className="table-active"),html.Td(CVTableValuesArray[0])]), 
    html.Tr([html.Td(CV_Table_cols[1],className="table-active"),html.Td(CVTableValuesArray[1])])
]    
    return graph_calcs,CV_Table_Data

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
def Pooled_SD(dataArray1,dataArray2):
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
    dataArray_MU = Data_Mean(dataArray)
    return str(ufloat(dataArray_MU,0.01))

# Compute the Calculate the Exponentially weighted moving average (EWMA)
def Data_EWMA(dataArray):
  EWMA = pd.DataFrame(dataArray).ewm
  return EWMA

# Calculate Cumulative Sum of data array (CUSUM)
def Data_CUSUM(dataArray):
    
    return np.cumsum(dataArray)


# Calculate all and return an array of all statistical calculations 
def Calculate_All(dataArray):
   dataArray_Mean = Data_Mean(dataArray)
   dataArray_SD = Data_SD(dataArray)
   dataArray_CV = Data_CV(dataArray)
   dataArray_MU = Data_MU(dataArray)
   dataArray_EWMA = Data_EWMA(dataArray)
   dataArray_CUSUM = Data_CUSUM(dataArray)
   Calculations_Array = [dataArray_Mean, dataArray_SD, dataArray_CV, dataArray_MU]
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
                    dbc.Col(miniSpace),
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

# Card to select Lab branch and unit of the data
Lab_control = dbc.Card(
    [
        dbc.FormGroup(
            [
            dbc.Label('Lab'),
            dbc.Col(space),
            dcc.Dropdown(
                id='Lab_branch',
                options=[
                    {'label':name, 'value':name} for name in Lab_df.lab_branch],
                placeholder = 'Select Branch'
            ),
            dbc.Col(space),
            dcc.Dropdown(
                id='Lab_unit',
                disabled = True,
                placeholder = 'Select Unit'
            ),
            ],
        ),
    ],
    body=True,
    className=cardShadow[0],
    style=cardShadow[1]
)

# Card to select Analyzer name and code of the data
Analyzer_control = dbc.Card(
    [
        dbc.FormGroup(
            [
            dbc.Label('Analyzer'),
            dbc.Col(space),
            dcc.Dropdown(
                id='Analyzer_Name',
                disabled = True,
                placeholder = 'Select Analyzer Name'
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
                    id='Test_Name',
                    disabled = True,
                    placeholder='Select Test Name'
                ),
                
                # dbc.Col(space),
                # dcc.Dropdown(
                #     id='Reagent_Num',
                #     value="Reagent_Num",
                #     multi=True,
                #     placeholder='Select Reagent Lot Number',
                #     disabled = True
                # ),
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
                        {"label": col, "value": col}for col in QC_df.qc_lot_number],
                    placeholder='Select QC Lot Number',
                    disabled = True

                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='QC_Name',
                    options=[
                        {"label": col, "value": col}for col in QC_df.qc_name],
                    disabled = True,
                    placeholder='Select QC Name'
                ),
                dbc.Col(space),
                dcc.Dropdown(
                    id='QC_Level',
                    options=[
                        {"label": col, "value": col}for col in iris.columns],
                    multi=True,
                    disabled = True,
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
plotButton = dbc.Button("Calculate and Plot", 
                        id='Plot_Button',n_clicks = 0, outline=True, color='secondary', block=True,
                        style={'background-color': '#2D4D61 !important',
                               "margin-top": "-1em"}
                        )

# Create Table of calculations

def creat_calc_table(graph_calcs):
    Calculations = dbc.Card([
                            dbc.Col(space),
                            dbc.Table(html.Tbody(graph_calcs),  id='Mean_Table',borderless = True,responsive = True, size = 'sm',
                            style = {'font-size':'small','width':'50%','margin-left':'15px'} )
                            ])
    return Calculations
# Calculations = dbc.Card(
#     [
#         dbc.Label(html.H4("Calculations", className="ml-2",
#                           style={'font-weight': 'bold', 'color': '#caccce', })),
#         dbc.Col(space),
#         dbc.Col(space),
#         dbc.Row([
#             dbc.Col([
#                 dbc.Table(html.Tbody(Mean_Table_Data),id = 'Mean_Table',bordered = True,responsive = True, 
#                 size = 'sm',
#                 style = {'font-size':'small','text-align': 'center'}
#                 )   
#                 ],
#             md=5)
#             ,
#             dbc.Col([
#                 dbc.Table(html.Tbody(CV_Table_Data),id = 'CV_Table',bordered = True,responsive = True,
#                 size = 'sm', 
#                 style = {'font-size':'small','text-align': 'center'}
#                 )], 
#             md=4)
#             ,
#         ]),    
#     ],
#     body=True,
#     className=cardShadow[0],
#     style={"width": "100%"}

# )

# Checkbox if the user want to show Calculated mean

def DrawCalcMeanOption():
    # ID = 'Draw_calc_Mean_option' + str(i)
    # print (ID)
    DrawCalcMeanOption = html.Div([
    
        dbc.Label('Calculated Mean Line'),
        dcc.RadioItems(
                    id='Draw_calc_Mean_option0',
                    options=[{'label': i, 'value': i} for i in ['Show', 'Hide']],
                    value='Hide',
                    labelStyle={'display': 'block',"text-align": "center"}
                )
    ])
    return DrawCalcMeanOption


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
            "Add QC", href="#", style={'color': '#caccce', 'hover': {'color': '#2e4d61'}})
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
                        dbc.Col(dbc.NavbarBrand(html.H4("SQC Module", className="ml-2",
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
                            dcc.Store(id ='myresult_analyzer_memory'),
                            dcc.Store(id='myresult_test_memory'),
                            dcc.Store(id='myresult_qc_lot_num_memory'),
                            dcc.Store(id='myresult_qc_name_memory'),     
                            dcc.Store(id='myresult_qc_level_memory'),
                            dcc.Store(id='myresult_qc_Duration_memory'),                                                       
                            dbc.Col(space),
                            dbc.Col(Duration),
                            dbc.Col(Lab_control),
                            dbc.Col(Analyzer_control,),
                            dbc.Col(Test_control),
                            dbc.Col(QC),
                            dbc.Col(plotButton),
                            dcc.ConfirmDialog(
                            id='error-message',
                            displayed = False,
                            message='Data Not Found'
                            ),
                            dbc.Col(space)
                        ],
                        body=True,
                        style={'height': '150 vmax',"overflowY": "scroll"}
                        # className = "shadow-sm p-3 mb-5 bg-white rounded"
                        
                    )
                ], md=4, style={'height':'fixed'}),

                # Calculations and plot card
                dbc.Col([
                    dbc.Col(space),
                    dbc.Card( 
                            [
                                
                                html.Div(
                                dbc.Card([
                                dbc.Col(space),
                                dbc.Col(creat_calc_table(graph_calcs)),
                                dbc.Col(space),
                                dcc.Graph(id="cluster-graph",)
                                ]),
                                id = "graph_container"),
                                html.Hr(
                                # style={"margin-top": "-1em"}
                                ),
                                dbc.Col(
                                    DrawCalcMeanOption()
                                ,md=4, style= {"text-align": "center"}
                                ),
                            ],
                            id = 'initial_graph',
                            body=True,
                            className = "shadow-sm p-3 mb-5 bg-white rounded",
                            style={"margin-top": "-0.5em"}
                        ),

                ], md=8, style={'width':'100%'}),
            ],
            align="top",
            style={"margin-top": "1rem", "padding-bottom": "1rem"}
        ),
    ],
    style={"background-color": "#eaeaea", "height": "100%", "position": 'flex'},
    # className = "container-xl",
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
    Output('myresult_qc_Duration_memory','data'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')], 
    prevent_initial_call = True)

def update_output(start_date, end_date):
    string_prefix = ''
    start_date_object=''
    end_date_object=''
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
        arr=[start_date_object,end_date_object]
        return string_prefix,arr


########################################################  START OF FILTERS  ########################################################
######################################################## To update lab unit ########################################################
@app.callback(
    Output('Lab_unit', 'options'),
    Output('Lab_unit', 'disabled'),
    Input('Lab_branch', 'value'),
    prevent_initial_call = True,
)
def update_unit_dropdowns(branch):
    arr = []
    if branch == None:
        return dash.no_update, True

    mycursor.execute("SELECT DISTINCT lab_unit FROM Lab JOIN Analyzer on analyzer_id = a_id WHERE lab_branch = %s", (branch,))
    myresult = mycursor.fetchall()
    for i in myresult:
        arr.append(i[0])

    return [{'label': j, 'value': j} for j in arr], False

######################################################## To update analyzer name ########################################################
@app.callback(
    Output('Analyzer_Name', 'options'),
    Output('Analyzer_Name', 'disabled'),
    Output('myresult_analyzer_memory', 'data'),
    Input('Lab_unit', 'value'),
    Input('Lab_branch', 'value'),
    prevent_initial_call = True,
)
def update_analyzer_name_dropdowns(unit, branch):
    arr = []

    if unit == None:
        return dash.no_update, True, arr

    mycursor.execute("SELECT analyzer_name, analyzer_id FROM Lab JOIN Analyzer on analyzer_id = a_id WHERE lab_unit = %s AND lab_branch = %s", (unit, branch,))
    myresult = mycursor.fetchall()

    for i in myresult:
        arr.append(i[0])

    return [{'label': j, 'value': j} for j in arr], False, myresult

######################################################## To update test name ########################################################
@app.callback(
    Output('Test_Name', 'options'),
    Output('Test_Name', 'disabled'),
    Output('myresult_test_memory', 'data'),
    Input('Analyzer_Name', 'value'),
    Input('myresult_analyzer_memory', 'data'),
    prevent_initial_call = True,
)
def update_test_name_dropdowns(name, a_names_ids):
    arr = []
    if name == None:
        return dash.no_update, True, arr

    t_names_codes = []
    for i in a_names_ids:
        mycursor.execute("SELECT test_name, test_code FROM test_analyzer JOIN Test ON test_code = t_code JOIN Analyzer ON analyzer_id = a_id WHERE analyzer_name = %s AND analyzer_id =  %s", (name, i[1],))
        myresult = mycursor.fetchall()
        for x in myresult:
            arr.append(x[0])
            t_names_codes.append(x)
        
    return [{'label': j, 'value': j} for j in arr], False, t_names_codes

######################################################## To update QC lot number ########################################################
@app.callback(
    Output('QC_Num', 'options'),
    Output('QC_Num', 'disabled'),
    Output('myresult_qc_lot_num_memory', 'data'),
    Input('Test_Name', 'value'),
    Input('myresult_test_memory', 'data'),   
    prevent_initial_call = True,
)
def update_qc_lot_num_dropdowns(name, t_names_codes):
    arr = []
    if name == None:
        return dash.no_update, True, arr
    qc_num_codes = []
    for i in t_names_codes:
        mycursor.execute("SELECT DISTINCT qc_lot_number FROM test_qc_results JOIN Test ON test_code = t_code JOIN QC_Parameters ON qc_id = q_c_id WHERE test_name = %s AND test_code = %s", (name, i[1],))
        myresult = mycursor.fetchall()
        for x in myresult:
            arr.append(x[0])
            qc_num_codes.append(x[0])
            
    return [{'label': j, 'value': j} for j in arr], False, qc_num_codes

######################################################## To update QC Name ########################################################
@app.callback(
    Output('QC_Name', 'options'),
    Output('QC_Name', 'disabled'),
    Output('myresult_qc_name_memory', 'data'),
    Input('QC_Num', 'value'),
    Input('myresult_qc_lot_num_memory', 'data'),   
    prevent_initial_call = True,
)
def update_qc_name_dropdowns(lot_num, qc_num_ids):
    arr = []
    if lot_num == None:
        return dash.no_update, True, arr
    qc_names = []

    mycursor.execute("SELECT DISTINCT qc_name FROM QC_Parameters WHERE qc_lot_number = %s ", (lot_num,))
    myresult = mycursor.fetchall()
    for x in myresult:
        arr.append(x[0])
        qc_names.append(x[0])
        
    return [{'label': j, 'value': j} for j in arr], False, qc_names

######################################################## To update QC Level ########################################################
@app.callback(
    Output('QC_Level', 'options'),
    Output('QC_Level', 'disabled'),
    Output('myresult_qc_level_memory', 'data'),   
    Input('QC_Name', 'value'),
    prevent_initial_call = True,
)
def update_qc_level_dropdowns(qcname):
    arr = []
    if qcname == None:
        return dash.no_update, True, arr
    # qc_levels = []
    # for i in qcname:
    mycursor.execute("SELECT DISTINCT qc_level FROM QC_Parameters WHERE qc_name = %s ", (qcname,))
    myresult = mycursor.fetchall()
    for x in myresult:
        arr.append(x[0])
        # qc_levels.append(x[0])
        
    return [{'label': j, 'value': j} for j in arr], False, arr

######################################################## END OF FILTERS ########################################################
    
######################################################## START GRAPH ########################################################

def Get_QC_Results_data(testCode, qcLotNum, qcName, qcLevel,Duration):
    Results_arr = []
    qc_date=[]
    assigned_mean = 0
    assigned_SD = 0
    # Mean = Plot_Mean_SD_df.qc_assigned_mean[0]
    # SD = int(Plot_Mean_SD_df.qc_assigned_sd[1])
    mycursor.execute("SELECT qc_result, qc_assigned_mean, qc_assigned_sd,qc_date FROM test_qc_results JOIN Test ON test_code = t_code JOIN QC_Parameters ON qc_id = q_c_id WHERE test_code = %s AND qc_lot_number = %s AND qc_name =%s AND qc_level = %s AND ( qc_date between %s and %s)", (testCode, qcLotNum, qcName, qcLevel,Duration[0],Duration[1]))
    myresult = mycursor.fetchall()
    for i in myresult:
        Results_arr.append(i[0])
        assigned_mean = i[1]
        assigned_SD = i[2]
        qc_date.append(i[3])


    return Results_arr, assigned_mean, assigned_SD,qc_date


def Qc_Plot(testCode,qcLotNum,qcName,qcLevel,CalcMeanShow,Duration):
    Results_arr = []
    Results_arr,Assigned_mean,Assigned_SD,Date_arr = Get_QC_Results_data(testCode,qcLotNum,qcName,qcLevel,Duration)

    if len(Results_arr)==0:
        return 0,0,0,0

    X_axis = [Date for Date in Date_arr]
    Ass_Mean = [ Assigned_mean for i in range(len(Results_arr))]
    calc_Mean = Data_Mean(Results_arr)
    calc_Mean_line = [ calc_Mean for i in range(len(Results_arr))]
    P_One_SD = [ (Assigned_mean + Assigned_SD) for i in range(len(Results_arr))]
    P_Two_SD = [ (Assigned_mean + 2*Assigned_SD) for i in range(len(Results_arr))]
    P_Three_SD = [ (Assigned_mean + 3*Assigned_SD) for i in range(len(Results_arr))]
    N_One_SD = [ (Assigned_mean - Assigned_SD) for i in range(len(Results_arr))]
    N_Two_SD = [ (Assigned_mean - 2*Assigned_SD) for i in range(len(Results_arr))]
    N_Three_SD = [ (Assigned_mean - 3*Assigned_SD) for i in range(len(Results_arr))]

    trace1 = go.Scatter(
        x=X_axis, 
        y=Results_arr,
        name = 'Data',
        line=dict(
                    color='orange', 
                    dash='solid')   
        )
    trace2 = go.Scatter(
        x=X_axis,
        y=Ass_Mean,
        name = 'Assigned Mean', 
        mode="lines",
        opacity=0.6,
        line=dict(width=1.1,  #line styling
                    color='black', 
                    dash='solid')
        )
    trace3 = go.Scatter(
        x=X_axis, 
        y=P_One_SD,
        name = '+1σ',
        mode="lines",
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='Purple', 
                    dash="dot")
    )
    trace4 = go.Scatter(
        x=X_axis, 
        y=N_One_SD,
        name = '-1σ',
        mode="lines",  
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='Purple', 
                    dash='dot')
    )
    
    trace5 = go.Scatter(
        x=X_axis, 
        y=P_Two_SD,
        name = '+2σ',
        mode="lines",
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='blue', 
                    dash='dot')  
    )
    trace6 = go.Scatter(
        x=X_axis, 
        y=N_Two_SD,
        name = '-2σ',
        mode="lines",  
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                color='blue', 
                dash='dot')  
    )
     
    trace7 = go.Scatter(
        x=X_axis, 
        y=P_Three_SD,
        name = '+3σ',
        mode="lines",
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='green', 
                    dash='dot')   
        )
    trace8 = go.Scatter(
        x=X_axis, 
        y=N_Three_SD,
        name = '-3σ',
        mode="lines",  
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='green', 
                    dash='dot')
    )
    trace9 = go.Scatter(
        x=X_axis, 
        y=calc_Mean_line,
        name = 'Calculated Mean',
        mode="lines",  
        opacity=0.6,
        line=dict(width=1.1,  #line styling
                    color='darkgreen', 
                    dash='solid')
    )
     
    if CalcMeanShow == "Hide":
        data = [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8]
    elif CalcMeanShow == "Show" :
        data = [trace1, trace2, trace9, trace3, trace4,trace5, trace6, trace7, trace8]
    
    layout = go.Layout(
        title = "QC Chart "+ qcLevel,
        xaxis = dict(
            showgrid = False,
            zeroline = True,
            showline = True,
            showticklabels = True,
            gridwidth = 1
        ),
        yaxis = dict(
            title = 'QC Results',
            zeroline=True,
            showgrid = False,
            showline = True ,

        )
    )
    fig = go.Figure(data = data ,layout = layout)

    return fig ,Results_arr,Assigned_mean,Assigned_SD

def graph_card(fig,graph_calcs):
    graph = html.Div(
    [   
        dbc.Col(space),
        dbc.Card([
        dbc.Col(space),
        dbc.Col(creat_calc_table(graph_calcs)),
        dbc.Col(space),
        dcc.Graph(id='level_graph' ,figure = fig),
        ],),
        dbc.Col(space),
    ])

    return graph

# Calculate Button Function
@app.callback(
            Output('Mean_Table', 'children'),
            # Output('CV_Table', 'children'),
            Output('graph_container', 'children'),
            Output('error-message', 'displayed'),
            Output('error-message', 'message'),
            Input('Plot_Button', 'n_clicks'),
            Input('Draw_calc_Mean_option0', 'value'),
            State('myresult_test_memory', 'data'),
            State('myresult_qc_lot_num_memory', 'data'),
            State('QC_Name', 'value'),
            State('QC_Level', 'value'), 
            State('myresult_qc_Duration_memory','data'),
            prevent_initial_call = True)
            
def Calculate(n_clicks,CalcMeanShow,testCode,qcLotNum,qcName,qcLevel,Duration):
    MeanTableData=[]
    MeanTableData = graph_calcs
    QC_Results = []
    displayed = False
    Message = ""
    table_arr = []
    # CvTableData=[]
    
    if not (testCode and qcLotNum and qcName and qcLevel and Duration) :
        return   html.Tbody(MeanTableData),dcc.Graph(),True,"Please Choose All Data"

    for i in testCode:
        t = i[1]
    testCode = t
    qcLotNum = qcLotNum[0]
    # ctx = dash.callback_context
    # input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if n_clicks == 0:
        # CvTableData = CV_Table_Data
        return html.Tbody(MeanTableData),dcc.Graph(),False,""
    
    if n_clicks > 0 :
        fig_arr = []
        for i in qcLevel:
            fig, QC_Results,Assigned_mean,Assigned_SD =Qc_Plot(testCode,qcLotNum,qcName,i,CalcMeanShow,Duration)

            if fig == 0 :
                displayed = True
                fig_arr.append(graph_card({}))
                Message = "Data Not Found"
                # return   html.Tbody(MeanTableData),,displayed ,
            else :
                Calculations_data = Calculate_All(QC_Results)
                Mean_Table_values[0],Mean_Table_values[2] = Assigned_mean,Assigned_SD
                Mean_Table_values[1],Mean_Table_values[3] = Calculations_data[0],Calculations_data[1]
                CV_Table_values[0],CV_Table_values[1] = Calculations_data[2],Calculations_data[3]
                MeanTableData,CvTableData = Updata_Calcs_Table_Data(Mean_Table_values,CV_Table_values)
                fig_arr.append(graph_card(fig,MeanTableData))
           
    # return html.Tbody(MeanTableData),html.Tbody(CvTableData),fig_arr
    return  html.Tbody(MeanTableData), fig_arr, displayed, Message


if __name__ == '__main__':
    app.run_server(debug=True)
