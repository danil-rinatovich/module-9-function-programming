first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#Основное задание:
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[x]) <= len(second[x]) for x in range(len(first)))
print(list(first_result))
print(list(second_result), '\n')

#Попробовал для себя:
third_result = (len(first[x]) - len(second[x]) for x in range(len(first)) if len(first[x]) != len(second[x]))
fourth_result = (len(x) <= len(y) for x, y in zip(first, second))
print(list(third_result))
print(list(fourth_result))