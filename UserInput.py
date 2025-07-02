userName = 'uttom.dev'
userPass = 409355

username = input("Enter your username: ")
password = input("Password: ")

try:
    if userName != username:
        print('Username invalid')
    elif userPass != int(password): 
        print('Wrong password')
    else:
        print('Verified successfully')
except:
    print('Something went wrong')
