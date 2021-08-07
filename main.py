# To learn more about 3x+1 problem visit https://en.wikipedia.org/wiki/Collatz_conjecture

input_number = int(input("Enter a number: "))


while (input_number != 1):
  if (input_number % 2 == 0):
    print (input_number)
    input_number = input_number / 2
    print (" is even number, so dividing by 2 --> "+ str(input_number))

   
    
    # (input_number)
  else:
    print (input_number)
    input_number = 3*(input_number) + 1
    print (" is odd number, so doing 3x+1 --> "+ str(input_number))

  #input("press any key continue...!")


if (input_number == 1):
  print ("Reached home !!!")
