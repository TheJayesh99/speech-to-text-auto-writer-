import speech_recognition as sr
import pyautogui
import pyttsx3
import datetime


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am speech to text program . i will help you to type  whatever you say . so let's go")


#### Determining the output audio ####
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#### This function is use to recognise the audio #### 
def speechRecognizer():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        
        audio = r.listen(source)
        
    ## This function is use to convert audio to text ##
    try:
       text = r.recognize_google(audio)
    except:
        text = ""
    return text

##### This Function use to write ####   
def writing(text):
    speak(f'Your Text :\n {text} \n \b Select the area where you want to write this and then press ok')
    confirm = pyautogui.confirm(f'Your Text :\n {text} \n \t Select the area where you want to write this and then press ok')
    if confirm == 'OK':
        pyautogui.write(text,interval=0.01)

# main Function 
if __name__ == "__main__":
    wishMe()
    while True:
        speak("do you want me to type something ?\n")
        choice = speechRecognizer()
        
        
        if 'yes' in choice.lower()  :
            speak("speak now")
            text = speechRecognizer()
            speak('OK , i am processing the text ')
          
            writing(text)
        elif 'no' in choice.lower() :
            speak(' i am closing this program . hope you have a good day today, byee')
            break
        #### Stand by #########
        elif 'stand by' in choice.lower() :
            speak("are you sure you want me on standby? yes or no ")
            choice = speechRecognizer()
        
            if 'yes' in choice.lower():
                speak("Ok, i am on standby say restart to activate me")
                while True:
                    decision = speechRecognizer()
                    if 'restart' in decision.lower():
                        speak("okay, i am starting speech to text program")
                        break
            else:
                speak("sorry , didn't get you can you speak again")
        else :
            speak("sorry , didn't get you can you speak again")































