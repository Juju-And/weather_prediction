import random
import csv

with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # filewriter.writerow(['Day', 'Temperature'])
    for j in range(1, 31):
        filewriter.writerow([j, random.randint(1, 40)])

with open('data.csv', 'rb') as exp_data:
    reader = csv.reader(exp_data)
    # for row in reader:
    #     print(row)

