import re
def password_check(password):
    if(len(password)<8):
        return "Password too short"
    has_digit=any(char.isdigit() for char in password)
    has_lower=any(char.islower() for char in password)
    has_upper=any(char.isupper() for char in password)
    has_special=any(char in "!@#$%^&*()_+-=<>,.?/:;'[{]}" for char in password)
    complexity=sum([has_digit,has_lower,has_upper,has_special])
    if(complexity<3):
        return "Password lacks complexity"
    commonpatterns=[r"123",r"abc",r"password",r"qwerty",r"111",r"admin"]
    for pattern in commonpatterns:
        if re.search(pattern,password,re.IGNORECASE):
            return "Password too common"
    return "Strong password"
p=input("Enter the password: ")
print(password_check(p))