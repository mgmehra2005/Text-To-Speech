from gtts import gTTS
from gtts import gTTSError
from playsound import playsound
try:
    inp = input("Enter the content : ")
    path = input("Enter Path and file name : ")
    tts = gTTS(inp)
    tts.save(path)
    print("File created successfully.")
    # playsound(inp)
except Exception as e:
    a = e
    print("Getting error while executing.")