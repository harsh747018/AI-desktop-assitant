# mainly devloped for daily use application ,like you use google,youtube,stackoverflow everyday you sent email,listen to music, 

# or watch movie     

#code is written in python and visual studio is used ,any python IDE can be used like pycharm or anything

import pyttsx3 #pip install pyttsx3
               #used for speak function


import speech_recognition as sr #pip install speechRecognition
                                #it recognises speech input given by user


import datetime


import wikipedia #pip install wikipedia
                 # for acessing wikipedia   


import webbrowser# it is inbuild module for acessing various websites


import os


import smtplib# python package for sending email 
              # less secure app should be allowed to provide third party login


# sapi5 is a windows API and we can take any voice with it usualy any system have two voices one male and one female
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')


#for selecting voice which ever you wish first is female and second is male
engine.setProperty('voice', voices[0].id)





# whatever speech input argument is given it speaks 
def speak(audio):
    engine.say(audio)           #it will speak the audio string
    engine.runAndWait()




#This will wish the user on basis of time and introduces itself  
def wishMe():
    
    hour = int(datetime.datetime.now().hour)#it will get time from system in hour variable
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    
    else:
        speak("Good Evening!")  

    
    speak("Sir I am Haley , AI desktop assistant . Please tell me how may I help you")       




#It takes microphone input from the user and returns string output

def takeCommand():
    

    r = sr.Recognizer()         # recogniser is class that will allow us to recognise audio
    
    
    with sr.Microphone() as source:
        print("Listening...")
       
        r.pause_threshold = 1   #it seconds of non audio session before input is consudered finish
                                #r.energy_threshold = 100
        
        audio = r.listen(source)# all recogniser ,microphone ,listen are class fuction comes from sppech_recognizer module
    
    
    
    #in case program doesn't pickup what user is saying try block is used 
    try:
        
        
        print("Recognizing...") 
    #there are many reconize fuction for speech recongnising like recognize_google,recognize_googlecloud,recognize_bing 
    #recognize_google is best among them 
    # it takes iput in any  language       
        
        
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
   
   
   
    #asks user to speak again
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query




def sendEmail(to, content):
    
    
    server = smtplib.SMTP('smtp.gmail.com', 587)# 587 is the port
    server.ehlo()
    server.starttls()
    server.login('kunarh371@gmail.com', 'qwerty@123')
    server.sendmail('harsh747018@gmail.com', to, content)
    server.close()




if __name__ == "__main__":
    
    wishMe()
    
    while True:        # for coutinously taking input 
    
    # if 1:
        
        query = takeCommand().lower()

        
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")# it replaces wikipedia is query with blank and search  iput will be left
            results = wikipedia.summary(query, sentences=2)# it will return return first two sentence of result
            speak("According to Wikipedia")
            print(results)                                 #it will write result in terminal
            speak(results)                                 #it will speak the result

        
        
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


       
        elif 'play music' in query:                   #function for playing music
            music_dir = 'F:\songs'                    #directory in which songs are present 
            songs = os.listdir(music_dir)             # os is inbuild module 
                                                      #listdir will play onre file after the other
            print(songs)                              # will print song name
            os.startfile(os.path.join(music_dir, songs[0]))#os.startfile will open the file and pth.join will play the first file in it
                                                      #random module can used for random songs

        
        
        elif 'play movie' in query:
            movie_dir = 'F:\movie'
            movie = os.listdir(movie_dir)
            print(movie)    
            os.startfile(os.path.join(movie_dir, movie[0]))    

        
        
        elif 'the time' in query:                      # for returning time  if asked by user
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        
        
        
        elif 'email to harsh' in query:                # sending email to a particular person
            try:
                speak("What should I say?")
                content = takeCommand()                # takes content to  be sent  
                to = "harsh747018@gmail.com"           # to  is the email of the sender 
                sendEmail(to, content)                 # sendemail fuction login and sent email
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my Sir due to internet error I am not able to send this email, please try later or allow less secure apps to your gmail account")    
