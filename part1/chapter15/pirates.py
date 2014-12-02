from matplotlib import pyplot as plt
import os
import csv

path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 15/Practice files'
save_path = '/home/alberick'
csv_file = os.path.join(path, 'pirates.csv')
temp_list = []
pirates_list = []
years_list = []

with open(csv_file, 'rb') as input_csv:
    reader = csv.reader(input_csv)
    next(reader)
    for year, temp, pirates in reader:
        temp_list.append(temp)
        pirates_list.append(pirates)
        years_list.append(year)

plt.title("Decrease of pirates")
plt.xlabel("Temperature")
plt.ylabel("Pirates")
plt.axis([-300, 48000, 14, 16])
plt.plot(pirates_list, temp_list)
for i in range(len(years_list)):
    plt.annotate(str(years_list[i]), xy=(pirates_list[i], temp_list[i]))

plt.savefig(os.path.join(save_path, "histogram.png"))
plt.show()


