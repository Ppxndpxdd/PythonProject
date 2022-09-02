def hbd(age):
    if age % 2 == 0:
        a = 20
        x = age / 2 
    else:
        a = 21
        x = age // 2 
    

year = int(input("Enter year : "))
print(hbd(year))