#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing printchar", True)
	# check = 'H*e*l*l*o*w*o*r*l*d*\!*H*e*l*l*o*p*r*i*n*t*f*\!*'
	# check = 'H.*e.*l.*l.*o.*w.*o.*r.*l.*d.*\!.*H.*e.*l.*l.*o.*p.*r.*i.*n.*t.*f.*\!'
	#check = 'H*e*l*l*o*p*r*i*n*t*f*\!'
	#check = 'H**e**l**l**o**p**r**i**n**t**f**\!'
	printchar_check = '$.#.@.$.#.@.'
	printf_check = 'S.Y.S.1.6.1.O.S.T.E.S.T.E.R.F.O.R.P.R.I.N.T.F'
	test.send_command("p /testbin/test_printchar")
	test.look_for_and_return_mark(printchar_check+printf_check, 20)


def main():
	path = str(sys.argv[1])
	testPrintChar(path)
	test.clean_kernel()



if __name__ == "__main__":
	main()
