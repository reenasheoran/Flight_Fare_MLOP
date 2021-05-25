from flask import Flask, request, render_template, jsonify
import os
import yaml
import joblib
import json
import numpy as np
import pandas as pd
from flask_cors import cross_origin

params_path= "params.yaml"
webapp_root = "webapp"

static_dir= os.path.join(webapp_root,"static")
template_dir= os.path.join(webapp_root,"templates")

app  =Flask(__name__, static_folder=static_dir,template_folder=template_dir)

def read_params(params_path):
    with open(params_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def find_model():
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    return model

@app.route("/")
@cross_origin()
def home():
    return render_template("homepage.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def index():
    if request.method == "POST":
        
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_Day = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").day)
        Journey_Month = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").month)
        
        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(date_dep, format = "%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arrival = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arrival, format = "%Y-%m-%dT%H:%M").hour)
        arrival_minute = int(pd.to_datetime(date_arrival, format = "%Y-%m-%dT%H:%M").minute)
        
        # Duration
        dur_hour = abs(arrival_hour - dep_hour)
        dur_min  =abs(arrival_minute - dep_minute)
        
        
        # Total Stops
        Total_Stops = int(request.form["stops"])
        
        # Airlines
        
        airline = request.form['airline']
        if (airline == 'Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
        elif (airline == 'IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
        elif (airline == 'Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        
        elif (airline == 'Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
        elif (airline == 'SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0            
        
        elif (airline == 'Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0            
        
        elif (airline == 'GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
        elif (airline == 'Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif (airline == 'Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        
        
        # Source
        
        Source = request.form["source"]
        if (Source == 'Delhi'):
            source_Delhi = 1
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0
            
        elif (Source == 'Kolkata'):
            source_Delhi = 0
            source_Kolkata = 1
            source_Mumbai = 0
            source_Chennai = 0
            
        elif (Source == 'Mumbai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 1
            source_Chennai = 0
            
        elif (Source == 'Chennai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 1
            
        else:
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0
            
            
        # Destination
        Destination = request.form["destination"]
        if (Source == 'Cochin'):
            destination_Cochin = 1
            destination_Delhi = 0
            
            destination_Hyderabad = 0
            destination_Kolkata = 0
            
        elif (Destination == 'Delhi'):
            destination_Cochin = 0
            destination_Delhi = 1
            
            destination_Hyderabad = 0
            destination_Kolkata = 0
            
        elif (Destination == 'Hyderabad'):
            destination_Cochin = 0
            destination_Delhi = 0
            
            destination_Hyderabad = 1
            destination_Kolkata = 0
            
        elif (Destination == 'Kolkata'):
            destination_Cochin = 0
            destination_Delhi = 0
            
            destination_Hyderabad = 0
            destination_Kolkata = 1
            
        else:
            destination_Cochin = 0
            destination_Delhi = 0
            
            destination_Hyderabad = 0
            destination_Kolkata = 0
        
        model = find_model()
        prediction =model.predict([[  
                Total_Stops,
                Journey_Day,
                Journey_Month,
                dep_hour,
                dep_minute,
                arrival_hour,
                arrival_minute,
                dur_hour,
                dur_min,
                Jet_Airways,
                IndiGo,
                Air_India,
                Multiple_carriers,
                SpiceJet,
                Vistara,
                GoAir,
                Multiple_carriers_Premium_economy,
                Jet_Airways_Business,
                Vistara_Premium_economy,
                Trujet,
                source_Delhi,
                source_Kolkata,
                source_Mumbai,
                source_Chennai,
                destination_Cochin,
                destination_Delhi,
                destination_Hyderabad,
                destination_Kolkata                               
        ]])
        
        output = np.round(prediction[0], 2)
        
        return render_template('homepage.html', prediction_text = "Total Flight Price is Rs. {}".format(output))
    
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug = True)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        