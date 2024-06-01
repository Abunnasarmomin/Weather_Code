########################### Welcome To Wheather App #################################

import requests
import json
import pyttsx3
#from image import DrawImage
#from PIL import Image

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the speaking rate (you may need to adjust this value)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',159)  # You can experiment with different values here

    engine.runAndWait()

###################Input And URL################################################
print("Welcome TO Weather App")
speak("Welcome TO Weather App")

speak(f"Enter The name of the City: ")
try:            
    #info9 = wdic["location"]["name"]
    c = input("Enter The name of the City: ")
    url = f"http://api.weatherapi.com/v1/current.json?key=21fe31d86a7f431f83e60717232611&q={c}&aqi=no"

    r = requests.get(url)
    #r.raise_for_status() 
    #print(r.text)
    #print(type(r.text))
    wdic = json.loads(r.text)
    info1 = wdic["current"]["temp_c"]
    info2 = wdic["current"]["temp_f"]
    info3 = wdic["current"]["last_updated"]
    info4 = wdic["current"]["wind_mph"]
    info5 = wdic["current"]["wind_kph"]
    info6 = wdic["current"]["wind_degree"]
    info7 = wdic["current"]["humidity"]
    info8 = wdic["current"]["condition"]["text"]
    info9 = wdic["current"]["condition"]["icon"]
    info10 = wdic["location"]["localtime"]

    #if url == :
    #    print("You Must Be Connected With Internet")
    #    speak("You Must Be Connected With Internet")

    #################Speak StateMent#######################################

    print(f"The Temperature of {c} city is celcius:{info1} and feranite:{info2}")
    speak(f"The Temperature of {c} city is celcius:{info1}Degrees and feranite:{info2}Degrees")

    speak("If you want more infomation Type: 'g' Or 'q' for Exit")
    get = input("If you want more infomation Type: 'g' Or 'q' for Exit:")


    if get == 'g':
        print("More Details:\n")
        print(f"MHP is {info4}")
        print(f"KPH is {info5}")
        print(f"Current Degree is {info6} degree")
        print(f"Its {info8} Weather!")
        #if info8 == "Overcast" : print("Its Cold Weather!") # Its should show that it is COld weather
        print(f"Humidity is {info7}")
        print(f"Current time of Update: {info10}")
        #print(info9)

    # else:
    #     print(info8)    

    print("Thanks For Visiting!!")
    speak("Thanks For Visiting!!")

    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    print("An error occurred. Please check your internet connection and try again.")
    speak("An error occurred. Please check your internet connection and try again.")

except json.JSONDecodeError:
    print("Try Connecting to the internet")            
except KeyError:
    print("--INTERNET ERROR--\nPlease Try Again")     
    speak("INTERNET ERROR Please Try Again")
except Exception:
    print("--Exit--")       
    