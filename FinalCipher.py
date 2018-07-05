'''
 Author: William Saleh
 Script: Caeser Cipher
 Version: CipherTest_v2
 Date: May 26, 2018
 Last Update: May 29, 2018
'''

# print greeting
# ask for name
# ask to encrypt or decrypt
# ask user to input message
# ask for key between 1 - 26
# print result
# loop back


myName = ''
# ONLY encrypt or decrypt
decision = ['E','D'] 
# title of program
greeting = "## Caesar Cipher With Python ##" 
# key max is for the 26 letters in the alphabet
key_size = 26 
# list used to limit YES input for try again loop
yList = ['yes', 'Yes', 'YES', 'y', 'Y'] 

# function to ask user to encrypt or decrypt
def callED(): 
	while True:
		print 'Type "E" to encrypt or "D" to decrypt: '
		mode = raw_input().lower() # to make sure it is lower case alpha
		if mode in 'encrypt e decrypt d'.split():
			return mode
		else:
			print 'Enter either "encrypt" or "e" or "decrypt" or "d" '

# function for user to input their message
def callMessage(): 
	print 'Enter your message: '
	return raw_input()

# user to enter their key between 1 - 26
def callKey():
	key = 0
	while True:
		print 'Enter the key number (1 - %s)' % (key_size) 
		key = int(raw_input())
		if (key >= 1 and key <= key_size):
			return key

# function for translated message 
def callTM(mode, message, key):
	if mode[0] == 'd': #decrypt
		key = -key # minus "key" which is 26
	translated = ' '
# ensure the message in alpha is assigned a number through "key" 
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'): # if the num is more than "Z" than use a negative key to loop back to the alphabet
					num -= 26
				elif num < ord('A'): # 
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num)
		else:
			translated += symbol
	return translated

# function for message validation, must be alpha
def mesVal(y):
	if str(y).isalpha() == True:
		return y
	else:
		return False

# function for name validation + no blank
def checkName(x): 
	if str(x).isalpha() == True: # check if alpha 
		if len(x) >=3 and len(x) <=12: # check if length >3 and <12
			return x 
		else:
			return False
	else:
		return False

# to loop the caesar cipher program
def checkAgain(): 
	
	print greeting 
	# input your first name
	myName = raw_input('Your first name? ').capitalize() 
	while checkName(myName) == False: # calling for checkName function to validate input
		myName = raw_input("Name must be between 3 to 12 characters. Try again: ")
	else:
		print "Hello " + myName.capitalize()

	mode = callED()
	message = callMessage().lower()
	key = callKey()

	print 'Your translated text is: '
	print callTM(mode, message, key)
	# try again message
	tAgain = raw_input('Would you like to try again? (Yes or No) ')
	if tAgain in yList:
		checkAgain()
	else:
		print 'Thanks for using my Caesar Cipher program! '
		exit()

checkAgain()

print("This is a test")

'''
	myMessage = raw_input('Enter your message: ').capitalize()
	while mesVal(myMessage) == False:
		myMessage = raw_input('Your message must only be letters. Try again: ')
	else: 
		print 'This is your message: ' + myMessage
	return myMessage.isalpha()
'''

