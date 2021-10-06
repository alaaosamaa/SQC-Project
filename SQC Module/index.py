import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from app import server
from apps import app2, report
import mysql.connector
import pandas as pd
import numpy as np
from datetime import date

# --------------------------------------------------------------Nav Bar---------------------------------------

Logo = "https://icon-library.com/images/graphs-icon/graphs-icon-4.jpg"
cardShadow = ["shadow-sm p-3 mb-5 bg-white rounded", {"margin-top": "-2em"}]
# Space components
space = dbc.Row("  ", style={"height": "10px"})

# Mini space
miniSpace = dbc.Row("  ", style={"height": "3px"})
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="SQC"
)
mycursor = mydb.cursor()
Lab_df = pd.read_sql("SELECT DISTINCT lab_branch FROM Lab ", mydb)
QC_df = pd.read_sql(
    "SELECT qc_lot_number,qc_name,qc_type,qc_level FROM QC_Parameters ", mydb)
name = np.unique(QC_df.qc_name)
Type = sorted(np.unique(QC_df.qc_type))
Level = np.unique(QC_df.qc_level)
Status = ['PENDING', 'COMPLETE', 'FAILED']
# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink(
    'Home', href="/apps/app2", style={"color": "#caccce"},))
nav_item2 = dbc.NavItem(dbc.NavLink(
    'Results', href="/apps/report", style={"color": "#caccce"},))
nav_item3 = dbc.NavItem(dbc.NavLink(
    'Add New QC', href="#", style={"color": "#caccce"}, id="open-body-scroll", n_clicks=0))
nav_item4 = dbc.NavItem(dbc.NavLink(
    'Add QC Result', href="#", style={"color": "#caccce"}, id="open-body-scroll2", n_clicks=0))


#  test_qc_results (t_code, a_id, r_lot_number, q_c_id, qc_assigned_mean, qc_assigned_sd, qc_assigned_cv, qualitative_assigned, qc_result, qc_flag, qc_date, qc_calculated_mean, qc_calculated_sd, qc_calculated_cv, qc_overall_status)
# QC_Parameters (qc_id, qc_lot_number, qc_name, qc_type, qc_level, qc_manufacturer,qc_speciality, qc_expiry_date)

QC_Parameter = dbc.Card(
    [
        dbc.FormGroup(
            [
                # dbc.Label('QC Parameters'),
                dbc.Col(miniSpace),
                dcc.Input(
                    id="qc_id",
                    type="number",
                    placeholder='enter QC ID',
                ),
                dbc.Col(miniSpace),
                dcc.Input(
                    id="qc_lot_number",
                    type="number",
                    placeholder='enter QC Lot Number',

                ),
                dbc.Col(miniSpace),
                dcc.Dropdown(
                    id='qc_name',
                    options=[
                        {'label': name, 'value': name} for name in name],
                    placeholder='Select QC Name'
                ),
                dbc.Col(miniSpace),
                dcc.Dropdown(
                    id='qc_type',
                    options=[
                        {'label': type, 'value': type} for type in Type],
                    placeholder='Select QC Type'
                ),
                dbc.Col(miniSpace),
                dcc.Dropdown(
                    id='qc_level',
                    options=[
                        {'label': level, 'value': level} for level in Level],
                    placeholder='Select QC Level'
                ),

            ],
        ),
    ],
    body=True,
    className=cardShadow[0],
    style=cardShadow[1]
)
QC_Result = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Row([
                    dbc.Col([
                        dbc.Col(miniSpace),
                        dcc.Input(
                            id="test_code",
                            type="number",
                            placeholder='Enter QC Test Code',
                        ),
                        dbc.Col(miniSpace),
                        dcc.Input(
                            id="analyzer code",
                            type="number",
                            placeholder='Enter Analyzer Code',

                        ),
                        dbc.Col(miniSpace),
                        dcc.Input(
                            id="reagent_lot_number",
                            type="number",
                            placeholder='Enter Reagent Lot Number',

                        ),
                        dbc.Col(miniSpace),
                        dcc.Input(
                            id="qc_id_test",
                            type="number",
                            placeholder='Enter QC ID',
                        ),
                        dbc.Col(miniSpace),
                        dcc.Input(
                            id="qc_assigned_mean",
                            type="number",
                            placeholder='Enter Assigned Mean',
                        ),
                        dbc.Col(miniSpace),
                        dcc.Input(
                            id="qc_assigned_sd",
                            type="number",
                            placeholder='Enter Assigned SD',
                        ),
                    ], md=5),
                    dbc.Col([

                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_assigned_cv",
                                type="number",
                                placeholder='Enter Assigned CV',
                            ),
                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_qualitative_assigned",
                                type="number",
                                placeholder='Enter Qualitative Assigned',
                            ),
                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_result",
                                type="number",
                                placeholder='Enter QC Result',
                            ),
                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_flag",
                                type="number",
                                placeholder='Enter QC Flag 1 or 0',
                                min=0,
                                max=1
                            ),

                            # html.Div(id='output-container-date-picker-single'),
                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_calculated_mean",
                                type="number",
                                placeholder='Enter Calculated Mean',
                            ),
                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_calculated_sd",
                                type="number",
                                placeholder='Enter Calculated SD',
                            ),
                            dbc.Col(miniSpace),
                            dcc.Input(
                                id="qc_calculated_cv",
                                type="number",
                                placeholder='Enter Calculated CV',
                            ),
                            ], md=5),
                    dbc.Col(md=2),
                    dbc.Col([
                        
                            dbc.Col(miniSpace),
                            dcc.DatePickerSingle(
                                id='my-date-picker-single',
                                # min_date_allowed=date(1995, 8, 5),
                                # max_date_allowed=date(2017, 9, 19),
                                # initial_visible_month=date(2017, 8, 5),
                                date=date.today(),
                                # clearable=True,
                                # with_portal=True,

                            ),

                            dbc.Col(miniSpace),
                            dcc.Dropdown(
                                id='qc_overall_status',
                                options=[
                                    {'label': status, 'value': status} for status in Status],
                                placeholder='Select Status',
                                # style={"height": "100%", 'width': '100%'}
                            ),
                        ], md=5
                        # className="h-25",

                    )
                ])

            ],
        ),
    ],
    body=True,
    className=cardShadow[0],
    style=cardShadow[1]
)
QC_Parameters = dbc.Container([QC_Parameter])
Test_QC_Results = dbc.Container([QC_Result])
QC_RESULT = html.Div(
    [
        nav_item4,
        dbc.Modal(
            [
                dbc.ModalHeader("QC Test Result"),
                dbc.ModalBody(Test_QC_Results),
                dbc.ModalFooter(
                    dbc.Button(
                        "Add",
                        id="close-body-scroll2",
                        className="ml-auto",
                        n_clicks=0,
                    ),
                ),
            ],
            id="modal-body-scroll2",
            scrollable=True,
            is_open=False,
            centered=True,
            size="xl",

        ),
    ]
)
QC_PARAMETER = html.Div(
    [
        nav_item3,
        dbc.Modal(
            [
                dbc.ModalHeader("QC Parameters"),
                dbc.ModalBody(QC_Parameters),
                dbc.ModalFooter(
                    dbc.Button(
                        "Add",
                        id="close-body-scroll",
                        className="ml-auto",
                        n_clicks=0,
                    ),
                ),
            ],
            id="modal-body-scroll",
            scrollable=True,
            is_open=False,
            centered=True,

        ),
    ]
)

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            "more pages", header=True),
        dbc.DropdownMenuItem(
            QC_PARAMETER, href="#", style={'color': '#caccce', 'hover': {'color': '#2e4d61'}}),
        dbc.DropdownMenuItem(
            QC_RESULT, href="#", style={'color': '#caccce', 'hover': {'color': '#2e4d61'}})
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
    right=True,
)


def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Pop up page
app.callback(
    Output("modal-body-scroll", "is_open"),
    [
        Input("open-body-scroll", "n_clicks"),
        Input("close-body-scroll", "n_clicks"),
        # Input("ADD", "n_clicks"),
    ],
    [State("modal-body-scroll", "is_open")],
)(toggle_modal)


def toggle_modal2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Pop up page2
app.callback(
    Output("modal-body-scroll2", "is_open"),
    [
        Input("open-body-scroll2", "n_clicks"),
        Input("close-body-scroll2", "n_clicks"),
        # Input("ADD", "n_clicks"),
    ],
    [State("modal-body-scroll2", "is_open")],
)(toggle_modal2)
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
                href="/apps/app2",
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

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row(dbc.Col(NavBar, md=12)),
        html.Div(id='page-content')

    ],
    style={"background-color": "#eaeaea",
           "height": "100%", "position": 'flex'},
    # className = "container-xl",
    fluid=True,

)

# Nav bar Callback


@app.callback(
    Output('output-container-date-picker-single', 'children'),
    Input('my-date-picker-single', 'date'))
def update_output(date_value):
    string_prefix = 'You have selected: '
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime('%B %d, %Y')
        # print(date_string)
        return string_prefix + date_string


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    # [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):

    if pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/report':
        return report.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
