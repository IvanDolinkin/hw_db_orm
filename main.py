import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Shop, Stock, Sale, Publisher
from queries import queries
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')


def add_data(session):
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()


if __name__ == '__main__':
    DSN = f"postgresql://{user}:{password}@localhost:5432/{db}"
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    add_data(session)
    queries(session)

    session.close()
