import os
import argparse
from get_data import read_params
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parsed_args=args.parse_args()
    split_data(config_path=Parsed_args.config)
