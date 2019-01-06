# Drexel Smart House Sign-In Automation System

DSH sign in system using Drexel ID cards. Included automatic addition to emailing list for new, unrecognized members.

## Contents
- [Features](#features)
- [Quick start](#quickstart)
  - [Requirements](#requirements)
  - [Hardware setup](#hardwaresetup)
  - [Software setup](#softwaresetup)
- [Releases](#releases)
- [Future Features](#future)
- [Contributors](#contributors)

## Features <a name="features"></a>
 - Fast RFID-Based DSHouse sign-in using Drexel ID cards
 - User management with Firebase
 - New member email automation with Mailchimp
 - Sound effects

## Quick start <a name="quickstart"></a>

### Requirements <a name="requirements"></a>
- Python 3.7
- Drexel RFID Scanner
- Internet-connected computer
- Necessary credential and setup files (creds.json, scriptDetails.txt) 

### Hardware setup <a name="hardwaresetup"></a>
1. Connect the RFID Scanner to the computer via USB.
2. Wait for the main LED light to turn red.

### Software setup <a name="softwaresetup"></a>
1. Clone the git repository to your local file system
2. Place the creds.json and scriptDetails.txt into the root folder (DSHouse-Login-Auto/)
3. In the root project folder, run `python3.7 -m pip install -r requirements.txt`
4. Then run `python3.7 cardReader.py`. The program should launch.

## Releases <a name="releases"></a>
Version 1.0 - Initial Release.
Version 2.0 - Made multiple sequential sign-ins faster. Added sounds, and connection to the mailchimp API.
Version 3.0 - Updated UI. List of members currently signed in to the house. Manual house sign-out. "Signed In" list now populates initially based on the Logs.

## Future Features <a name="future"></a>
- Async/threaded tasks for faster sign-in and better user experience
- 24 Hour automatic sign out and alerting system for members who forget to sign out

## Contributors <a name="contributors"></a>
- [Joshua Cohen](https://github.com/jcohen98)
- [Kris Lopez](https://github.com/krislopez99)
