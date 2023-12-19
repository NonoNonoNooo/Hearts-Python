# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"

# функція тернарного оператора 
def ternary_operator(x: int, y: int) -> str:
    """
    :param x: int
    :param y: int 
    :return: str
    """
    # Спочатку ми перевіряємо умови з рівностями та нулями,
    # так як через неправильний пріоритет умов у нас будуть невірні відповіді. 
    # Потім ми перевіряємо умови більше-менше, якщо умови з нулями та рівностями не виконуються
    ans = "game over" if x == 0 and y == 0 else (0 if x == y else (x + y if x < y else x - y))

    # Повертає рядок, що представляє ціле число, якщо 'ans' є цілим числом, в іншому випадку повертає 'ans' без змін.
    return str(ans) if isinstance(ans, int) else ans


# Тести
if __name__ == "__main__":
    print(ternary_operator(3, 5))  # Повинно вивести 8
    print(ternary_operator(5, 5))  # Повинно вивести 0
    print(ternary_operator(7, 4))  # Повинно вивести 3
    print(ternary_operator(0, 0))  # Повинно вивести "game over"
