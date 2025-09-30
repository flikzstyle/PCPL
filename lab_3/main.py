#!/usr/bin/env python3
import os

def main():
    while True:
        print("\n=== МЕНЮ ЛАБОРАТОРНОЙ РАБОТЫ ===")
        print("1. Задача 1 - field.py")
        print("2. Задача 2 - gen_random.py")
        print("3. Задача 3 - unique.py")
        print("4. Задача 4 - sort.py")
        print("5. Задача 5 - print_result.py")
        print("6. Задача 6 - cm_timer.py")
        print("7. Задача 7 - process_data.py")
        print("0. Выход")

        choice = input("\nВыберите задание: ")

        if choice == '1':
            os.system('python3 lab_python_fp/field.py')
        elif choice == '2':
            os.system('python3 lab_python_fp/gen_random.py')
        elif choice == '3':
            os.system('python3 lab_python_fp/unique.py')
        elif choice == '4':
            os.system('python3 lab_python_fp/sort.py')
        elif choice == '5':
            os.system('python3 lab_python_fp/print_result.py')
        elif choice == '6':
            os.system('python3 lab_python_fp/cm_timer.py')
        elif choice == '7':
            os.system('python3 lab_python_fp/process_data.py lab_python_fp/data_light.json')
        elif choice == '0':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
