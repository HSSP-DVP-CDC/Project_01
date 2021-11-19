#Reading files
#relateive path, absolute path, or filename if it is in the same directory
#Second param is the mode
##r: read; w: write; a: append; r+: read and write

house_occupants = open("File.txt", "r+")
print(house_occupants.readable())

#Extracts all information in the file
# print(house_occupants.read())

#Prints lines one at a time in the order the are listed for however many function calls you use
# print(house_occupants.readline())
# print(house_occupants.readline())

#Print all the lines of a file into an array
# print(house_occupants.readlines())

#Or use a for loop
for occupants in house_occupants.readlines():
    print(occupants)

#Append text
# house_occupants = open("File.txt", "a")

# print(house_occupants.write("\nThe Ghosts"))

# house_occupants.close()

#Write a file, will write over or create a new file
# house_occupants = open("File.txt", "w")

# print(house_occupants.write("\nThe Ghosts"))

# house_occupants.close()