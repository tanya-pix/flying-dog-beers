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

###########################################################
# SDG COVERAGE OVER TIME
import plotly as plt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import plotly.express as px
import seaborn as sns
import mpld3
plt.style.use('ggplot')
colors = ['#FF0000','#FFA500','#90EE90','#006400','#FF00FF','#4169e1','#add8e6','#FFD700','#696969']

sns.set_palette(sns.color_palette(colors))

SDG=(r'C:\Users\Admin\Desktop\Final Templates for Code\SDG Coverage.xlsx')
df = pd.read_excel(SDG,header=0,names=["Cluster", "Bar", "Bar_part", "Count"])
df = df.groupby(["Cluster", "Bar", "Bar_part"])["Count"].sum().unstack(fill_value=0)


# plotting

clusters = df.index.levels[0]
##
clusters= clusters[0:4:1]
##
inter_graph = 0
maxi = np.max(np.sum(df, axis=1))
total_width = len(df)+inter_graph*(len(clusters)-1)

fig = plt.figure(figsize=(total_width+20,10))
gridspec.GridSpec(1, total_width+10)
axes=[]

ax_position = 0
for cluster in clusters:
    subset = df.loc[cluster]
    ax = subset.plot(kind="bar", stacked=True, width=0.5, ax=plt.subplot2grid((1,total_width), (0,ax_position), colspan=len(subset.index)))
    axes.append(ax)
    ax.set_title(cluster)
    ax.set_xlabel("")
    plt.xticks(rotation= 35,ha='right',fontsize=15)
    plt.subplots_adjust(bottom=0.15)
    ax.set_ylim(0,maxi+1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax_position += len(subset.index)+inter_graph

for i in range(1,len(clusters)):
    axes[i].set_yticklabels("")
    axes[i-1].legend().set_visible(False)



plt.rcParams.update({
    "figure.facecolor": '#DCDCDC',
    "axes.facecolor":  '#DCDCDC',
    "savefig.facecolor": '#DCDCDC',
})

legend = axes[-1].legend(loc='upper left', fontsize=16, framealpha=1).get_frame()
legend.set_linewidth(3)
legend.set_edgecolor("black")
#mpld3.save_html(fig,'SDG.html')

plt.savefig('SDG1.jpg',dpi=300,bbox_inches='tight')
##############################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import plotly.express as px
import seaborn as sns
import mpld3
plt.style.use('ggplot')
colors = ['#FF0000','#FFA500','#90EE90','#006400','#FF00FF','#4169e1','#add8e6','#FFD700','#696969']

sns.set_palette(sns.color_palette(colors))

SDG=(r'C:\Users\Admin\Desktop\Final Templates for Code\SDG Coverage.xlsx')
df = pd.read_excel(SDG,header=0,names=["Cluster", "Bar", "Bar_part", "Count"])
df = df.groupby(["Cluster", "Bar", "Bar_part"])["Count"].sum().unstack(fill_value=0)


# plotting

clusters = df.index.levels[0]
##
clusters= clusters[4:7:1]
##
inter_graph = 0
maxi = np.max(np.sum(df, axis=1))
total_width = len(df)+inter_graph*(len(clusters)-1)

fig = plt.figure(figsize=(total_width+20,10))
gridspec.GridSpec(1, total_width+10)
axes=[]

ax_position = 0
for cluster in clusters:
    subset = df.loc[cluster]
    ax = subset.plot(kind="bar", stacked=True, width=0.5, ax=plt.subplot2grid((1,total_width), (0,ax_position), colspan=len(subset.index)))
    axes.append(ax)
    ax.set_title(cluster)
    ax.set_xlabel("")
    plt.xticks(rotation= 35,ha='right',fontsize=15)
    plt.subplots_adjust(bottom=0.15)
    ax.set_ylim(0,maxi+1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax_position += len(subset.index)+inter_graph

for i in range(1,len(clusters)):
    axes[i].set_yticklabels("")
    axes[i-1].legend().set_visible(False)



plt.rcParams.update({
    "figure.facecolor": '#DCDCDC',
    "axes.facecolor":  '#DCDCDC',
    "savefig.facecolor": '#DCDCDC',
})

legend = axes[-1].legend(loc='upper left', fontsize=16, framealpha=1).get_frame()
legend.set_linewidth(3)
legend.set_edgecolor("black")
#mpld3.save_html(fig,'SDG.html')

plt.savefig('SDG2.jpg',dpi=300,bbox_inches='tight')

##############################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import plotly.express as px
import seaborn as sns
import mpld3
plt.style.use('ggplot')
colors = ['#FF0000','#FFA500','#90EE90','#006400','#FF00FF','#4169e1','#add8e6','#FFD700','#696969']

sns.set_palette(sns.color_palette(colors))

SDG=(r'C:\Users\Admin\Desktop\Final Templates for Code\SDG Coverage.xlsx')
df = pd.read_excel(SDG,header=0,names=["Cluster", "Bar", "Bar_part", "Count"])
df = df.groupby(["Cluster", "Bar", "Bar_part"])["Count"].sum().unstack(fill_value=0)


# plotting

clusters = df.index.levels[0]
##
clusters= clusters[7::1]
##
inter_graph = 0
maxi = np.max(np.sum(df, axis=1))
total_width = len(df)+inter_graph*(len(clusters)-1)

fig = plt.figure(figsize=(total_width+20,10))
gridspec.GridSpec(1, total_width+10)
axes=[]

ax_position = 0
for cluster in clusters:
    subset = df.loc[cluster]
    ax = subset.plot(kind="bar", stacked=True, width=0.5, ax=plt.subplot2grid((1,total_width), (0,ax_position), colspan=len(subset.index)))
    axes.append(ax)
    ax.set_title(cluster)
    ax.set_xlabel("")
    plt.xticks(rotation= 35,ha='right',fontsize=15)
    plt.subplots_adjust(bottom=0.15)
    ax.set_ylim(0,maxi+1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax_position += len(subset.index)+inter_graph

for i in range(1,len(clusters)):
    axes[i].set_yticklabels("")
    axes[i-1].legend().set_visible(False)



plt.rcParams.update({
    "figure.facecolor": '#DCDCDC',
    "axes.facecolor":  '#DCDCDC',
    "savefig.facecolor": '#DCDCDC',
})

legend = axes[-1].legend(loc='upper left', fontsize=16, framealpha=1).get_frame()
legend.set_linewidth(3)
legend.set_edgecolor("black")
#mpld3.save_html(fig,'SDG.html')

plt.savefig('SDG3.jpg',dpi=300,bbox_inches='tight')
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
SexRatio=(r'C:\Users\Admin\Desktop\Final Templates for Code\Sex Ratio.xlsx')
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
fig3.show()
###################################################
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
AgeRatio=(r'C:\Users\Admin\Desktop\Final Templates for Code\Age Ratio.xlsx')
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

#####################################################
##Employability of Beneficiaries
Emp= (r"C:\Users\Admin\Desktop\Final Templates for Code\% employed.xlsx")
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
field= (r'C:\Users\Admin\Desktop\Final Templates for Code\IT vs Non IT.xlsx')
df_field = pd.read_excel(field,header=0,names=['Field','Katalyst India', 'PSS','IandEye','Total'])
fig6 = px.pie(df_field, values='Total', names='Field',color_discrete_sequence=px.colors.sequential.Purp)
fig6.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
)
####################################################
#self-sufficiency in ARUN beneficiaries
self_sufficiency= r'C:\Users\Admin\Desktop\Final Templates for Code\Self Sufficiency.xlsx'
df_self_sufficiency = pd.read_excel(self_sufficiency,sheet_name='Input for Code')
fig7 = px.bar(df_self_sufficiency, x='Project', y='Percentage Of Beneficiaries',color='Project', color_discrete_sequence=['#000764','#f0250e','#FFA500'])
fig7.update_layout(
    paper_bgcolor='#DCDCDC',
    plot_bgcolor='#DCDCDC'
    )
fig7.update_xaxes(visible=False, showticklabels=False)
####################################################
# Digital Access

Digital= (r'C:\Users\Admin\Desktop\Final Templates for Code\Digital Empowerment.xlsx')
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
FocusAreas= (r"C:\Users\Admin\Desktop\Final Templates for Code\Focus Areas.xlsx")
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

A = r'C:\Users\Admin\Desktop\Final Templates for Code\Payroll giving - Amount-Scatter.xlsx'
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

B= r"C:\Users\Admin\Desktop\Final Templates for Code\Payroll giving- Number.xlsx"
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
MIDAS= r"C:\Users\Admin\Desktop\Final Templates for Code\MIDAS.xlsx"
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
                html.H3('ADP India', style={'margin-bottom': '0px', 'color': 'red','font-family':'Playfair','font-size': '100px'}),
                html.H5('Corporate Social Responsibility Scorecard 2020', style={'margin-bottom': '0px', 'color': 'blue'})
            ])

        ], className='one-halfc column', id='title'),

        html.Div([
            html.H6('Last Updated: 9th July, 2021',
                    style={'color': 'black'})
        ], className='one-third column', id='title1')
        ],id='header',className='row flex-display', style ={'margin-bottom': '25px'}),
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

    
   ##########################
    ],id='mainContainer',style={'display':'flex','flex-direction':'column'})

if __name__ == '__main__':
    app.run_server()
