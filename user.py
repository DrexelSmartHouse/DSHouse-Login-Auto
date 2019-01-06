class User:
    def __init__(self, fName, lName, ID, cardId, signedIn):
        self.first = fName
        self.last = lName
        self.id = ID #Drexel ID
        self.cardId = cardId #RFID number associated with Drexel ID Card
        self.isSignedIn = signedIn
        self.email = ID.lower() + '@drexel.edu'
