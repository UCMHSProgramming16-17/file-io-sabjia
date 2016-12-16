# import module
import csv
import math

# create file
file = open('cvs.csv', 'w')

# create csvwriter
csvwriter = csv.writer(file, delimiter=',')

# write info
csvwriter.writerow(['a', 'b', 'hypotenuse'])
for a in range(1,101):
    for b in range(1, 101):
        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        csvwriter.writerow([a, b, hypotenuse])

# close file
file.close()