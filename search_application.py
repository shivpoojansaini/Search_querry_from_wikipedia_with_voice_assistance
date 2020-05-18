#import necessary library of python
from tkinter import *
from threading import *
from tkinter.font import Font
import  wikipedia
import speech_recognition as sr
########################## Background functions ########################
#fuction for voice search
def mic():
    #speech_Recognition instant
    r1 = sr.Recognizer()
    r2 = sr.Recognizer()

    with sr.Microphone() as source:
        #clear answer box and print message
        answer.delete(1.0,END)
        answer.insert(INSERT,"speak now....")
        # Taking input from microphone
        audio = r1.listen(source)
        answer.delete(1.0, END)
        answer.insert(INSERT, "Searching....")
        # converting voice into text
        voice_text = r2.recognize_google(audio)
        #searching querry from wikipedia
        try:
            answer.delete(1.0, END)
            answer_value = wikipedia.summary(voice_text)
            answer.insert(INSERT, answer_value)
        #Message if does't get any any answer from wikipedia
        except:
            answer.insert(INSERT, "we doest find anything on wikipedia")

#On click of voice assistant logo
def voice_to_text(event =" "):
    #create thred for mic function
    t2 = Thread(target=mic)
    t2.start()

#On click or press of enter button
def get_me(event =" "):
    enty_value = enty_query.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(enty_value)
        answer.insert(INSERT, answer_value)

    except:
        answer.insert(INSERT, "we doest find anything on wikipedia")

########################## Root window code ##################################

#create window
root = Tk()
root.geometry("350x500+200+100")
#create top frame in root
top_frame = Frame(root)
#entry box on window
enty_query = Entry(top_frame,font = 'verdana ',width = 12,bd =3)
enty_query.grid(row = 0,column = 0)
#voice assistance logo
photo = PhotoImage(file = r"D:/tkinter_python/mic.png")
mic_button = Button(top_frame,image = photo,command =voice_to_text).grid(row = 0,column = 5)
#search button
button = Button(top_frame,text= "search",command = get_me).grid(row = 1,column = 0)
#binding 'enter' key with search button
root.bind('<Return>',get_me)
#create bottom frame
top_frame.pack(side = TOP)
bottom_frame = Frame(root)
#scrollbar
scroll =Scrollbar(bottom_frame)
scroll.pack(side = RIGHT,fill =Y)
#result  text area
answer = Text(bottom_frame,width = 100,height = 30,font = 'verdana ', yscrollcommand = scroll.set,wrap = WORD,background = "gray")
scroll.config(command = answer.yview)
answer.pack()
bottom_frame.pack(side = BOTTOM)
#root in mainloop
root.mainloop()