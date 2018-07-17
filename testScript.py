#!usr/bin/env python

from tkinter import *
from firebase import firebase
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from sendEmail import *

def cardRead():
	global cardN
	global rootA
	
	rootA = Tk()
	rootA.configure(background='#24336C')
	rootA.title('Scan Card')	

	instruction = Label(rootA, text='Please Scan Your Card\n', font=("Futura", 20), fg="white", bg="#24336C")
	instruction.grid(row=0, columnspan=2)

	cardL = Label(rootA, text='Card ID:', font=("Futura", 16), fg="white", bg="#24336C")
	cardL.grid(row=1, column=0, sticky=W)
	
	sL = Label(rootA, text='S', font=("Futura", 16), fg="#24336C", bg="#24336C") 
	sL.grid(row=3, column=0, sticky=W)
	
	cardN = Entry(rootA, show="*", font=("Futura", 16), width=25)
	cardN.grid(row=2, column=0, sticky=E)
	
	cardN.focus_set()
	rootA.focus_force()
	
	enterButton = Button(rootA, text='ENTER', command=checkExistence, font=("Futura", 12), fg="#24336C", bg="white")
	enterButton.grid(row=4, columnspan=2, sticky=S)
	enterButton.bind("<FocusIn>", checkExistence)

	rootA.eval('tk::PlaceWindow %s center' % rootA.winfo_pathname(rootA.winfo_id()))
	rootA.mainloop()

def checkExistence(event=""):
	if(cardN.get() != ""):
		c = cardN.get()
		rootA.destroy()
		result = firebase.get('/USERS/'+c+'/', None)
		if(result != None):
			writeToLog(result['FIRST'], result['LAST'], result['ID'])
		else:
			enterInfo(c)
	else:
		aL = Label(rootA, text='Fill in all fields!', font=("Futura", 16), fg="white", bg="#24336C") 
		aL.grid(row=3, columnspan=2)

def enterInfo(c):
	global firstN
	global lastN
	global idN
	global rootB
	global cardID
	
	cardID = c
	rootB = Tk()
	rootB.configure(background='#24336C')
	rootB.title('Enter Info')
	
	instruction = Label(rootB, text='Hello New User! Please Enter The\nFollowing Info:\n', font=("Futura", 20), fg="white", bg="#24336C")
	instruction.grid(row=0, columnspan=2)

	firstL = Label(rootB, text='Full First Name:', font=("Futura", 16), fg="white", bg="#24336C")
	lastL = Label(rootB, text='Full Last Name:', font=("Futura", 16), fg="white", bg="#24336C")
	idL = Label(rootB, text='Drexel ID (ABC123):', font=("Futura", 16), fg="white", bg="#24336C") 
	firstL.grid(row=1, column=0, sticky=W)
	lastL.grid(row=3, column=0, sticky=W)
	idL.grid(row=5, column=0, sticky=W)
	
	sL = Label(rootB, text='S', font=("Futura", 16), fg="#24336C", bg="#24336C") 
	sL.grid(row=7, column=0, sticky=W)
	
	firstN = Entry(rootB, font=("Futura", 16), width=25)
	lastN = Entry(rootB, font=("Futura", 16), width=25)
	idN = Entry(rootB, font=("Futura", 16), width=25)
	firstN.grid(row=2, column=0, sticky=E)
	lastN.grid(row=4, column=0, sticky=E)
	idN.grid(row=6, column=0, sticky=E)
	
	firstN.focus_set()
	rootB.focus_force()
	
	enterButton = Button(rootB, text='ENTER', command=checkField, font=("Futura", 12), fg="#24336C", bg="white")
	enterButton.grid(row=8, columnspan=2)
	
	firstN.bind("<Return>", checkField)
	lastN.bind("<Return>", checkField)
	idN.bind("<Return>", checkField)
	enterButton.bind("<Return>", checkField)
	
	rootB.eval('tk::PlaceWindow %s center' % rootB.winfo_pathname(rootB.winfo_id()))
	rootB.mainloop()

def checkField(event=""):
	if(re.search('[a-zA-Z]', firstN.get()) and re.search('[a-zA-Z]', lastN.get()) and re.search('[a-zA-Z]', idN.get()) and len(idN.get()) <=10):
		holdValues = [firstN.get(), lastN.get(), idN.get()]
		rootB.destroy()
		writeToBase(holdValues[0].capitalize(), holdValues[1].capitalize(), holdValues[2].upper(), cardID)
	else:
		aL = Label(rootB, text='Fill in all fields and use Drexel id!', font=("Futura", 16), fg="white", bg="#24336C") 
		aL.grid(row=7, columnspan=2)

def writeToBase(first, last, id, card):
	result = firebase.put('/USERS/', cardID, {'FIRST' : first, 'LAST' : last, 'ID' : id})
	sendEmail(id, detailsArray[0], detailsArray[1])
	writeToLog(first, last, id)
	
def writeToLog(first, last, id):
	authorize()
	now = datetime.datetime.now()
	
	lastEntry = worksheet.findall(id)
	if(lastEntry == []):
		worksheet.append_row([first, last, id, now.strftime("%m-%d-%Y %H:%M:%S")])
		alertUser(first)
	else:
		checkSign = worksheet.acell('E' + str(lastEntry[len(lastEntry)-1].row)).value
		if(checkSign == ""):
			lastDate = datetime.datetime.strptime(worksheet.acell('D' + str(lastEntry[len(lastEntry)-1].row)).value, "%m-%d-%Y %H:%M:%S")
			timeSpent = now - lastDate
			worksheet.update_acell('E' + str(lastEntry[len(lastEntry)-1].row), now.strftime("%m-%d-%Y %H:%M:%S"))
			worksheet.update_acell('F' + str(lastEntry[len(lastEntry)-1].row), timeSpent)
			alertUser(first, timeSpent)
		else:
			worksheet.append_row([first, last, id, now.strftime("%m-%d-%Y %H:%M:%S")])
			alertUser(first)
	
def alertUser(first, t=""):
	global rootC
	
	rootC = Tk()
	rootC.configure(background='#24336C')
	rootC.title('Card Read Successful')
	rootC.focus_force()
	
	if(t == ""):
		typeL = Label(rootC, text=('\n   Welcome ' + first + ',   \n   You Have Signed In   \n'), font=("Futura", 16), fg="white", bg="#24336C") 
		typeL.grid(row=1, column=0)
	else:
		typeL = Label(rootC, text=('\n   Farewell ' + first + ',   \n   You Have Signed Out   \n\n   Total Time: ' + str(t) + '   \n'), font=("Futura", 16), fg="white", bg="#24336C") 
		typeL.grid(row=1, column=0)
	
	rootC.after(3000, clearScreen)
	rootC.eval('tk::PlaceWindow %s center' % rootC.winfo_pathname(rootC.winfo_id()))
	rootC.mainloop()

def clearScreen():
	rootC.destroy()
	cardRead()

def authorize():
	global worksheet
	gc = gspread.authorize(credentials)
	sheet = gc.open_by_url(detailsArray[3])
	worksheet = sheet.get_worksheet(0)
	
if __name__ == "__main__":
	detailsArray = []
	filepath = 'scriptDetails.txt'  
	with open(filepath) as fp:  
		line = fp.readline()
		while line:
			detailsArray.append(line.strip())
			line = fp.readline()
	
	firebase = firebase.FirebaseApplication(detailsArray[2], None)
	credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', ['https://spreadsheets.google.com/feeds'])
	
	cardRead()