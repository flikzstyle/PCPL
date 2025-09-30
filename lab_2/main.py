#!/usr/bin/env python3

import requests
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = 27

    print("Демонстрация работы с геометрическими фигурами:\n")

    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(rectangle)
    print(circle)
    print(square)

    print("\n" + "="*50)
    print("Демонстрация работы внешнего пакета (requests):")

    # Пример использования внешнего пакета
    try:
        response = requests.get('https://httpbin.org/get', timeout=5)
        print(f"Статус код HTTP запроса: {response.status_code}")
        print("Запрос выполнен успешно!")
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    main()
