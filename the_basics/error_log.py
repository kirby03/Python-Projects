num = input("Enter a number: ")

try:
    int(num) + "1"
    print("okay")
except TypeError as err:
    with open("error_log.txt", "a+") as file:
        log = ()
        file.write(str(err))
        file.close()
    