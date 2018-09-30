from tkinter import *
from PyDictionary import PyDictionary
dictionary=PyDictionary()



x = []
y = []
root = Tk()
word = root.clipboard_get()#"aggregation"
data = dictionary.meaning(word)#{'parakeet': ['fly', 'bird']}
for key in data.keys():
    x.append(key)
    y.append(data[key])

clip_text = root.clipboard_get()
Label(root, text = word , font=("Helvetica", 30)).grid(row=0,ipadx = 10,ipady = 10)
Label(root, text = x ,font=("Helvetica", 25)).grid(row=1,ipadx = 10,ipady = 50)
#Label(root, text = clip_text ,font=("Helvetica", 25) ).grid(row=2,ipadx = 10,ipady = 50)


#ourMessage ='This is our Message'
messageVar = Message(root, text = y,font=("Helvetica", 25)).grid(row=3,ipadx = 10,ipady = 50)
#messageVar.config(bg='lightgreen') 
#messageVar.pack( ) 
mainloop()