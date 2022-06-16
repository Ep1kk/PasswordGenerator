import random

# inefficient chracter table
characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "`", "¬", "'", "~", "#", "[", "]", "{", "}", "(", ")", "?", ">", "<", ",", ".", "/", "'", "?", ":", ";", "|",
    "!", "£", "$", "€", "%", "^", "&", "*", "-", "_", "=", "+", " "
]


def Generate(length):

    password = ("")

    passlength = ("-" * length)

    for i in passlength:
        rcase = random.randint(0, len(characters) - 1)
        password = (password + characters[rcase])

    return(password)


def SavePass(password):
    print("What would you like your password to be called? (do not include file extension)")
    print("(Warning : this will overwrite old passwords with the same file name)")
    filename = input("")

    passfile = open("passwords/" + filename + ".txt", "w")

    passfile.write(password)


print("Really Jank password generator")
print("=+=" * 10)

print("type the number of characters you want your password to be: ")
passlen = input("")


password = Generate(int(passlen))

print(password)


print("Would you like to save this password? (y/n)")


savepassword = input("")


if savepassword == "y":
    SavePass(password)
