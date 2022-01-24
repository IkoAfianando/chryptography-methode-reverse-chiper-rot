ROT18 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz0123456789",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm5678901234",
)


def rot18(text):
    return text.translate(ROT18)


x = input("Masukkan Text: ")
print(rot18(x))
