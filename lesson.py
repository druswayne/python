import math
try:
    radius = float(input("введите длину радиуса  блинчика "))
    while radius<=0:
        print("Длина радиуса должна быть положительной. Повторите пожалуйста ввод")
        radius = float(input("введите длину стороны печеньки "))
    print("Площадь: ",round(radius**2*math.pi,2),"\n","Периметр: ", round(2*radius*math.pi,2))

except:
    print("ошибочка вышла\nНаверное вы ввели недопустимое значение длины")