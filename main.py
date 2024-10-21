import datetime

flights = [
    [
        'vno',
        'kns',
        datetime.datetime(2024, 10, 15, 14, 30, 0),
        datetime.datetime(2024, 10, 15, 16, 30, 0)
    ],
    [
        'vno',
        'tln',
        datetime.datetime(2024, 10, 15, 14, 30, 0),
        datetime.datetime(2024, 10, 15, 20, 30, 0)
    ],
    [
        'vno',
        'chr',
        datetime.datetime(2024, 10, 15, 14, 30, 0),
        datetime.datetime(2024, 10, 15, 15, 00, 0)
    ]
]

def printInfo():
    print("-------------------------------")
    print("1. sarasas 2. ideti 3. redaguoti 4. trinti 5. baigti programa")
    print("1. Skrydziu atvaizdavimas")
    print("2. Naujo skrydzio ikelimas")
    print("3. Skrydzio redagavimas")
    print("4. Skrydzio salinimas")
    print("5. Iseiti is programos")
    print("-------------------------------")


def printFlags(fl, num = 1):
    print(f'{num}, Skrydzio is {fl[0]} i { fl[1]}. Pakyla {fl[2]}, nusileidzia {fl[3]}. Skrydzio tukme {fl[3] - fl[2]} ')


def printFlights():
    num = 1
    for fl in flights:
        printFlights(fl, num)
        num += 1


def addFlight():
    print('Is kur skrenda?')
    flFrom = input()
    print('I kur skrenda?')
    flTo = input()
    print('Kada kyla? (yyyy-mm-dd hh:mm:ss)')
    flLeave = datatime.datetime.strptime(input(), "%Y-%m-%d %H-%M-%S")
    print('Kada leidziasi? (yyyy-mm-dd hh:mm:ss)')
    flArrive = datatime.datetime.strptime(input(), "%Y-%m-%d %H-%M-%S")
    flights.append([flFrom, flTo, flLeave, flArrive])


def editFlight():
    print('Iveskite skrydzio numeri kuri norite redaguoti')
    ed = int(input())
    printFlight(flights[ed - 1])
    print('Suveskite naujas reiksmes: ')
    print('Is kur skrenda?')
    flFrom = input()
    print('I kur skrenda?')
    flTo = input()
    print('Kada kyla? (yyyy-mm-dd hh:mm:ss)')
    flLeave = datatime.datetime.strptime(input(), "%Y-%m-%d %H-%M-%S")
    print('Kada leidziasi? (yyyy-mm-dd hh:mm:ss)')
    flArrive = datatime.datetime.strptime(input(), "%Y-%m-%d %H-%M-%S")
    flights[ed - 1] = ([flFrom, flTo, flLeave, flArrive])

def removeFlight():
    print('Iveskite skrydzio numeri kuri norite pasalinti')
    rem = int(input())
    flights.pop(rem - 1)

print('-----SKRYDZIU VALDYMO SISTEMA-----')

while True:
    printInfo()
    opt = int(input())
    match opt:
        case 1:
            printFlights()
        case 2:
            addFlight()
            printFlights()
        case 3:
            editFlight()
            printFlights()
        case 4:
            removeFlight()
            printFlights()
        case 5:
                exit(1)