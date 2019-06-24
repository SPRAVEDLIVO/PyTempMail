import postshiftapi
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry('1075x665')
root.title('PyTemp')
keyList = []
mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
def createmail():
    api = postshiftapi.Api()
    MailData = api.CreateNew()
    print(MailData)
    mail = MailData.get('email')
    key = MailData.get('key')
    root.title('PyTemp - '+mail)
    keyList.append(key)
    del api, MailData, key, mail
def delmail():
    api = postshiftapi.Api()
    api.DeleteMail(keyList[-1])
    root.title('PyTemp')
    del keyList[-1], api
def GetAlive():
    api = postshiftapi.Api()
    tm = api.GetLiveTime(keyList[-1]).get('livetime')
    root.title('PyTemp')
    messagebox.showinfo('Info', 'Will be alived'+tm.decode('utf-8'))
    del api
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Создать", command = createmail)
filemenu.add_command(label="Удалить", command = delmail)
filemenu.add_command(label="Время", command = GetAlive)
mainmenu.add_cascade(label="Почта", menu=filemenu)

root.mainloop()