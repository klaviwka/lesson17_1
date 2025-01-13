from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.schema import CreateTable

# Создаем движок SQLite (или другую БД)
engine = create_engine('sqlite:///taskmanager.db', connect_args={"check_same_thread": False})

# Создаем базовый класс для моделей
Base = declarative_base()

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функция для создания всех таблиц
def create_tables():
    Base.metadata.create_all(bind=engine)


# Функция для вывода SQL-запросов на создание таблиц
def print_sql():
    for table in Base.metadata.sorted_tables:
        print(CreateTable(table).compile(engine))


# Пример использования
if __name__ == "__main__":
    # Создание всех таблиц в базе данных
    create_tables()

    # Вывод SQL-запросов на создание таблиц
    print_sql()
