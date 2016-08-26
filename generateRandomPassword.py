#!/usr/bin/python
import sys , getopt
import string
import random
from subprocess import Popen, PIPE

def copyToClipboard(txt):
        p = Popen(['xsel', '-bi'], stdin=PIPE)
        p.communicate(input=txt)


def id_generator(argv):
	size=12
	chars=string.ascii_letters + string.digits + '!@#$%^&*()'
	help = 'grp -l <pass lenght>'

	try:
		opts , args = getopt.getopt(argv,"l:")
	except getopt.GetoptError:
		print help
		sys.exit(2)
	for opt , arg in opts:
		if opt == '-l':
			size = int(arg)
		else:	
			print help
			sys.exit()			
	
	return ''.join(random.choice(chars) for _ in range(size))

password = id_generator(sys.argv[1:])
copyToClipboard(password)
print password + ' #Is on your clipboard'

