
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import datetime
import pyjokes
import os
import smtplib
import random
import time
import wolframalpha
import pyautogui
import requests
from tkinter import *
from PIL import ImageTk, Image

client = wolframalpha.Client('6VW827-98ULYAR627')
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
email_list = {'program': '@gmail.com',
              'red': '@gmail.com ',
              'thunder': '@gmail.com ',
              'black': '@gmail.com',
              'me': '@gmail.com'
              }


# def sendemail(reciver,subject,tell):
#     server =smtplib.SMTP('smtp.gmail.com',587)
#     server.starttls()
#     server.login('email','password')
#     email=EmailMessage()
#     email['From']="email"
#     email['To']=reciver
#     email['Subject']=subject
#     email.set_content(tell)
#     server.send_message(email)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)

# this function will fetch news from news api
def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0728bbf8d6d7480b90b9cc9021a36d57"

    main_page = requests.get(main_url).json()
    article = main_page['articles']
    head = []
    day = ["First", " second", "third", "foruth", "fifth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"Todays {day[i]} news is :\n{head[i]}")



# this fution will do text to speech
def speak(audio):
    print('Jarvis:' + audio)
    engine.say(audio)
    engine.runAndWait()


# this function will wishme good morning goodday or goodnigh
def wishme():
    d = datetime.datetime.now().strftime("%I:%M %p")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good moring sir its \t" + d)
    elif hour > 12 and hour < 18:
        speak("Good afternoon sir its \t" + d)
    else:
        speak("Good evening its \t" + d)

    speak("I am your digital assistant jarivs  What can i do for you")


# this function will do voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"UserSaid :{query}")

    except Exception:
        speak("sorry Please say that again")
        return "None"
    return query


class Wigdet:
    def  __init__(self):
        root = Tk()
        root.title('Jarvis(Mark-1)')
        root.config(background='Red')
        root.geometry('1200x1000')
        root.resizable(0, 0)
        self.compText = StringVar()
        self.userText = StringVar()
        self.userText.set('Click \'Start \' to Give commands')

        userFrame = LabelFrame(root, text="USER", font=('Black ops one', 19, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, bg='#B983FF', fg='white')
        left2.config(font=("Comic Sans MS", 20, 'bold'))
        left2.pack(fill='both', expand='yes')

        img = ImageTk.PhotoImage(Image.open("F:\ironjarvis.jpg"))
        panel = Label(root, image=img)
        panel.pack(side="top", fill="both", expand="yes")

        compFrame = LabelFrame(root, text="JARVIS", font=('Black ops one', 19, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='#94B3FD', fg='white')
        left1.config(font=("Comic Sans MS", 20, 'bold'))
        left1.pack(fill='both', expand='yes')

        btn = Button(root, text="Start Listening!", font=("Airal", 19, 'bold'), bg="#F90716", fg="white", bd=5,
                     height=1, pady=3, command=self.clicked)
        btn.pack(fill='x')
        btn2 = Button(root, text="Close!", font=("Airal", 19, 'bold'), bg="#FFF323", fg="white", bd=5, height=1, pady=3,
                      command=root.destroy)
        btn2.pack(fill='x')
        self.compText.set('Hello, I am Jarvis! What can i do for you Sir ??')

        root.bind("<Return>", self.clicked)  # handle the enter key event of your keyboard
        root.mainloop()

    def clicked(self):
            print('Working')
            self.userText.set('Listening...')

            query = takecommand().lower()
            self.userText.set('Listening...')
            self.userText.set(query)

            if 'who are you' in query:
                speak(
                    "Jarvis is a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man, Iron Man 2 ")
                print(
                    "Jarvis is a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man, Iron Man 2 ")

            # elif 'who' in query:
            #     speak("Searching Wikipedia..")
            #     query=query.replace("wikipedia","")
            #     results=wikipedia.summary(query, 2)
            #     print(results)
            #     speak(results)

            elif 'open youtube' in query:
                speak("Opening youtube")
                self.compText.set('okay Opening youtube')
                webbrowser.open("youtube.com")


            elif 'open facebook' in query:
                speak("Opening facebook")
                self.compText.set('okay Opening facebook')
                webbrowser.open("facebook.com")

            elif 'open google' in query:

                speak("Opening google.com")
                self.compText.set('Opening google.com ')
                speak("sir ! What you want to search on goggle")
                self.compText.set('sir what you want to search on goggle ')

                cm = takecommand()
                webbrowser.open(f"{cm}")

            elif 'play' in query:
                songs = query.replace('play', '')
                speak('playing' + songs)
                self.compText.set('okay ' + songs)
                pywhatkit.playonyt(songs)

            elif 'time' in query:
                t = datetime.datetime.now().strftime("%I:%M %p")
                speak("Current time is" + t)
                self.compText.set('okay ')

            elif 'wikipedia' in query:
                speak("Searching Wikipedia")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                self.compText.set(results)
                print(results)
                speak(results)


            # elif 'the' in query:
            #     speak("Searching Wikipedia")
            #     results=wikipedia.summary(query, 2)
            #     print(results)
            #     speak(results)

            elif 'how are you' in query or 'whatsapp' in query:
                st = ['Just doing my thing', 'Nice', 'I am nice and full of energy', ]
                speak(random.choice(st))
                self.compText.set(random.choice(st))

            elif 'gmail' in query:
                speak("Opening Gmail")
                self.compText.set('okay')
                webbrowser.open('www.gmail.com')

            elif 'are you single' in query:
                speak("I am in relationship with alexa")
                self.compText.set('I am in relationship with alexa')


            elif 'Thankyou' in query:
                speak('Have a nice day')
                self.compText.set('have a nice day')

            elif 'joke' in query or "tell me joke" in query:
                speak(pyjokes.get_joke())
                self.compText.set(pyjokes.get_joke())


            elif 'make me laugh' in query:
                speak(pyjokes.get_joke())
                self.compText.set(pyjokes.get_joke())

            elif 'open visual studio' in query:
                codepath = "C:\\Users\\Maaz Shaikh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("opening Visual studios")
                os.startfile(codepath)
                self.compText.set('Opening visual studio code')

            elif 'open pycharm' in query:
                codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
                os.startfile(codepath)

            elif 'open android studios' in query:
                codepath = "C:\\Program Files\\Android\Android Studio\\bin\\studio64.exe"
                os.startfile(codepath)
                self.compText.set('Opening Android Studios')

            elif "open command prompt" in query or "cmd" in query:
                os.system("start cmd")
                self.compText.set('Opening CommandPrompt')
            elif 'open notepaad' in query:
                codepath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
                os.startfile(codepath)
                self.compText.set('Opening notepaad')

            elif 'open chrome' in query:
                codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codepath)
                self.compText.set('Opening Chrome')

            elif 'nothing' in query or 'stop' in query or 'abort' in query or 'quit' in query or 'no thanks' in query:
                speak('okay')
                speak('Bye sir,have a good day')
                self.compText.set('okay')
                self.compText.set('Bye sir have a good day')
                sys.exit()

            elif 'switch' in query or 'window' in query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "Tell me the news" in query or 'news' in query:
                self.compText.set('Please wait featching the latest news')
                speak('Please wait featching the latest news')

                news()



            elif "what is my ip" in query or 'ip' in query:
                ip = requests.get('https://api64.ipify.org').text
                print(ip)
                speak(f"Your ip is {ip}")
                self.compText.set(f"Your ip is {ip}")

            elif 'hello' in query:
                speak("Hello Sir")
                self.compText.set("Hello Sir")

            # elif 'send email' in query:
            #     speak("To whom you want to send email")
            #     self.compText.set("To Whom you wand to send email")
            #     name=takecommand().lower()
            #     reciver=email_list[name]
            #     print(reciver)
            #     speak("What is the subjects of our email")
            #     self.compText.set("What is the subjects of our email")
            #     subject=takecommand().lower()
            #     speak("Tell me the text of your email")
            #     self.compText.set("Tell me the text of your email")
            #     message=takecommand().lower()
            #     sendemail(reciver,subject,message)
            #     speak("Hey lazy your email has been sent")
            #     self.compText.set("Hey lazy your email has been sent")
            elif 'send email' in query:
                try:
                    speak("What should I say?")
                    self.compText.set('What should I say?')
                    content = takecommand()
                    to = 'kaifmukri123@gmail.com'
                    sendEmail(to, content)
                    speak("Email has been sent !")
                    self.compText.set('Email has been sent')
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
                    self.compText.set('I am not able to send this email')

            elif "close notepad" in query:
                speak("okay sir closing")
                os.system("taskkill/f/im notepad.exe")
            elif "close visualstudio" in query:
                speak("okay sir closing")
                os.system("taskkill/f/im Code.exe")
            elif 'shutdown' in query or "shutdown the system" in query:
                os.system("shutdown /r /t 5")
            elif 'restart' in query or "restart the system" in query:
                os.system("restart /r /t 5")

            elif "weather" in query or 'temperature' in query:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak("Got it")
                    self.compText.set(results)
                    speak(results)
                except StopIteration:
                    print("No results")


            else:
                query = query.replace("Wikipedia", "Google")
                results = wikipedia.summary(query, sentences=1)
                speak("According to google")
                speak('Got it')
                self.compText.set('Got it')
                self.compText.set(results)
                speak(results)
                query = query
                webbrowser.open(f"{query}")



if __name__ == "__main__":
        wishme()
        widget=Wigdet()
        speak("Closing Jarvis")