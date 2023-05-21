import speech_recognition as sr
from tts import speak
from chat import chat

r = sr.Recognizer()
mic = sr.Microphone()


def listen(lang="en-US"):
    with mic as source:
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            return r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return "" #empty string as error

byeWords = ("bye bye bye", "goodbye goodbye", "exit exit", "quit quit", "stop stop")

def askAI(lang="en_US"):
    while True:
        speak("Say something...")
        text = listen(lang)
        if text == "":
            speak("Sorry, I did not understand you.")
            continue
        elif text.lower() in byeWords:
            speak("Bye!")
            break
        aiResp = chat(text)
        speak(aiResp)

askAI()