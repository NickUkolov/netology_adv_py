from datetime import *
from application.db.people import *
from application.salary import *
from application.Google_maps import *

def main():
    print(datetime.now().strftime('%X %A %d-%m-%Y'))
    get_employees()
    calculate_salary()
    map()

if __name__ == '__main__':
    main()