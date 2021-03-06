import os
import argparse
import yaml
import pandas as pd

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config= read_params(config_path)
    data_path=config["data_source"]["gdrive_source"]
    df= pd.read_excel(data_path)
    raw_data_path=config["load_data"]["raw_data_csv"]
    df.to_csv(raw_data_path,sep=',',encoding='utf-8',header=True,index=False)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parsed_args=args.parse_args()
    get_data(config_path=Parsed_args.config)
