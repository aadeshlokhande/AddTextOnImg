from gtts import gTTS 

def tts(mytext):    
    myobj = gTTS(text=mytext, lang='en', slow=True)
    myobj.save("hello.mp3")


tts("Hello")