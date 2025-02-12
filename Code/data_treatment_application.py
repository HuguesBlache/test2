import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display
from ipywidgets import interact, Dropdown
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import numpy as np
import statistics

#### Delete probleme and value red 

pd.options.mode.chained_assignment = None

###################################### FUNCTION #########################################################

##############plot_category_kpi_2d##########          



def plot_category_kpi_2d(x_axis,y_axis):
    df=Category_KPI.iloc[:, np.r_[1:11]]
    fig = px.scatter(df, x=df[x_axis],y=df[y_axis],color=df.index, log_x=True,log_y=True)
    return fig.show()
   
   
##############plot_technologies##########          


def plot_technologies(x_axis,y_axis):
    fig = px.scatter(technologies_data,text=technologies_data.index, x=x_axis,y=y_axis,color="Range Type", log_x=True,log_y=True)
    return fig.show()
####


##############Application_Categories_Sankey##########

def Application_Categories_Sankey(df):
    Specifique=df['Acronym']
    Application=df['Category']
    Color=df['Color']
    Source=[]
    Target=[]
    index=[]
    Col=[]

    Specifique=list(set(Specifique))
    Application=list(set(Application))


    for h in range(0,len(df["Acronym"])):
        for i in range(0,len(Application)):
            for j in range(0,len(Specifique)):
                if df["Category"][h]==Application[i] and df["Acronym"][h]==Specifique[j]:
                    Source.append(j)
                    Target.append(len(Specifique)+i)
                    Col.append(Color[j])
                    index.append(j)


    for i in range(0,len(Source)):
        for j in range(0,len(Source)):
            if Source[i]==Source[j] and Target[i]==Target[j]  and i!=j:
                Source[j]="Nan"
                Target[j]="Nan"
    label1=Specifique


    for i in range(0,len(Application)):
        label1.append(Application[i])

    Value=[1 for i in range(len(Source))]
    
    fig = go.Figure(data=[go.Sankey(
        orientation="h",
        valueformat = ".0f",


        hoverlabel = dict (
            align="left",
            bordercolor='black'
        ),
        node = dict(
          pad = 300,


          thickness = 30,

          line = dict(color = "black", width = 1),

          label = label1,

          color = "white",


        ),
        link = dict(
          source = Source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = Target,
          value = Value,
          color=df['Color'],
      )
    )])

    fig.update_layout(font_size=20, width=1000,
    height=2000)
    
    return fig

##############Application_KPI_Sankey##########

def Application_KPI_Sankey(KPI):
    Specifique=df['Name']
    Application=df[KPI]
    Color=df['Color']
    Source=[]
    Target=[]
    index=[]
    Col=[]

    Specifique=list(set(Specifique))
    Application=list(set(Application))


    for h in range(0,len(df["Name"])):
        for i in range(0,len(Application)):
            for j in range(0,len(Specifique)):
                if df[KPI][h]==Application[i] and df["Name"][h]==Specifique[j]:
                    Source.append(j)
                    Target.append(len(Specifique)+i)
                    Col.append(Color[j])
                    index.append(j)


    for i in range(0,len(Source)):
        for j in range(0,len(Source)):
            if Source[i]==Source[j] and Target[i]==Target[j]  and i!=j:
                Source[j]="Nan"
                Target[j]="Nan"
    label1=Specifique


    for i in range(0,len(Application)):
        label1.append(Application[i])

    Value=[1 for i in range(len(Source))]
    
    fig = go.Figure(data=[go.Sankey(
        orientation="h",
        valueformat = ".0f",


        hoverlabel = dict (
            align="left",
            bordercolor='black'
        ),
        node = dict(
          pad = 300,


          thickness = 30,

          line = dict(color = "black", width = 1),

          label = label1,

          color = "white",


        ),
        link = dict(
          source = Source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = Target,
          value = Value,
          color=df['Color'],
      )
    )])

    fig.update_layout( font_size=10, width=1000,
        height=1000)
    
    return fig


##############Application_User_Sankey##########

def Application_User_Sankey(df):
    Specifique=df['Name']
    Application=df['User']
    Color=df['Color']
    Source=[]
    Target=[]
    index=[]
    Col=[]

    Specifique=list(set(Specifique))
    Application=list(set(Application))


    for h in range(0,len(df["Name"])):
        for i in range(0,len(Application)):
            for j in range(0,len(Specifique)):
                if df["User"][h]==Application[i] and df["Name"][h]==Specifique[j]:
                    Source.append(j)
                    Target.append(len(Specifique)+i)
                    Col.append(Color[j])
                    index.append(j)


    for i in range(0,len(Source)):
        for j in range(0,len(Source)):
            if Source[i]==Source[j] and Target[i]==Target[j]  and i!=j:
                Source[j]="Nan"
                Target[j]="Nan"
    label1=Specifique


    for i in range(0,len(Application)):
        label1.append(Application[i])

    Value=[1 for i in range(len(Source))]
    
    fig = go.Figure(data=[go.Sankey(
        orientation="h",
        valueformat = ".0f",


        hoverlabel = dict (
            align="left",
            bordercolor='black'
        ),
        node = dict(
          pad = 300,


          thickness = 30,

          line = dict(color = "black", width = 1),

          label = label1,

          color = "white",


        ),
        link = dict(
          source = Source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = Target,
          value = Value,
          color=df['Color'],
      )
    )])

    fig.update_layout(font_size=15, width=1000,
        height=1200)
    
    return fig
    
    

##############bar_attribut########## 


def bar_attribut(attribut):
    a=application_data[['Passenger','Commercial Vehicle Driver','Cyclist','Motorcyclist','Pedestrian','Public Transit','Driver/Car','Emergency vehicle']].count()
    b=application_data[['Limited Access Highways','Roads with at-grade crossings','Intersections']].count()
    c=application_data[['Automated','Connected information','Connected coordination']].count()
    _partie_ = {
    
    #Application chose
    'User Types':go.Figure(data=[go.Bar(x=a.index, y=a,text=a,textposition='auto')]),
            
    #Technologie chose    
    'Road Types':go.Figure(data=[go.Bar(x=b.index, y=b,text=b,textposition='auto')]),
    
    #Fusion chose 
    'Application Mechanisms':go.Figure(data=[go.Bar(x=c.index, y=c,text=c,textposition='auto')])}
    


    return _partie_[attribut].show()
    
    
    

##############boxplot_distribution##########     


def boxplot_category(test,application_categories):
    new_test=test.rename({'Application': 'Acronym'}, axis=1)
    application_categories_new=application_categories[['Acronym','Category','Color']]
    fusion_tech_category=application_categories_new.merge(new_test,on='Acronym')
    boxtest=new_test.drop_duplicates()
    boxplot_fusion=boxtest.groupby(['Acronym']).count()
    plot_box=application_categories_new.merge(boxplot_fusion,on="Acronym")
    Catagory_sort=plot_box.groupby('Category').median().reset_index().sort_values(['Technology'])
    size_categrory_merge=plot_box.groupby('Category').count().reset_index().merge(Catagory_sort,on="Category")
    array_name=size_categrory_merge.sort_values(['Technology_y','Technology_x'], ascending=[True, False])
    #plot_box=plot_box.sort_values(['Technology'])
    fig=px.box(plot_box,y='Technology', x='Category',color='Category')
    fig.update_layout(
                   yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
        title='Number of usable technologies'
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),

    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
                  showlegend=False)
    fig.update_xaxes(categoryorder='array',categoryarray=array_name['Category'])
    return fig

    
    

##############Category_Parallel_Cordianate##########     
   
def Category_Parallel_Cordianate(Category):    
    df1=Category_KPI[Category_KPI.index==Category]
    b=df1.index    
    new_list1 = [] 
    for i in b : 
        if i not in new_list1: 
            new_list1.append(i) 
            
    a=df1["Count"]    
    new_list = [] 
    for i in a : 
        if i not in new_list: 
            new_list.append(i) 


    c=df1["Messaging Type"]    
    new_list2 = [] 
    for i in c : 
        if i not in new_list2: 
            new_list2.append(i) 
    d=df1["MeCount"]    
    new_list3 = [] 
    for i in d : 
        if i not in new_list3: 
            new_list3.append(i)     
            
            
    #########'Message size up (bits)'#############

    test=df1['Message size up (bits)']
    for j in range(0,len(test)):
        if not test[j]>0:
            test[j]=200
    index_message_up=[]
    for i in df1['Message size up (bits)'].drop_duplicates().sort_values( ascending=False):
        if i==0:
            index_message_up.append('nan')
        else:
            index_message_up.append(i)
            
            
#########Message Period (ms)#############

    test1=df1['Message Period (ms)']
    for j in range(0,len(test1)):
        if not test1[j]>0:
            test1[j]=0
    index_Period=[]
    for i in df1['Message Period (ms)'].drop_duplicates().sort_values( ascending=False):
        if i==0:
            index_Period.append('nan')
        else:
            index_Period.append(i)

#########Message Frequency (msg/sec)#############


    test2=df1['Message Frequency (msg/sec)']
    for j in range(0,len(test2)):
        if not test2[j]>0:
            test2[j]=0
    index_Frequency=[]
    for i in df1['Message Frequency (msg/sec)'].drop_duplicates().sort_values( ascending=False):
        if i==0:
            index_Frequency.append('nan')
        else:
            index_Frequency.append(i)
        

   
    fig = go.Figure(data=
        go.Parcoords(

            dimensions = list([
                
                dict(range = [min(df1["Max latency (ms)"]),max(df1["Max latency (ms)"])],
                     label = 'Max Latency (ms)', values = df1["Max latency (ms)"]),
                  
                       dict(range = [min(test),max(test)],
    tickvals =  test.drop_duplicates().sort_values( ascending=False),
    label = 'Message size up (bits)',
    values =test,
    ticktext = index_message_up),
                
                dict(range = [min(test1),max(test1)],
    tickvals =  test1.drop_duplicates().sort_values( ascending=False),
    label = 'Message Period (ms)',
    values =test1,
    ticktext = index_Period),
                 dict(range = [min(df1["Range"]),max(df1["Range"])],
                     label = 'Range', values = df1["Range"]),  
             dict(range = [min(test2),max(test2)],
    tickvals =  test2.drop_duplicates().sort_values( ascending=False),
    label = 'Message Frequency (msg/sec)',
    values =test2,
    ticktext = index_Frequency),   

                ])
        )
    )
    return fig.show()
    
##############Category_Parallel_Cordianate_Application##########      
def Category_Parallel_Cordianate_Application(df1):    

    df1["Count"]=1
    a=df1["Count"]
    new_list = [] 
    for i in a : 
        if i not in new_list: 
            new_list.append(i) 


    c=df1["Messaging Type"]    
    new_list2 = [] 
    for i in c : 
        if i not in new_list2: 
            new_list2.append(i) 
    df1["MeCount"]=1
    d=df1["MeCount"]    
    new_list3 = [] 
    for i in d : 
        if i not in new_list3: 
            new_list3.append(i)         


#########'Message size up (bits)'#############

    test=Application_KPI['Message size up (bits)']
    for j in range(0,len(test)):
        if not test[j]>0:
            test[j]=200
    index_message_up=[]
    for i in Application_KPI['Message size up (bits)'].drop_duplicates().sort_values( ascending=False):
        if i==0:
            index_message_up.append('nan')
        else:
            index_message_up.append(i)
            
            
#########Message Period (ms)#############

    test1=Application_KPI['Message Period (ms)']
    for j in range(0,len(test1)):
        if not test1[j]>0:
            test1[j]=0
    index_Period=[]
    for i in Application_KPI['Message Period (ms)'].drop_duplicates().sort_values( ascending=False):
        if i==0:
            index_Period.append('nan')
        else:
            index_Period.append(i)

#########Message Frequency (msg/sec)#############


    test2=Application_KPI['Message Frequency (msg/sec)']
    for j in range(0,len(test2)):
        if not test2[j]>0:
            test2[j]=0
    index_Frequency=[]
    for i in Application_KPI['Message Frequency (msg/sec)'].drop_duplicates().sort_values( ascending=False):
        if i==0:
            index_Frequency.append('nan')
        else:
            index_Frequency.append(i)


####### Fonction ###


    fig = go.Figure(data=
        go.Parcoords(

            dimensions = list([
                
                dict(range = [min(df1["Max latency (ms)"]),max(df1["Max latency (ms)"])],
                     label = 'Max Latency (ms)', values = df1["Max latency (ms)"]),
                  
                       dict(range = [min(test),max(test)],
    tickvals =  test.drop_duplicates().sort_values( ascending=False),
    label = 'Message size up (bits)',
    values =test,
    ticktext = index_message_up),
                
                dict(range = [min(test1),max(test1)],
    tickvals =  test1.drop_duplicates().sort_values( ascending=False),
    label = 'Message Period (ms)',
    values =test1,
    ticktext = index_Period),
                 dict(range = [min(df1["Range"]),max(df1["Range"])],
                     label = 'Range', values = df1["Range"]),  
             dict(range = [min(test2),max(test2)],
    tickvals =  test2.drop_duplicates().sort_values( ascending=False),
    label = 'Message Frequency (msg/sec)',
    values =test2,
    ticktext = index_Frequency),   

                ])
        )
    )
    return fig
    
    
    
    
##############Application_communication_mode##########         
   

def Application_communication_mode(df):
    Specifique=df['Name']
    Application=df['Comm']
    Color=df['Color']
    Source=[]
    Target=[]
    index=[]
    Col=[]

    Specifique=list(set(Specifique))
    Application=list(set(Application))


    for h in range(0,len(df["Name"])):
        for i in range(0,len(Application)):
            for j in range(0,len(Specifique)):
                if df["Comm"][h]==Application[i] and df["Name"][h]==Specifique[j]:
                    Source.append(j)
                    Target.append(len(Specifique)+i)
                    Col.append(Color[j])
                    index.append(j)


    for i in range(0,len(Source)):
        for j in range(0,len(Source)):
            if Source[i]==Source[j] and Target[i]==Target[j]  and i!=j:
                Source[j]="Nan"
                Target[j]="Nan"
    label1=Specifique


    for i in range(0,len(Application)):
        label1.append(Application[i])

    Value=[1 for i in range(len(Source))]
    
    fig = go.Figure(data=[go.Sankey(
        orientation="h",
        valueformat = ".0f",


        hoverlabel = dict (
            align="left",
            bordercolor='black'
        ),
        node = dict(
          pad = 300,


          thickness = 30,

          line = dict(color = "black", width = 1),

          label = label1,

          color = "white",


        ),
        link = dict(
          source = Source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = Target,
          value = Value,
          color=df['Color'],
      )
    )])

    fig.update_layout( font_size=17, width=1000,
        height=1500)
    
    return fig
   
   
##############Communication_Mode_Sankey_Fusion##########            

def Communication_Mode_Sankey_Fusion(fusion):
    Specifique=fusion['Name']
    Application=fusion['Technologies']
    Functions=fusion['Type'] ##Latency
    Specifique=list(set(Specifique))
    Application=list(set(Application))
    Functions=list(set(Functions))
    for i in range(0,len(Functions)-1):
        if Functions[i]=="nan":
            del(Functions[i])
    Source=[]
    Target=[]
    for h in range(0,len(fusion["Name"])):
         for i in range(0,len(Specifique)):
            for j in range(0,len(Functions)):
                if fusion["Name"][h]==Specifique[i] and fusion['Type'][h]==Functions[j]:
                     Source.append(i)
                     Target.append(len(Specifique)+j)
    for h in range(0,len(fusion["Name"])):
        for i in range(0,len(Application)):
             for j in range(0,len(Functions)):
                if fusion['Technologies'][h]==Application[i] and fusion['Type'][h]==Functions[j]:
                    Source.append(len(Specifique)+j)
                    Target.append(len(Specifique)+len(Functions)+i)
    label1=Specifique
    for i in range(0,len(Functions)):
        label1.append(Functions[i])

    for i in range(0,len(Application)):
        label1.append(Application[i])
    Value=[1 for i in range(749*45)]


    a=[]
    for i in range(0,len(fusion['Color_x'])):
        a.append(fusion['Color_y'][i])
    for i in range(0,len(fusion['Color_y'])):
        a.append(fusion['Color_x'][i])


    fig = go.Figure(data=[go.Sankey(
        orientation="h",
        valueformat = ".0f",
        valuesuffix = "TWh",
        node = dict(
          pad = 300,


          thickness = 12,
          line = dict(color = "red", width = 1),
          label = label1,
          color = a
        ),
        link = dict(
          source = Source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = Target,
          value = Value,
          color= a
      )
    )])

    fig.update_layout( font_size=17, width=1000,
        height=1000)
    return fig
    
    

##############Communication_Mode_Technologies_Sankey##########      
def Communication_Mode_Technologies_Sankey(df):
    Specifique=df['Type']
    Application=df['Technologies']
    Specifique=list(set(Specifique))
    Application=list(set(Application))
    Source=[]
    Target=[]
    for h in range(0,len(df["Type"])):
        for i in range(0,len(Application)):
            for j in range(0,len(Specifique)):
                if df["Technologies"][h]==Application[i] and df["Type"][h]==Specifique[j]:
                    Source.append(j)
                    Target.append(len(Specifique)+i)
    for i in range(0,len(Source)):
        for j in range(0,len(Source)):
            if Source[i]==Source[j] and Target[i]==Target[j]  and i!=j:
                Source[j]="Nan"
                Target[j]="Nan"
    label1=Specifique
    for i in range(0,len(Application)):
        label1.append(Application[i])
    Value=[1 for i in range(len(Source))]
    import plotly.graph_objects as go
    fig = go.Figure(data=[go.Sankey(
        orientation="h",
        valueformat = ".0f",
        valuesuffix = "TWh",
        node = dict(
          pad = 300,


          thickness = 12,
          line = dict(color = "black", width = 1),
          label = label1,
          color = "white"
        ),
        link = dict(
          source = Source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = Target,
          value = Value,
         color=df['Color']

      )
    )])

    fig.update_layout( font_size=15, width=1000,
        height=1000)
    return fig

##############plot_bar_category##########      


def plot_bar_category(KPI):
    df=Category_KPI.iloc[:, np.r_[1:11]]
    df = df.reset_index()
    df_percent = df.groupby(['Category', KPI]).size().reset_index()
    df_percent['percentage'] = df.groupby(['Category',KPI]).size().groupby(level=1).apply(lambda x: 100 * x / float(x.sum())).values
    df_percent.columns = ['Category', KPI, 'Counts', 'Percentage']
    fig=px.bar(df_percent, x=KPI, y='Percentage', color='Category',)
    return fig.show()

##############plot_category_kpi_2d##########          



def plot_category_kpi_2d(x_axis,y_axis):
    df=Category_KPI.iloc[:, np.r_[1:11]]
    fig = px.scatter(df, x=df[x_axis],y=df[y_axis],color=df.index, log_x=True,log_y=True)
    return fig.show()
   
   
##############plot_technologies##########          




##############plot_technologies##########          



    return fig.show()

##############tableau_fusion##########          
def tableau_fusion(df):
    fig = go.Figure(data=[go.Table(header=dict(values=['Application', 'Technology']),
                         cells=dict(values=[df['Application'], df['Technology']]))
                         ])
    return fig  
   
##############Technologies_Parallel_Cordianate##########     


def Technologies_Parallel_Cordianate(Range):     
    df=technologies_data[technologies_data["Range Type"]==Range]
    b=df["Range Type"]  
    new_list1 = [] 
    for i in b : 
        if i not in new_list1: 
            new_list1.append(i) 
            
    a=df["Value"]    
    new_list = [] 
    for i in a : 
        if i not in new_list: 
            new_list.append(i) 

    fig = go.Figure(data=
    go.Parcoords(
        
        dimensions = list([
            dict(tickvals = df["Value"],
                 ticktext = df.index,
                 label = "Technology", values = df["Value"]),
          
              dict(range = [min(df['Delay (ms)']),max(df['Delay (ms)'])],
                 label = 'Delay (ms)', values = df['Delay (ms)']),
        
              dict(range = [min(df['Max Range (m)']),max(df['Max Range (m)'])],
                 label = 'Max Range (m)', values = df['Max Range (m)']),
             dict(range = [min(df['Data Rate (Mb/s)']),max(df['Data Rate (Mb/s)'])],
                 label = 'Data Rate (Mb/s)', values = df['Data Rate (Mb/s)']),
            dict(range = [min(df['Frequency Band(s) (GHz)']),max(df['Frequency Band(s) (GHz)'])],
                 label = 'Frequency Band(s) (GHz)', values = df['Frequency Band(s) (GHz)']),
             dict(range = [min(df['Frequency Band(s) (GHz)']),max(df['Frequency Band(s) (GHz)'])],
                 label = 'Frequency Band(s) (GHz)', values = df['Frequency Band(s) (GHz)']),
            ] ) 
        )
    )
    
    
    return fig.show()   

##############bar_technoly_app##########      
  
def bar_technoly_app(test):
    count=test.groupby('Technology').count().reset_index()
    count=count.merge(technologies_data_modif.reset_index()[['Technology','Range Type']],on='Technology')
    fig=px.bar(count,y='Application',x='Technology',color='Range Type', text='Application',pattern_shape="Range Type", pattern_shape_sequence=["\\", "+", "+",""])
    fig.update_layout(
                       yaxis=dict(
            autorange=True,
            showgrid=True,
            zeroline=True,
            dtick=5,
            gridcolor='rgb(255, 255, 255)',
            gridwidth=1,
            zerolinecolor='rgb(255, 255, 255)',
            zerolinewidth=2,
            title='Number of applications',spikecolor="white"
                           
                        
        ),
        margin=dict(
            l=40,
            r=30,
            b=50,
            t=85,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)')
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
    fig.update_traces( textposition='outside')
    fig.update_layout(uniformtext_minsize=5, uniformtext_mode='show')    
    return fig
##################################### END FUNCTION #######################################################



##################################### DATA TRAITEMENT ###################################################

sheet_application_data = "https://docs.google.com/spreadsheets/d/1OfUOVvTzfcZZhlYli21-WmcEfmikRiymsMdYXG2SAA4/edit#gid=386603968"
application_data_url = sheet_application_data.replace('/edit#gid=', '/export?format=csv&gid=')
application_data=pd.read_csv(application_data_url,header=1)
sheet_communication_mode_data = "https://docs.google.com/spreadsheets/d/1OfUOVvTzfcZZhlYli21-WmcEfmikRiymsMdYXG2SAA4/edit#gid=1185192284"
communication_mode_data_url = sheet_communication_mode_data.replace('/edit#gid=', '/export?format=csv&gid=')
communication_mode_data=pd.read_csv(communication_mode_data_url,header=1)
sheet_technologies_data = "https://docs.google.com/spreadsheets/d/1OfUOVvTzfcZZhlYli21-WmcEfmikRiymsMdYXG2SAA4/edit#gid=2129413061"
technologies_data_url = sheet_technologies_data.replace('/edit#gid=', '/export?format=csv&gid=')
technologies_data=pd.read_csv(technologies_data_url,index_col="Technology")

#### DATA TRAITEMENT AND MERGE

### data_treatment_application
for j in application_data.columns:
    for i in range(0,len(application_data[j])):
        if application_data[j][i]=="Yes":
    
            application_data.__getitem__(j).__setitem__(i, j)
colnames = ['Acronym','Category']
application_categories = pd.DataFrame(columns = colnames)
for i in application_data.columns[4:20]:
    for j in range(0,len(application_data[i])):
        if application_data[i][j] is i :
            application_categories=application_categories.append(pd.DataFrame({'Acronym': [application_data['Acronym'][j]],'Category':[application_data[i][j]]}))
## Redefinition des indices
            ind=[i for i in range(len(application_categories))]
application_categories=application_categories.set_index([ind])


## Creer une colomn couleur pour les Sankey... Pour l'instant que des valeurs aléatoires
application_categories["Color"] = np.nan
for i in application_categories['Category']:
    r = lambda: random.randint(150,255)
    b = lambda: random.randint(150,255)
    g= lambda: random.randint(150,255)
    color='#%02X%02X%02X' % (r(),b(),g())
    for j in range(0,len(application_categories)):
        if application_categories['Category'][j]==i:
            application_categories.__getitem__('Color').__setitem__(j, color)

    #### Category_KPI 

    
Category_KPI=pd.merge(application_categories,application_data.iloc[:, np.r_[1,39:49]],on='Acronym')
del(Category_KPI['Acronym'])
Category_KPI.set_index(Category_KPI['Category'],inplace = True)
Category_KPI["Count"]  = np.nan
Category_KPI["MeCount"]  = np.nan
for i in Category_KPI.index:
    for j in range(0,len(Category_KPI)):
        if Category_KPI.index[j]==i:
            Category_KPI.loc.__setitem__((slice(None), ('Count', j)), j+1)

for i in Category_KPI['Priority']:
    for j in range(0,len(Category_KPI)):
        if Category_KPI['Priority'][j]==i:
           Category_KPI.loc.__setitem__((slice(None), ('MeCount', j)), j+1)
			
colnames = ['Name','User']
application_user = pd.DataFrame(columns = colnames)
for i in application_data.columns[23:31]:
    for j in range(0,len(application_data[i])):
        if application_data[i][j] is i :
            application_user=application_user.append(pd.DataFrame({'Name': [application_data['Acronym'][j]],'User':[application_data[i][j]]}))
            
ind=[i for i in range(len(application_user))]
application_user=application_user.set_index([ind])   

    ## Creer une colomn couleur pour les Sankey... Pour l'instant que des valeurs aléatoires
application_user["Color"] = np.nan
for i in application_user['User']:
    r = lambda: random.randint(150,255)
    b = lambda: random.randint(150,255)
    g= lambda: random.randint(150,255)
    color='#%02X%02X%02X' % (r(),b(),g())
    for j in range(0,len(application_user)):
        if application_user['User'][j]==i:
            application_user['Color'][j]=color  
			
			
colnames = ['Name','Comm']
application_communication_mode = pd.DataFrame(columns = colnames)
for i in application_data.columns[50:53]:
    for j in range(0,len(application_data[i])):
        if application_data[i][j] is i :
            application_communication_mode=application_communication_mode.append(pd.DataFrame({'Name': [application_data['Acronym'][j]],'Comm':[application_data[i][j]]}))
## Redefinition des indices
ind=[i for i in range(len(application_communication_mode))]
application_communication_mode=application_communication_mode.set_index([ind])   

    ## Creer une colomn couleur pour les Sankey... Pour l'instant que des valeurs aléatoires
application_communication_mode["Color"] = np.nan
for i in application_communication_mode['Comm']:
    r = lambda: random.randint(150,255)
    b = lambda: random.randint(150,255)
    g= lambda: random.randint(150,255)
    color='#%02X%02X%02X' % (r(),b(),g())
    for j in range(0,len(application_communication_mode)):
        if application_communication_mode['Comm'][j]==i:
            application_communication_mode['Color'][j]=color
			
Application_KPI=application_data.iloc[:, np.r_[0,39:49]]

colnames = ['Name','Road']
application_road = pd.DataFrame(columns = colnames)
for i in application_data.columns[31:34]:
    for j in range(0,len(application_data[i])):
        if application_data[i][j] is i :
            application_road=application_road.append(pd.DataFrame({'Name': [application_data['Acronym'][j]],'Road':[application_data[i][j]]}))
## Redefinition des indices
ind=[i for i in range(len(application_road))]
application_road=application_road.set_index([ind])   

    ## Creer une colomn couleur pour les Sankey... Pour l'instant que des valeurs aléatoires
application_road["Color"] = np.nan
for i in application_road['Road']:
    r = lambda: random.randint(150,255)
    b = lambda: random.randint(150,255)
    g= lambda: random.randint(150,255)
    color='#%02X%02X%02X' % (r(),b(),g())
    for j in range(0,len(application_road)):
        if application_road['Road'][j]==i:
            application_road['Color'][j]=color 
            
            
            
#### data_treatment_communication



for j in communication_mode_data.columns:
    for i in range(0,len(communication_mode_data[j])):
        if communication_mode_data[j][i]=="Yes":
            ##communication_mode_data.loc.__setitem__((slice(None), (j, i)), i)  
            communication_mode_data[j][i]=j
            
colnames = ['Type','Technologies']
communication_mode_technologies = pd.DataFrame(columns = colnames)
for i in communication_mode_data.columns[2:25]:
    for j in range(0,len(communication_mode_data[i])):
        if communication_mode_data[i][j] is i :
            communication_mode_technologies=communication_mode_technologies.append(pd.DataFrame({'Type': [communication_mode_data['Type'][j]],'Technologies':[communication_mode_data[i][j]]}))
## Redefinition des indices
            ind=[i for i in range(len(communication_mode_technologies))]
communication_mode_technologies=communication_mode_technologies.set_index([ind])


## Creer une colomn couleur pour les Sankey... Pour l'instant que des valeurs aléatoires
communication_mode_technologies["Color"] = np.nan
for i in communication_mode_technologies['Type']:
    r = lambda: random.randint(150,255)
    b = lambda: random.randint(150,255)
    g= lambda: random.randint(150,255)
    color='#%02X%02X%02X' % (r(),b(),g())
    for j in range(0,len(communication_mode_technologies)):
        if communication_mode_technologies['Type'][j]==i:
            communication_mode_technologies['Color'][j]=color 
            
            
### data_treatment_mapping

application_communication_mode_columns = application_communication_mode.rename(columns={'Comm': 'Type'})
merge_com_app_tech=pd.merge(communication_mode_technologies, application_communication_mode_columns, on="Type")


application_requirement=application_data.iloc[:, np.r_[1,38:48,50:53]]
application_requirement.set_index("Acronym", inplace = True)
technologies_performances=technologies_data.iloc[:, np.r_[2:16]]
#technologies_performances=technologies_performances.merge(communication_mode_technologies.rename(columns={'Technologies':'Technology'}),on="Technology")
colnames = ['Application','Technology']
test = pd.DataFrame(columns = colnames)
for i in range(0,len(merge_com_app_tech)):
    Name_app=merge_com_app_tech['Name'][i]
    Name_tech=merge_com_app_tech['Technologies'][i]
    if merge_com_app_tech[merge_com_app_tech.Name==Name_app]['Type'][i]=='V2P' and \
    'V2I' not in merge_com_app_tech[merge_com_app_tech.Name==Name_app]['Type'].tolist() and \
    int(application_requirement["Max latency (ms)"][merge_com_app_tech['Name'][i]])>int(technologies_performances["Delay (ms)"][merge_com_app_tech['Technologies'][i]]) and\
    int(application_requirement["Range"][Name_app])<int(technologies_performances["Max Range (m)"][Name_tech])and\
    int(application_requirement["Data Rate"][Name_app])<int(technologies_performances['Data Rate (Mb/s)'][Name_tech]*10**6):
        test=test.append(pd.DataFrame({'Application':[merge_com_app_tech['Name'][i]],"Technology":[merge_com_app_tech['Technologies'][i]]}))
        
        
    elif merge_com_app_tech[merge_com_app_tech.Name==Name_app]['Type'][i]=='V2V' and \
    'V2I' not in merge_com_app_tech[merge_com_app_tech.Name==Name_app]['Type'].tolist() and \
    int(application_requirement["Max latency (ms)"][merge_com_app_tech['Name'][i]])>int(technologies_performances["Delay (ms)"][merge_com_app_tech['Technologies'][i]]) and\
    int(application_requirement["Range"][Name_app])<int(technologies_performances["Max Range (m)"][Name_tech])and\
    int(application_requirement["Data Rate"][Name_app])<int(technologies_performances['Data Rate (Mb/s)'][Name_tech]*10**6):
        test=test.append(pd.DataFrame({'Application':[merge_com_app_tech['Name'][i]],"Technology":[merge_com_app_tech['Technologies'][i]]}))
    
    elif 'V2I' in merge_com_app_tech[merge_com_app_tech.Name==Name_app]['Type'].tolist() and int(application_requirement["Max latency (ms)"][merge_com_app_tech['Name'][i]])>int(technologies_performances["Delay (ms)"][merge_com_app_tech['Technologies'][i]]) and\
    int(application_requirement["Data Rate"][Name_app])<int(technologies_performances['Data Rate (Mb/s)'][Name_tech]*10**6):
         if int(application_requirement["Range"][merge_com_app_tech['Name'][i]])<int(technologies_performances["Max Range (m)"][merge_com_app_tech['Technologies'][i]]) and\
         technologies_performances["Dense Deployment"][Name_tech]=='No':
            test=test.append(pd.DataFrame({'Application':[merge_com_app_tech['Name'][i]],"Technology":[merge_com_app_tech['Technologies'][i]]}))
         elif technologies_performances["Dense Deployment"][Name_tech]=='Yes':
            test=test.append(pd.DataFrame({'Application':[merge_com_app_tech['Name'][i]],"Technology":[merge_com_app_tech['Technologies'][i]]})) 
    
test=test.drop_duplicates()

## Treatement Techologie

technologies_data_modif=technologies_data
technologies_data_modif["Value"]  = np.nan

for i in technologies_data_modif.index:
    for j in range(0,len(technologies_data_modif)):
        if technologies_data_modif.index[j]==i:
            technologies_data_modif['Value'][j]=j+1
            
### Matrice PIVOT

percentage_category_tech=application_categories.merge(test.rename(columns={'Application':'Acronym'}),on="Acronym").groupby(['Category','Technology']).size().reset_index()
percentage_category_tech['Percentage']=np.nan
for i in range(0,len(percentage_category_tech['Category'])):
    percentage_category_tech['Percentage'][i]=100*percentage_category_tech[0][i]/max(percentage_category_tech[percentage_category_tech['Category']==percentage_category_tech['Category'][i]][0])
pivot_percentage=percentage_category_tech.pivot(index='Technology', columns='Category', values='Percentage').round(1)
for i in pivot_percentage.columns:
    for j in pivot_percentage.index:
        if np.isnan(pivot_percentage[i][j]):
            pivot_percentage[i][j]=0

pivot_table=pivot_percentage.style.format('{0}%').background_gradient(cmap='RdYlGn',axis=None)