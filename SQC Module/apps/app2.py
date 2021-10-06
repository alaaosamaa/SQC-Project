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
from numpy.core.arrayprint import printoptions
from numpy.core.fromnumeric import size
from numpy.core.numeric import NaN
from numpy.lib.function_base import append
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
from app import app


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

graph_flag = 0
def update_graph_flag(graph_flag):

    return 1


# Array of table attributes
# tableCols = ['Mean', 'SD', 'CV', 'MU measurments', 'EWMA',
#              'CUSUM', 'Target Mean', 'Actual Mean', 'Target SD', 'Actual SD']
Mean_Table_cols = ['Assigned Mean','Caculated Mean', 'Assigned SD',  'Calculated SD']
CV_Table_cols = ['CV %', 'MU Measurments']
# tableCols = [Analyzer_df.analyzer_name[0],Analyzer_df.analyzer_name[1], Analyzer_df.analyzer_name[2]]

# Array of table values
Mean_Table_values = [0,0,0,0,0,0]
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
                html.Tr( [html.Th('Assigned Mean'), html.Th(Mean_Table_values[0],style={'font-weight':'normal','border-right':'1px solid #B3B6B7'}),html.Th("Calculated Mean"), html.Th(Mean_Table_values[1],style={'font-weight':'normal','border-right':'1px solid #B3B6B7'}),html.Th('Assigned CV %'), html.Th(Mean_Table_values[4],style={'font-weight':'normal'},)], style={'font-size':'small','border-bottom':'1px solid #B3B6B7'} ),
                html.Tr( [html.Td('Assigned SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[2],style={'border-right':'1px solid #B3B6B7'}),html.Td('Calculated SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[3],style={'border-right':'1px solid #B3B6B7'}),html.Td('Calculated CV %',style={'font-weight':'bold'}),html.Td(Mean_Table_values[5])]),
                
            ]

# function that updates table data
    
def Updata_Calcs_Table_Data(Mean_Table_values,CVTableValuesArray):
    graph_calcs=[
                html.Tr( [html.Th('Assigned Mean'), html.Th(Mean_Table_values[0],style={'font-weight':'normal','border-right':'1px solid #B3B6B7'}),html.Th("Calculated Mean"), html.Th(Mean_Table_values[1],style={'font-weight':'normal','border-right':'1px solid #B3B6B7'}),html.Th('Assigned CV %'), html.Th(Mean_Table_values[4],style={'font-weight':'normal'},)], style={'font-size':'small','border-bottom':'1px solid #B3B6B7'} ),
                html.Tr( [html.Td('Assigned SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[2],style={'border-right':'1px solid #B3B6B7'}),html.Td('Calculated SD',style={'font-weight':'bold'}),html.Td(Mean_Table_values[3],style={'border-right':'1px solid #B3B6B7'}),html.Td('Calculated CV %',style={'font-weight':'bold'}),html.Td(Mean_Table_values[5])]),
                
            ]
    # Mean_Table_Data = [
    # html.Tr([html.Td(Mean_Table_cols[0],className="table-active"),html.Td(Mean_Table_values[0]),html.Td(Mean_Table_cols[1],className="table-active"),html.Td(MeanTableValuesArray[1])]), 
    # html.Tr([html.Td(Mean_Table_cols[2],className="table-active"),html.Td(Mean_Table_values[2]),html.Td(Mean_Table_cols[3],className="table-active"),html.Td(MeanTableValuesArray[3])])
    # ]
    # CV_Table_Data = [
    # html.Tr([html.Td(CV_Table_cols[0],className="table-active"),html.Td(CVTableValuesArray[0])]), 
    # html.Tr([html.Td(CV_Table_cols[1],className="table-active"),html.Td(CVTableValuesArray[1])])
    # ]    
    return graph_calcs

# App Logo image
Logo = "https://icon-library.com/images/graphs-icon/graphs-icon-4.jpg"


# --------------------------------------------------------------Calculations---------------------------------------

# Computing mean for array of data 
def Data_Mean(dataArray):
    return round(statistics.mean(dataArray),2)


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
    return round((dataArray_SD/dataArray_Mean)*100,2)

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

# Huge space
HugeSpace = dbc.Row("  ", style={"height": "20px"})

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
    Calculations = [
                    dbc.Row([    
                    dbc.Col([
                    dbc.Col(space),
                    dbc.Table(html.Tbody(graph_calcs),  id='Mean_Table',borderless = True,responsive = True, size = 'sm',
                    style = {'font-size':'small','width':'50%','margin-left':'15px'} )
                    ],md=8,style= {"text-align": "center"}),
                    Update_database_buttons
                    ])
                    ]
    return Calculations



# Checkbox if the user want to show Calculated mean

def DrawCalcMeanOption():
    # ID = 'Draw_calc_Mean_option' + str(i)
    # print (ID)
    DrawCalcMeanOption = dbc.Col([
    
        dbc.Label('Show Calculated Mean Line'),
        dcc.RadioItems(
                    id='Draw_calc_Mean_option0',
                    options=[{'label': i, 'value': i} for i in ['Show', 'Hide']],
                    value='Hide',
                    labelStyle={'display': 'block',"text-align": "center"}
                )
    ],md=6, style= {"text-align": "center"}
    )
    return DrawCalcMeanOption

# Checkbox if the user want to Activate Westgard Multi-Rules
Apply_Graph_Rules = dbc.Col([
    dbc.Label('Activate Westgard Multi-Rules'),
    dcc.RadioItems(
            id='Apply_Graph_Rules',
            options=[
                {'label': ' ON' , 'value': 'ON'},
                {'label': ' OFF', 'value': 'OFF'},  
                ],
            value='OFF',
            labelStyle={'display': 'block',"text-align": "center"}
        )
],md=6, style= {"text-align": "center"}
)

Graph_Rules = dbc.Col([
    dbc.Label('Choose Graph Rule'),
    dcc.Checklist(
    id = 'Graph_Rules',
    options=[
        {'label': ' 1-2S', 'value': '1-2S'},
        {'label': ' 1-3S', 'value': '1-3S'},
        {'label': ' 2-2S', 'value': '2-2S'},
        {'label': ' 4-1S', 'value': '4-1S'},
        {'label': ' n-XS', 'value': 'n-XS'},
    ],
    # value=['1-2S', '1-3S'],
    labelStyle={'display': 'block'}
)],md=6, style= {"text-align": "center"}
)

Rules_Inputs = dbc.Col([
    dbc.Label('Enter Number of Points for n-XS Rule'),
    dcc.Input(id='nX-input', value= 5 , type='number',style = {'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    dbc.Col(space),

],md=6, style= {"text-align": "center"}
)

Update_database_buttons =dbc.Col([
        # dbc.Col(HugeSpace),
        dbc.Col(space),
        dbc.Col(space),
        dbc.Button("Update Assigned Data", 
                        id='Update_Assigned_Data_Button',n_clicks = 0, outline=True, color='secondary', disabled=True, block=True,
                        style={'background-color': '#2D4D61 !important'}
                        ),
        # dbc.Col(HugeSpace),
        dbc.Col(space),
        dbc.Button("Update QC Status", 
                        id='Update_QC_Status_Button',n_clicks = 0, outline=True, color='secondary', disabled=True, block=True,
                        style={'background-color': '#2D4D61 !important','font-size':'medium'}
                        ),
        dbc.Col(space),
        # dbc.Col(HugeSpace),

],md=3, style= {"text-align": "center", 'margin-left':'5px'}
)


# -----------------------------------------------------------Whole Page-------------------------------------------------------------

# Call app cards
Home = dbc.Container(
    [
        # dbc.Row(dbc.Col(NavBar, md=12)),
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
                            dcc.Store(id='calculated_data_memory'),                                                       
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
                        # style={'height': '150 vmax',"overflowY": "scroll"}
                        # className = "shadow-sm p-3 mb-5 bg-white rounded"
                        
                    )
                ], md=4, style={'height':'fixed'}),

                # Calculations and plot card
                dbc.Col([
                    dbc.Col(space),
                    dbc.Card( 
                            [
                                dbc.Row([                        
                                Apply_Graph_Rules,
                                DrawCalcMeanOption(),
                                
                                ]),
                                html.Hr(
                                    style={"margin-buttom": "2em"}
                                ),
                                html.Div([
                                dbc.Card([
                                dbc.Col(space),
                                dbc.Card(
                                    creat_calc_table(graph_calcs),
                                    style = {'margin' : '15px'} 
                                ),
                                dbc.Col(space),
                                dcc.Graph(id="cluster-graph",)
                                ]),
                                ],
                                id = "graph_container"),
                                html.Hr(
                                # style={"margin-top": "-1em"}
                                ),
                                
                                dbc.Row([                                
                                    Graph_Rules,
                                    Rules_Inputs,
                                    # Update_database_buttons,
                                    
                                ],
                                id = "rules_container",
                                style = {'display':'none'}
                                )
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

layout = Home 


# --------------------------------------------------------------------Functions------------------------------------------
######################################################## START GRAPH Functions ########################################################

def Get_code(arr,name):
    for i in arr :
        if i[0] == name:
            return i[1]


def Get_QC_Results_data(testCode, analyzerCode, qcLotNum, qcName, qcLevel, Duration):
    Results_arr = []
    qc_date=[]
    assigned_mean = 0
    assigned_SD = 0
    assigned_CV = 0
    # Mean = Plot_Mean_SD_df.qc_assigned_mean[0]
    # SD = int(Plot_Mean_SD_df.qc_assigned_sd[1])

    mycursor.execute("SELECT qc_result, qc_assigned_mean, qc_assigned_sd, qc_assigned_cv, qc_date FROM test_qc_results JOIN QC_Parameters ON qc_id = q_c_id WHERE t_code = %s AND a_id = %s AND qc_lot_number = %s AND qc_name =%s AND qc_level = %s AND ( qc_date between %s and %s)", (testCode, analyzerCode, qcLotNum, qcName, qcLevel,Duration[0],Duration[1]))
    myresult = mycursor.fetchall()
    for i in myresult:
        Results_arr.append(i[0])
        assigned_mean = i[1]
        assigned_SD = i[2]
        assigned_CV = i[3]
        qc_date.append(i[4])


    return Results_arr, assigned_mean, assigned_SD, assigned_CV, qc_date

def rules(arr,pSD,nSD,rule, mean = 0, n = 0):
    y_arr = []
    for i in range(len(arr)):
            y_arr.append(NaN)
    ind = []
    pos_arr = positions(arr, pSD, nSD, mean)

    if rule == '1-2S':
        for i in range(len(arr)):
            if (arr[i] >= pSD[1] and arr[i] < pSD[2]) or (arr[i] <= nSD[1] and arr[i] > nSD[2]) :
                y_arr[i] = arr[i]

    if rule == '1-3S':
        for i in range(len(arr)):
            if (arr[i] >= pSD[2] ) or (arr[i] <= nSD[2] ) :
                y_arr[i] = arr[i]

    if rule == '2-2S':        
        for i in range(len(arr) -1):
            if (arr[i] >= pSD[1] and arr[i] < pSD[2] and arr[i+1] >= pSD[1] and arr[i+1] < pSD[2]) or (arr[i] <= nSD[1] and arr[i] > nSD[2] and arr[i+1] <= nSD[1] and arr[i+1] > nSD[2]):
                if (not (search_arr(ind, i))):
                    ind.append(i)
                ind.append(i+1)
        for i in ind:
            y_arr[i] = arr[i]

    if rule == '4-1S':
        cp = cn = 0
        for i in range(len(arr)):
            if (pos_arr[i] == 2):
                cp += 1
                cn = 0
                ind.append(i)
            elif (pos_arr[i] == -2):
                cn += 1
                cp = 0
                ind.append(i)
            else:
                cp = cn = 0
                ind =[]
            if cp >= 4 or cn >= 4:       
                for i in ind:
                    y_arr[i] = arr[i]
                    

    if rule == 'xs':
        # n = 5
        c = 0
        
        for i in range(len(pos_arr) - 1):

            if pos_arr[i] == pos_arr[i+1]:
                c += 1
                if (not (search_arr(ind, i))):
                    ind.append(i)
                ind.append(i+1)

            else:
                c = 0
                ind = []

            if ((c +1) >= n):
                for i in ind:
                    y_arr[i] = arr[i]

    return y_arr    

def positions(y_arr, pSD, nSD, mean):
    pos = []
    for i in y_arr:
        if i >= mean and i < pSD[0]:
            pos.append(1)
        elif i >= pSD[0] and i < pSD[1]:
            pos.append(2)
        elif i >= pSD[1] and i < pSD[2]:
            pos.append(3)
        elif i >= pSD[2]:
            pos.append(4)

        elif i < mean and i > nSD[0]:
            pos.append(-1)
        elif i <= nSD[0] and i > nSD[1]:
            pos.append(-2)
        elif i <= nSD[1] and i > nSD[2]:
            pos.append(-3)
        elif i <= nSD[2]:
            pos.append(-4)

    return pos

def search_arr(arr, val):
    ans = False
    for i in arr:
        if i == val:
            ans = True
    return ans

def Qc_Plot(analyzerCode,analyzerName,testName,testCode,qcLotNum,qcName,qcLevel,CalcMeanShow,Duration,GraphRules,n):
    Results_arr = []
    Results_arr, Assigned_mean, Assigned_SD, Assigned_CV, Date_arr = Get_QC_Results_data(testCode,analyzerCode,qcLotNum,qcName,qcLevel,Duration)

    if len(Results_arr)==0:
        return 0,0,0,0

    X_axis = [Date for Date in Date_arr]
    Ass_Mean = [ Assigned_mean for i in range(len(Results_arr))]
    calc_Mean = Data_Mean(Results_arr)
    calc_Mean_line = [ calc_Mean for i in range(len(Results_arr))]
   
    pSD = []
    nSD = []
    for i in range(1,4):
        pSD.append(Assigned_mean + i*Assigned_SD)
    for i in range(1,4):
        nSD.append(Assigned_mean - i*Assigned_SD)

    P_One_SD = [ (pSD[0]) for i in range(len(Results_arr))]
    P_Two_SD = [ (pSD[1]) for i in range(len(Results_arr))]
    P_Three_SD = [ (pSD[2]) for i in range(len(Results_arr))]
    N_One_SD = [ (nSD[0]) for i in range(len(Results_arr))]
    N_Two_SD = [ (nSD[1]) for i in range(len(Results_arr))]
    N_Three_SD = [ (nSD[2]) for i in range(len(Results_arr))]


    # df = pd.DataFrame({'x': X_axis, 'y': Results_arr})

    trace1 = go.Scattergl(
        x=X_axis, 
        y=Results_arr, 
        name = 'Data',
        mode = "lines+markers",
        line=dict(
                    color='#c89696', 
                    dash='solid')   
        )

    trace_rule_1_2s = go.Scattergl(
        x=X_axis, 
        y=rules(Results_arr,pSD,nSD,'1-2S'), 
        name = '1-2S Rule',
        mode = "markers",
        line={'color': 'orange'},
        )
    trace_rule_1_3s = go.Scattergl(
        x=X_axis, 
        y=rules(Results_arr,pSD,nSD,'1-3S'), 
        name = '1-3S Rule',
        mode = "markers",
        line={'color': 'red'},
        )
    trace_rule_2_2s = go.Scattergl(
        x=X_axis, 
        y=rules(Results_arr,pSD,nSD,'2-2S'), 
        name = '2-2S Rule',
        mode = "markers",
        line={'color': 'lime'},
        )
    trace_rule_4_1s = go.Scattergl(
        x=X_axis, 
        y=rules(Results_arr,pSD,nSD,'4-1S', Assigned_mean), 
        name = '4-1S Rule',
        mode = "markers",
        line={'color': 'yellow'},
        )
    trace_rule_xs = go.Scattergl(
        x=X_axis, 
        y=rules(Results_arr,pSD,nSD,'xs', Assigned_mean,n), 
        name = str(n)+ 's Rule',
        mode = "markers",
        line={'color': 'fuchsia'},
        )
    trace2 = go.Scattergl(
        x=X_axis,
        y=Ass_Mean,
        name = 'Assigned Mean', 
        mode="lines",
        opacity=0.6,
        line=dict(width=1.1,  #line styling
                    color='black', 
                    dash='solid')
        )
    trace3 = go.Scattergl(
        x=X_axis, 
        y=P_One_SD,
        name = '+1σ',
        mode="lines",
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='Purple', 
                    dash="dot")
    )
    trace4 = go.Scattergl(
        x=X_axis, 
        y=N_One_SD,
        name = '-1σ',
        mode="lines",  
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='Purple', 
                    dash='dot')
    )
    
    trace5 = go.Scattergl(
        x=X_axis, 
        y=P_Two_SD,
        name = '+2σ',
        mode="lines",
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='blue', 
                    dash='dot')  
    )
    trace6 = go.Scattergl(
        x=X_axis, 
        y=N_Two_SD,
        name = '-2σ',
        mode="lines",  
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                color='blue', 
                dash='dot')  
    )
     
    trace7 = go.Scattergl(
        x=X_axis, 
        y=P_Three_SD,
        name = '+3σ',
        mode="lines",
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='green', 
                    dash='dot')   
        )
    trace8 = go.Scattergl(
        x=X_axis, 
        y=N_Three_SD,
        name = '-3σ',
        mode="lines",  
        opacity=0.4,
        line=dict(width=1.1,  #line styling
                    color='green', 
                    dash='dot')
    )
    trace9 = go.Scattergl(
        x=X_axis, 
        y=calc_Mean_line,
        name = 'Calculated Mean',
        mode="lines",  
        opacity=0.9,
        line=dict(width=1.1,  #line styling
                    color='#32c896', 
                    dash='solid')
    )
    

    if CalcMeanShow == "Hide":
        data = [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8]
    elif CalcMeanShow == "Show" :
        data = [trace1, trace2, trace9, trace3, trace4,trace5, trace6, trace7, trace8]

    if GraphRules != None:    
        for i in GraphRules:
            if i == '1-2S':
                data.append(trace_rule_1_2s)
            if i == '1-3S':
                data.append(trace_rule_1_3s)
            if i == '2-2S':
                data.append(trace_rule_2_2s)
            if i == '4-1S':
                data.append(trace_rule_4_1s)
            if i == 'n-XS':
                data.append(trace_rule_xs)


    layout = go.Layout(
        title = "QC Chart For "+ analyzerName +", Test: "+ testName + ", QC Lot Num: " + str(qcLotNum) +", QC Name: "+ qcName +", QC Level: "+ qcLevel,
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
    fig = go.Figure(data = data ,layout = layout )

    return fig, Results_arr, Assigned_mean, Assigned_SD, Assigned_CV 

def graph_card(fig,graph_calcs):
    graph = html.Div(
    [   
        dbc.Col(space),
        dbc.Card([
        dbc.Col(space),
        dbc.Col(dbc.Card(
                creat_calc_table(graph_calcs),
                style = {'margin' : '15px'} 
                ),),
        dbc.Col(space),
        dcc.Graph(id='level_graph' ,figure = fig),
        ],),
        dbc.Col(space),
    ])

    return graph

######################################################## End GRAPH Functions ########################################################


########################################################  Callback Functions  ########################################################


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
    

# Calculate Button Function
@app.callback(
            Output('Mean_Table', 'children'),
            # Output('CV_Table', 'children'),
            Output('graph_container', 'children'),
            Output('error-message', 'displayed'),
            Output('error-message', 'message'),
            Output('calculated_data_memory', 'data'),
            Input('Plot_Button', 'n_clicks'),
            Input('Draw_calc_Mean_option0', 'value'),
            Input('Graph_Rules', 'value'),
            State('myresult_test_memory', 'data'),
            State('myresult_qc_lot_num_memory', 'data'),
            State('QC_Name', 'value'),
            State('QC_Level', 'value'), 
            State('myresult_qc_Duration_memory','data'),
            State('Analyzer_Name','value'),
            Input('nX-input', 'value'),
            State('myresult_analyzer_memory','data'),

            prevent_initial_call = True)
            
def Calculate(plot_n_clicks,CalcMeanShow,GraphRules,testCode,qcLotNum,qcName,qcLevel,Duration,analyzerName,n_Rules,analyzer_data):
    MeanTableData=[]
    MeanTableData = graph_calcs
    QC_Results = []
    displayed = False
    Message = ""
    fig_arr = []
    calc_data = []

    # CvTableData=[]
    
    if not (testCode and qcLotNum and qcName and qcLevel and Duration) :
        displayed = True
        fig_arr.append(graph_card({},graph_calcs))
        Message = "Please Choose All Data"
        # return   html.Tbody(MeanTableData),dcc.Graph(),True,

    else :
        for i in testCode:
            t = i[1]
            testName = i[0]

        testCode = t
        qcLotNum = qcLotNum[0]
        analyzerCode = Get_code(analyzer_data, analyzerName)
        # ctx = dash.callback_context
        # input_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if plot_n_clicks == 0:
            # CvTableData = CV_Table_Data
            return html.Tbody(MeanTableData),dcc.Graph(),False,"",calc_data
        
        if plot_n_clicks > 0 :
            fig_arr = []
            for i in qcLevel:
                # Call Plot function that returns figure, qc results array, Assigned mean and assigned SD 
                fig, QC_Results, Assigned_mean, Assigned_SD, Assigned_CV =Qc_Plot(analyzerCode,analyzerName,testName,testCode,qcLotNum,qcName,i,CalcMeanShow,Duration,GraphRules,n_Rules)

                if fig == 0 :
                    displayed = True
                    # fig_arr.append(graph_card({},graph_calcs))
                    Message = "Data Not Found for " + i
                    # return   html.Tbody(MeanTableData),,displayed ,
                else :
                    update_graph_flag()
                    Calculations_data = Calculate_All(QC_Results)
                    calc_data = Calculations_data
                    Mean_Table_values[0],Mean_Table_values[2], Mean_Table_values[4] = Assigned_mean, Assigned_SD, Assigned_CV
                    Mean_Table_values[1],Mean_Table_values[3], Mean_Table_values[5] = Calculations_data[0],Calculations_data[1], Calculations_data[2]
                    
                    MeanTableData = Updata_Calcs_Table_Data(Mean_Table_values,CV_Table_values)
                    fig_arr.append(graph_card(fig,MeanTableData))
           
    # return html.Tbody(MeanTableData),html.Tbody(CvTableData),fig_arr
    return  html.Tbody(MeanTableData), fig_arr, displayed, Message, calc_data


@app.callback(

    Output('rules_container', 'style'),
    Input('Apply_Graph_Rules', 'value'),
    prevent_initial_call = True,
)
def Apply_Graph_Rules_function(val):
    if val == 'ON':
        return 
    else :
        return {'display':'none'}

# @app.callback(

#     State('calculated_data_memory', 'data'),
#     # Input('Update_Assigned_Data_Button', 'n_clicks'),
#     prevent_initial_call = True,
# )

def update_database_assigned_data(calcData,testCode,analyzerCode,qcLotNum,qcName,qcLevel,Duration):
    mycursor.execute("UPDATE test_qc_results SET qc_overall_status = %s JOIN QC_Parameters ON qc_id = q_c_id WHERE t_code = %s AND a_id = %s AND qc_lot_number = %s AND qc_name =%s AND qc_level = %s AND ( qc_date between %s and %s)", (calcData,testCode, analyzerCode, qcLotNum, qcName, qcLevel,Duration[0],Duration[1]))