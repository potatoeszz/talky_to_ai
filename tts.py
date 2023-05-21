
import os
#os.system("say [[volm 1]] hello world")

def speak(text, rate=125, volm=1):
    command = "say -r" + str(rate) + " [[volm " + str(volm) + "]] " + text
    os.system(command)


#def speak(text, rate=125, volm=1):
    #if text == "":
        #pass
    #else:
        #os.system("say " "-r " + rate + " [[ volm " + volm " ]]" + text )
        #pass

speak("hello world", 200, 1)