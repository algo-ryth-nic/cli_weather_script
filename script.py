import requests
import json
import argparse
import pickle
import os




# create a cli that shows the current weather of a city 
parser = argparse.ArgumentParser()
# take api key
parser.add_argument("-k", "--key", help="API key")
parser.add_argument("-c", "--city", help="City to get the weather for", required=True)
args = parser.parse_args()

