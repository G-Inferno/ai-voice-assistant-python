import speech_recognition as sr
import webbrowser
import pyttsx3
import random
import datetime
from websites import sites
from api import get_weather
from api import search_video
from api import aiProcess
from quotes import get_random_quote


r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()  
    
def processCommand(c):
    greet = ["how are you", "how r u", "how're you", "how r you", "kaise ho"]
    
    # Check for time
    if any(time in c.lower() for time in ["what's the time", "what is the time", "give me the time", "what time"]):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    # Check for date
    elif any(phrase in c.lower() for phrase in ["what's the date", "what is the date", "give me the date", "what's today's date"]):
        current_date = datetime.datetime.now().strftime("%B %d, %Y")  # Example: 'November 26, 2024'
        speak(f"Today's date is {current_date}")
        
    # Check for weather
    elif "what's the weather" in c.lower() or "what is the weather" in c.lower():
        weather_info = get_weather()  # Call the get_weather function
        speak(weather_info)
        
    # open sites    
    elif c.lower().startswith("open"):
        site = c.lower().split(" ")[1]
        if site in sites:
            link, response = sites[site]
            webbrowser.open(link)
            speak(response)
        else:
            speak("Sorry, couldn't find the site") 
    
    # Tell Quotes
    elif any(quote_phrase in c.lower() for quote_phrase in ["thoughts", "thought of the day", "give me a quote", "tell me a quote"]):
        quote = get_random_quote()
        speak(quote)
        print(quote)                 
        
    # Play a game
    elif "game" in c.lower():
        choices = [
            ("2048", "https://elgoog.im/2048/"),
            ("Space Invaders", "https://elgoog.im/space-invaders/"),
            ("Dino Jump", "https://elgoog.im/dinosaur-game/birthday/"),
            ("Breakout", "https://elgoog.im/breakout/"),
            ("Tetris", "https://tetris.com/play-tetris")
        ]
        site_name, site_url = random.choice(choices)
        webbrowser.open(site_url)
        speak(f"Let's visit {site_name}")
                
    # Greet the user
    elif any(phrase in c.lower() for phrase in greet):
        speak("I am fine, thank you")
        
    # Search for a video on YouTube
    elif "play" in c.lower() or "video" in c.lower():
        # Extract the entire phrase after "play" to capture the full video name
        video_name = c.lower().split("play")[1].strip()  # This ensures everything after "play" is captured
        
        if video_name:
            print(f"Searching for video: {video_name}")
            video_url = search_video(video_name)  # Using the search_video function from the api
            if video_url:
                webbrowser.open(video_url)
                speak(f"Playing {video_name} on YouTube.")
            else:
                speak(f"Sorry, I couldn't find a video for '{video_name}'.")   
                
    else: 
        # Using OpenAI to handle this
        output = aiProcess(c)
        speak(output)    
                


#initialisation
if __name__ == "__main__":
    speak("Hello, Myself poppy. Nice to meet you.")
     
#wakeup call "Poppy"
# obtain audio from the microphone
    while True:     
# recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
                word = r.recognize_google(audio)
                print(word)
            
            # Define a list of keywords
            keywords = ["hello poppy","hi poppy","hey poppy","poppy","hello puppy", "hello bobby"]

            if word.lower() in keywords:
                speak("How may I assist you?"); print("Active...")
                
                #listens command                
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=3, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    print(f"Recognized: {command}")
                    processCommand(command)
                                       
                      
        except sr.UnknownValueError:
            print("Could not understand audio;")
        except Exception as e:
            print("error; {0}".format(e))

