import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import random
import sys
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing..")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")    
        return "none"
    return query
if __name__ == "__main__":
    wish()
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "what's up seri" in query or "how are you" in query:
            msg=["just doing my thing!","i am fine","nice","i am good what about you"]
            speak(random.choice(msg))
        elif "play online music" in query:
            speak("which actor or singer music you want to listen")
            k=takecommand().lower()
            webbrowser.open(f"https://gaana.com/playlist/inhouse-dj-{k}-hits")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "what is your name" in query:
            speak("Hi I am seri Sir")
        elif "stop" in query:
            speak("okay have a nice day")
            sys.exit()
        elif "play music" in query:
            music="E:\\songs"
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[random.randint(1,30)]))
        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {time}")
        elif "send email" in query:
            speak("please enter the your email id and to whom you want to send the mail")
            g=input("enter email id of sender here.....")
            t=input("enter email id of reciever here.....")
            speak("what is subject of your mail")
            h=takecommand().lower()
            speak("what is the content of your mail")
            l=takecommand().lower()
            co=smtplib.SMTP("smtp.gmail.com",587)
            co.ehlo()
            co.starttls()
            co.login("f{g}","Sanjupooja@9")
            co.sendmail("f{g}", f"{t}",f"Subject: {h} \n\n {l}")
            co.quit()
