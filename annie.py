from ctypes.wintypes import MSG
import ntpath
import sys
import time
from tkinter import Message
from tkinter.constants import YES
from urllib import request
from jaraco.context import temp_dir 
import pyttsx3 as pyt
import speech_recognition as sr
import datetime
import pyjokes
from torch.types import Number
import wikipedia
import webbrowser
import os
import subprocess
import json
import requests
from wikipedia.wikipedia import search
import wolframalpha
import random
import smtplib
import pyautogui
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email import encoders
from instadownloader import instaloader
import pywhatkit
from bs4 import BeautifulSoup
import PyPDF2
import speedtest
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from annieui import Ui_AnnieUI
 

engine = pyt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# --------------------------------------------------------------------------------------------------------------------------------------------------

def speak(audio):
    engine.say(audio)
    engine.setProperty("rate", 178)
    engine.runAndWait()

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Wish me

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Annie. Please tell me how may I help you")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

def sendmail(to, content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rv9718970448@gmail.com', 'passwordrv')
    server.sendmail('rv9718970448@gmail.com', to, content)
    server.close()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=c69abd8d8b4e468a8b61c42f65f62cf2'

    main_page = requests.get(main_url).json()
    article = main_page["article"]
    head = []
    day = ["first", "second", "third", "forth", "fifth",
           "sixth", "seventh", "eighth", "nineth", "tenth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
    Take mic. input from user and returns string output
'''

class MainThread(QThread):  
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            # r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f" user said: {query}")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
                            
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takeCommand().lower()

            # logics for executing tasks based on query
            if "about" in self.query:
                speak("searching wikipedia...")
                query = self.query.replace("Wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to wikipedia..")
                print(results)
                speak(results)
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            # time
            elif "time" in self.query:
                strtime = datetime.datetime.now().strftime("%H,%M,%S")
                speak(f"Sir, the time is{strtime}")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------   
            # close
            elif "goodbye" in self.query or "ok bye" in self.query or "stop" in self.query:
                speak('your personal assistant aanie is shutting down,Good bye')
                break
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # youtube
            elif 'open youtube' in self.query:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # google
            elif 'open google' in self.query:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # gmail
            elif 'open gmail' in self.query:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # news
            elif 'news' in self.query:
                # webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                # speak('Here are some headlines from the Times of India.')
                speak("please wait sir, featching latest news")
                news()
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------    
            # search
            elif 'search' in self.query:
                query = query.replace("search", "")
                webbrowser.open_new_tab(self.query)
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # Ask
            elif 'ask' in self.query:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question = self.takeCommand()
                app_id = "76QHQA-YY74JRK2TP "
                client = wolframalpha.Client('76QHQA-YY74JRK2TP')
                res = client.self.query(question)
                answer = next(res.results).text
                speak(answer) 
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------    
            # music
            elif 'play music' in self.query:
                music_dir = 'C:\\Users\\hp\\OneDrive\\Desktop\\pd\\mama\\mama\\Personal\\urvashi\\Personal Data\\Misc. Data\\Personal\\photo\\arvind'
                songs = os.listdir(music_dir)
                print(songs)
                number = random.randint(1.100)
                os.startfile(os.path.join(music_dir, songs[number]))
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------    
            # weather
            elif "weather" in self.query:
                speak("tell me the place sir.")
                weather = self.takeCommand().lower()
                search = weather
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # logout
            elif "log off" in self.query or "sign out" in self.query:
                speak(
                    "Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # who r u
            elif 'who are you' in self.query or 'what can you do' in self.query:
                speak('I am annie version 1 point o your personal assistant. I am programmed to minor tasks like'
                    'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                    'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            elif "who made you" in self.query or "who created you" in self.query or "who discovered you" in self.query:
                speak("I was built by Arnav")
                # print("I was built by Arnav")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # cmd
            elif 'open cmd' in self.query:
                os.system("Start CMD")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # ip
            elif 'my ip Address' in self.query:
                ip = webbrowser.get('https://api.ipfy.org').text
                speak('your IP Address is {ip}')
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # set alarm
            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music = "E:\\music"
                    song = os.listdir(music)
                    os.startfile(os.path.join(music, song[0]))
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # speedtest
            elif 'speedtest' in self.query:
                st = speedtest.Speedtest()
                d1 = st.download()
                up = st.upload()
                speak(f"sir we have {d1} bit per second downloading speed and {up} bit per second uploading speed")

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # joke
            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # shuddown, sleep, restart
            elif 'shutdown the system' in self.query:
                os.system("shutdown /s /t S")
            elif 'restart the system' in self.query:
                os.system("shutdown /r /t S")
            elif 'sleep the system' in self.query:
                os.system("round1132.exe powrprof.dll,SetSuspendState 0,1,0")
            # switch window
            elif 'switch window' in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # email
            elif 'mail' in self.query:
                try:
                    speak("What should i say?")
                    content = self.takeCommand()
                    to = 'arnavkhatri123@gmail.com'
                    sendmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry, i am not able send mail at this time.")
            elif "send a mail" in self.query:
                speak('what should i say sir')
                self.query = self.takeCommand().lower()
                if "send a file" in self.query:
                    email = 'rv9718970448@gmail.com'
                    password = 'passwordrv'
                    speak("please enter the receivers mail id into the shell")
                    send_mail_to = input("please enter mail here: ")
                    speak("ok sir, what is the subject for this mail")
                    self.query = self.takeCommand().lower()
                    subject = self.query
                    speak("and sir, what is the message for this mail")
                    self.query2 = self.takeCommand().lower()
                    message = self.query2
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here: ")

                    speak("please wait i am sending mail now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_mail_to
                    msg['subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # setup attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = ('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Description',
                                    'attachment; filename=%s' % filename)

                    # attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_mail_to, text)
                    server.quit()
                    speak("Email has been sent")

                else:
                    email = "rv9718970448@gmail.com"
                    password = "passwordrv"
                    send_mail_to = input(
                        "please enter the receivers mail id into the shell")
                    message = query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_mail_to, message)
                    server.quit()
                    speak("Email has been sent")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # location
            elif "where i am" or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = "https://get.geojs.io/v1/ip/geo/"+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(
                        f"Sir i am not sure, but we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, due to network issue  i am not able to find where we are.")
        
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # screenshot
            elif "take screenshot" or "take a screenshot" in self.query:
                speak("sir please tell me the name of the screenshot file")
                name = self.takeCommand().lower()
                speak("please sir hold screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is svaed in our main folder.")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # send messages
            elif "send a whatsapp message" in self.query:
                speak("to whome?")
                number1 = self.takeCommand().lower()
                speak("What message?")
                message1 = self.takeCommand().lower()
                pywhatkit.sendwhatmsg_instantly(number1, message1)
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # pdf reader
            elif "read pdf" in self.query:
                speak("Enter pdf name")
                a = self.takeCommand().lower()
                book = open(a, 'rb')
                pdfreader = PyPDF2.PdfFileReader(a)
                page = pdfreader.numPages
                speak(f"total no. of pages in this book {page}")
                speak("sir please tell me the page number i have to read")
                pg = self.takeCommand().lower()
                page = pdfreader.getPage(pg)
                text = page.extractText()
                speak(text)
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # thank you
            elif "thank you" in self.query:
                speak("it's my pleaseure sir")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
            # instagram profile
            elif "instagram profile" or "profile on instagram" in self.query:
                speak("Sir please enter your user name: ")
                name = input("Enter user name: ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here is the profile of the user {name}")
                time.sleep(5)
                speak("Would you like to download profile pic of the user:")
                condition = self.takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile pic is saved in our main folder.")
                else:
                    speak("ok sir")
        
            else:
                speak("This command not found.")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AnnieUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("00.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()
        
app = QApplication(sys.argv)
annie = Main()
annie.show()
exit(app.exec_())