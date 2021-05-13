import webbrowser
import speech_recognition as sr 
import os,time,random
import datetime as dt 
import requests,re,sys
from dictionary import telugudictionary as td
import threading
import rsaAlgo as rs 
def userInput() :   
    recAud = sr.Recognizer()
    with sr.Microphone() as source :
        print(b'\xE0\xB0\x9A\xE0\xB1\x86\xE0\xB0\xAA\xE0\xB1\x8D\xE0\xB0\xAA\xE0\xB0\x82\xE0\xB0\xA1\xE0\xB0\xBF'.decode('utf-8'))
        recAud.pause_threshold = 1.5
        audio = recAud.listen(source)
    try : 
        print(b'\xE0\xB0\xB5\xE0\xB0\xBF\xE0\xB0\x82\xE0\xB0\x9F\xE0\xB1\x81\xE0\xB0\xA8\xE0\xB1\x8D\xE0\xB0\xA8'.decode('utf-8'))
        command = recAud.recognize_google(audio,language='te-IN')
        print(b'\xE0\xB0\x9C\xE0\xB0\xBE\xE0\xB0\xB0\xE0\xB1\x80\x20\xE0\xB0\x9A\xE0\xB1\x87\xE0\xB0\xB8\xE0\xB0\xBF\xE0\xB0\xA8\x20\xE0\xB0\x86\xE0\xB0\xA6\xE0\xB1\x87\xE0\xB0\xB6\xE0\xB0\x82\x20 :'.decode('utf-8'),command)
    except Exception as e :
        print(b'\xE0\xB0\xAE\xE0\xB0\xB3\xE0\xB1\x8D\xE0\xB0\xB3\xE0\xB1\x80\x20\xE0\xB0\x9A\xE0\xB1\x86\xE0\xB0\xAA\xE0\xB1\x8D\xE0\xB0\xAA\xE0\xB0\xA1\xE0\xB0\xBE\xE0\xB0\xA8\xE0\xB0\xBF\xE0\xB0\x95\xE0\xB0\xBF\x20\xE0\xB0\xAA\xE0\xB1\x8D\xE0\xB0\xB0\xE0\xB0\xAF\xE0\xB0\xA4\xE0\xB1\x8D\xE0\xB0\xA8\xE0\xB0\xBF\xE0\xB0\x82\xE0\xB0\x9A\xE0\xB0\x82\xE0\xB0\xA1\xE0\xB0\xBF...'.decode('utf-8'))
        return "None"
    return command
def runVoiceAssistant() :
    userComm = ""
    action = ['open','close','search']
    images = [' open gallery','show images','images','photos','show','photos']
    browsers = ['broswer','edge','google.com','google','firefox','open browser']
    music = ['music','song','songs','play music','play','music player']
    while userComm != 'exit' :
        userComm = td.getenglish(userInput())
        rs.encrypt(''.join(userComm))
        if "canvas" in userComm :
            process = os.startfile(r"C:\Users\user\OneDrive\Desktop\Final Project\Python files\canvasThread.py")
            while(process) :
                time.sleep(5)
        if any(browsers in userComm for browsers in browsers) :
            ffbrow = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(ffbrow))
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
            else :
                if "close" in userComm :
                    os.system('taskkill  /im chrome.exe')
                elif "open" or "search" in userComm :
                    webbrowser.open('https://www.'+site)
        elif ('weather update' in userComm) or ('weather'  in userComm):
            cities=['delhi','hyderabad','kolkata','mumbai','chennai','sydney','california','unitedKingdom','srilanka','egypt']
            city ='hyderabad'
            cm  = list(userComm.split())
            for i in cities :
                if i in userComm :
                    city = i 
                    print(city)
            print(city+ b'\xe0\xb0\xb5\xe0\xb0\xbe \xe0\xb0\xa4\xe0\xb0\xbe \xe0\xb0\xb5 \xe0\xb0\xb0 \xe0\xb0\xa3\xe0\xb0\x82 \xe0\xb0\x87 \xe0\xb0\xb2\xe0\xb0\xbe \xe0\xb0\x89\xe0\xb0\x82 \xe0\xb0\xa6\xe0\xb0\xbf'.decode('utf-8'))
            res = requests.get('http://api.openweathermap.org/data/2.5/weather?'+"q="+city+'&appid=936a4d1ae329696c9921840fde868f19')
            result = res.json()
            farht = result['main']['temp']
            cels = int(int(farht-32)*0.55)
            print( b'\xe0\xb0\x89 \xe0\xb0\xb7\xe0\xb1\x8d\xe0\xb0\xa3\xe0\xb1\x8b \xe0\xb0\x97\xe0\xb1\x8d\xe0\xb0\xb0 \xe0\xb0\xa4 : '.decode('utf-8'), str(result['main']['temp']) +" F")
            print(b'\xe0\xb0\xa4\xe0\xb1\x87 \xe0\xb0\xae    : '.decode('utf-8')+ str(result['main']['humidity']) +" g/Kg") 
        elif any(music in userComm for music in music) :
            if ('open' in userComm) or ('play' in userComm) :
                path = "C:\\Users\\user\\OneDrive\\Desktop\\Final Project\\Songs\\"
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
            if 'open' in userComm or 'show' in userComm:
                path = 'C:\\Users\\user\\OneDrive\\Desktop\\Final Project\\Images\\'
                image = os.listdir(path)
                pic = random.choice(image) 
                pic = random.choice(image) 
                os.startfile(path+pic)
            elif 'close' in userComm or 'exit' in userComm:
                os.system('taskkill /f /im Microsoft.Photos.exe')
        elif 'news' in userComm :
            res = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=920f8ab777584d5da8999efebb4d7777')
            news = res.json() 
            for i in (news['articles']) : 
                print('------------------------------------')   
                print(i['description'])
        elif 'jokes' in userComm or 'bored' in userComm or 'laugh' in userComm:
            print(b'\xE0\xB0\xA8\xE0\xB1\x87\xE0\xB0\xA8\xE0\xB1\x81\x20\xE0\xB0\xAE\xE0\xB1\x80\x20\xE0\xB0\x95\xE0\xB1\x8B\xE0\xB0\xB8\xE0\xB0\x82\x20\xE0\xB0\x95\xE0\xB1\x8A\xE0\xB0\xA8\xE0\xB1\x8D\xE0\xB0\xA8\xE0\xB0\xBF\x20\xE0\xB0\x9C\xE0\xB1\x8B\xE0\xB0\x95\xE0\xB1\x81\xE0\xB0\xB2\xE0\xB1\x81\x20\xE0\xB0\xB5\xE0\xB1\x86\xE0\xB0\xA4\xE0\xB1\x81\xE0\xB0\x95\xE0\xB1\x81\xE0\xB0\xA4\xE0\xB1\x81\xE0\xB0\xA8\xE0\xB1\x8D\xE0\xB0\xA8\xE0\xB0\xBE\xE0\xB0\xA8\xE0\xB1\x81'.decode('utf-8'))
            time.sleep(0.5)
            res = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,sexist&type=twopart&amount=5')
            result = res.json()
            for i in (result['jokes']) :
                print('setup   : ',i['setup']) 
                print('delivery: ',i['delivery'])
                print('-------------------------------------')
        elif 'exit' in userComm :
            sys.exit(0)
if __name__ == '__main__' :
    thread1 = threading.Thread(target=runVoiceAssistant())
    thread1.start()
    runVoiceAssistant()
