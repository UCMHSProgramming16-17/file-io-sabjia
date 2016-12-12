# open file
file = open('mylist.txt', 'w')

# add items to file
for n in range(10):
    file.write(str(n+1) + ". " + input("What should I add to the list? ") + '\n')

# close file
file.close()