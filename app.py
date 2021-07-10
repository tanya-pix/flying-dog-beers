import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### 
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'
########### Set up the chart
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_interactive_graphviz
##########################################################


###########################################################

########################################################
## Amount spent on CSR per year
import plotly.express as px
import pandas as pd
import numpy as np
Year=['2014','2015','2016','2017','2018','2019','2020']
Amount=[
13002153,
15862364,
20761510,
23257443,
32510406,
37175722,
35294241
]
fig1 = px.line(x=Year, y=Amount,labels=dict(x="Fiscal Year", y="Amount Spent"))
fig1.add_bar(x=Year, y=Amount,marker_color=['green']*8)
fig1.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC')
fig1.update_layout(showlegend=False)
fig1.update_yaxes(tickprefix="₹")
fig1.update_yaxes(tickformat=".f")
#fig1.show()
######################################################
## Beneficiaries per year
import plotly.express as px
import pandas as pd
import numpy as np
Year=['2014','2015','2016','2017','2018','2019','2020']
Number_of_Beneficiaries=[
9794,
13405,
18589,
20545,
28426,
25523,
22867]
fig2 = px.line(x=Year, y=Number_of_Beneficiaries,labels=dict(x=" Fiscal Year", y="Beneficiaries"))
fig2.add_bar(x=Year, y=Number_of_Beneficiaries,marker_color=['#FFC000']*8)
fig2.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC')
fig2.update_layout(showlegend=False)
###################################################
##Gender Ratio
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
SexRatio=(r'assets/Sex Ratio.xlsx')

df1= pd.read_excel(SexRatio,sheet_name='Input for Code')
fig3 = px.bar(df1, x='Year', y='Beneficiaries',color="Sex", barmode="group")

colors2 = {'Male':'#006400',
          'Female':'#FFA500'
         }
fig3 =go.Figure()
for t in df1['Sex'].unique():
    df1p = df1[df1['Sex']==t]
    fig3.add_traces(go.Bar(x=df1p['Year'], y = df1p['Beneficiaries'], name=t,
                         marker_color=colors2[t]))
fig3.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)
fig3.update_layout(barmode='stack')
fig3.update_layout(
    xaxis_title="Gender",
    yaxis_title="Beneficiaries",

)
###################################################
###################################################
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
AgeRatio=(r'assets/Age Ratio.xlsx')
df2= pd.read_excel(AgeRatio)
fig4 = px.bar(df2, x='Year', y='Beneficiaries',color="Age", barmode="group")

colors3 = {'Under Ten':'#FF0000',
          'Ten to Twenty':'#FFA500',
          'Above Twenty':'#90EE90'
         }
fig4=go.Figure()
for k in df2['Age'].unique():
    df2p = df2[df2['Age']==k]
    fig4.add_traces(go.Bar(x=df2p['Year'], y = df2p['Beneficiaries'], name=k,
                         marker_color=colors3[k]))
fig4.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)
fig4.update_layout(
    xaxis_title="Age",
    yaxis_title="Beneficiaries",

)

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
                html.H3('ADP India', style={'margin-bottom': '0px', 'color': 'red','font-family':'Playfair','font-size': '100px','textAlign': 'center'}),
                html.H5('Corporate Social Responsibility Scorecard 2020', style={'margin-bottom': '0px', 'color': 'blue','textAlign': 'center'})
            ])

        ], className='one-halfc column', id='title'),

        html.Div([
            html.H6('Last Updated: 9th July, 2021',
                    style={'color': 'black','textAlign': 'center'})
        ], className='one-third column', id='title1')
        ],id='header',className='row flex-display', style ={'margin-bottom': '25px'}),
##########################################################################
    html.Div([
        html.Div([
            html.H6(children='Current CSR Projects:',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),

        ], className='card_container thirteen columns'),
    ], className='row flex display'),
##########################################################################
    html.Div([
        html.Div([
            html.H4(
                children='- MIDAS(Pratham) : Supporting schools with quality education, digital literacy and infrastructural enhancements.',
                style={'textAlign': 'center',
                       'color': 'blue',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children='- PSS Trust : Scholarship programme to support the education and employability cause of 62 academically well-performing undergrads from underprivileged backgrounds. ',
                style={'textAlign': 'center',
                       'color': 'blue',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children='-Aashray Akruti: Education, counselling, and hearing aid support to 70 hearing impaired children.',
                style={'textAlign': 'center',
                       'color': 'blue',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),

            html.H4(
                children='- SriVidhyaSchool for Special Children: Educational support for autistic youth.',
                style={'textAlign': 'center',
                       'color': 'blue',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),

        ], className='card_container six columns'),

        ####################################################
html.Div([
    html.H4(
        children="- Nirmaan(Jeevika): Funding for a Vocational centre for women ",
        style={'textAlign': 'center',
               'color': 'blue',
               'font-family': 'Helvetica',
               'font-size': '30 px'}),
    html.H4(
        children='- ARUN: Provision of three shelter homes for those in need.',
        style={'textAlign': 'center',
               'color': 'blue',
               'font-family': 'Helvetica',
               'font-size': '30 px'}),
    html.H4(
        children='- Cheyutha: Educational support to children impacted by HIV.',
        style={'textAlign': 'center',
               'color': 'blue',
               'font-family': 'Helvetica',
               'font-size': '30 px'}),
    html.H4(
        children='- Katalyst India: Training female students for leadership roles through professional education.',
        style={'textAlign': 'center',
               'color': 'blue',
               'font-family': 'Helvetica',
               'font-size': '30 px'}),
    html.H4(
        children='- IandEye: Education, employability and self-reliance training to visually impaired youth.',
        style={'textAlign': 'center',
               'color': 'blue',
               'font-family': 'Helvetica',
               'font-size': '30 px'}),


            ], className='card_container six columns')

    ], className='row flex display'),
#########################################################################
     html.Div([
            html.Div([
                html.H6(children='Coverage of Sustainable Development Goals',
                        style={'textAlign':'center',
                               'color':'orange',
                                'font-family':'Helvetica',
                                 'font-size': '40px'}),

                html.H4(children='-17 Goals set by the UN General Assembly in 2015, to be achieved by 2030. ADP currently supports 6.',
                        style={'textAlign':'center',
                               'color': 'black',
                               'font-family': 'Helvetica',
                               'font-size': '30 px'}),

                html.Img(src=app.get_asset_url('SDG1.jpg'),
                         id='SDGFIG',
                         style={'height': '500px',
                                'width': 'auto',
                                'margin-bottom': '0px'}
                         ),

                html.Img(src=app.get_asset_url('SDG2.jpg'),
                         id='SDGFIG2',
                         style={'height': '500px',
                                'width': 'auto',
                                'margin-bottom': '0px'}
                         ),
                html.Img(src=app.get_asset_url('SDG3.jpg'),
                         id='SDGFIG3',

                         style={'height': '500px',
                                'width': 'auto',
                                'margin-bottom': '0px',
                                'margin-left': '400px',
                                'margin-right':'auto',
                                }
                         )
                ],className='card_container thirteen columns'),


        ],className='row flex display'),
#########################################################
     html.Div([
        html.Div([
            html.H6(children='CSR Spend over time',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(
                children='-Decrease in 2020 observed due to a change in accounting standards, combined with a reduction in ARUN Spending.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            dcc.Graph(

                        id='graph-1',
                        figure=fig1)

            ],className='card_container thirteen columns')

    ], className='row flex display'),

############################################################
    html.Div([
        html.Div([
            html.H6(children='Direct Beneficiaries over time',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(
                children='-Should ideally be linear.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children='-Drop in 2019 due to discontinuation of the Bhoomika helpline.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children="-Drop in 2020 due to Covid19's impact on education, causing a loss of 4500 beneficiaries.",
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            dcc.Graph(

                id='graph-2',
                figure=fig2)

        ], className='card_container thirteen columns')

    ], className='row flex display'),
    
########################################################################
     html.Div([
        html.Div([
            html.H6(children='Gender Ratio of Direct Beneficiaries',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(
                children='-Gradual shift to more female beneficiaries',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            dcc.Graph(

                id='graph-3',
                figure=fig3)

        ], className='card_container six columns'),
        ####################################################
html.Div([
            html.H6(children='Age Distribution of Direct Beneficiaries',
                    style={'textAlign': 'center',
                            'color': 'orange',
                            'font-family': 'Helvetica',
                            'font-size': '40px'}),

            html.H4(children='-A high focus on education leading to a large number of beneficiaries who are below the age of twenty.',
                     style={'textAlign': 'center',
                     'color': 'black',
                     'font-family': 'Helvetica',
                     'font-size': '30 px'}),

                    dcc.Graph(

                    id='graph-4',
                    figure=fig4)

            ], className='card_container six columns')

    ], className='row flex display'),

###################################################################################
    ],id='mainContainer',style={'display':'flex','flex-direction':'column'})

if __name__ == '__main__':
    app.run_server()
