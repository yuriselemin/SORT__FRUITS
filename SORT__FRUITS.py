


# Сортировка фруктов в два списка

favorite_fruits = []
not_favorite_fruits = []

while True:
    fruits = input('Название фрукта: ').lower()  # Приводим ввод к нижнему регистру

    if fruits in ['яблоко', 'груша', 'персик']:
        print('Вы угадали! Это я люблю ')
        favorite_fruits.append(fruits)
        print(f'Список любимых фруктов: \n{favorite_fruits}')
    else:
        print('Нет, спасибо - это не вкусно!')
        not_favorite_fruits.append(fruits)
        print(f'Список  не любимых фруктов: \n{not_favorite_fruits}')

    continue_game = input("Хотите ввести ещё один фрукт? (y/n)")
    if continue_game != 'y':
        break  # Выходим из цикла, если пользователь не хочет продолжать

print(f"Мои нелюбимые фрукты: {not_favorite_fruits}")




