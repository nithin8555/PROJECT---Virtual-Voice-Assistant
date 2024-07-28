import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()

speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)

#voices = speaker.getProperty('voices')
#speaker.setProperty('voice', voices[1].id)

def speak(text):
    speaker.say("yes boss" + text)
    speaker.runAndWait()
def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

v_name = "fibo"

speak_ex("i am your " + v_name + "tell me boss.")
def take_command():
    command = " "
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if v_name in command:
                command=command.replace(v_name + " "," ")
    except :
        print("check your Microphone")
    return command

while True :
    User_command = take_command()
    if "close" in User_command:
        print("see you again bye ")
        speak("see you again bye ")
        break
    elif "time" in User_command:
        cur_time=dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif "play" in User_command:
        User_command=User_command.replace('play'," ")
        print("playing"+User_command)
        speak("playing" + User_command + "enjoy.")
        pk.playonyt(User_command)
        break
    elif "search for" in User_command or "google" in User_command:
        User_command = User_command.replace("search for"," ")
        User_command = User_command.replace("google"," ")
        speak("searching for" + User_command)
        pk.search(User_command)
        break
    elif "who is" in User_command:
        User_command = User_command.replace("who is "," ")
        info = wiki.summary(User_command, 2)
        print(info)
        speak(info)
    elif "who are you" in User_command:
        speak_ex("i am your" + v_name + 'tell me boss.')
    else:
        speak_ex("please say it again.")