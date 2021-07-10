import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### 
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'
########### Set up the chart


########### Initiate the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app= dash.Dash(__name__,)
server = app.server
#app.title=tabtitle

########### Set up the layout
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('adp-png-logo-6428.png'),
                     id='ADPlogo',
                     style={'height': '90px',
                            'width': 'auto',
                            'margin-bottom': '25px'})
        ],className='one-third column'),
        html.Div([
            html.Div([
                html.H3('ADP India', style={'margin-bottom': '0px', 'color': 'red','font-family':'Playfair','font-size': '100px'}),
                html.H5('Corporate Social Responsibility Scorecard 2020', style={'margin-bottom': '0px', 'color': 'blue'})
            ])

        ], className='one-halfc column', id='title'),

        html.Div([
            html.H6('Last Updated: 9th July, 2021',
                    style={'color': 'black'})
        ], className='one-third column', id='title1')
        ],id='header',className='row flex-display', style ={'margin-bottom': '25px'}),
    
    ],id='mainContainer',style={'display':'flex','flex-direction':'column'})

if __name__ == '__main__':
    app.run_server()
