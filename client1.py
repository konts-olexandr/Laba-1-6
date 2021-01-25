import socket
import _thread
import os



os.system('')

def main():
	ua = "абвгґдуєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
	UA = ua.upper()
	ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
	eng = ENG.lower()
	num = "12345678901234567890"
	key = 5
	o_eng = ord("a")
	o_ENG = ord("A")


	host = '192.168.56.1'
	port = 5555

	for x in range(70):
		print('')

	try:
		file = open('config.txt', 'r+')
		write = False
	except:
		file = open('config.txt', 'w')
		write = True

	if not write:
		lines = file.readlines()
		un = lines[0][:-1]
		colour = lines[1]
	else:
		un = input('\033[2;32;40mPlease pick a username:\033[0m ')
		file.write(un + '\n')
		while True:
			try:
				print("""Pick a colour:
\033[1;30;40m30 - Black
\033[1;31;40m31 - Red
\033[1;32;40m32 - Green
\033[1;33;40m33 - Yellow
\033[1;34;40m34 - Blue
\033[1;35;40m35 - Purple
\033[1;36;40m36 - Cyan
\033[1;37;40m37 - White\033[0m""")
				colour = int(input())
				if colour:
					break
			except:
				print('\033[2;31;40mERROR: Colour must be an integer between 30 and 37\033[0m')
		file.write(str(colour))
	file.close()

	s = socket.socket()
	s.connect((host, port))

	def getMessages():
		while True:
			data = s.recv(1024).decode('utf-8')
			DCtextt=''
			for letter in data:
				new_num = num.find(letter) - key
				new_ua = ua.find(letter) - key
				new_UA = UA.find(letter) - key

				if letter in ua:
					DCtextt = DCtextt + ua[new_ua]

				elif letter in UA:
					DCtextt =DCtextt + UA[new_UA]

				elif letter in str(eng):
					DCtextt += chr(((ord(letter) - o_eng - key) % 32) + o_eng)

				elif letter in str(ENG):
					DCtextt += chr(((ord(letter) - o_ENG - key) % 32) + o_ENG)

				elif letter in str(num):
					DCtextt = DCtextt + num[new_num]

				else:
					DCtextt = DCtextt + letter
			data1 = DCtextt
			print(data1)

	def sendMessage():
		while True:
			text = input()
			textt=''
			for letter in text:

				new_num = num.find(letter) + key
				new_ua = ua.find(letter) + key
				new_UA = UA.find(letter) + key

				if letter in ua:
					textt = textt + ua[new_ua]

				elif letter in UA:
					textt = textt + UA[new_UA]

				elif letter in str(eng):
					textt += chr(((ord(letter) - o_eng + key) % 32) + o_eng)

				elif letter in str(ENG):
					textt += chr(((ord(letter) - o_ENG + key) % 32) + o_ENG)

				elif letter in str(num):
					textt = textt + num[new_num]

				else:
					textt = textt + letter
			msg = textt
			s.send(('\033[1;' + str(colour) + ';40m' + un + ':\033[0m '  + msg).encode('utf-8'))

	_thread.start_new_thread(getMessages, ())
	_thread.start_new_thread(sendMessage, ())

	while True:
		pass

if __name__ == "__main__":
	main()