# open file
file = open('mylist.txt', 'w')

# add items to file
for n in range(10):
    file.write(str(n+1) + ". " + input("What's your #" + str(n+1) + " favorite fruit? ") + '\n')

# close file
file.close()