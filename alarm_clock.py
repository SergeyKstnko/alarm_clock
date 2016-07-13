#alarm_clock.py
#@author Sergey Kostenko

#This program is the alarm clock. It takes time for the alarm to go off from the 
#command line. When the time is right, it opens one of the 4 links.

import sys, time, argparse
import webbrowser, random

url1 = "https://www.youtube.com/watch?v=DclzQCVIIrM&index=2&list=PLMMHnZBscWoE3HbPgeALPO1rCJsBa_QVS"
url2 = "https://www.youtube.com/watch?v=g-jwWYX7Jlo&index=14&list=PLMMHnZBscWoE3HbPgeALPO1rCJsBa_QVS"
url3 = "https://www.youtube.com/watch?v=4KGELExSnXU&list=FLgPP-SlW0ECBMa7f-WVEPgw"
url4 = "https://www.youtube.com/watch?v=FG0fTKAqZ5g&index=2&list=FLgPP-SlW0ECBMa7f-WVEPgw"
url = [url1, url2, url3, url4]


def alarm(hr, mn, per):
	'''This function take in time for the alarm to go off. And opens the url when the
	time is for the alarm is equal to the current time. Has no return
	hr 	int 	hour
	mn 	int 	minute
	per str 	period (AM/PM)'''
	if time.localtime().tm_hour > 12:
		current_hr = time.localtime().tm_hour - 12
		current_per = 'pm'
	else: current_per = 'am'
	while True:
		if current_hr == hr and time.localtime().tm_min == mn:
			if __name__ == "__main__":
				rand = random.randint(0,len(url)-1)
				webbrowser.open(url[rand], new=2, autoraise = True)
			print("Knock, Knock, Neo.")
			break
		print("Time is: %s:%s %s. Alarm was set for: %s:%s %s" % (current_hr, time.localtime().tm_min, current_per, hr, mn, per))			
		time.sleep(15)

def command_line(arguments):
	'''This function uses argparse to provide a user friendly user interface'''
	parser = argparse.ArgumentParser(description='Set your alarm clock.')
	parser.add_argument('--h', '--hour', type = int, choices = range(1,13), required = True, help ='CHoo')
	parser.add_argument('--m', '--minute', type = int, choices = range(0,61), required = True, help ='CHoo')
	parser.add_argument('--p', '--period', choices = ['AM', 'PM', 'am', 'pm'], required = True)
	return vars(parser.parse_args(arguments))

if __name__ == "__main__":
	print(sys.argv)
	args = command_line(sys.argv[1:])
	alarm(args['h'], args['m'], args['p'])
