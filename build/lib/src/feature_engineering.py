import os
import argparse
from get_data import read_params
import pandas as pd

def feature_engg_data(config_path):
    config= read_params(config_path)
    data_path=config["load_data"]["raw_data_csv"]
    df= pd.read_csv(data_path,sep=',',encoding='utf-8')
    
    df.dropna(how='any',inplace=True)
    
    df['Destination'].replace('New Delhi','Delhi', inplace = True)
    
    df['Date_of_Journey']=pd.to_datetime(df['Date_of_Journey'],format="%d/%m/%Y")
    df['Day_of_Journey']=(df['Date_of_Journey']).dt.day
    df['Month_of_Journey']=(df['Date_of_Journey']).dt.month
    df.drop('Date_of_Journey',axis=1,inplace=True)
    
    df['Dep_Time']=pd.to_datetime(df['Dep_Time'],format="%H:%M")
    df['Dep_Hour']=(df['Dep_Time']).dt.hour
    df['Dep_Minute']=(df['Dep_Time']).dt.minute
    df.drop('Dep_Time',axis=1,inplace=True)
    
    df['Arrival_Hour']=(pd.to_datetime(df['Arrival_Time'])).dt.hour
    df['Arrival_Minute']=(pd.to_datetime(df['Arrival_Time'])).dt.minute
    df.drop('Arrival_Time',axis=1,inplace=True)
    
    duration = df.Duration.str.split(' ',expand = True).fillna('00m')
    df['Duration_hours']=duration[0].apply(lambda x: x[:-1])
    df['Duration_minutes']=duration[1].apply(lambda x: x[:-1])
    df[['Duration_hours','Duration_minutes']]=df[['Duration_hours','Duration_minutes']].astype(int)
    df.drop('Duration',axis=1,inplace=True)
    
    dict={'non-stop':0,'2 stops':2,'1 stop':1,'3 stops':3,'4 stops':4}
    df['Total_Stops']=df['Total_Stops'].map(dict)
    
    Airlines = pd.get_dummies(df['Airline'],drop_first=True)
    places = pd.get_dummies(df[['Source','Destination']],drop_first=True)
    df=pd.concat([Airlines,places,df],axis=1)
    df.drop(['Airline','Source','Destination'],axis=1,inplace=True)
    
    df.drop(['Route','Additional_Info'],axis=1,inplace=True)
    df[['Duration_hours','Duration_minutes']]=df[['Duration_hours','Duration_minutes']].astype(int)
    
    filter_data_path=config["filter_data"]["filter_data_csv"]
    df.to_csv(filter_data_path,sep=',',encoding='utf-8',header=True,index=False)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parsed_args=args.parse_args()
    feature_engg_data(config_path=Parsed_args.config)
