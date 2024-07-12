"""
1. Сложность алгоритма O(n)
2. Допустимый порог значений переменных от 1 до 1000000. При которых алгоритм работает не более 5 секунд
3. Сложность задачи: 1
4. Затраченное время: 8.3 минуты
"""


def calculate_shares(shares_number: int, shares: list):
    shares_sum = sum(shares) #Считаем сумму всех долей
    for i in range(0, shares_number): #пробегаемся циклом от 0 до кол-ва долей
        print(f'{shares[i]/shares_sum:.3f}') # выводим процентное представление для каждой доли с точностью о 3 знаков



shares_number:int = int(input("Enter shares number > ")) # запрашиваем кол-во долей
shares:list = [float(input("enter share> ")) for i in range(0, shares_number)] # запрашиваем доли и помещаем их сразу в список

# shares_number = 1000000 пороговое значение при котором алгоритм выполняется не более 5 секунд
# shares = [i for i in range(0, shares_number)]

calculate_shares(shares_number, shares) # вызов функции


