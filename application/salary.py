import pandas as pd

def calculate_salary() -> None:
    """Demonstrate salary calculation using pandas."""
    employees = pd.DataFrame(
        {
            'name': ['Анна', 'Иван', 'Ольга'],
            'salary': [100000, 120000, 95000],
        }
    )

    average_salary = employees['salary'].mean()
    total_salary = employees['salary'].sum()

    print('\nРасчёт зарплаты выполнен')
    print(employees)
    print(f'Средняя зарплата: {average_salary:.2f}')
    print(f'Общий фонд зарплаты: {total_salary}')
