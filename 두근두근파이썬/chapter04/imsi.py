# import datetime

# x = datetime.datetime(2022,9,1)
# y = datetime.datetime.now()

# d = y-x
# print("만난 일: "+str(x))
# print("현재: "+str(y))
# print("만난지",d.days,"되었습니다")

from gtts import gTTS
import os

text = "안녕하세요 반갑습니다 저는 누구입니다"

tts = gTTS(text=text,lang='ko')
tts.save("ttt.mp3")
os.system("ttt.mp3")
