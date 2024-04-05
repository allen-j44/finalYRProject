from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.ProjectDB
staff = db.staffCollection

#Create Dataset for the staff used for authentication later

staff_list = [
    {
        "name": "William Sproule",
        "username": "wsproule",
        "password": b"w_sproule",
        "role": "STF",
        "email": "w.sprouleGreenwell@gmail.com",
        "admin": False
    },
    {
        "name": "Steven Irvine",
        "username": "sirvine",
        "password": b"s_irvine",
        "role": "STF",
        "email": "s.irvineGreenwell@gmail.com",
        "admin": False
    },
    {
        "name": "David Milligan",
        "username": "dmilligan",
        "password": b"d_milligan",
        "role": "STF",
        "email": "d.milliganGreenwell@gmail.com",
        "admin": False
    },
    {
        "name": "Matthew Patton",
        "username": "mpatton",
        "password": b"m_patton",
        "role": "STF",
        "email": "m.pattonGreenwell@gmail.com",
        "admin": False
    }
]


#Encrpyt hash password
for new_staff_user in staff_list:
      new_staff_user["password"] = bcrypt.hashpw(new_staff_user["password"], bcrypt.gensalt())
      staff.insert_one(new_staff_user)