def encrypt(message, shift_num):
    encode = ""
    for i in message:
        if ord(i) < 97 or ord(i) > 122:
            encode += i
        else:
            temp = ord(i) + shift_num
            if temp <= 122:
                encode += chr(temp)
            else:
                encode += chr(temp - 122 + 97)
                        
    print(encode)

def decrypt(message, shift_num):
    decode = ""
    for i in message:
        if ord(i) < 97 or ord(i) > 122:
            decode += i
        else:
            temp = ord(i) - shift_num
            if temp >= 97:
                decode += chr(temp)
            else:
                decode += chr(122 - (97 - temp))
                        
    print(decode)


while(True):
    choice = input("Type 'encode' tp encrypt, type 'decode' to decrypt:\n")

    if choice == "encode":
        print("encode")
        message = list(input("Type your message:\n").lower())
        shift_num = int(input("Type the shift number:\n")) % 26 # to scale the number to the range of available alphabets
        encrypt(message,shift_num)
    elif choice == "decode":
        message = list(input("Type your message:\n").lower())
        shift_num = int(input("Type the shift number:\n")) % 26
        decrypt(message,shift_num)
    else:
        print("Invalid choice, choose between 'encode' or 'decode'")
        continue

    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if cont == "yes":
        continue
    else:
        break

print("GoodBye")