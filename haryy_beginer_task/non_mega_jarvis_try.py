import speech_recognition as sr
import webbrowser
import requests
import music_library
import edge_tts
import asyncio
import pygame
import os
import time # Added for a small delay

# --- Configuration ---
#news_api = "950ad8a063e2436e82be0df16a8c6e8e"
VOICE = "en-US-AvaNeural"
OUTPUT_FILE = "response.mp3"
r = sr.Recognizer()

# Async speak function using edge-tts
async def speak(text):
    print(f"meera : {text}")
    try:
        # 1. Generate the speech file
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(OUTPUT_FILE)
        
        # 2. Initialize and play the audio file
        pygame.mixer.init()
        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()
        
        # 3. Wait for playback to finish
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
        
        # 4. Stop music and UNLOAD the file (Crucial for Windows)
        pygame.mixer.music.stop()
        pygame.mixer.music.unload() # This releases the file lock
        pygame.mixer.quit()

        # 5. Small delay to let the OS catch up
        await asyncio.sleep(0.2) 
        
        # 6. Clean up the file
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)

    except Exception as e:
        print(f"Speech generation/playback error: {e}")
        # Attempt cleanup if something failed
        try:
            pygame.mixer.quit()
            if os.path.exists(OUTPUT_FILE):
                os.remove(OUTPUT_FILE)
        except:
            pass
# Process command function (now async to call speak)
async def processCommand(c):
    c = c.lower()
    print(f"Processing command: {c}")

    if "open google" in c:
        webbrowser.open("https://www.google.com")
        await speak("Opening Google")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
        await speak("Opening Facebook")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
        await speak("Opening YouTube")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
        await speak("Opening LinkedIn")
    elif c.startswith("play"):
        try:
            # Fixed the logic to get the song name correctly
            song_name = c.split(" ", 1)[1] 
            if song_name in music_library.music:
                link = music_library.music[song_name]
                webbrowser.open(link)
                await speak(f"Playing {song_name}")
            else:
                await speak(f"Sorry, I couldn't find {song_name} in your library")
        except IndexError:
            await speak("Please specify a song name to play")
        except Exception:
            await speak("Error playing song")
            
    elif "news" in c:
        await speak("Fetching top headlines from India")
        try:
            # CORRECTED: Added the base URL back in
            req = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=950ad8a063e2436e82be0df16a8c6e8e")
            if req.status_code == 200:
                data = req.json()
                articles = data.get("articles", [])
                for i, article in enumerate(articles[:3], start=1):
                    await speak(f"Headline number {i}: {article.get('title')}")
        except requests.exceptions.RequestException:
             await speak("I can't connect to the news service right now")
        except Exception:
            await speak("An unexpected error occurred while processing the news")

    else:
        await speak("Sorry, I don't understand command")


async def main():   # Main async function USED TO  run the loop when i call meera
    await speak("Initializing Meera...")
    
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("\nListening..... ")
                
                audio = r.listen(source, timeout=5, phrase_time_limit=2) # Listen for the wake word when it call
                word = r.recognize_google(audio)
                print(f"Heard wake word: {word}")

                if "Meera" in word.lower() or "hello" in word.lower():
                    await speak("Yes boss")
                    
                    # Listen for the actual command
                    print("Listening for command...")
                    audio_command = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio_command)
                    # Process the command asynchronously
                    await processCommand(command)

        except sr.UnknownValueError:
            pass # Ignore if no speech detected
        except sr.WaitTimeoutError:
            pass # Ignore if listening times out
        except Exception as e:
            print(f"An error occurred in the main loop: {e}")
        except KeyboardInterrupt:
            await speak("Goodbye boss, shutting down system")
            break

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program interrupted safely. Exiting...")
