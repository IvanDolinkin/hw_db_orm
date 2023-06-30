from models import Book, Shop, Stock, Sale, Publisher


def queries(session):
    print('Введите номер издателя:\n'
          '1 - O\u2019Reilly\n'
          '2 - Pearson\n'
          '3 - Microsoft Press\n'
          '4 - No starch press\n')
    number = input()
    publisher_name = {'1': 'O\u2019Reilly', '2': 'Pearson', '3': 'Microsoft Press', '4': 'No starch press'}

    query = session.query(Book, Shop, Sale, Publisher).join(Book).join(Stock).join(Sale).join(Shop).filter(
        Publisher.name == publisher_name[number])

    for row in query:
        print(row.Book.title, row.Shop.name, row.Sale.price, row.Sale.date_sale, sep=' | ')
