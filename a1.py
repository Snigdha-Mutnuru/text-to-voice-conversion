from gtts import gTTS
import os

myText = "Hello! This is Snigdha!Hope you are doing good."

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")
