# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from joblib import load
import pandas as pd
from datetime import datetime as dt
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
pipeline = load ('assets/pipeline.joblib')
# thedate = pd.to_datetime('date-picker-single', format="%m/%d/%Y")
from datetime import datetime as dt
# Imports from this application
from app import app


markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
        dcc.Markdown(
            """
    

            Select Chicago neighborhood  



            
            """
            
        ),
        html.Br(),
        dcc.Markdown(
            """
    

              



            
            """
            
        ),
                dcc.Dropdown(
                id='Community_Area',
                options=[
                    {'label': 'Rogers Park', 'value': '1'},
                    {'label': 'West Ridge', 'value': '2'},
                    {'label': 'Uptown', 'value': '3'},
                    {'label': 'Lincoln Square', 'value': '4'},
                    {'label': 'North Center', 'value': '5'},
                    {'label': 'Lakeview', 'value': '6'},
                    {'label': 'Lincoln Park', 'value': '7'},
                    {'label': 'Near North Side', 'value': '8'},
                    {'label': 'Edison Park', 'value': '9'},
                    {'label': 'Norwood Park', 'value': '10'},
                    {'label': 'Jefferson Park', 'value': '11'},
                    {'label': 'Forest Glen', 'value': '12'},
                    {'label': 'North Park', 'value': '13'},
                    {'label': 'Albany Park', 'value': '14'},
                    {'label': 'Portage Park', 'value': '15'},
                    {'label': 'Irving Park', 'value': '16'},
                    {'label': 'Dunning', 'value': '17'},
                    {'label': 'Montclaire', 'value': '18'},
                    {'label': 'Belmont Cragin', 'value': '19'},
                    {'label': 'Hermosa', 'value': '20'},
                    {'label': 'Avondale', 'value': '21'},
                    {'label': 'Logan Square', 'value': '22'},
                    {'label': 'Humboldt Park', 'value': '23'},
                    {'label': 'West Town', 'value': '24'},
                    {'label': 'Austin', 'value': '25'},
                    {'label': 'West Garfield Park', 'value': '26'},
                    {'label': 'East Garfield Park', 'value': '27'},
                    {'label': 'Near West Side', 'value': '28'},
                    {'label': 'North Lawndale', 'value': '29'},
                    {'label': 'South Lawndale', 'value': '30'},
                    {'label': 'Lower West Side', 'value': '31'},
                    {'label': 'Loop', 'value': '32'},
                    {'label': 'Near South Side', 'value': '33'},
                    {'label': 'Armour Square', 'value': '34'},
                    {'label': 'Douglas', 'value': '35'},
                    {'label': 'Oakland', 'value': '36'},
                    {'label': 'Fuller Park', 'value': '37'},
                    {'label': 'Grand Boulevard', 'value': '38'},
                    {'label': 'Kenwood', 'value': '39'},
                    {'label': 'Washington Park', 'value': '40'},
                    {'label': 'Hyde Park', 'value': '41'},
                    {'label': 'Woodlawn', 'value': '42'},
                    {'label': 'South Shore', 'value': '43'},
                    {'label': 'Chatham', 'value': '44'},
                    {'label': 'Avalon Park', 'value': '45'},
                    {'label': 'South Chicago', 'value': '46'},
                    {'label': 'Burnside', 'value': '47'},
                    {'label': 'Calumet Heights', 'value': '48'},
                    {'label': 'Roseland', 'value': '49'},
                    {'label': 'Pullman', 'value': '50'},
                    {'label': 'South Deering', 'value': '51'},
                    {'label': 'East Side', 'value': '52'},
                    {'label': 'West Pullman', 'value': '53'},
                    {'label': 'Riverdale', 'value': '54'},
                    {'label': 'Hegewisch', 'value': '55'},
                    {'label': 'Archer Heights', 'value': '57'},
                    {'label': 'Brighton Park', 'value': '58'},
                    {'label': 'McKinley Park', 'value': '59'},
                    {'label': 'Bridgeport', 'value': '60'},
                    {'label': 'New City', 'value': '61'},
                    {'label': 'West Elsdon', 'value': '62'},
                    {'label': 'Gage Park', 'value': '63'},
                    {'label': 'Clearing', 'value': '64'},
                    {'label': 'West Lawn', 'value': '65'},
                    {'label': 'Chicago Lawn', 'value': '66'},
                    {'label': 'West Englewood', 'value': '67'},
                    {'label': 'Englewood', 'value': '68'},
                    {'label': 'Greater Grand Crossing', 'value': '69'},
                    {'label': 'Ashburn', 'value': '70'},
                    {'label': 'Auburn Gresham', 'value': '71'},
                    {'label': 'Beverly', 'value': '72'},
                    {'label': 'Washington Height', 'value': '73'},
                    {'label': 'Mount Greenwood', 'value': '74'},
                    {'label': 'Morgan Park', 'value': '75'},
                    {'label': "O'hare", 'value': '76'},
                    {'label': 'Edgewater', 'value': '77'}
                ],
                value='25'
            ), 
            html.Br(), 








                dcc.Markdown(
            """
    

            Select Date to predict



            
            """
        ),
            dcc.DatePickerSingle(
                id='date-picker-single',
                date=dt(2020, 3, 10)
            ),
            html.Br(),
            html.Br(),


# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.layout = html.Div([
#     dcc.DatePickerSingle(
#         id='my-date-picker-single',
#         min_date_allowed=dt(1995, 8, 5),
#         max_date_allowed=dt(2017, 9, 19),
#         initial_visible_month=dt(2017, 8, 5),
#         date=str(dt(2017, 8, 25, 23, 59, 59))
#     ),
#     html.Div(id='output-container-date-picker-single')
# ])


        dcc.Markdown(
            """
    

            Select month 1-12
            



            """
            ),
            html.Br(),
            daq.Slider(
                id='Month',
                min=1,
                max=12,
                value=7,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Month"},
                step=1
            ),
            html.Br(),
                dcc.Markdown(
            """
    

            Select day of month
            



            """
            ),
            html.Br(),
            daq.Slider(
                id='Day',
                min=1,
                max=31,
                value=29,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Day"},
                step=1
            ),
            html.Br(),
                        dcc.Markdown(
            """
    

            Select day of week 1-7
            



            """
            ),
            html.Br(),
            daq.Slider(
                id='Weekday',
                min=1,
                max=7,
                value=1,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Weekday"},
                step=1
            ),
            html.Br(),
   
        dcc.Markdown(
            """
    

            Select temperature in Farenheit  
            



            """
            ),
            html.Br(),
            daq.Slider(
                id='DailyAverageDryBulbTemperature',
                min=-10,
                max=110,
                value=78,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Temperature"},
                step=1
            ),
            html.Br(),

            dcc.Markdown(
            """
    

            Select average daily MPH windspeed 



            
            """

        ),
        html.Br(),
            daq.Slider(
                id='DailyAverageWindSpeed',
                min=0,
                max=60,
                value=8,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Windspeed"},
                step=1
            ),
            html.Br(),
            
            dcc.Markdown(
            """
    

            Select inches of precipitation



            
            """
            ),
            html.Br(),

            daq.Slider(
                id='DailyPrecipitation',
                min=0,
                max=10,
                value=0,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Precipitation"},
                step=.5
            ), 
            html.Br(),
                    dcc.Markdown(
            """
    

            Select inches of snow on ground



            
            """
        ),
        html.Br(),

            daq.Slider(
                id='DailySnowDepth',
                min=0,
                max=10,
                value=0,
                size=250,
                handleLabel={"showCurrentValue": True,"label": "Snow"},
                step=.5
            ), 


                                      
    ],
    md=4,
)



column2 = dbc.Col(
    [
        dcc.Markdown(
            """
    

            this moves things down

            yes it does  



            
            """
            
        ),
        html.Br(),
        html.Br(),
    # html.Div(id='prediction-gauge', style={'marginTop': '2.2em'}),

        html.Br(),

    html.Div(id='prediction-label', className='lead', style={'fontWeight': 'bold', 'fontSize': '1px', 'position': 'relative', 'left': '180px', 'bottom': '82px'})
        
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-label', 'children'),
    
    # Output('prediction-content', 'children'),
    [Input('Community_Area', 'value'),
    Input('DailyAverageDryBulbTemperature', 'value'),
    Input('DailyAverageWindSpeed', 'value'),
    Input('DailyPrecipitation', 'value'),
    Input('DailySnowDepth', 'value'),
    Input('Month', 'value'),
    Input('Day', 'value'),
    Input('Weekday', 'value')],
)
def predict (Community_Area,
             DailyAverageDryBulbTemperature,
             DailyAverageWindSpeed,
             DailyPrecipitation,
             DailySnowDepth,
             Month,
             Day,
             Weekday):
    df=pd.DataFrame(
        columns = ['Community_Area',
                   'DailyAverageDryBulbTemperature',
                   'DailyAverageWindSpeed',
                   'DailyPrecipitation',
                   'DailySnowDepth',
                   'Month',
                   'Day',
                   'Weekday'],
        data =[[Community_Area,
        DailyAverageDryBulbTemperature,
        DailyAverageWindSpeed,
        DailyPrecipitation,
        DailySnowDepth,
        Month,
        Day,
        Weekday]]
    )
    y_pred = pipeline.predict(df)[0]

    output1 = f'{y_pred:.0f}'
    

    output2 = daq.Gauge(id='my-daq-gauge',
                        showCurrentValue=True,
                        units="Street Crimes",
                        max=50,
                        value=y_pred,
                        min=0,
                        color={"gradient":True,"ranges":{"green":[0,10],"yellow":[10,20],"red":[20,50]}},
                        size=400)  
    return output1, output2
# @app.callback(
#     dash.dependencies.Output('my-daq-gauge', 'value'),
#     [dash.dependencies.Input('prediction-content','children')]
# )
def update_output(value):
    return value

