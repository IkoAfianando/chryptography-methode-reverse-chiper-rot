ROT13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
)


def rot13(text):
    return text.translate(ROT13)


x = input("Masukkan Text: ")
print(rot13(x))
