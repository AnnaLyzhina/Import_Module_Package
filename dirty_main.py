from datetime import datetime

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(f"Текущая дата и время: {datetime.now():%d.%m.%Y %H:%M:%S}")
    get_employees()
    calculate_salary()
