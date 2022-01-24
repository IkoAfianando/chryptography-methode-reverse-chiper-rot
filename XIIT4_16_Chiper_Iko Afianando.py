def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]

        # apabila huruf besar
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)

        # apabila berupa number
        elif (char.isnumeric()):
            result += chr((ord(char) + key - 30) % 26 + 30)

        # apabila berupa huruf kecil
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


value = str(input("Masukkan teks yang akan dienkripsi: "))
key = int(input("Masukkan chiper key: "))
print("Plain Text: ", value)
print("Chiper Key: ", key)
print("Chiper Text: ", encrypt(value, key))
