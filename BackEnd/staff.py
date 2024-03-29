from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.playersDB
staff = db.staffCollection

#Create Dataset for the staff used for authentication later

staff_list = [
          { 
            "name" : "Martin O'Neill",
            "username" : "moneill",  
            "password" : b"m_oneill",
            "role" : "Manager",
            "email" : "moneill@IFAemail.com",
            "admin" : False
          },
          { 
            "name" : "Jimmy Nicholl",
            "username" : "jnicholl",  
            "password" : b"j_nicholl",
            "role" : "Assistant Manager",
            "email" : "jnicholl@IFAemail.com",
            "admin" : False
          },
          { 
            "name" : "Aaron Hughes",
            "username" : "ahughes",  
            "password" : b"a_hughes",
            "role" : "Senior Coach",
            "email" : "ahughes@IFAemail.com",
            "admin" : False
          },        
          { 
            "name" : "Diarmuld O'Carroll",
            "username" : "docarroll",  
            "password" : b"d_ocarroll",
            "role" : "Senior Coach",
            "email" : "docarroll@IFAemail.com",
            "admin" : True
          },
          { 
            "name" : "David White",
            "username" : "dwhite",  
            "password" : b"d_white",
            "role" : "Team Doctor",
            "email" : "dwhite@IFAemail.com",
            "admin" : False
          }
       ]

#Encrpyt hash password
for new_staff_user in staff_list:
      new_staff_user["password"] = bcrypt.hashpw(new_staff_user["password"], bcrypt.gensalt())
      staff.insert_one(new_staff_user)