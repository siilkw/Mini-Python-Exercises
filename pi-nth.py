import math

places = input("Enter a number between 1 and 10 and have the program generate pi up to that many decimal places > ")

if places < 10 and places > 0:
	print round(math.pi, places)
else:
    print "Sorry, that is not a valid number"


 
