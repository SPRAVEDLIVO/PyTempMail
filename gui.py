import postshiftapi
import tkinter as tk
from tkinter import messagebox, simpledialog
root = tk.Tk()
root.geometry('1075x665')
root.title('PyTemp')
keyList = []
mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
def createmail():
    name = simpledialog.askstring('Input', 'Give a name')
    api = postshiftapi.Api()
    MailData = api.CreateNew(name)
    print(MailData)
    mail = MailData.get('email')
    key = MailData.get('key')
    root.title('PyTemp - '+mail)
    keyList.append(key)
    setMessages()
def setMessages():
    api = postshiftapi.Api()
    messages = api.GetList(keyList[-1])
    print(messages)
    for message in messages:
        subject = message.get('subject')
        fromuser = message.get('from')
        mID = message.get('id')
        tk.Button(text = subject+'\nFrom:'+fromuser, command = lambda: print(mID), width=5,height=5).place(x=100, y=mID*20)
def delmail():
    api = postshiftapi.Api()
    api.DeleteMail(keyList[-1])
    root.title('PyTemp')
    del keyList[-1], api
def GetAlive():
    api = postshiftapi.Api()
    tm = api.GetLiveTime(keyList[-1]).get('livetime')
    messagebox.showinfo('Info', 'Will be alived '+str(tm))
def UpdateLiveTime():
    api = postshiftapi.Api()
    api.UpdateLiveTime(keyList[-1])
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Создать", command = createmail)
filemenu.add_command(label="Удалить", command = delmail)
filemenu.add_command(label="Время", command = GetAlive)
filemenu.add_command(label="Обновить", command = UpdateLiveTime)
filemenu.add_command(label="Обновить письма", command = setMessages)
mainmenu.add_cascade(label="Почта", menu=filemenu)

root.mainloop()