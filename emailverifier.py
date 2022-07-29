# email validation program using regex module - Mann Patel

import re

email_condition = "^[a-z]+ [\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input(" Enter your Email : ")

if re.search(email_condition , user_email) :
    print("Email entered is correct.!!")
    print("Thank You..!!")
else :
    print("Incorrect Email is entered.!!")
    print("Thank You..!!")
