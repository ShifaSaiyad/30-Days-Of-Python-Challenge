import speech_recognition as sr
import webbrowser
import pyttsx3  #used for text to speech
import music_library
import requests
#pip installl pocketsphinx


r = sr.Recognizer()    #give permition to recognize the speech
engine = pyttsx3.init() #initilize thie speech
news_api = "950ad8a063e2436e82be0df16a8c6e8e"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    print(c)

    if "open google" in c:
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")

        if r.status_code == 200:
            data = r.json()  # Parse JSON
            articles = data.get("articles", [])

            # Print the top headlines
            print("Top Headlines:")
            for i, article in enumerate(articles, start=1):
                speak(f"{i}. {article.get('title')}")

    else:
        speak("Sorry, I don't understand that command")
        
if __name__ == "__main__":
    #speak("hello  shifa this is jarvis... nice to meet you i am here to work with you ")
    speak("initializing tinu......")
    
    while True:
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                #audio = r.listen(source, timeout=3, phrase_time_limit=3)


            word = r.recognize_google(audio)
            print("Heard word:", word)


            if "hello t" in word.lower():
                speak("Yaaaaa")
                speak("yes i listen my bosss")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    #audio = r.listen(source)
                    audio = r.listen(source, timeout=4, phrase_time_limit=5)

                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))

        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break
