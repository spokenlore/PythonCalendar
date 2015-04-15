# Samson Fung 
# github.com/spokenlore
# April 13, 2015

# Simple calendar using a text file, to be converted to using a database hosted on a website or cloud service
# Mobile / Web app usage to be added later
# Sharing capabilites?

# TODO (in order of importance):
# Implement a calendar date sorting method
# Add ability to mark events / event entries as completed so that they will not be listed, or placed in a separate file
# Android support / Usage of Django in order to support web capability.
# Offline storage on a mobile device? Primarily android
# Text / Phone / Push / Email

# Possible technologies:
# Django / Flask
# Twilio
# Intel Bluemix / Microsoft Azure

import sys, time, os

def main():
	if checkForCalendar() == True:
		displayBool = raw_input("Enter d to display, or e for new event, or c to delete calendars.\n")
		if displayBool == 'd':
			displayCalendar()
		elif displayBool == 'e':
			calendarEvent = raw_input("Please enter a new calendar event as a string.\n")
			calendarDate = raw_input("Please enter a date in the format of mm/dd/yyyy, or u for 'Upcoming'.\n")
			if str(calendarTime) == 'u':
				addUpcoming(calendarEvent)
			else:
				calendarTime = raw_input("Please enter a time in the format of hours:minutes.\n")
				parseDate(calendarDate, calendarTime)
		elif displayBool == 'c':
			if os.path.isfile("past.txt"):
				os.remove("past.txt")
			if os.path.isfile("calendar.txt"):
				os.remove("calendar.txt")
		else:
			print "Invalid entry. Ending program.\n"
	else:
		print "Empty calendars created. Exiting program.\n"


def checkForCalendar():
	# If calendar.txt does not exist, create a base calendar.txt
	# Format should be Upcoming, then dated entries
	calendarBool = os.path.isfile("calendar.txt")
	pastCalendarBool = os.path.isfile("pastCalendar.txt")
	if calendarBool and pastCalendarBool: 
		return True
	else:
		if calendarBool:
			with open("calendar.txt", 'w') as calendar:
				calendar.write("Upcoming:\n")
				calendar.close()
		if pastCalendarBool:
			with open("pastCalendar.txt", 'w') as pastCalendar:
				# pastCalendar.write
				pastCalendar.close()
		return False

def addUpcoming(calendarEvent):
	# Adds events to calendar's "Upcoming"
	with open("calendar.txt", 'r') as calendar:
		start = time.time()
		minElapsed = 0
		while calendar.readline() != "Upcoming":
			while time.time() < start + minElapsed:
				print "Loading...\n"
				minElapsed += .2

def displayCalendar():
	# Open calendar
	with open("calendar.txt", 'r') as calendar:
		minimumElapsedTime = .5
		startTime = time.time()
		calendarLine = calendar.readline()
		if calendarLine == "":
			calendar.close()
			with open("calendar.txt", 'a') as calendar:
				calendar.write("Upcoming:")
			calendar.close()
		else:
			while calendarLine != "Upcoming:":
				calendarLine = calendar.readline()
				if calendarLine == "":
					break
				elif startTime + minimumElapsedTime < time.time():
					print "Loading..."
					minimumElapsedTime += .5

		calendar.close()
	# Print calendar "Upcoming"

	# Print past, if desired
	pastCalendarBool = raw_input("Enter Y/Yes/YES if you would like to view past events.\n")
	if pastCalendarBool == 'y' or pastCalendarBool == 'Y' or pastCalendarBool == "Yes" or pastCalendarBool == "YES":
		displayPastCalendar()

def displayPastCalendar():
	try: 
		with open("past.txt", 'r') as past:
			if past.read() != "":
				print past.read()
		past.close()
	except:
		pass
	open("past.txt", 'w')

main()

# Notes:
# Opening Options:
# r : read, w : write, a : appending, r+ : reading + writing