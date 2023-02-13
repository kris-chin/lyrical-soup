import csv
import random

#The name of the content section of your data. 
NAME_OF_CONTENT_HEADER = "Note Content"

FILENAME = "data/keep_notes.csv"

OUTPUT_DIR = "out/"

class STYLES():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

if __name__ == "__main__":
    with open(FILENAME, newline='') as file:
        reader = list(csv.reader(file))

        #The values of the first row of the CSV
        header = reader[0]
        
        print("CSV HEADERS:")
        print(header)

        total_items = len(reader) - 2

        #Helper function that converts each row into a dict based on the header rows
        def convert_to_dict(row: list):
            item = {}
            for i in range(len(header)):
                header_key = header[i]
                item_value = row[i]
                item[header_key] = item_value
            return item

        #use a list comprehension to shape all of the data in the CSV
        items = [ convert_to_dict(row) for row in reader[1:] ]

        number_of_bars = input("Number of bars: ")
        while (number_of_bars.isdigit() != True):
            print("Invalid input. Please enter a number")
            number_of_bars = input("Number of bars: ")

        #generate bars
        bars = []
        for i in range(int(number_of_bars)):
            bars.append(items[random.randint(0, total_items)])

        for i, bar in enumerate(bars):
            print(STYLES.BLUE + str(i + 1))
            print(STYLES.YELLOW + bar[NAME_OF_CONTENT_HEADER])
