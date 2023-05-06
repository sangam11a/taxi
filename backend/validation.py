import re

def namevalidation(name):
    n=re.compile("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    if re.fullmatch(n, name):
        nameResult=True
    else:
        nameResult=False
    return nameResult


def numbervalidation(number):
    num=re.compile("^(?:0|\+?977)\s?(?:\d\s?){9,11}$")
    if  re.fullmatch(num, number):
        numberResult=True
    else:
        numberResult=False

    return numberResult

def emailvalidation(email):
    em=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(em, email):
        result = True

    else:
        result = False

    return result

def passwordvalidation(password):
    reel=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    if re.fullmatch(reel,password):
        passwordResult=True
    else:
        passwordResult=False
    return passwordResult
