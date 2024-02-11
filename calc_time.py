
def calc(a):
    min = 00
    sec = 00
    hours = 00

    if a % 60 == 0:
        pass
    else:
        sec = a % 60
        a -= sec
        print(sec)
        print(a)
        hour = int(a / 3600)
        print(hour)
        min = int((a % 3600) / 60)
        print(min)
        print(f'{hour} hours {min} minutes {sec} seconds')
a = input("press")
calc(int(a))

