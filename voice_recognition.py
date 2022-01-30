import speech_recognition as sr



recognizer : sr = sr.Recognizer() 

#We´re using the micro
with sr.Microphone() as source:
    print('Speak Anything : ')
    #save the audio
    audio = recognizer.listen(source)
 
    try:
        #pass the audio to text
        text = recognizer.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry could not hear')