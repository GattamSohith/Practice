def is_armstrong_number(number):
    dig = str(number)       
    p = len(dig)      
    return number == sum(int(d)**p for d in dig)
