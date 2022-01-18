import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('regonitioning.....')
        command= r.recognize_google(audio, language='en-in')
        print("user said: ",command)

    except Exception as e:
        print('say it again please....')
        return "none"
    return command

    
            
talk("this is vairab roy and we want to convert it more sequently features")
while True:
    command = take_command().lower()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %S')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
