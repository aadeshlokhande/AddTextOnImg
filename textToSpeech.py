from gtts import gTTS 
from words import words

import pyttsx3

keys = words.keys()

def tts(word):   

    data  = f"'{word}'."*3 
    data = data + f" aaj hum bat karne wale hai {word} ke baare me." 
    data = data + f" . {word} ka matlab. {words[word]}. hota hayi. " * 3

    myobj = gTTS(text=data, lang='en', slow=False,)
    myobj.save(f"audio/{word}.mp3")

for key in keys:
    print(key)
    tts(key)

# tts("enter")