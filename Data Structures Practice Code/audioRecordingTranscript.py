'''I want you to build a function that can take in an audio recording and return the transcript

'''

import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.AudioFile('harvard.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print('converting audio to text...')
        time.sleep(3)
        print(text)
    except: 
        print('sorry..try that again')