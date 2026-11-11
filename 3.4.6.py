hat_list = [1, 2 , 3, 4, 5] # this is an existing list of numbers hidden in the hat.
#step 1: write a line of code that promts the user
#to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter a number:"))
#step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
#step 3 : write a line of code that prints the lengeth of the existing list.
print(len(hat_list))
print (hat_list)
