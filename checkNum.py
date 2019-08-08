import re
def checkPhoneNumber(n):
	x = re.findall("\d{3}-\d{3}-\d{4}", n)
	if(len(x) != 0):
		print("Valid")
	else:
		print("Invalid")

n = input("Enter a number (xxx-xxx-xxxx): ")
checkPhoneNumber(n)
