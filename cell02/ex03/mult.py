#!/urs/bin/pyhton3
print ("Enter the first number: ")
num1 = int(input())
print ("Enter the second number: ")
num2 = int(input())
product = num1 * num2
print (num1,"x",num2,"=", product)
if product >0:
    print ("The result is positive.")
if product <0:
    print ("The result is negative.")
if product == 0:
    print ("The product is both positive and negative.")