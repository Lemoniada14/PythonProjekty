import time

def WprowadzanieLiczby():
    print("podaj liczbę")
    x = input()
    while x.isnumeric() == False:
        print("error")
        print("Podaj liczbę")
        x = input()
    return int(x)

a = WprowadzanieLiczby()
b = WprowadzanieLiczby()
c = WprowadzanieLiczby()

print(a - b - c)
time.sleep(2)
