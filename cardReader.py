import asyncio
import datetime
from tkinter import *
from PIL import ImageTk, Image

import gspread
import pyrebase
from mailchimp3 import MailChimp
from oauth2client.service_account import ServiceAccountCredentials
from pygame import mixer
import user

cardN = None
scanScreen = Tk()
userList = None
usersSignedIn = []
text = StringVar()
logoPath = "pictures/bannerLogo.png"

WIDTH = scanScreen.winfo_screenwidth()
HEIGHT = scanScreen.winfo_screenheight()


def init():
    global scanScreen
    global cardN
    global usersSignedIn
    global userList
    global frame3

    scanScreen.geometry('%dx%d' % (WIDTH, HEIGHT))
    scanScreen.configure(background='#24336C')
    scanScreen.title('Drexel Smart House Card Scanner')

    photoFrame = Frame(scanScreen, bg="#24336C")
    photoFrame.pack(side=TOP)

    img = Image.open(logoPath)
    [imageWidth, imageHeight] = img.size
    # Compute resize ratio for max size with half height of the screen and full width
    n = min(WIDTH/imageWidth, HEIGHT/2/imageHeight)
    img = img.resize(
        (int(imageWidth * n), int(imageHeight * n)), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    Label(photoFrame, image=photo, bg="#24336C").pack(fill=X)

    frame1 = Frame(scanScreen, relief=RAISED, borderwidth=5, bg="#24336C")
    frame1.pack(fill=Y, side=LEFT, padx=50, expand=1)

    Label(frame1, text='Please Scan Your Card\n',
          font=("Futura", 20), fg="white", bg="#24336C").pack()

    Label(frame1, text='Card ID:', font=(
        "Futura", 16), fg="white", bg="#24336C").pack()

    cardN = Entry(frame1, show="*", font=("Futura", 16), width=25)
    cardN.pack()

    enterButton = Button(frame1, text='ENTER', command=checkExistence, font=(
        "Futura", 12), fg="#24336C", bg="white")
    enterButton.pack(pady=20)
    enterButton.bind("<FocusIn>", checkExistence)

    frame2 = Frame(scanScreen, relief=RAISED, borderwidth=5, bg="#24336C")
    frame2.pack(fill=Y, side=RIGHT, padx=50, expand=1)

    Label(frame2, text='Users Signed In\n', font=("Futura", 20),
          fg="white", bg="#24336C").pack()

    scrollbar = Scrollbar(frame2)
    scrollbar.pack(side=RIGHT, fill=Y)
    userList = Listbox(frame2, font=("Futura", 16),
          fg="black", selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
    userList.pack()
    scrollbar.config(command=userList.yview)

    signOutButton = Button(frame2, text='Sign Out', command=signOut, font=(
        "Futura", 12), fg="#24336C", bg="white")
    signOutButton.pack(pady=20)

    frame3 = Frame(scanScreen, bg="#24336C")
    frame3.pack(fill=Y, padx=50, expand=1)

    text.set('')
    Label(frame3, textvariable=text, font=(
        "Futura", 16), fg="white", bg="#24336C").pack()


    cardN.focus_set()
    scanScreen.focus_force()

    scanScreen.mainloop()


def signOut():
    global userList

    signOutIndex = userList.curselection()

    for index in signOutIndex:
        userList.delete(index)
        writeToLog(usersSignedIn[index])
    

def checkExistence(event=""):
    if(cardN.get() != ""):
        c = cardN.get()
        cardN.delete(0, 'end')
        result = db.child('USERS').child(c).get().val()
        if(result != None):
            writeToLog(user.User(result['FIRST'],
                                 result['LAST'], result['ID'], c, True))
        else:
            enterInfo(c)


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

    instruction = Label(rootB, text='Hello New User! Please Enter The\nFollowing Info:\n', font=(
        "Futura", 20), fg="white", bg="#24336C")
    instruction.grid(row=0, columnspan=2)

    firstL = Label(rootB, text='Full First Name:', font=(
        "Futura", 16), fg="white", bg="#24336C")
    lastL = Label(rootB, text='Full Last Name:', font=(
        "Futura", 16), fg="white", bg="#24336C")
    idL = Label(rootB, text='Drexel ID (ABC123):', font=(
        "Futura", 16), fg="white", bg="#24336C")
    firstL.grid(row=1, column=0, sticky=W)
    lastL.grid(row=3, column=0, sticky=W)
    idL.grid(row=5, column=0, sticky=W)

    sL = Label(rootB, text='S', font=("Futura", 16),
               fg="#24336C", bg="#24336C")
    sL.grid(row=7, column=0, sticky=W)

    firstN = Entry(rootB, font=("Futura", 16), width=25)
    lastN = Entry(rootB, font=("Futura", 16), width=25)
    idN = Entry(rootB, font=("Futura", 16), width=25)
    firstN.grid(row=2, column=0, sticky=E)
    lastN.grid(row=4, column=0, sticky=E)
    idN.grid(row=6, column=0, sticky=E)

    firstN.focus_set()
    rootB.focus_force()

    enterButton = Button(rootB, text='ENTER', command=checkField, font=(
        "Futura", 12), fg="#24336C", bg="white")
    enterButton.grid(row=8, columnspan=2)

    firstN.bind("<Return>", checkField)
    lastN.bind("<Return>", checkField)
    idN.bind("<Return>", checkField)
    enterButton.bind("<Return>", checkField)

    rootB.eval('tk::PlaceWindow %s center' %
               rootB.winfo_pathname(rootB.winfo_id()))

    mixer.music.load('sounds/welcome.mp3')
    mixer.music.play()

    rootB.mainloop()


def checkField(event=""):
    if(re.search('[a-zA-Z]', firstN.get()) and re.search('[a-zA-Z]', lastN.get()) and re.search('[a-zA-Z]', idN.get()) and len(idN.get()) <= 10):
        holdValues = [firstN.get(), lastN.get(), idN.get()]
        rootB.destroy()
        writeToBase(user.User(holdValues[0].capitalize(
        ), holdValues[1].capitalize(), holdValues[2].upper(), cardID, True))
    else:
        aL = Label(rootB, text='Fill in all fields and use Drexel id!',
                   font=("Futura", 16), fg="white", bg="#24336C")
        aL.grid(row=7, columnspan=2)
        mixer.music.load('sounds/error.mp3')
        mixer.music.play()


def writeToBase(newUser):
    db.child("USERS").child(newUser.cardId).set(
        {'FIRST': newUser.first, 'LAST': newUser.last, 'ID': newUser.id})
    subscribeToList(newUser, detailsArray[5], detailsArray[6])
    writeToLog(newUser)


def writeToLog(newUser):
    global usersSignedIn

    scanScreen.focus_set() #Removes focus from the text box temporarily
    authorize()
    now = datetime.datetime.now()
    lastEntry = worksheet.findall(newUser.id)

    if(lastEntry == []):
        worksheet.append_row(
            [newUser.first, newUser.last, newUser.id, now.strftime("%m-%d-%Y %H:%M:%S")])
        usersSignedIn.append(newUser)
        userList.insert(END, newUser.first + ' ' + newUser.last)

        alertUser(newUser.first)
    else:
        checkSign = worksheet.acell(
            'E' + str(lastEntry[len(lastEntry)-1].row)).value
        if(checkSign == ""):
            lastDate = datetime.datetime.strptime(worksheet.acell(
                'D' + str(lastEntry[len(lastEntry)-1].row)).value, "%m-%d-%Y %H:%M:%S")
            timeSpent = now - lastDate
            worksheet.update_acell(
                'E' + str(lastEntry[len(lastEntry)-1].row), now.strftime("%m-%d-%Y %H:%M:%S"))
            worksheet.update_acell(
                'F' + str(lastEntry[len(lastEntry)-1].row), str(timeSpent))
            for cur in usersSignedIn:
                if cur.id == newUser.id:
                    usersSignedIn.remove(cur)
                    try:
                        delIndex = userList.get(0,END).index(cur.first + ' ' + cur.last)
                        userList.delete(delIndex)
                    except ValueError:
                        print('Item can not be found in the list!')
                    break
            alertUser(newUser.first, timeSpent)
        else:
            worksheet.append_row(
                [newUser.first, newUser.last, newUser.id, now.strftime("%m-%d-%Y %H:%M:%S")])
            usersSignedIn.append(newUser)
            userList.insert(END, newUser.first + ' ' + newUser.last)
            alertUser(newUser.first)


def alertUser(first, t=""):
    global cardN
    if(t == ""):
        text.set('\n   Welcome ' + first + ',   \n   You Have Signed In   \n')
        mixer.music.load('sounds/hello.mp3')

    else:
        text.set('\n   Farewell ' + first +
                 ',   \n   You Have Signed Out   \n\n   Total Time: ' + str(t) + '   \n')
        mixer.music.load('sounds/goodbye.mp3')
    scanScreen.after(2000, text.set, '')
    scanScreen.after(2000, cardN.focus_set)

    mixer.music.play()


def authorize():
    global worksheet
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(detailsArray[3])
    worksheet = sheet.get_worksheet(0)


def subscribeToList(newUser, listId, key):
    client = MailChimp(mc_api=key, mc_user='DSH_CARD_READER')
    client.lists.members.create(listId, {
        'email_address': newUser.email,
        'status': 'subscribed',
        'merge_fields': {
            'FNAME': newUser.first,
            'LNAME': newUser.last,
        },
    })


if __name__ == "__main__":
    detailsArray = []
    filepath = 'scriptDetails.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            detailsArray.append(line.strip())
            line = fp.readline()

    config = {
        "apiKey": detailsArray[4],
        "authDomain": "projectId.firebaseapp.com",
        "databaseURL": detailsArray[2],
        "storageBucket": "projectId.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', ['https://spreadsheets.google.com/feeds'])
    mixer.init()
    init()
