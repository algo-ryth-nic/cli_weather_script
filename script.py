import requests
import json
import argparse
import pickle
import os

# for debugging
from pprint import pprint


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



def get_weather(city):
    # get the weather for the given city
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city.lower(), cred['key'])
    r = requests.get(url)
    content = r.json()
    
    # debugging 
    pprint(r.json())
    
    # print(r.status_code)
    if r.status_code == 200:
        # request is successful, return the weather
        return content
    else:
        print(content['message'])
        return None


data = get_weather(args.city)
# create message 
if data is not None:
    message = "The weather in {} is {} with a temperature of {} degrees Celsius".format(args.city, data['weather'][0]['description'], data['main']['temp'])
