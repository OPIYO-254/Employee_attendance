from scanner import EmployeeScanner
def menu():
    es = EmployeeScanner()
    print('-------------------------------------')
    print("Welcome to Employee Management System")
    print('-------------------------------------')
    print('Select option')
    print('1. Scan card')
    print('2. Search attendance')
    print('3. Exit')
    try:
        option = int(input('Enter option\n'))
        if option == 1:
            es.capture_qr()
        elif option ==2:
            es.search_record()
        elif option == 3:
            quit()
        else:
            print('Invalid option. Try again')
            menu();
    except ValueError:
        print('Invalid option. Try again')
        menu()

if __name__ == '__main__':
    menu()

