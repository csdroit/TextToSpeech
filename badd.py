from gtts import gTTS
import os

def say(to_speech):
    l = 'en'
    txt = to_speech
    out = gTTS(text=txt , lang=l , slow=False )
    out.save("voice.mp3")
    os.system("mpg123 voice.mp3")

def delete(file):
    os.system("rm "+file)


say("welcome")

x = input("Enter you name :")
what_to_say = "i love you " +x+ " so fucking much haha"

say(what_to_say)

os.system('read -n 1 -s -r -p "Press any key to continue" ')

say("see you later")
