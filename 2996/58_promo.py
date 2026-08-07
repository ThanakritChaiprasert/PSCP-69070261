'''Promotion'''
def total():
    '''Promotion'''
    PRODUCTS = input().split(' ')
    pencils = PRODUCTS[0]
    books = PRODUCTS[1]
    colors = PRODUCTS[2]
    pencil_cost = int(pencils) * 25
    book_cost = int(books) * 40
    color_cost = int(colors) * 55
    if 0 <= int(pencils) <= 1000 and 0 <= int(books) <= 1000 and 0 <= int(colors) <= 1000:
        TOTAL = (int(pencil_cost) + int(book_cost) + int(color_cost))
        if (int(pencil_cost) + int(book_cost) + int(color_cost)) >= 3:
            print(int(TOTAL) - (int(TOTAL) * 0.1))
        else:
            print(TOTAL)

total()
