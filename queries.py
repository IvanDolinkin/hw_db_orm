from models import Book, Shop, Stock, Sale, Publisher


def queries(session):
    print('Введите id или имя издателя:\n'
          '1 - O\u2019Reilly\n'
          '2 - Pearson\n'
          '3 - Microsoft Press\n'
          '4 - No starch press\n')
    find_publisher = input()
    if find_publisher.isdigit():
        publisher_name = session.query(Publisher.name).filter(Publisher.id == find_publisher).all()
    else:
        publisher_name = session.query(Publisher.name).filter(Publisher.name == find_publisher).all()
    if publisher_name != []:
        query = session.query(Book, Shop, Sale, Publisher).join(Book).join(Stock).join(Sale).join(Shop).filter(
            Publisher.name == publisher_name[0][0])
        print(f"{'Книга': ^40}|{'Магазин': ^15}|{'Цена': ^15}|{'Дата продажи': ^20}")
        print('=' * 93)
        for row in query:
            print(f'{row.Book.title: <40}|{row.Shop.name: ^15}|{row.Sale.price: ^15}|'
                  f'{row.Sale.date_sale.strftime("%d-%m-%Y"): ^20}')
    else:
        print('Издатель не найден')
