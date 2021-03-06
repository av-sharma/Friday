import speech_recognition as sr
from gtts import gTTS
import mp3play
from mutagen.mp3 import MP3
import sys
import os
import random
import time

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
            r1 = random.randint(1,10000000)
            r2 = random.randint(1,10000000)
            randfile = "audio\\" + str(r2) + "" + str(r1) + ".mp3"
            print("You: ", input)
            print("Friday: Awake!")
            tts = gTTS(text="I\'m now Listening!", lang='en')
            tts.save(randfile)
            audio = MP3(randfile)
            length=audio.info.length
            clip = mp3play.load(randfile)
            clip.play()
            time.sleep(length)
            clip.stop()
            os.remove(randfile)
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
        if tries > 3:
            listen_for_keyword()
        else:
            listener(tries+1)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("Try again")
        if tries > 3:
            listen_for_keyword()
        else:
            listener(tries+1)

### Function that controls all the commands
def commands(input):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = "audio\\" + str(r2) + "" + str(r1) + ".mp3"

    if input == 'hello':
        print("You: ", input)
        print("Friday: Hello Sir! How may i help you?")
        tts = gTTS(text="Hello Sir! How may i help you?", lang='en')
        tts.save(randfile)
        audio = MP3(randfile)
        length=audio.info.length
        clip = mp3play.load(randfile)
        clip.play()
        time.sleep(length)
        clip.stop()
        os.remove(randfile)
        listener(0)

    elif input == 'sleep' or input == 'goto sleep' or input == 'go to sleep' or input == 'stop listening':
        print("You: ", input)
        print("Friday: Going to Sleep!")
        tts = gTTS(text="Going to Sleep!", lang='en')
        tts.save(randfile)
        audio = MP3(randfile)
        length=audio.info.length
        clip = mp3play.load(randfile)
        clip.play()
        time.sleep(length)
        clip.stop()
        os.remove(randfile)
        sleep()

    elif input == 'open atom' or input == 'open atom text editor' or input == 'open atom editor' or input == 'open text editor':
        print("You: ", input)
        print("Friday: Opening atom")
        tts = gTTS(text="Opening Atom", lang='en')
        tts.save(randfile)
        audio = MP3(randfile)
        length=audio.info.length
        clip = mp3play.load(randfile)
        clip.play()
        os.startfile("C:\\Users\\Arnav\\AppData\\Local\\atom\\atom.exe")
        time.sleep(length)
        clip.stop()
        os.remove(randfile)

    elif input == 'goodbye' or input == 'goodbye friday' or input == 'bye bye' or input == 'bye friday':
        print("You: ", input)
        print("Friday: Goodbye Sir!")
        tts = gTTS(text="Goodbye Sir!", lang='en')
        tts.save(randfile)
        audio = MP3(randfile)
        length=audio.info.length
        clip = mp3play.load(randfile)
        clip.play()
        time.sleep(length)
        clip.stop()
        os.remove(randfile)
        exit()

    else:
        tts = gTTS(text="Sorry i didn't understand what you said!", lang='en')
        tts.save(randfile)
        audio = MP3(randfile)
        length=audio.info.length
        clip = mp3play.load(randfile)
        clip.play()
        time.sleep(length)
        clip.stop()
        os.remove(randfile)
        listen_for_keyword()

### The main function
def main():
    while(True):
        listen_for_keyword()

main()
