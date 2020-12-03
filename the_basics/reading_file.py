# read once only due to cursor position at end of last text
# myfile = open("fruits.txt")
# print(myfile.read())
# print(myfile.read()) - empty string

# print multiple times, store in variable the read
# myfile = open("fruits.txt")
# myfile = open('fruits.txt')
# content = myfile.read()
# close to delte temp memory
# myfile.close()

import time

with open('fruits.txt', "r+") as f:
    content = f.read()
    f.write("\n" + content + "\n" + content)
    content = f.seek(0)
    content2 = f.read()
for contents in content2:
    print(contents)
    time.sleep(5)




