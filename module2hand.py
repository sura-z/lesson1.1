field = int(input("Укажите любое число от 3 до 20 "))
if (field >= 3) and (field <= 20):
    first_number = 1
    second_number = 1
    rezult = ' '
    for i in range(1, 21):
        first_number = i
        for j in range(1, 21):
            second_number = j
            if field % (first_number + second_number) == 0:
                if first_number < second_number:
                    rezult = rezult + str(first_number) + str(second_number)
    print('Пароль: ', rezult)
else:
    print('None')

