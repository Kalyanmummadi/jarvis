
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS




newsapi ="f27e112d78104e39a0313f2b189f3df2"

def processcommand(c):
    if c.lower().startswith("open"):
        cmd = c.lower().split(" ")[1]
        link = f"http://{cmd}.com"
        webbrowser.open(link) 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=f27e112d78104e39a0313f2b189f3df2"
        response = requests.get(url)

        # Parse the JSON response
        data = response.json()

        # Extract and print the headlines
        if data.get("status") == "ok":
            articles = data.get("articles", [])
            headlines = [article["title"] for article in articles]
            for idx, headline in enumerate(headlines, start=1):
                speak(f"{idx}. {headline}")
        else:
            print("Failed to retrieve news headlines")
 
    

recogniser = sr.Recognizer()
engine = pyttsx3.init()
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):

    tts = gTTS(text)
    tts.save('temp.mp3')


if __name__=="__main__":
    speak("Initializing jarvis... Hi how can i help you")
    while True:
        r = sr.Recognizer()

            # Reading Microphone as source
            # listening the speech and store in audio_text variable
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
                # recoginze_() method will throw a request
                # error if the API is unreachable,
                # hence using exception handling
                
            try:
                    # using google speech recognition
                print("Text: "+r.recognize_google(audio_text))
                word = r.recognize_google(audio_text)
                if(word.lower()=="jarvis"):
                    speak("hey kalyan how are you?")
                    with sr.Microphone() as source:
                        print("Talk")
                        audio_text = r.listen(source)
                        command = r.recognize_google(audio_text)
                        
                        processcommand(command)
                    
            except:
                print("Sorry, I did not get that")
