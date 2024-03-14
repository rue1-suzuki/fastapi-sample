from apis.Item.models import Base as ItemBase
from database import engine

# migrateの実行順に注意
target_bases = [
    ItemBase,
]


def migrate():
    for Base in target_bases:
        Base.metadata.create_all(bind=engine)

        for table in Base.metadata.tables:
            title = table.title()
            print(f'{title} table created successfully')


if __name__ == '__main__':
    migrate()
