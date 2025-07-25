import pyttsx3 as p
import speech_recognition as sr
from Selenium import *  # Adjust import according to your actual file structure
from video import *
from news import *
import randfacts
from weather import *
import datetime

engine = p.init()
# Adjust the rate of speech
# Select a voice from the available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# # Function to initialize the text-to-speech engine and speak the text
def speak(text):
   engine.say(text)
   engine.runAndWait()
today_date=datetime.datetime.now()
# # Function to get current date and time in a detailed manner
def speak_date_time():
    now = datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%d %B %Y")
    time = now.strftime("%H:%M %p")
    detailed_time = f"Today is {day}, {date}. The current time is {time}."
    speak(detailed_time)

r=sr.Recognizer()
speak("Hello, I am your voice assistant")
# speak("today is "+today_date.strftime("%d %B %Y") + " and current time is "+today_date.strftime("%H:%M %p"))
# speak("Temperature in delhi is " + str(temp()) + " degrees Celsius and with " + str(des()))
# speak("What can I do for you?")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening........")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what about you" in text:
    speak("am having good day")
speak("what about you")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
if "information" in text2:
    speak("you need info on which topic?")
    
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        assist=infow()
        assist.get_info(infor)
elif "play" in text2 and "video" in text2:
    speak("You want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening........")
        audio = r.listen(source)
        video = r.recognize_google(audio)
    print("Playing {} on YouTube........".format(video))
    assist = music()
    assist.play(video)

elif "news" in text2:
    print("Sure, here is the news for you!")
    speak("Sure, here is the news for you!")
    arr = news()  # Fetch fresh news items
    for i in range(len(arr)):
        speak(arr[i])
        print(arr[i])
        

elif "fact" in text2 or "facts" in text2:
    speak("Here is a fact for you!")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)
