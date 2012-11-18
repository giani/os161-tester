#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Checking the OS does not crash when OOM")
	fail_check = 'No such file or directory'
	check = 'OS\/161 kernel \[\? for menu\]\: '
	for i in range(1,10):
		test.send_command("p /testbin/sty")
		ret = test.look_for_and_print_result(check, 0)

	test.send_command("p /testbin/sty")
	#This is a hacky check to see we actually built sty
	fail = test.look_for(fail_check)
	if fail >= 0:
		test.print_result(0, 6)
	else:
		test.look_for_and_print_result(check, 6)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()
