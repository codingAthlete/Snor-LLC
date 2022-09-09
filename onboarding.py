employee_first_name =input("What is your first name? ")
employee_last_name =input("What's your last name? ")
print("Thank you," + employee_first_name + 
 employee_last_name + ". Welcome to the Snor LLC team!")
email_address = employee_first_name[0:2] +employee_last_name
print("We here at Snor LLC use a company email to communicate with your peers and with your supervisors. Your email is " + email_address.lower() + "@snorllc.com")
employee_id =input("When is your birthday? Please type it out in MMDDYYYY format.")
print("Your employee id is " + employee_id[4:8]+employee_first_name[0]+employee_last_name[0]+employee_id[0:2]+ " ,don't loose this. It will be used to clock in and out.")