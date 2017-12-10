# Задача 1
# Галкин Антон 1 группа 2 курс
# Задача - Вычислите сумму цифр данного натурального числа

def enter():
    number = int(input("Enter the number = "))
    return number

def sum_number(number):
	number = str(number)
	sum = 0
	for ch in number:
		sum = sum + int(ch)
	return sum

def out(number):
	print("Sum of numbers {} = {}".format(number, sum_number(number)))

out(sum_number(enter()))
