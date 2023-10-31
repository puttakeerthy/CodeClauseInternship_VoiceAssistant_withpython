import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def talk(text):
    global command
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('HELLO I AM ALEXA\n')
            print('I AM HERE TO HELP U ')
            print('say something.....')
            talk('i am alexa i am here to help u say some thing' )
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            
    except:
        pass
    return command

def run_alexa():
    global command,key
    command=take_command()
    print(command)
    if'alexa' in command:
        if 'play' in command:
            song=command.replace('play','')
            talk('playing'+song)
            pywhatkit.playonyt(song)
            key=False

        elif 'time' in command:
            time=datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            talk('current time is '+time)
        elif 'wikipedia' in command:
            person=command.replace('who the is','')
            info=wikipedia.summary(person,1)
            print(info)
            talk(info)
            #key=False
        elif 'date' in command:
            talk('sorry,I have a headache we can go next time and thank you for asking me')
        elif 'are you single' in command:
            talk('i am in a relationship with internet.....i hope we will meet in another university ')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('please say the command again')
    else:
        talk('please call me with a correct name by the way i am alexa')
key=True
while (key==True):
    run_alexa()