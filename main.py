from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def userInput():
    opt = [
        "Lowercase",
        "Uppercase",
        "Numbers",
        "Symbols",
        "All of the above",
        "I have selected what I want",
    ]
    gen, length = [], 0
    while True:
        if len(gen) >= 1:
            print(f"The password contains: {', '.join(gen)}")
        print("What should the password contain?")
        for index, options in enumerate(opt):
            print(f"{index + 1}. {options}")
        try:
            a = int(input("Your choice: "))
            if a > 6:
                raise ValueError
            if a == 6:
                break
            if opt[a - 1] in gen:
                gen.remove(opt[a - 1])
            else:
                if a != 5 and opt[4] in gen:
                    gen.clear()
                elif a == 5:
                    gen.clear()
                gen.append(opt[a - 1])
        except:
            print("Please enter the number corresponding to your choice.")
    print()
    while True:
        try:
            length = int(input("Please enter the length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except:
            print("Please enter a valid positive number.")
    return gen, length


def creatingPass(a: list, b: int):
    op, inp = "", ""
    choices = {
        "Lowercase": ascii_lowercase,
        "Uppercase": ascii_uppercase,
        "Numbers": digits,
        "Symbols": punctuation,
        "All of the above": ascii_lowercase + ascii_uppercase + digits + punctuation,
    }
    for x in gen:
        inp += choices[x]
    for i in range(b):
        op += choice(inp)
    return op


gen, length = userInput()
output = creatingPass(gen, length)
print(rf"The generated password is: {output}")
