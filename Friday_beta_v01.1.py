import speech_recognition as sr
from gtts import gTTS
import mp3play
from mutagen.mp3 import MP3
import sys
import os

name = "friday"     # write name in lowercase

r = sr.Recognizer()
mic = sr.Microphone()

def listen_for_keyword():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("listening for keyword")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
        input = list(text.split(' '))
        if text.lower() == 'hey ' + name:
            listener(0)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

### Sleep function for the Assistant to go to sleep or stop listening
def sleep():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Sleeping..")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
        input = list(text.split(' '))
        if text.lower() == 'wake up friday':
            print("You: ", input)
            print("Friday: Awake!")
            tts = gTTS(text="I\'m now Listening!", lang='en')
            tts.save("audio\sleep.mp3")
            clip = mp3play.load(r"audio\sleep.mp3")
            clip.play()
            listener(0)
    except sr.UnknownValueError:
        # print("Google Speech Recognition could not understand audio")
        sleep()
    except sr.RequestError as e:
        # print("Could not request results from Google Speech Recognition service; {0}".format(e))
        sleep()
    sleep()

### Main listener function that listens from the mic for the command
def listener(tries):
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening... try ", tries)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        commands(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        print("Try again")
        listener(tries+1)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("Try again")
        listener(tries+1)

### Function that controls all the commands
def commands(input):
    if input == 'hello':
        print("You: ", input)
        print("Friday: Hello Sir! How may i help you?")
        tts = gTTS(text="Hello Sir! How may i help you?", lang='en')
        tts.save("audio\output.mp3")
        clip = mp3play.load(r"audio\output.mp3")
        clip.play()
        # listener(0)

    elif input == 'sleep' or input == 'goto sleep' or input == 'go to sleep' or input == 'stop listening':
        print("You: ", input)
        print("Friday: Going to Sleep!")
        tts = gTTS(text="Going to Sleep!", lang='en')
        tts.save("audio\output.mp3")
        clip = mp3play.load(r"audio\output.mp3")
        clip.play()
        sleep()

    else:
        tts = gTTS(text="Sorry i didn't understand what you said!", lang='en')
        tts.save("audio\output.mp3")
        clip = mp3play.load(r"audio\output.mp3")
        clip.play()
    listen_for_keyword()

### The main function
def main():
    while(True):
        listen_for_keyword()

main()
