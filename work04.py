number = int(input("Введите число N: "))
counter1 = 0
counter2 = 0
while number > 0:
    counter1 = number % 10
    number = number // 10
    if counter1 > counter2:
        counter2 = counter1
print("Максимальная цифра в числе N: ", counter2)

