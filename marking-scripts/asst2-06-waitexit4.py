#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing use of wait and exit I")
	check = 'wekp'
	test.send_command("p /testbin/waitexit1")
	test.look_for_and_print_result(check, 6)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()
