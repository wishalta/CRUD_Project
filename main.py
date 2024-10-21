import datetime

books = [
    [
        'George Orwell ',
        '"1984"',
        50,
        240
     ],
    [
        'J.R.R. Tolkien ',
        '"The Lord of the Rings"',
        100,
        500
     ],
    [
        'Stephenie Meyer',
        'The Twilight Saga',
        78,
        367
    ]
]
def printInfo():
    print("-------------------------------")
    print("1. List 2. Add 3. Edit 4. Delete 5. Finish program")
    print("1. Finished books")
    print("2. New book")
    print("3. Your current page or edit book")
    print("4. Remove book from list")
    print("5. Exit")
    print("-------------------------------")


def printBook(bk, num = 1):
        print(f'{num} Author: {bk[0]} Book: {bk[1]} Pages: {bk[2]}/{bk[3]}')


def printBooks():
    num = 1
    for bk in books:
        printBook(bk, num)
        num += 1
    # num = 1
    # for bk in books:
    #     printBook(bk, num)
    #     num += 1


def addBook():
    print('Book author: ')
    bkauthor = input()
    print('Book name: ')
    bkname = input()
    print('Pages you read: ')
    bkPageread = int(input())
    print('Total pages: ')
    bkTotalpage = int(input())
    books.append([bkauthor, bkname, bkPageread, bkTotalpage])


def editBook():
    print('knyga kuria norite redaguoti: ')
    ed = int(input())
    printBook(books[ed - 1])
    print('Suveskite naujas reiksmes: ')
    print('Book author: ')
    bkauhtor = input()
    print('Book name: ')
    bkname = input()
    print('Pages you read: ')
    bkpagesread = int(input())
    print('Pages in book: ')
    bkpages = int(input())
    books[ed - 1] = ([bkauhtor, bkname, bkpagesread, bkpages,])

def removeBook():
    print('Which book you want to remove (number): ')
    rem = int(input())
    books.pop(rem - 1)

def editPages():
    print('Kuri knyga: ')
    order = int(input())
    printBook(books[order - 1])
    print('Pages done: ')
    pagesdone = int(input())
    books[order -1][2] = pagesdone

print('-----BOOK LIST-----')

while True:
    printInfo()
    opt = int(input('Choice: '))
    match opt:
        case 1:
            printBooks()
        case 2:
            addBook()
            printBooks()
        case 3:
            print('Change pages or book info (1 - if pages/2 - if book)')
            choice = int(input())
            if choice == 1:
                editPages()
                printBooks()
            if choice == 2:
                editBook()
                printBooks()
        case 4:
            removeBook()
            printBooks()
        case 5:
            print('Page numbers or authors?')
            kas = input()
            print('Book cover?')
            koks = input()

            print("opt kas")
            if kas == 'page numbers':
                print('Filtered by page numbers')
                printBooks(range(2, 3))
            if kas == 'authors':
                print('Filtered by authors')
        case 6:
            print('Good luck')
            exit(1)
