import firebase_admin
from firebase_admin import credentials, db
cred=credentials.Certificate("C:/Users/Lenovo/OneDrive/Desktop/Python Basis/newpython-27ed2-firebase-adminsdk-fbsvc-eb058be97e.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app (cred,{"databaseURL":"https://newpython-27ed2-default-rtdb.firebaseio.com/"})


a=int(input("enter first number"))
op=input("enter oprator")
b=int(input("enter second number"))
d=0

if op=="+":
   d=d=print("your addition is",a+b)

elif op=="-":
   d=print("your substraction is",a-b)

elif op=="*":
   d=print("your multiplication is",a*b)

elif op=="/":
   #print("division is",a/b)

   if(b==0):
      d=print("do not divisible by zero")
   else:
      d=print(a/b) 

else:
   d=print("invalid number")



ref=db.reference('calculator_app')
ref.push({"your calculations is ":d,})

print("data sent successfully...!")