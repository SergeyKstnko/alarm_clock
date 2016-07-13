#test_alarm.py
#@author Sergey Kostenko

#This file is the automated test for the alarm_clock.py

import unittest, sys
import alarm_clock, time

class TestStringMethods(unittest.TestCase):
	def test_everything_ok(self):
		'''Test_everything_ok Tests the case when the current time is equal to the alarm time.'''
		if time.localtime().tm_hour > 12:
			hr = time.localtime().tm_hour - 12
			per = 'pm'
		else: per = 'am'
		mn = time.localtime().tm_min
		args = {'h': hr, 'm': mn, 'p': per}
		alarm_clock.alarm(args['h'], args['m'], args['p'])

	def test_command_line(self):
		'''This tests command line arguments input'''
		test_arguments = ['alarm_clock.py', '--h', '6', '--m', '05', '--p', 'pm']
		alarm_clock.command_line(['--h', '12', '--m', '2', '--p', 'AM'])

if __name__ == '__main__':
	unittest.main()
