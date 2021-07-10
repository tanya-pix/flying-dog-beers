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
from graphviz import Digraph
import pydot

####
dot_source = """
digraph {
 graph [bgcolor="#DCDCDC"]
 node [style=filled, fillcolor="#C4A484"] 
"MIDAS In 2020" -> "Pune"
"MIDAS In 2020"-> "Hyderabad"
"MIDAS In 2020" -> "PraDigi App"
"PraDigi App"-> "400 Videos in Telegu"->"100 Digital Devices Provided per location"
"Pune"-> "7762 Students"
"7762 Students"-> "STAR Programme"
"STAR Programme"-> "210 Students receiving career guidance per location"
"7762 Students"-> "Community Learning Hubs"
"Community Learning Hubs"-> "2500 Students reached per location"
"7762 Students"-> "30 Schools"
"30 Schools"-> "12 Model Schools"
"30 Schools"-> "Classrooms Painted in 12"-> "Washrooms Built in 6"-> "Solar Panels Installed in 4"-> "Computer Labs built in 10"-> "Library Provided in 10"->  "Thematic Paintings in 6"-> "Outdoor Play Equipment installed in 12"-> "Sports Kits provided in 12"-> "Water Purifiers installed in 5"-> "Science Labs constructed in 3"-> "Automatic Sanitizer Units Installed in 32"
"Hyderabad"-> "12705 Students"
"12705 Students"-> "STAR Programme"
"12705 Students"-> "Community Learning Hubs"
"12705 Students"-> "33 Schools"
"33 Schools"-> "22 Model Schools"
"33 Schools"-> "Classrooms Painted in 21"->"Washrooms built in 5"-> "Solar Panels Installed in 7"-> "Tables and Chairs bought for 2"-> "Computer Labs built in 11"-> "Science Labs constructed in 7"-> "Library Provided in 26"-> "Thematic Paintings in 19"-> "Outdoor Play Equipment Installed in 12"-> "Sports Kits provided in 18"->"Water Purifiers installed in 7"-> "Automatic Sanitizer Units Installed in 33"
"PraDigi App" [style=filled, fillcolor="orange"]
"400 Videos in Telegu"[style=filled, fillcolor="orange"]
"12 Model Schools"[style=filled, fillcolor="#32CD32"]
"30 Schools"[style=filled, fillcolor="#FF0000"]
"22 Model Schools"[style=filled, fillcolor="#32CD32"]
"33 Schools"[style=filled, fillcolor="#FF0000"]
"MIDAS In 2020"[style=filled, fillcolor="orange"]
"STAR Programme"[style=filled, fillcolor="orange"]
"Community Learning Hubs"[style=filled, fillcolor="orange"]
"100 Digital Devices Provided per location"[style=filled, fillcolor="orange"]
"2500 Students reached per location"[style=filled, fillcolor="orange"]
"210 Students receiving career guidance per location"[style=filled, fillcolor="orange"]
"Pune"[style=filled, fillcolor="#ffdf00"]
"Hyderabad"[style=filled, fillcolor="#4169e1"]
"7762 Students"[style=filled, fillcolor="#ffdf00"]
"12705 Students"[style=filled, fillcolor="#4169e1"]
}
"""



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
###

#####################################################
##Employability of Beneficiaries
Emp= (r"assets/% employed.xlsx")
df3 = pd.read_excel(Emp,header=0)
df3.dropna(axis=1, how='any', inplace=True)

fig5 = px.scatter(
    df3, x='Year', y='Percentage', opacity=0.99,
    trendline="ols", trendline_color_override='red',
)
fig5.update_traces(marker=dict(size=20,color='orange',symbol='star'))
fig5.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)

####################################################
#field of education
field= (r'assets/IT vs Non IT.xlsx')
df_field = pd.read_excel(field,header=0,names=['Field','Katalyst India', 'PSS','IandEye','Total'])
fig6 = px.pie(df_field, values='Total', names='Field',color_discrete_sequence=px.colors.sequential.Purp)
fig6.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)
####################################################
#self-sufficiency in ARUN beneficiaries
self_sufficiency= r'assets/Self Sufficiency.xlsx'
df_self_sufficiency = pd.read_excel(self_sufficiency,sheet_name='Input for Code')
fig7 = px.bar(df_self_sufficiency, x='Project', y='Percentage Of Beneficiaries',color='Project', color_discrete_sequence=['#000764','#f0250e','#FFA500'])
fig7.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
    )
fig7.update_xaxes(visible=False, showticklabels=False)
####################################################
# Digital Access

Digital= (r'assets/Digital Empowerment.xlsx')
df_digital = pd.read_excel(Digital,header=0)
df_digital.dropna(axis=1, how='any', inplace=True)

fig8 = px.scatter(
    df_digital, x='Year', y='Beneficiaries', opacity=0.99,
    trendline="ols", trendline_color_override='orange',
)
fig8.update_traces(marker=dict(size=20,color='green',symbol='star-diamond'))
fig8.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
    )
####################################################
##Amount spent per focus Area
FocusAreas= (r"assets/Focus Areas.xlsx")
df_focus = pd.read_excel(FocusAreas,sheet_name='Sheet1')

fig9 = px.bar(df_focus, x="Year", y="Amount", color="Focus Area", barmode="group",color_discrete_map=
        {"Education":'#FF0000',
          "Women's_Empowerment":'#FFA500',
          "Citizen Initiatives":'#90EE90'
         })
fig9.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)
fig9.update_traces(marker_line_width=0)
fig9.update_yaxes(tickprefix="₹")
fig9.update_yaxes(tickformat=".f")
#################################################
##Beneficiaries per focus area


fig10 = px.bar(df_focus, x="Year", y="Beneficiaries", color="Focus Area", barmode="group",color_discrete_map=
        {"Education":'#FF0000',
          "Women's_Empowerment":'#ffa500',
          "Citizen Initiatives":'#90EE90'
         })

fig10.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)
fig10.update_traces(marker_line_width=0)

####################################################
# Payroll Giving Amount

A = r'assets/Payroll giving - Amount-Scatter.xlsx'
dfA = pd.read_excel(A)

fig11 = px.line(dfA, x="Year", y="Amount contributed by Associates")
fig11['data'][0]['line']['color'] = 'orange'

fig11.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
 )
fig11.update_yaxes(tickprefix="₹")
fig11.update_yaxes(tickformat=".f")
###################################################
#Payroll Giving Number-Hyderabad

B= r"assets/Payroll giving- Number.xlsx"
dfB = pd.read_excel(B, sheet_name='Hyderabad')

fig12 = px.line(dfB, x="Year", y="Number of Contributors ")
fig12['data'][0]['line']['color'] = 'orange'

fig12.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
 )
# Payroll Giving Number-Pune
dfC = pd.read_excel(B, sheet_name='Pune')

fig13 = px.line(dfC, x="Year", y="Number of Contributors ")
fig13['data'][0]['line']['color'] = 'orange'

fig13.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
 )
#################################################
# MIDAS- Number of Students
MIDAS= r"assets/MIDAS.xlsx"
df_Students= pd.read_excel(MIDAS, sheet_name='Students')

fig14 = px.line(df_Students, x="Year", y="Students")
fig14['data'][0]['line']['color'] = 'blue'

fig14.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
 )
# MIDAS- Amount Contributed

df_Amount= pd.read_excel(MIDAS, sheet_name='Amount')

fig15 = px.line(df_Amount, x="Year", y="Amount Contributed")
fig15['data'][0]['line']['color'] = 'blue'

fig15.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
 )
fig15.update_yaxes(tickprefix="₹")
fig15.update_yaxes(tickformat=".f")
##################################################
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
 ########
       html.Div([
        html.Div([
            html.H6(children='Employability of Direct Beneficiaries',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(
                children='-Data from IandEye, Nirmaan and ARUN.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children='-A positive trend observed, from close to 2% of Beneficiaries being placed in 2015 to around 48% in 2020.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children='-Sudden spike in 2016 due to collaboration with Nirmaan, a project in which employability is relatively high.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            dcc.Graph(

                id='graph-5',
                figure=fig5)

        ], className='card_container six columns'),
        ####################################################
html.Div([
            html.H6(children='Field of education of Beneficiaries',
                    style={'textAlign': 'center',
                            'color': 'orange',
                            'font-family': 'Helvetica',
                            'font-size': '40px'}),

            html.H4(children='- Data from PSS Trust, Katalyst India and IandEye.',
                style={'textAlign': 'center',
               'color': 'black',
               'font-family': 'Helvetica',
               'font-size': '30 px'}),

                    dcc.Graph(

                    id='graph-6',
                    figure=fig6)

            ], className='card_container six columns')

    ], className='row flex display'),


###############################################################################
    html.Div([
        html.Div([
            html.H6(children='Self-Sufficiency in ARUN Beneficiaries',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(children='-Measured by the possession of Aadhaar accounts which are necessary to avail government support.',
                    style={'textAlign': 'center',
                           'color': 'black',
                           'font-family': 'Helvetica',
                           'font-size': '30 px'}),
            dcc.Graph(

                id='graph-7',
                figure=fig7)

        ], className='card_container six columns'),
        ####################################################
html.Div([
            html.H6(children='Enabling Digital Access',
                    style={'textAlign': 'center',
                            'color': 'orange',
                            'font-family': 'Helvetica',
                            'font-size': '40px'}),

            html.H4(children='-‘Leveling out’ of digital access due to Covid19: Only those  digitally connected were able to receive support from ADP.',
                  style={'textAlign': 'center',
                   'color': 'black',
                   'font-family': 'Helvetica',
                   'font-size': '30 px'}),

                    dcc.Graph(

                    id='graph-8',
                    figure=fig8)

            ], className='card_container six columns')

    ], className='row flex display'),


####################################################################

    html.Div([
        html.Div([
            html.H6(children='Progress on Focus Areas',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(
                children="-Three focus areas: Woman's Empowerment, Education, and Citizen Initiatives.",
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            html.H4(
                children="(Each project falls under only one of the three initiatives)",
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),

        ], className='card_container thirteen columns'),
    ], className='row flex display'),
######################################################################
    html.Div([
        html.Div([
            html.H6(children='Amount Spent per Focus Area',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),

            dcc.Graph(

                id='graph-9',
                figure=fig9)

        ], className='card_container six columns'),

html.Div([
            html.H6(children='Beneficiaries per Focus Area',
                    style={'textAlign': 'center',
                            'color': 'orange',
                            'font-family': 'Helvetica',
                            'font-size': '40px'}),

                    dcc.Graph(

                    id='graph-10',
                    figure=fig10)

            ], className='card_container six columns')

    ], className='row flex display'),
#####################################################################

    html.Div([
        html.Div([
            html.H6(children='Payroll Giving',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H4(
                children='-We urge you to contribute! Payroll Contributions are used to fund IandEye and The SriVidhya School.',
                style={'textAlign': 'center',
                       'color': 'black',
                       'font-family': 'Helvetica',
                       'font-size': '30 px'}),
            dcc.Graph(

                id='graph-11',
                figure=fig11)

        ], className='card_container thirteen columns')

    ], className='row flex display'),

######################################################################
    html.Div([
        html.Div([
            html.H6(children='Contributors from Hyderabad',
                    style={'textAlign': 'center',
                           'color': 'green',
                           'font-family': 'Helvetica',
                           'font-size': '30px'}),

            dcc.Graph(

                id='graph-12',
                figure=fig12)

        ], className='card_container six columns'),
        ####################################################
html.Div([
            html.H5(children='Contributors from Pune',
                    style={'textAlign': 'center',
                            'color': 'green',
                            'font-family': 'Helvetica',
                            'font-size': '30px'}),

                    dcc.Graph(

                    id='graph-13',
                    figure=fig13)

            ], className='card_container six columns')

        ], className='row flex display'),

##################################################################
    html.Div([
        html.Div([
            html.H6(children='Flagship Programme: MIDAS',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),
            html.H5(children='“Many companies can fund our programs and provide monetary help to support our work. But what makes ADP a great partner is their longterm involvement and continued interest in the work we’re doing and the lives we’re trying to improve.” ',
                    style={'textAlign': 'center',
                           'color': 'green',
                           'font-family': 'Helvetica',
                           'font-size': '25px'}),
            html.H4(children='-Nandini Dasgupta: lead of Corporate Fundraising, Pratham India ',
                    style={'textAlign': 'center',
                           'color': 'blue',
                           'font-family': 'Helvetica',
                           'font-size': '20px'}),
            html.H4(children='Source: Management ReThink : December 2020| Volume 01 Issue 01 ',
                    style={'textAlign': 'center',
                           'color': 'blue',
                           'font-family': 'Helvetica',
                           'font-size': '15px'}),

        ], className='card_container thirteen columns'),
    ], className='row flex display'),
#################################################################

###############################################################
    html.Div([
        html.Div([
            html.H6(children='Students per year',
                    style={'textAlign': 'center',
                           'color': 'green',
                           'font-family': 'Helvetica',
                           'font-size': '30px'}),

            dcc.Graph(

                id='graph-14',
                figure=fig14)

        ], className='card_container six columns'),
        ####################################################
html.Div([
            html.H5(children='Amount Contributed per year',
                    style={'textAlign': 'center',
                            'color': 'green',
                            'font-family': 'Helvetica',
                            'font-size': '30px'}),
            dcc.Graph(

            id='graph-15',
            figure=fig15)

            ], className='card_container six columns')

        ], className='row flex display'),

###################################################################################
    html.Div([
        html.Div([
            html.H6(children='Programme Overview for 2020',
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'font-family': 'Helvetica',
                           'font-size': '40px'}),

            dash_interactive_graphviz.DashInteractiveGraphviz(
                id="graph-16",
                dot_source=dot_source,
                style={'height': '1000px',
                       'width': '1200px'})

        ], className='card_container thirteen columns')

    ], className='row flex display'),
###################################
    ],id='mainContainer',style={'display':'flex','flex-direction':'column'})

if __name__ == '__main__':
    app.run_server()
