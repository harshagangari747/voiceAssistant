import webbrowser
import speech_recognition as sr 
import pyaudio
import wave,sys
import os,time,random
import subprocess,datetime as dt 
import pytz,requests,re

def userInput() :
    recAud = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        recAud.pause_threshold = 1
        audio = recAud.listen(source)
    try : 
        print("Interpreting...")
        command = recAud.recognize_google(audio,language='en-in')
        print("Command is : ", command)
    except Exception as e :
        print("Try saying that again...")
        return "None"
    return command

def runVoiceAssistant() :
    userComm = ""
    action = ['open','close','search']
    images = [' open gallery','show images','images','photos','show']
    browsers = ['broswer','edge','google.com','google','firefox','open browser']
    music = ['music','song','songs','play music','play','music player']
    while userComm != "exit" :
        userComm = userInput().lower()
        if any(browsers in userComm for browsers in browsers) :
            ffbrow = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(ffbrow))
            # edge = "C:\\Windows\\SystemApps\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\msedge.exe"
            # webbrowser.register('edge',None,webbrowser.BackgroundBrowser(edge))
            websiteRegex = re.compile("[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" +"{2,6}\\b([-a-zA-Z0-9@:%" +"._\\+~#?&//=]*)")
            site = websiteRegex.search(userComm)
            if site == None :
                site = "google.com"
            else :
                site = site.group()
            if 'firefox' in userComm :
                if "close" in userComm :
                    os.system('taskkill /im firefox.exe')
                elif "open" or "search" in userComm:
                    webbrowser.get('firefox').open('https://www.'+site)
            # elif 'edge' in userComm :
            #     if "close" in userComm :
            #         os.system('taskkill  /im msedge.exe')
            #     elif "open" in userComm :
            #         webbrowser.get('edge').open('https://www.'+site)
            else :
                if "close" in userComm :
                    os.system('taskkill  /im chrome.exe')
                elif "open" or "search" in userComm :
                    webbrowser.open('https://www.'+site)
        elif ('weather update' in userComm) or ('weather'  in userComm):
            cities=['delhi','hyderabad','kolkata','mumbai','chennai','sydney','california','unitedKingdom','sriLanka','egypt']
            city ='hyderabad'
            cm=list(userComm.split(' '))
            for i in cm :
                if i in cities :
                    city = i 
            print(city)
            res = requests.get('http://api.openweathermap.org/data/2.5/weather?'+"q="+city+'&appid=936a4d1ae329696c9921840fde868f19')
            result = res.json()
            farht = result['main']['temp']
            cels = int(int(farht-32)*0.55)
            print("Temparature is : ",result['main']['temp'])
            print("Humidity is :",result['main']['humidity']) 
        elif any(music in userComm for music in music) :
            if ('open' in userComm) or ('play' in userComm) :
                path = "C:\\Users\\user\\OneDrive\\Desktop\\Final Project\Songs\\"
                song=random.choice(os.listdir(path))
                os.startfile(path+song)
                song = song.strip('.mp3')
                qtrack=list(song.split('-'))[0]
                qartist = list(song.split('-'))[1]
                if 'next song' in userComm :
                    os.startfile(path+random.choice(os.listdir(path)))
                lyrics = requests.get('https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track='+qtrack+'&q_artist='+qartist+'&apikey=58bb9d76e4aba628c54a4d24ac5cc412')
                result = lyrics.json()
                print(result['message']['body']['lyrics']['lyrics_body'])
            elif 'close' in userComm or 'stop' in userComm :
                os.system('TASKKILL /F /IM Music.UI.exe')
        elif any(images in userComm for images in images) :
            if 'open' in userComm :
                path = 'C:\\Users\\user\\OneDrive\\Desktop\\Final Project\\Images\\'
                image = os.listdir(path)
                pic = random.choice(image)
                os.startfile(path+pic)
            elif 'close' in userComm :
                os.system('taskkill /f /im Microsoft.Photos.exe')
        elif 'news' in userComm :
            res = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=920f8ab777584d5da8999efebb4d7777')
            news = res.json()
            for i in (news['articles']) :
                print(i['description'])
if __name__ == '__main__' :
    runVoiceAssistant()