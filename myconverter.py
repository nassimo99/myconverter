#!/usr/bin/python
# calculator for programmers

import sys
import binascii


def dec2bin(arg):
	print bin(arg)
def dec2hex(arg):
	print hex(arg)
def hex2dec(arg):
	print int(arg, 16)
def hex2bin(arg):
	print bin(int(arg, 16))[2:]

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "usage: ./%s.py [option] [code]" % sys.argv[0]
		print "options :"
		print "-dec2bin            converts decimal to binary"
		print "-dec2hex            converts decimal to hexadecimal"
		print "-hex2dec            converts hexadecimal to decimal"
		print "-hex2bin            converts hexadecimal to binary"
		sys.exit()


if sys.argv[1] == "-dec2bin":
	dec2bin(int(sys.argv[2]))
if sys.argv[1] == "-dec2hex":
	dec2hex(int(sys.argv[2]))
if sys.argv[1] == "-hex2dec":
	hex2dec(sys.argv[2])
if sys.argv[1] == "-hex2bin":
	hex2bin(sys.argv[2])
sys.exit()
