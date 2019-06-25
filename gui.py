import postshiftapi, threading, time
import tkinter as tk
from tkinter import messagebox, simpledialog
root = tk.Tk()
root.geometry('1075x665')
root.title('PyTemp')
keyList = []
y=0
scrolls = []
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
	messagebox.showinfo('Mail', 'Mail: '+mail+'\nKey: '+key+'\nLiveTime: '+str(GetAlive('system')))
	global th 
	th = threading.Thread(target=refreshList, args=())
	th.start()
def setMessages():
	global y
	api = postshiftapi.Api()
	if api.CheckInbox(keyList[-1]) == True:
		messages = api.GetList(keyList[-1])
		for message in messages:
			subject = message.get('subject')
			fromuser = message.get('from')
			mID = message.get('id')
			tk.Button(text = 'Subject: '+subject+'\nFrom:'+fromuser, command =lambda e=mID:displayMessage(e), width=40,height=2).place(x=0, y=y*40)
			y+=1
		y=0
def scrolls_clear():
	for scroll in scrolls:
		scroll.pack_forget()
def displayMessage(mID):
	scrolls_clear()
	api = postshiftapi.Api()
	message = api.GetText(keyList[-1], mID).get('message')
	text = tk.Text(width=60,height=20)
	text.place(x=500,y=20)
	scroll = tk.Scrollbar(command=text.yview)
	scroll.pack(side=tk.RIGHT, fill=tk.Y)
	scrolls.append(scroll)
	text.config(yscrollcommand=scroll.set)
	text.insert(1.0,message)
def delmail():
	api = postshiftapi.Api()
	api.DeleteMail(keyList[-1])
	root.title('PyTemp')
	global th
	try:
		th._stop()
	except: pass
	del keyList[-1], api
def GetAlive(mode):
	if mode == 'system':
		api = postshiftapi.Api()
		tm = api.GetLiveTime(keyList[-1]).get('livetime')
		return tm
	if mode == 'display':
		api = postshiftapi.Api()
		tm = api.GetLiveTime(keyList[-1]).get('livetime')
		messagebox.showinfo('Info',str(tm))
def UpdateLiveTime():
	api = postshiftapi.Api()
	api.UpdateLiveTime(keyList[-1])
def enter_key():
	key = simpledialog.askstring('Input', 'Enter your key')
	keyList.append(key)
	setMessages()
def refreshList():
	tm = time.time()
	while time.time() - tm < 10:
		pass
	else: 
		if postshiftapi.Api.CheckInbox(0, keyList[-1]) is True:
			setMessages()
		else:
			refreshList()
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Создать", command = createmail)
filemenu.add_command(label="Удалить", command = delmail)
filemenu.add_command(label="Время", command = lambda: GetAlive('display'))
filemenu.add_command(label="Обновить время", command = UpdateLiveTime)
filemenu.add_command(label="Обновить письма", command = setMessages)
filemenu.add_command(label="Вставить ключ", command = enter_key)
mainmenu.add_cascade(label="Почта", menu=filemenu)
root.mainloop()