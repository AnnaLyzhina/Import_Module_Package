from datetime import datetime
from application import calculate_salary
from application.db import get_employees
import pandas as pd

def show_current_date() -> None:
    """Print the current date and time."""
    now = datetime.now()
    print(f"Текущая дата и время: {now:%d.%m.%Y %H:%M:%S}")

def main():
    show_current_date()

    get_employees()
    calculate_salary()

    # Пример использования pandas
    data = {
        'name': ['Ann', 'Ivan', 'Olga'],
        'salary': [100000, 120000, 95000]
    }

    df = pd.DataFrame(data)
    print("\nDataFrame:")
    print(df)

    print("\nСредняя зарплата:", df['salary'].mean())

if __name__ == '__main__':
    main()