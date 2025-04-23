def task_1(num_1, num_2):
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)

task_1(5, 6)


def task_2(num_1, num_2):
    if abs(num_1 - num_2) == 135:
        print('YES')
    else:
        print('NO')

task_2(100,200)


def task_3(num_of_month):
    if num_of_month in (12,1,2):
        print('Зима')
    elif num_of_month in (3,4,5):
        print('Весна')
    elif num_of_month in (6,7,8):
        print('Лето')
    elif num_of_month in (9,10,11):
        print('Осень')
    else:
        print('Введите корректный номер месяца')

task_3(8)


def task_4(num_1, num_2, num_3):
    if num_1 and num_2 and num_3 > 10:
        print('Yes')
    else:
        print('No')

task_4(11,12,13)

def task_5(list_1):
    count = 0
    for num in list_1:
        if num > 0:
            count += 1
    return print(count)
task_5([1,-2,-3,4,-5])
def task_6(num_years,num_months):
    return print(((num_years * 12)+ num_months)* 29)
task_6(12,6)
