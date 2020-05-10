import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    '''
    Initial function to wish me checking the time of the day and starting the main work! 
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am jarvis at your service SIR!")


def command():
    '''
    Inputs from mic goes here and returns string output!
    '''
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
        return "None"

    return query


if __name__ == '__main__':
    wish()
    flag = True
    while True:
        query = command().lower()
        if query == "none":
            if flag:
                speak('I did not get that?...')
            flag = False

        elif 'quit' in query:
            speak("Thank you Sir..Going to sleep!")
            break

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}\n")

        elif "the date" in query:
            strDate = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is{strDate}\n")

        elif "the weather" in query:
            speak('Todays weather according to google...')
            webbrowser.open(
                'https://www.google.com/search?q=todays+weather&rlz=1C1CHZL_enIN787IN787&oq=todays&aqs=chrome.1.69i57j0l7.3230j0j9&sourceid=chrome&ie=UTF-8')

        elif "about today" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            strDate = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is{strDate}\n")
            speak(f"Current time is{strTime}\n")
            speak('Todays weather according to google...')
            webbrowser.open(
                'https://www.google.com/search?q=todays+weather&rlz=1C1CHZL_enIN787IN787&oq=todays&aqs=chrome.1.69i57j0l7.3230j0j9&sourceid=chrome&ie=UTF-8')
            speak('Also opened special occasion occured today on google...')
            webbrowser.open('https://www.google.com/search?rlz=1C1CHZL_enIN787IN787&ei=4kGHXrCHLtKR4-EPw5ur2AQ&q=today&oq=today&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgtURoAHABeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiwgNnotczoAhXSyDgGHcPNCksQ4dUDCAs&uact=5')

        elif 'open code' in query:
            codePath = "C:\\Users\\Yutish-pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'open android studio' in query:
            codePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codePath)

        elif 'open code blocks' in query:
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)

        elif 'open image editor' in query:
            codePath = "C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe"
            os.startfile(codePath)

        elif 'open web editor' in query:
            codePath = "C:\\Program Files (x86)\\Brackets\\Brackets.exe"
            os.startfile(codePath)

        elif 'open idea' in query:
            codePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2018.3.4\\bin\\idea64.exe"
            os.startfile(codePath)

        elif 'in wikipedia search' in query:
            speak("Searching Wikipedia...")
            query = query.replace("in wikipedia search", "")
            results = wikipedia.summary(query, sentences=2)
            print(query)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'google search' in query:
            query = query.replace("google search", "")
            webbrowser.open('https://www.google.com/search?rlz=1C1CHZL_enIN787IN787&ei=4kGHXrCHLtKR4-EPw5ur2AQ&q='+query+'&oq='+query +
                            '&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgtURoAHABeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiwgNnotczoAhXSyDgGHcPNCksQ4dUDCAs&uact=5')

        elif 'all coding' in query:
            webbrowser.open('https://www.interviewbit.com/practice/')
            webbrowser.open('https://www.hackerearth.com/challenges/')
            webbrowser.open('https://leetcode.com/problemset/all/')
            webbrowser.open('https://www.codechef.com/')
            webbrowser.open('https://codeforces.com/')

        elif 'open hackerearth' in query:
            webbrowser.open('https://www.hackerearth.com/challenges/')

        elif 'open interviewbit' in query:
            webbrowser.open('https://www.interviewbit.com/practice/')

        elif 'open leetcode' in query:
            webbrowser.open('https://leetcode.com/problemset/all/')

        elif 'open codechef' in query:
            webbrowser.open('https://www.codechef.com/')

        elif 'open codeforces' in query:
            webbrowser.open('https://codeforces.com/')

        elif 'open geeksforgeeks' in query:
            webbrowser.open('https://www.geeksforgeeks.org/')

        elif 'jarvis' in query:
            speak("How can I help you Sir!")

        else:
            speak("I am googling about" + query +
                  "Showing you the results sir!")
            webbrowser.open('https://www.google.com/search?rlz=1C1CHZL_enIN787IN787&ei=4kGHXrCHLtKR4-EPw5ur2AQ&q='+query+'&oq='+query +
                            '&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgtURoAHABeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiwgNnotczoAhXSyDgGHcPNCksQ4dUDCAs&uact=5')

        if query != "none":
            flag = True
