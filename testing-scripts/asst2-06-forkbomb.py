#!/usr/bin/python

import core
import sys

def testForkBomb(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing forkbomb")
	check = 'OS\/161 kernel \[\? for menu\]\: '
	test.send_command("p /testbin/forkbomb")
	result = test.look_for(check)

	if result != -1:
		test.print_result(0, 8)
	else:
		test.print_result(8, 8)

def main():
	path = str(sys.argv[1])
	testForkBomb(path)



if __name__ == "__main__":
	main()
