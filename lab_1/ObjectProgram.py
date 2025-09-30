import sys
import math

class BiquadraticEquationSolver:

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0

    def isValidFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def getCoefficient(self, prompt, defaultValue = None):
        while True:
            if defaultValue is not None and self.isValidFloat(defaultValue):
                return float(defaultValue)

            try:
                value = input(prompt)
                if self.isValidFloat(value):
                    return float(value)
                else:
                    print("Ошибка! Введите действительное число.")

            except KeyboardInterrupt:
                print("\nВвод прерван. Попробуйте снова.")

    def setCoefficients(self, a_default=None, b_default=None, c_default=None):
        print("Решение биквадратного уравнения: Ax⁴ + Bx² + C = 0")
        print("=" * 50)

        self.a = self.getCoefficient("Введите коэффициент A: ", a_default)
        self.b = self.getCoefficient("Введите коэффициент B: ", b_default)
        self.c = self.getCoefficient("Введите коэффициент C: ", c_default)

    def solve(self):
        a, b, c = self.a, self.b, self.c

        if a == 0:
            return self.solveQuadratic(b, c)

        D = b**2 - 4*a*c

        if D < 0:
            return ["Нет действительных корней"]

        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)

        roots = []

        roots.extend(self._get_roots_from_t(t1))
        roots.extend(self._get_roots_from_t(t2))

        if not roots:
            return ["Нет действительных корней"]

        # Убираем дубликаты и сортируем
        unique_roots = sorted(list(set(roots)))
        return unique_roots

    def solveQuadratic(self, b, c):
        """Решает квадратное уравнение bx² + c = 0"""
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

    def _get_roots_from_t(self, t):
        """Получает корни из значения t (где t = x²)"""
        roots = []
        if t >= 0:
            if t == 0:
                roots.append(0.0)
            else:
                roots.append(math.sqrt(t))
                roots.append(-math.sqrt(t))
        return roots

    def display_results(self, roots):
        print(f"\nУравнение: {self.a}x⁴ + {self.b}x² + {self.c} = 0")
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

def main():
    args = sys.argv[1:]

    a_default = args[0] if len(args) > 0 else None
    b_default = args[1] if len(args) > 1 else None
    c_default = args[2] if len(args) > 2 else None

    solver = BiquadraticEquationSolver()
    solver.setCoefficients(a_default, b_default, c_default)
    roots = solver.solve()
    solver.display_results(roots)

if __name__ == "__main__":
    main()
