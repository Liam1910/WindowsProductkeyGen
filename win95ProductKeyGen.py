import random
import sys

def generateS():
	while True:
		num = random.randint(0, 9999999)
		digit_sum = sum(int(digit) for digit in str(num))

		if digit_sum % 7 == 0:
			return f"{num:07}"

def generateX():
	while True:
		num = random.randint(0, 999)

		if formatted not in {"333", "444", "555", "666", "777", "888", "999"}:
			return f"{num:03}"

def main():
	if len(sys.argv) != 2:
		print("Error: You must provide either rtm or osr2+ for the generation of the product key! Or use help for knowing what the args are!")
		return
	
	arg = sys.argv[1].lower()

	if arg == "rtm":
		xxx = generateX()
		S = generateS()
		print(f"{xxx}-{S}")
	if arg == "osr2+":
		ddd = random.randint(1, 366)
		yy = random.randint(1995, 2003)
		S = generateS()
		rrrrr = random.randint(0, 99999)
		print(f"{ddd:03}{str(yy)[-2:]}-OEM-{S}-{rrrrr:05}")
	elif arg == "debug":
		xxx = generateX()
		S = generateS()
		print(f"{xxx} - {S}")

		ddd = random.randint(1, 366)
		yy = random.randint(1995, 2003)
		S = generateS()
		rrrrr = random.randint(0, 99999)
		print(f"{ddd:03} {str(yy)[-2:]} -OEM- {S} - {rrrrr:05}")
	elif arg == "help":
		print("rtm:     generates a product key for Windows 95 rtm and osr 1 (xxx-xxxxxxx)")
		print("osr2+:   generates a product key for Windows 95 osr 2+ (2, 2.1, 2.5) (xxxxx-OEM-xxxxxxx-xxxxx)")
	else:
		print("Invalid Argument!")
		return

if __name__ == "__main__":
	main()
