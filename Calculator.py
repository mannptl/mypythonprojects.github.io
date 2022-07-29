first = input ( "Enter First number :")
operator = input ( "Enter operator (+,-,*,/) : " )
second = input ( "Enter Second number :")

first = int(first)
second = int(second)


if operator == "+" :
    print (" Addition of Given Number is : " + str(first + second))

elif operator == "*" :
    print ( " Multiplication of Given Number is : " + str(first * second))

elif operator == "/" :
    print ( " Division of Given Number is : " + str(first / second))

elif operator == "-" :
    print ( " Subtraction of Given Number is : " + str(first - second))

elif operator == "%" :
    print ( " Modulus of Given Number is : " + str(first % second))

else :
    print ( " Enter Valid Operator. ")