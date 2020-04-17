import datetime
import threading
import time
from tkinter import *

import gspread
from PIL import ImageTk, Image
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from mailchimp3 import MailChimp
from mailchimp3 import helpers
from oauth2client.service_account import ServiceAccountCredentials
from pygame import mixer

import user

scanScreen = Tk()
usersSignedIn = []
text = StringVar()
logoPath = "pictures/bannerLogo.png"

WIDTH = scanScreen.winfo_screenwidth()
HEIGHT = scanScreen.winfo_screenheight() - 60

DELAY = 120


def init():
    global cardN
    global userList

    # Configure main card scanner screen
    scanScreen.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, 0, 0))
    scanScreen.configure(background='#24336C')
    scanScreen.title('Drexel Smart House Card Scanner')
    scanScreen.columnconfigure(0, weight=1)
    scanScreen.rowconfigure(0, weight=1)

    photoFrame = Frame(scanScreen, bg="#24336C")
    photoFrame.pack(side=TOP, pady=20)

    img = Image.open(logoPath)
    [imageWidth, imageHeight] = img.size
    # Compute resize ratio for max size with half height of the screen and full width
    n = min(WIDTH / imageWidth, HEIGHT / 2.3 / imageHeight)
    img = img.resize(
        (int(imageWidth * n), int(imageHeight * n)), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    Label(photoFrame, image=photo, bg="#24336C").pack(fill=X)

    frame1 = Frame(scanScreen, relief=RAISED, borderwidth=5, bg="#24336C")
    frame1.pack(fill=Y, side=LEFT, padx=50, expand=1, pady=20)

    Label(frame1, text='Please Scan Your Card\n',
          font=("Futura", 20), fg="white", bg="#24336C") \
        .pack()

    Label(frame1, text='Card ID:', font=(
        "Futura", 16), fg="white", bg="#24336C") \
        .pack()

    # Picks up RFID card number from scanned card
    cardN = Entry(frame1, show="*", font=("Futura", 16), width=25)
    cardN.pack()

    enterButton = Button(frame1, text='ENTER', command=checkExistence, font=(
        "Futura", 12), fg="#24336C", bg="white")
    enterButton.pack(pady=20)
    enterButton.bind("<FocusIn>", checkExistence)

    frame2 = Frame(scanScreen, relief=RAISED, borderwidth=5, bg="#24336C")
    frame2.pack(fill=Y, side=RIGHT, padx=50, expand=1, pady=20)

    Label(frame2, text='Users Signed In\n', font=("Futura", 20), fg="white", bg="#24336C") \
        .pack()

    scrollbar = Scrollbar(frame2)
    scrollbar.pack(side=RIGHT, fill=Y)
    userList = Listbox(frame2, font=("Futura", 16), fg="black", selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
    userList.pack()
    scrollbar.config(command=userList.yview)

    signOutButton = Button(frame2, text='Sign Out', command=signOutButtonAction, font=(
        "Futura", 12), fg="#24336C", bg="white")
    signOutButton.pack(pady=20)

    frame3 = Frame(scanScreen, bg="#24336C")
    frame3.pack(fill=Y, padx=50, expand=1)

    text.set('')
    Label(frame3, textvariable=text, font=("Futura", 16), fg="white", bg="#24336C") \
        .pack()

    cardN.focus_set()
    scanScreen.focus_force()

    pullSignedInUsersFromLog()
    scanScreen.mainloop()


def signOutButtonAction():
    signOutIndex = list(userList.curselection())
    signOutIndex.reverse()
    for index in signOutIndex:
        writeToLog(usersSignedIn[index])
        usersSignedIn.remove(usersSignedIn[index])
        userList.delete(index)


def checkExistence(event=""):
    if cardN.get() != "":
        c = cardN.get()
        cardN.delete(0, 'end')
        result = firebase.get('/USERS/' + c, None, params={'print': 'pretty'}, headers={'X_FANCY_HEADER': 'very fancy'})
        # If person has signed in before, write to the sign in log
        if result is not None:
            writeToLog(user.User(result['FIRST'],
                                 result['LAST'], result['ID'], c))
        else:
            enterInfo(c)


def enterInfo(c):
    global firstN
    global lastN
    global idN
    global rootB
    global cardID
    global emailOptOut

    cardID = c
    rootB = Tk()
    rootB.configure(background='#24336C')
    rootB.title('Enter Info')

    instruction = Label(rootB, text='Hello New User! Please Enter The\nFollowing Info:\n', font=(
        "Futura", 20), fg="white", bg="#24336C")
    instruction.grid(row=0, columnspan=2)

    firstL = Label(rootB, text='First Name:', font=(
        "Futura", 16), fg="white", bg="#24336C")
    lastL = Label(rootB, text='Last Name:', font=(
        "Futura", 16), fg="white", bg="#24336C")
    idL = Label(rootB, text='Drexel ID (ABC123):', font=(
        "Futura", 16), fg="white", bg="#24336C")

    firstL.grid(row=1, column=0, sticky=W)
    lastL.grid(row=3, column=0, sticky=W)
    idL.grid(row=5, column=0, sticky=W)

    sL = Label(rootB, text='S', font=("Futura", 16),
               fg="#24336C", bg="#24336C")
    sL.grid(row=8, column=0, sticky=W)

    firstN = Entry(rootB, font=("Futura", 16), width=25)
    lastN = Entry(rootB, font=("Futura", 16), width=25)
    idN = Entry(rootB, font=("Futura", 16), width=25)
    emailOptOut = IntVar()
    Checkbutton(rootB, text="Would you like to opt out of receiving important emails from Drexel Smart House?",
                variable=emailOptOut, font=("Futura", 10), selectcolor="#24336C", fg="white",
                bg="#24336C").grid(row=7, column=0)
    firstN.grid(row=2, column=0)
    lastN.grid(row=4, column=0)
    idN.grid(row=6, column=0)

    firstN.focus_set()
    rootB.focus_force()

    enterButton = Button(rootB, text='ENTER', command=checkField, font=(
        "Futura", 12), fg="#24336C", bg="white")
    enterButton.grid(row=9, columnspan=2)

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
    if (re.search('[a-zA-Z]', firstN.get()) and re.search('[a-zA-Z]', lastN.get()) and re.search(
            '([a-zA-Z]{3}[1-9]{2,3})',
            idN.get())):
        holdValues = [firstN.get(), lastN.get(), idN.get()]
        rootB.destroy()
        writeToBase(user.User(holdValues[0].capitalize(
        ), holdValues[1].capitalize(), holdValues[2].upper(), cardID, emailOptOut.get()))
    else:
        aL = Label(rootB, text='Fill in all fields and use Drexel id!',
                   font=("Futura", 16), fg="white", bg="#24336C")
        aL.grid(row=7, columnspan=2)
        mixer.music.load('sounds/error.mp3')
        mixer.music.play()


def writeToBase(newUser):
    data = {'FIRST': newUser.first, 'LAST': newUser.last, 'ID': newUser.id}
    firebase.put('/USERS', newUser.cardId, data)
    if newUser.emailOptOut == 0:
        emailSubThread = threading.Thread(target=subscribeToList, args=(newUser, detailsArray[5], detailsArray[6]))
        emailSubThread.start()
    writeToLog(newUser)


def pullSignedInUsersFromLog():
    sign_in_col_vals = worksheet.col_values(4)
    sign_out_col_vals = worksheet.col_values(5)
    # Search within the sheet to see if anyone has not properly signed out
    signedInUserIdxs = [i for i, x in enumerate(sign_out_col_vals) if x == ""]
    # Search the end of the sheet to see if anyone has not properly signed out
    signedInUserIdxs.extend(x for x in range(len(sign_out_col_vals), len(sign_in_col_vals)))
    for i in signedInUserIdxs:
        fName = worksheet.acell('A' + str(i + 1)).value
        lName = worksheet.acell('B' + str(i + 1)).value
        drexelId = worksheet.acell('C' + str(i + 1)).value
        userList.insert(END, fName + ' ' + lName)
        usersSignedIn.append(user.User(fName, lName, drexelId, None))


def signInUser(newUser):
    now = datetime.datetime.now()
    worksheet.append_row(
        [newUser.first, newUser.last, newUser.id, now.strftime("%m-%d-%Y %H:%M:%S")])
    usersSignedIn.append(newUser)
    userList.insert(END, newUser.first + ' ' + newUser.last)


def signOutUser(newUser, lastEntry):
    signType = "SIGNOUT"
    now = datetime.datetime.now()
    lastDate = datetime.datetime.strptime(worksheet.acell(
        'D' + str(lastEntry[len(lastEntry) - 1].row)).value, "%m-%d-%Y %H:%M:%S")
    timeSpent = now - lastDate
    worksheet.update_acell(
        'E' + str(lastEntry[len(lastEntry) - 1].row), now.strftime("%m-%d-%Y %H:%M:%S"))
    worksheet.update_acell(
        'F' + str(lastEntry[len(lastEntry) - 1].row), str(timeSpent))


def writeToLog(newUser):
    scanScreen.focus_set()  # Removes focus from the text box temporarily
    lastEntry = worksheet.findall(newUser.id)
    timeSpent = datetime.timedelta
    # If the user is signing in and is a new user (Did not find in the logs)
    if lastEntry == []:
        signType = "SIGNIN"
        signInThread = threading.Thread(target=signInUser, args=(newUser,))
        signInThread.start()
    # If the user has signed in before
    else:
        # Check whether they are signing in or out
        checkSign = worksheet.acell(
            'E' + str(lastEntry[len(lastEntry) - 1].row)).value
        if checkSign == "":
            signType = "SIGNOUT"
            signOutThread = threading.Thread(target=signOutUser, args=(newUser, lastEntry))
            signOutThread.start()
        else:
            signType = "SIGNIN"
            signInThread = threading.Thread(target=signInUser, args=(newUser,))
            signInThread.start()
    alertUser(newUser.first, signType)


def alertUser(first, signType):
    if signType == "SIGNIN":
        text.set('\n   Welcome ' + first + ',   \n   You Have Signed In   \n')
        mixer.music.load('sounds/hello.mp3')

    else:
        text.set('\n   Farewell ' + first + ',   \n   You Have Signed Out   \n')
        mixer.music.load('sounds/goodbye.mp3')
    scanScreen.after(1500, text.set, '')
    scanScreen.after(1500, cardN.focus_set)
    mixer.music.play()


def authorize():
    global worksheet
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(detailsArray[3])
    worksheet = sheet.get_worksheet(0)


def keepAuthorized():
    while True:
        authorize()
        time.sleep(DELAY)


def subscribeToList(newUser, listId, key):
    client = MailChimp(mc_api=key, mc_user='DSH_CARD_READER')
    client.lists.members.create_or_update(listId, helpers.get_subscriber_hash(newUser.email), {
        'email_address': newUser.email,
        'status': 'subscribed',
        'status_if_new': 'subscribed',
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

    authentication = FirebaseAuthentication(detailsArray[7], detailsArray[0], True, True)
    firebase = FirebaseApplication(detailsArray[2], authentication)

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', ['https://spreadsheets.google.com/feeds'])

    mixer.init()
    authorize()
    timerThread = threading.Thread(target=keepAuthorized)
    timerThread.daemon = True
    timerThread.start()
    init()
