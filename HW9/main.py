from helpers import save, get_all_employers, get_employee_by_email, update_employee_with_phone


while True:
    print("1.Add new Employee\n2.Get all Employees\n3.Get employee by email\n4.Update Employee")
    flag = input("Choose menu item: ")
    if flag == "1":
        email = input("Employee email: ")
        first_name = input("Employee first name: ")
        last_name = input("Employee last name: ")
        phone_number = input("Employee phone number: ")
        save(email, first_name, last_name, phone_number)
    elif flag == "2":
        get_all_employers()
    elif flag == "3":
        email_to_find = input("Type email of employee which you want to find: ")
        get_employee_by_email(email_to_find)
    elif flag == "4":
        phone = input("Enter the number of the employee to be changed: ")
        update_employee_with_phone(phone)




