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

# check if the api key is given
if args.key is None:
    # looks for the api key in the cred.pickle file (previously saved)
    if os.path.exists('./cred.pickle') == False:
        print("Please provide an openweathermap's API key using -k or --key,\n \
            view help for more info")
        exit()
    else:
        # Getting credentials read pickle file 
        with open('./cred.pickle', 'rb') as f:
            cred = pickle.load(f)
else:
    # if the api key is given, save it in the cred.pickle file
    cred = {'key': args.key}
    with open('./cred.pickle', 'wb') as f:
        pickle.dump(cred, f)



