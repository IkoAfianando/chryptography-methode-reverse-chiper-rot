x = input("Masukkan Kata:")
translated = ''

i = len(x) - 1
while i >= 0:
    translated = translated + x[i]
    i = i - 1

print("The Chiper Text is : ", translated)
