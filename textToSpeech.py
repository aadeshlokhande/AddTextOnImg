from gtts import gTTS 

def tts(mytext):    
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save("hello.mp3")


tts("Hello")