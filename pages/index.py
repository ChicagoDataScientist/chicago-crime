# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash
app = dash.Dash(__name__)

app.layout = html.Div(html.Img(src=app.get_asset_url('skyline.jpg')))
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict crime in Chicago based on weather and date



            """
        ),
        # dcc.Link(dbc.Button('Predict Crime', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        


            Are you traveling to a neighborhood in Chicago and want to know how many street crimes will be committed that day?

            ✅ Our advanced machine learning algorithm will tell you which days are good and which days are bad

            On average, this app can predict within 1.5 crimes, how many street crimes will occur in a given community on a given day.

            """
        ),
        dcc.Link(dbc.Button('Predict Crime', color='primary'), href='/predictions')
    ],
    md=4,
)

layout = dbc.Row([column1, column2])