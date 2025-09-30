import sys
import math

def isValidFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def getCoefficient(prompt, defaultValue = None):
    while True:
        if defaultValue is not None and isValidFloat(defaultValue):
            return float(defaultValue)

        try:
            value = input(prompt)
            if isValidFloat(value):
                return float(value)
            else:
                print("Ошибка! Введите действительное число.")

        except KeyboardInterrupt:
            print("\nВвод прерван. Попробуйте снова.")

def solveBiquadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ["Бесконечное множество решений (x - любое число)"]
            else:
                return ["Нет действительных корней"]
        else:
            x_squared = -c / b
            if x_squared < 0:
                return ["Нет действительных корней"]
            elif x_squared == 0:
                return [0.0]
            else:
                x1 = math.sqrt(x_squared)
                x2 = -x1
                return [x1, x2]

    D = b**2 - 4*a*c

    if D < 0:
        return ["Нет действительных корней"]

    t1 = (-b + math.sqrt(D)) / (2*a)
    t2 = (-b - math.sqrt(D)) / (2*a)

    roots = []

    if t1 >= 0:
        if t1 == 0:
            roots.append(0.0)
        else:
            roots.append(math.sqrt(t1))
            roots.append(-math.sqrt(t1))

    if t2 >= 0 and t2 != t1:
        if t2 == 0:
            if 0.0 not in roots:
                roots.append(0.0)
        else:
            roots.append(math.sqrt(t2))
            roots.append(-math.sqrt(t2))

    if not roots:
        return ["Нет действительных корней"]

    uniqueRoots = sorted(list(set(roots)))
    return uniqueRoots

def main():
    print("Решение биквадратного уравнения: Ax⁴ + Bx² + C = 0")
    print("=" * 50)

    args = sys.argv[1:] 

    a_default = args[0] if len(args) > 0 else None
    b_default = args[1] if len(args) > 1 else None
    c_default = args[2] if len(args) > 2 else None

    a = getCoefficient("Введите коэффициент A: ", a_default)
    b = getCoefficient("Введите коэффициент B: ", b_default)
    c = getCoefficient("Введите коэффициент C: ", c_default)

    print(f"\nУравнение: {a}x⁴ + {b}x² + {c} = 0")

    roots = solveBiquadratic(a, b, c)

    print("\nРезультаты:")
    print("-" * 30)

    if len(roots) == 1 and isinstance(roots[0], str):
        print(roots[0])
    elif roots:
        print(f"Найдено корней: {len(roots)}")
        for i, root in enumerate(roots, 1):
            print(f"x{i} = {root:.6f}")
    else:
        print("Нет действительных корней")

if __name__ == "__main__":
    main()
