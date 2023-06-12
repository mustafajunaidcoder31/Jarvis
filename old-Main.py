#extarnal modules

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import requests
from bs4 import BeautifulSoup



#internal modules

import time
import datetime
import webbrowser
import os
import smtplib


#pyttsx3 engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)





#def

def speak(audio ):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("wellcome back sir . I am jarvis . Please tell me how may i help you")     


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarviskaemail@gmail.com', 'Saeeda@22')
    server.sendmail('mustafajunaidcoder@gmail.com', to, content)
    server.close()



 #Main code
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()







        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            url = f"https://www.google.com/search?q={query}" 
            r = requests.get(url)
            speak('opening results for you sir ')
            webbrowser.open(url)
         

        elif 'open school website' in query:
            webbrowser.open("http://lmcacademics.in/StuDashboardMain.aspx")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
           webbrowser.open("https://www.youtube.com/watch?v=Qp7OCDpJfwU&list=PLVNLN9MWB_kRNTSlqO_Az6arAJKVIk76Q") 


        elif 'jarvis' in query:
            speak("please tell me how may i help you ")
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
        
     
        


        elif 'who am i' in query:  
            speak("You are mister mustafa junaid")

        elif 'open code' in query:
            codePath = "C:\\Users\\prote\\AppData\\Local\\Programs\\Microsoft VS Code\\"
            os.startfile(codePath)

        elif 'open microsoft word' in query:
            microsoft = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD"
            os.startfile(microsoft)

        elif 'open excel' in query:
            excel = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL"
            os.startfile(excel)

        elif 'open PowerPoint' in query:
            poverpoint = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POVERPNT"
            os.startfile(poverpoint)

      

    

        elif 'thanks' in query:  
            speak("no problem sir ")
    



     

        elif 'email to bro' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mustafajunaidcoder31@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend mustafa bhai. I am not able to send this email") 

        elif 'temperature' in query:
             search = "temperature in lucknow"
             url = f"https://www.google.com/search?q={search}" 
             r = requests.get(url)
             data = BeautifulSoup(r.text,"html.parser")
             temp = data.find("div",class_="BNeawe").text
             speak(f"current {search} is {temp}")
             print(f"current {search} is {temp}")

        elif 'date' in query:
             searchdate = "date"
             url = f"https://www.google.com/search?q={searchdate}" 
             r = requests.get(url)
             data = BeautifulSoup(r.text,"html.parser")
             date = data.find("div",class_="BNeawe").text
             speak(f"current {searchdate} is {date}")
             print(f"current {searchdate} is {date}")

            
       

 


                



 
        




