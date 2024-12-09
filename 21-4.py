def remove_duplicates(input_list):
    """Видаляє повторювані елементи зі списку."""
    return list(dict.fromkeys(input_list))

def sort_custom(input_list):
    """Сортує список: спочатку числа за зростанням, потім рядки за алфавітом."""
    numbers = sorted([x for x in input_list if isinstance(x, (int, float))])
    strings = sorted([x for x in input_list if isinstance(x, str)])
    return numbers + strings

# Вихідний список
original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'привіт', 'анаконда']

# Видаляємо дублікати
delet_list = remove_duplicates(original_list)
print("Список без повторень:", delet_list)

# Сортуємо за правилами
sorted_list = sort_custom(delet_list)
print("Відсортований список:", sorted_list)
