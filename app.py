from flask import Flask, request, render_template, jsonify
import os
import yaml
import joblib
import json
import numpy as np
import pandas as pd

params_path= "params.yaml"
webapp_root = "webapp"

static_dir= os.path.join(webapp_root,"static")
template_dir= os.path.join(webapp_root,"templates")

app  =Flask(__name__, static_folder=static_dir,template_folder=template_dir)

def read_params(params_path):
    with open(params_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try: 
        data=np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":response}
        return response
    except Exception as e:
            print(e)
            error={"error":"Found Error in entries.Try Again!!!"}
            return render_template("404.html",error=error)


@app.route('/', methods=["GET","POST"])
def launch():
    if request.method == 'POST':
        try:
            if request.form:
                # Departure Date
                departure_date = request.form["Dep_Time"]
                Start_Day = int(pd.to_datetime(departure_date, format = "%Y-%m-%dT%H:%M").day)
                Start_Month = int(pd.to_datetime(departure_date, format = "%Y-%m-%dT%H:%M").month)
                
                # Departure Time
                departure_hour = int(pd.to_datetime(departure_date, format = "%Y-%m-%dT%H:%M").hour)
                departure_minute = int(pd.to_datetime(departure_date, format = "%Y-%m-%dT%H:%M").minute)

                # Arrival Time
                arrival_time = request.form["Arrival_Time"]
                arrival_hour = int(pd.to_datetime( arrival_time, format = "%Y-%m-%dT%H:%M").hour)
                arrival_minute = int(pd.to_datetime( arrival_time, format = "%Y-%m-%dT%H:%M").minute)
                
                # Flight duration
                Duration_hours = abs(arrival_hour - departure_hour)
                Duration_minutes  =abs(arrival_minute - departure_minute)
                
                
                # Total Stops
                Total_Stops = int(request.form["stops"])
                
                # Airline
                
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
                if (Destination == 'Cochin'):
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
                 
                data = pd.DataFrame([{"Unnamed: 0" :0,
                        "Air India":Air_India,
                       "GoAir": GoAir,
                        "IndiGo":IndiGo,
                        "Jet Airways":Jet_Airways,
                        "Jet Airways Business":Jet_Airways_Business,
                        "Multiple carriers":Multiple_carriers,
                        "Multiple carriers Premium economy":Multiple_carriers_Premium_economy,
                        "SpiceJet":SpiceJet,
                        "Trujet":Trujet,
                        "Vistara":Vistara,
                        "Vistara Premium economy":Vistara_Premium_economy,
                        "Source_Chennai":source_Chennai,
                        "Source_Delhi":source_Delhi,
                        "Source_Kolkata":source_Kolkata,
                        "Source_Mumbai":source_Mumbai,
                        "Destination_Cochin":destination_Cochin,
                        "Destination_Delhi":destination_Delhi,
                        "Destination_Hyderabad":destination_Hyderabad,
                        "Destination_Kolkata":destination_Kolkata,  
                        "Total_Stops":Total_Stops,
                        "Day_of_Journey":Start_Day,
                        "Month_of_Journey":Start_Month,
                        "Dep_Hour":departure_hour,
                        "Dep_Minute":departure_minute,
                        "Arrival_Hour":arrival_hour,
                        "Arrival_Minute":arrival_minute,
                        "Duration_hours":Duration_hours,
                        "Duration_minutes":Duration_minutes
                                                     
                }])
            
                response = np.round(predict(data),2)
                return render_template("index.html", prediction_text="The flight fare will be : {}". format(response))
            
            elif request.json:
                response = api_response(request)
                return jsonify(response)

        except Exception as e:
            print(e)
            error={"error":"Found Error in entries.Try Again!!!"}
            return render_template("404.html",error=error)

        
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
