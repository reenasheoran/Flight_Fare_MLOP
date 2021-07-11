# FLIGHT-FARE-PREDICTOR 
It is a machine learning project to predict the price for domestic flights in India.
## Demo
![Home Page](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/1.png)
![Fill Entries](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/2.png)
![Prediction](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/3.png)
## Motivation
There is a general idea that the earlier we book the flight, the lower be the ticket prices. But the question is, whenever anyone plans to book the flight, how one could know which flight would be cheaper.  Moreover, the price of a flight ticket is highly dependent upon demand and changes accordingly. In this project, I am trying to solve this issue with the help of data science.
## Problem Statement
The objective of this project is to create a web app that could help the users to get an estimate of the Indian flight ticket prices, given the details about the flights such as source, destination, departure/arrival date and time, etc.
## Data Collection
The dataset has been taken from kaggle https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh?select=Data_Train.xlsx. It contains the data about prices of flight tickets for various airlines and between various cities for the period between the months of March and June of 2019. Here is the details about data:-

Size of training set: 10683 records<br>
Size of test set: 2671 records

**FEATURES**: <br>
Airline: The name of the airline.<br>
Date_of_Journey: The date of the journey.<br>
Source: The source from which the service begins.<br>
Destination: The destination where the service ends.<br>
Route: The route taken by the flight to reach the destination.<br>
Dep_Time: The time when the journey starts from the source.<br>
Arrival_Time: Time of arrival at the destination.<br>
Duration: Total duration of the flight.<br>
Total_Stops: Total stops between the source and destination.<br>
Additional_Info: Additional information about the flight.<br>
Price: The price of the ticket.<br>
## Data Cleaning
Fortunately, there were only 2 missing values that too in the same row. Therefor, I dropped the rows with NA values. 
## Feature Engineering
Then, I did feature engineering as follows: - <br>
-Converted column 'Date_of_Journey' from categorical to datetime dtype. Since all data is from same year, I am just extracted day and month from "Date_of_journey"<br>
-Extracted hours and minutes form "Dep_Time" <br>
-Extracted hour and minute from "Arrival_Time" <br>
-Extracted hour and minute from "Duration"<br>
-Applied one-hot encoding on categorical data such as total_stops, airline, source and destination features.<br>
## EDA
I looked at the distributions of the data and the prices of various airlines based on stoppages, source, destination, etc. Below are few highlights from EDA section.
![EDA1](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/4.png)
![EDA2](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/5.png)
![EDA3](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/6.png)
## Model Building
For building the model, I first splitted the data into train and test set in 80:20 ratio respectively. Then I tried following models: -<br>
1. Linear Regression <br>
2. Ridge Regression <br>
3. Lasso Regression<br>
4. ExtraTrees Regressor <br>
5. RandomForest Regressor <br>
6. CatBoost Regressor <br>
7. XGBoost Regressor <br>
8. Lightgbm Regressor
## Models Evaluation and Performance Metrics
For evaluating the model I recorded Training R2 score, Prediction R2 Score, Mean Absolute Error(MAE), Root Mean Squared Error(RMSE). For making the final decision I considered two metrics, Prediction R2 Score and Mean Absolute Error as these two metrics shows how good the model is on unknown data. Following is the performance table: - 
|Model|R2 Score(Training)|R2 Score(Prediction)|MAE|RMSE|


## Installation
This project is developed using python 3.7. If you are using any lower version of python then I recommend you to upgrade your python to the latest version by using pip command. Once you clone this repository just type this command in the cloned project directory in order to install all the required packages:
## Deployment

