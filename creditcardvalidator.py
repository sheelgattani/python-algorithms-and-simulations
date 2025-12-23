def validate(st):
    ind = 15
    total = 0
    while ind >=0:
        if ind % 2 == 0:
            if (2 * int(st[ind])) > 9:
                a = (2 * int(st[ind])) - 9
            else:
                a = (2 * int(st[ind]))
            total = total + a
        else:
            a = int(st[ind])
            total = total + a
        ind -= 1

    if total % 10 == 0:
        return True
    else:
        return False

while True:
    num = input("Enter 16 digit credit card number:")
    if len(num) != 16:
        print("Try again")
    else:
        if validate(num):
            print("The credit card number is valid")
        else:
            print("The credit card number is invalid")
        break
