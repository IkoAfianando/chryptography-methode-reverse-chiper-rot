def factorial(value):
    if value <= 0:
        return 1
    else:
        return value * factorial(value - 1)

print("Ini adalah program untuk menghitung faktorial dari angka yang diinputkan", factorial(5))