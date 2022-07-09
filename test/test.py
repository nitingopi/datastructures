
import sys
import fileinput


# numbers_int = ["1","2","3","4","5","6","7","8","9","0"]
# numbers_str = ["one", "two", "three", "four", "five", "six", "seven" , "eight", "nine", "zero"]
mapping_int_str = {"1":"one", "2" : "two", "3":"three","4":"four", "5":"five", "6":"six","7":"seven"  }

def start():
    input = sys.argv[1]
    box = []
    for line_count, line in enumerate(fileinput.input("input.txt"), start=1):
        # print(line)
        for k,v in mapping_int_str.items():
            
        if str(input) in line:
            box.append(line_count)
    for line_number in box:
        print(line_number)        

if __name__ == "__main__":
    start()