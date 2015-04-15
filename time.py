import time

def main():
	start = time.time()
	minimumElapsed = .5

	while True:
		if time.time() - start > minimumElapsed:
			print "Loading..."
			minimumElapsed += .5

main()
