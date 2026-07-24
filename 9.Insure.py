married = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if married.lower() == "married":
    print("Driver is Insured.")
    
elif married.lower() == "unmarried":
    
    if gender.lower() == "male" and age > 30:
        print("Driver is Insured.")
    elif gender.lower() == "female" and age > 25:
        print("Driver is Insured.")
    else:
        print("Driver is Not Insured.")
else:
    print("Invalid marital status.")
