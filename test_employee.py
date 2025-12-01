from employee import employee_details

def employee_details(name, emp_id, dept, salary):
    return (
        f"Employee Name:{name}\n"
        f"Employee ID:{emp_id}\n"
        f"Department:{dept}\n"
        f"Salary:{salary}"
    )
    assert employee_details("Alice", "E1001", "IT", 55000) == expected_output
    
