import requests
from dotenv import load_dotenv
import os
from openai import OpenAI

# Weather API
API_KEY = os.getenv("weather_api_key")
API_HOST = "open-weather13.p.rapidapi.com"
CITY = "delhi"  # City for weather query

def get_weather():
    """Get the current weather from OpenWeather API for the specified city."""
    url = f"https://open-weather13.p.rapidapi.com/city/{CITY}/EN"
    
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    # Send the GET request to the API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract the weather details
        weather_description = data.get("weather", [{}])[0].get("description", "No description available")
        temperature = data.get("main", {}).get("temp", "No temperature data available")
        
        return f"The current weather in {CITY.capitalize()} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information."


# YouTube API key
API_KEY = os.getenv("yt_api_key")
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def search_video(video_name):
    """
    Searches YouTube for a video by name and returns its URL.
    
    :param video_name: The name of the video to search for
    :return: The video URL if found, otherwise None
    """
    try:
        # Prepare the API request parameters
        params = {
            "part": "snippet",
            "q": video_name,  # Search query
            "type": "video",  # Only search for videos
            "key": API_KEY,
            "maxResults": 1,  # Fetch the first result only
        }
        
        # Make the API request
        response = requests.get(YOUTUBE_SEARCH_URL, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        
        # Parse the JSON response
        results = response.json()
        
        # Check if any results were returned
        if "items" not in results or len(results["items"]) == 0:
            print("No videos found for the given search query.")
            return None
        
        # Extract the video ID of the first result
        video_id = results["items"][0]["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    
    except Exception as e:
        print(f"An error occurred while searching for the video: {e}")
        return None
    
# Using OpenAI api
def aiProcess(command):
    client = OpenAI(
    api_key=os.getenv("openai_api_key")
)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a witty assistant, adding a bit of sass in answers, have skills like Alexa and Google Assistant ."},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return(completion.choices[0].message.content) 