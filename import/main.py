from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
from application.Google_maps import map

def main():
    print(datetime.now().strftime('%X %A %d-%m-%Y'))
    get_employees()
    calculate_salary()
    map()

if __name__ == '__main__':
    main()