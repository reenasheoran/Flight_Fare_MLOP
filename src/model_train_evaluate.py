import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from catboost import CatBoostRegressor
from get_data import read_params
import argparse
import joblib
import json


def evaluate_model(actual, predicted):
    MSE = np.round(mean_squared_error(actual, predicted),3)
    RMSE = np.round(np.sqrt(MSE),3)
    MAE = np.round(mean_absolute_error(actual, predicted),3)
    R2_scores = np.round(r2_score(actual, predicted),3)
    return MSE, RMSE, MAE, R2_scores

def train_model(config_path):
    config = read_params(config_path)
    
    train_data_path = config["split_data"]["train_data"]
    test_data_path = config["split_data"]["test_data"]
    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")
   
    target = config["base"]["target"]   
 
    X_train = train.drop(target, axis=1)
    X_test = test.drop(target, axis=1)
    Y_train = train[target]
    Y_test = test[target]

    random_state = config["base"]["random_state"]
    itrns = config["estimators"]["CatBoost"]["params"]["iterations"]
    lr = config["estimators"]["CatBoost"]["params"]["learning_rate"]
    depth = config["estimators"]["CatBoost"]["params"]["depth"]

    CBR = CatBoostRegressor(iterations=itrns,learning_rate=lr,depth=depth,random_state=random_state)
    CBR.fit(X_train, Y_train)

    Y_pred= CBR.predict(X_test)
    
    (MSE, RMSE, MAE, R2_scores) = evaluate_model(Y_test,Y_pred)

    print("CatBoost model (iterations=%f, learning_rate=%f, depth=%f):" % (itrns,lr,depth))
    print("  MSE: %s" % MSE)
    print("  RMSE: %s" % RMSE)
    print("  MAE: %s" % MAE)
    print("  R2_score: %s" % R2_scores)


    # scores_file = config["reports"]["scores"]
    # params_file = config["reports"]["params"]

    # with open(scores_file, "w") as f:
    #     scores = {
    #         "MSE": MSE
    #         "RMSE": RMSE,
    #         "MAE": MAE,
    #         "R2_score": R2_score
    #     }
    #     json.dump(scores, f, indent=4)

    # with open(params_file, "w") as f:
    #     params = {
    #         "alpha": alpha,
    #         "l1_ratio": l1_ratio,
    #     }
    #     json.dump(params, f, indent=4)

    # model_dir = config["model_dir"]

    # os.makedirs(model_dir, exist_ok=True)
    # model_path = os.path.join(model_dir, "model.joblib")

    # joblib.dump(lr, model_path)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_model(config_path=parsed_args.config)