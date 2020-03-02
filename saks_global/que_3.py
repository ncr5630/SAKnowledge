# import csv library 
import csv
#open cities csv file 
with open('cities.csv') as csv_file:
    # read the open file using csv reader
    readCSV = csv.reader(csv_file, delimiter=',')
    # looping one by one every rows in csv file
    for row in readCSV:
      # check "Tulsa" city in row 
      if ' "Tulsa"' in row:
        # print contain row if it's set
        print (row)