import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
import speedtest
from pygame import mixer
from plyer import notification
from Translator import translategl


# Asking for Password
for i in range(3):
    a = input("Enter Password to open SARA :\n")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SAY [HEY SARA] TO BOOT ME UP")
        break
    elif (a!=pw):
        print("Try Again")
    elif (i==2 and a!=pw):
        exit()
# Graphic User Interface
from BootUpGUI import play_gif
play_gif

# Gives the voice of the Assistant
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# defines the command to take from the User
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Please Rephrase that")
        return "None"
    return query
# Alarm Function
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# Greetings after the Initial Bootup
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hey sara" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "sleep now" in query:
                    speak("Ok sir! You can call me anytime")
                    break 
                
                    #Translation to any language Function
                elif "translate" in query:
                    query = query.replace("SARA","")
                    query = query.replace("translate","")
                    translategl(query)

                #  Making a Schedule Function
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("Schedule.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("Schedule.txt","w")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("Schedule.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                # Delivering the schedule via popup notification Function               
                elif "what is my schedule" in query:
                    file = open("Schedule.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )    

                # Normal Conversation Function
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("i am Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "who are you"in query:
                    speak("i am Systematically Automated Response Assistant. you can call me SARA")
                elif "who is your developer" in query or "who is your creator" in query:
                    speak("My creator is Sayan Dutta, a engineer who turns fascinations into reality")

                # opening any application be it online or on the host system Function
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                # Searching anything through the Internet Function
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                # Delivering the news Function
                elif "news" in query:
                    from News import latestnews
                    latestnews()

                # Calculating Arithmetic problems Function
                elif "calculate" in query:
                    from Calculate import WolfRamAlpha
                    from Calculate import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                # Inquiring about the Weather Function
                elif "temperature" in query or "weather" in query:
                    search = "temperature in Burdwan"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                # Inquiring about the time Function
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                # Exiting the program Function/Turning the assistant off     
                elif "terminate" in query:
                    speak("ok sir! Terminating in, 3, 2, 1")
                    exit()

                # setting an alarm Function
                elif "set an alarm" in query:
                    print("input time format:- HH MM SS")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                # Playing Rock Paper Sissor Game Function
                elif "bored" in query or "game" in query:
                    from game import game_play
                    game_play()

                # Multimedia controls Function
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                # Setting a Reminder Function
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that i have","\nremind you")
                    speak("ok sir! noting it down in your reminders" )
                    remember = open("Reminder.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "reminder" in query:
                    remember = open("Reminder.txt","r")
                    speak("You told me to." + remember.read())

                # Playing Audio Visual Function
                elif "tired" in query or  "music" in query:
                    speak("Ok Sir! just relax and chill while i play some soothing music")
                    a = (1,2,3) 
                    b = random.choice(a)
                    if b==1:
                        os.startfile("1.mp4")
                    elif b==2:
                        os.startfile("2.mp4")
                    else:
                        os.startfile("3.mp4")
                elif "stop it" in query or "quit" in query:
                    speak("Ok, stopping the music")
                    os.system(f"taskkill /f /im vlc.exe")

                # Inquiring the wifi speed Function
                elif "internet speed" in query:
                    speak("Fetching the WIFI speed. Please Wait a minute ")
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi download speed is ",download_net)
                    print("Wifi Upload Speed is", upload_net)
                    speak(f"Wifi download speed is {download_net} Megabytes per second")
                    speak(f"Wifi Upload speed is {upload_net}Megabytes per second")                


                # Taking a real time screenshot Function
                elif "screenshot" in query:
                     import pyautogui 
                     speak("ok sir! taking a screenshot")
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                #Accessing the camera Function
                elif "photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                # Changing the program password Function
                elif "change the password" in query:
                    speak("ok sir! What's the new password ")
                    new_pw = input("Enter the new password:\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                # Turning the entire system off Function
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no):\n")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] \n "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("D:\PYTHON CODES\SARA - Systematically Automated Response Assistant\\FocusMode.py")
                    else:
                        pass