password = input("Enter password: ")

if ' ' in password:
    print("Invalid Password: Should not contain spaces")

elif len(password) < 8 or len(password) > 15:
    print("Invalid Password: Length must be between 8 and 15 characters")

elif not any(ch.isdigit() for ch in password):
    print("Invalid Password: Must contain at least one digit")

elif not any(ch.islower() for ch in password):
    print("Invalid Password: Must contain at least one lowercase letter")

elif not any(ch.isupper() for ch in password):
    print("Invalid Password: Must contain at least one uppercase letter")

elif not any(ch in "@#$%&!^*+_=-()~" for ch in password):
    print("Invalid Password: Must contain at least one special character")

else:
    print("Valid Password")