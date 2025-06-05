email = input("Enter your email id:")
password = input("Enter your password:")
correct_email ="anjalisharivas@gmail.com"
correct_password = "anjvas2510"
if email == correct_email:
    if password == correct_password:
        print("Login Successful")
    else:
        print("incorrect password")
else:
       print("incorrect email")