import random
import sys

def generateS():
    while True:
        num = random.randint(1000000, 9999999)
        digit_sum = sum(int(digit) for digit in str(num))

        if digit_sum % 7 == 0:
            return num

def generateX():
    while True:
        num = random.randint(0, 999)
        formatted = "%03d" % num

        if formatted not in set(["333", "444", "555", "666", "777", "888", "999"]):
            return formatted

def main():
    if len(sys.argv) != 2:
        print "Error: You must provide either rtm or osr2+ for the generation of the product key!"
        return
    
    arg = sys.argv[1].lower()

    if arg == "rtm":
        xxx = generateX()
        S = generateS()
        print "%s-%d" % (xxx, S)
    elif arg == "osr2+":
        ddd = random.randint(1, 366)
        yy = random.randint(1995, 2003)
        S = generateS()
        rrrrr = random.randint(10000, 99999)
        print "%03d%s-OEM-%d-%d" % (ddd, str(yy)[-2:], S, rrrrr)
    elif arg == "debug":
        ddd = random.randint(1, 366)
        yy = random.randint(1995, 2003)
        S = generateS()
        rrrrr = random.randint(10000, 99999)
        print "%03d %s -OEM- %d - %d" % (ddd, str(yy)[-2:], S, rrrrr)

        xxx = generateX()
        S = generateS()
        print "%s - %d" % (xxx, S)
    elif arg == "help":
        print "rtm:   generates a product key for Windows 95 rtm and osr 1 (xxx-yyyyyyy)"
        print "ors2+: generates a product key for Windows 95 osr 2+ (2, 2.1, 2.5) (xxxyy-OEM-SSSSSSS-rrrrr)"
    else:
        print "Invalid argument!"
        return

if __name__ == "__main__":
    main()
