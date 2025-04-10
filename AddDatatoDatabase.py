import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountkey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://face-attendance-af128-default-rtdb.firebaseio.com/"})

ref = db.reference('students')

data = {
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2024,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-04-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-04-11 00:54:34"
        },
    "356894":
        {
            "name": "Aditya gupta",
            "major": "Physics",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "H",
            "year": 2,
            "last_attendance_time": "2024-04-11 00:54:34" 
        } 
           
}

for key, value in data.items():
    ref.child(key).set(value)