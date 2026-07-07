import hashlib
import getpass

username = "admin"

password_hash = hashlib.sha256("12345".encode()).hexdigest()

user = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

entered_hash = hashlib.sha256(password.encode()).hexdigest()

if user == username and entered_hash == password_hash:
    print("Login Successful")
else:
    print("Invalid Login")