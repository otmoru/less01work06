time_seconds = int(input("Введите время в секундах: "))
time_minutes = time_seconds // 60
time_seconds = time_seconds - (time_minutes * 60)
time_hours = time_minutes // 60
time_minutes = time_minutes - (time_hours * 60)
print("Время - %dч.:%dмин.:%dсек."%( time_hours,time_minutes,time_seconds))