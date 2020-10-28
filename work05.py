profit = int(input("Введите прибыль предприятия: ")) #выручка
cost = int(input("Введите издержки фирмы: ")) #издержки
profit_num = 0 #прибыль или убыток
num = 0 #переменная для вычисления
if profit >= cost:
    profit_num = profit - cost
    if profit > cost:
        print("Ваша прибыль составляет: ", profit_num)
        num = round(profit_num / profit,2) #вычисляем рентабельность (прибыль к выручке)
        print("Ваша рентабельность: ",num)
        staff = int(input("Введите колличество сотрудников: "))
        num = round(profit_num / staff,2) #вычисляем прибыль в расчёте на 1 сотрудника
        print("Прибыль на одного сотрудника: ",num)
    else:
        print("Вы работаете по себестоимости")
else:
    profit_num = cost - profit
    print("Ваш убыток составляет: ", profit_num)