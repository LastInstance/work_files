from .system_helpers import save_to_file, get_file_data, save_list_to_file
from .decorators_helpers import is_email_valid, is_phone_valid

@is_phone_valid
@is_email_valid
def save(email, first_name, last_name, phone):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_to_file(new_employee)

def get_all_employers():
    employees = get_file_data()
    for employee in employees:
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])

def get_employee_by_email(email):
    employees = get_file_data()
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])

def update_employee_with_phone(phone):
    employers = get_file_data()
    for employee in employers:
        if employee["phone"] == phone:
            employee["email"] = input("New email: ")
            employee["first_name"] = input("New first name: ")
            employee["last_name"] = input("New last name: ")
            employee["phone"] = input("New phone number: ")
    save_list_to_file(employers, "database/employees.json")