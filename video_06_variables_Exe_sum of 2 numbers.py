#string variable
#type: str
#i.e: "Hello", "7,5"

#int variable
#type: int
#i.e: 7, -4, 0, 9875

#float variable
#type: float
#i.e: 7.0, -4.5, 0.5, 9.875

#bool variable
#type bool
#i.e: False, True


#Exercise 1 - Read 2 numbers and sum them

number1 = int(input ("Number 1:"))
number2 = int(input ("Number 2:"))
#if we don't insert the "int" before the input, it will be read as string
total = number1+number2
print ("The sum of the numbers {} and {} is {}.".format(number1, number2, total))
       

#Exercise 2 - To know the type/class of the data

number1 = int(input ("Number 1:"))
print (type(number1))
