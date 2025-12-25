import unittest

class Manufacturer:
    """Производитель"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'Manufacturer({self.id}, "{self.name}")'


class Part:
    """Деталь"""
    def __init__(self, id, name, price, manufacturer_id):
        self.id = id
        self.name = name
        self.price = price
        self.manufacturer_id = manufacturer_id

    def __repr__(self):
        return f'Part({self.id}, "{self.name}", {self.price}, {self.manufacturer_id})'


class PartManufacturer:
    """
    'Детали производителя' для реализации связи многие-ко-многим
    """
    def __init__(self, part_id, manufacturer_id):
        self.part_id = part_id
        self.manufacturer_id = manufacturer_id


# Инициализация данных
def init_data():
    """Инициализация тестовых данных"""
    manufacturers = [
        Manufacturer(1, 'АвтоВАЗ'),
        Manufacturer(2, 'ГАЗ'),
        Manufacturer(3, 'УАЗ'),
        Manufacturer(4, 'КАМАЗ'),
        Manufacturer(5, 'АЗЛК'),
    ]

    parts = [
        Part(1, 'Двигатель ВАЗ-2108', 50000, 1),
        Part(2, 'Коробка передач ГАЗель', 75000, 2),
        Part(3, 'Мост УАЗ-Патриот', 90000, 3),
        Part(4, 'Поршень ВАЗ-2108', 2000, 1),
        Part(5, 'Рама ГАЗ-66', 120000, 2),
        Part(6, 'Турбина КАМАЗ', 65000, 4),
        Part(7, 'Редуктор УАЗ', 30000, 3),
        Part(8, 'Карбюратор ВАЗ', 5000, 1),
        Part(9, 'Двигатель Москвич-412', 45000, 5),
    ]

    parts_manufacturers = [
        PartManufacturer(1, 1), PartManufacturer(8, 1), PartManufacturer(4, 1),  # АвтоВАЗ
        PartManufacturer(2, 2), PartManufacturer(5, 2),                          # ГАЗ
        PartManufacturer(3, 3), PartManufacturer(7, 3),                          # УАЗ
        PartManufacturer(6, 4),                                                  # КАМАЗ
        PartManufacturer(9, 5),                                                  # АЗЛК
        PartManufacturer(1, 2),                                                  # Двигатель ВАЗ-2108 произв на ГАЗ
        PartManufacturer(9, 1),                                                  # Двигатель Москвич-412 произв на АвтоВАЗ
    ]
    
    return manufacturers, parts, parts_manufacturers


# Запрос 1: Детали с "ВАЗ" в названии
def get_parts_with_vaz(manufacturers, parts):
    """Получить список деталей, содержащих 'ВАЗ' в названии, и их производителей"""
    one_to_many = [
        (p.name, p.price, m.name)
        for p in parts
        for m in manufacturers
        if p.manufacturer_id == m.id
    ]
    
    return [item for item in one_to_many if 'ВАЗ' in item[0]]


# Запрос 2: Производители отсортированные по средней цене деталей
def get_manufacturers_sorted_by_avg_price(manufacturers, parts):
    """Получить список производителей, отсортированный по средней цене их деталей"""
    grouped_prices = {}
    for m in manufacturers:
        prices = [p.price for p in parts if p.manufacturer_id == m.id]
        if prices: 
            grouped_prices[m.name] = prices
            
    avg_prices = [
        (name, sum(prices) / len(prices))
        for name, prices in grouped_prices.items()
    ]
    
    return sorted(avg_prices, key=lambda item: item[1])


# Запрос 3: Производители на букву 'А' и их детали
def get_manufacturers_starting_with_a(manufacturers, parts, parts_manufacturers):
    """Получить список производителей на 'А' и их детали"""
    parts_by_id = {p.id: p for p in parts}
    
    filtered_manufacturers = filter(lambda m: m.name.startswith('А'), manufacturers)
    
    result = []
    for m in filtered_manufacturers:
        part_ids = [pm.part_id for pm in parts_manufacturers if pm.manufacturer_id == m.id]
        part_names = [parts_by_id[pid].name for pid in part_ids]
        
        result.append({
            'manufacturer': m.name,
            'parts': part_names
        })
    
    return result


# Основная функция
def main():
    manufacturers, parts, parts_manufacturers = init_data()
    
    print('='*60)
    print('ПРОГРАММА ПОГРАНИЧНОГО КОНТРОЛЯ №1')
    print('='*60)
    
    print('\n--- Задание Д1 ---')
    query1_result = get_parts_with_vaz(manufacturers, parts)
    print("Список деталей, содержащих 'ВАЗ' в названии, и их производители:")
    for name, price, manufacturer_name in query1_result:
        print(f'  {name} (Цена: {price}) - Производитель: {manufacturer_name}')
    
    print('\n--- Задание Д2 ---')
    query2_result = get_manufacturers_sorted_by_avg_price(manufacturers, parts)
    print("Список производителей, отсортированный по средней цене их деталей:")
    for name, avg_price in query2_result:
        print(f'  Производитель: {name}, Средняя цена деталей: {avg_price:.2f}')
    
    print('\n--- Задание Д3 ---')
    query3_result = get_manufacturers_starting_with_a(manufacturers, parts, parts_manufacturers)
    print("Список производителей на 'А' и их детали:")
    for item in query3_result:
        print(f'\n  Производитель: {item["manufacturer"]}')
        if item['parts']:
            for part_name in item['parts']:
                print(f'    - {part_name}')
        else:
            print('    - Деталей не найдено.')
    
    print('\n' + '='*60)


# ============================================================================
# МОДУЛЬНЫЕ ТЕСТЫ (TDD подход)
# ============================================================================

class TestBorderControlProgram(unittest.TestCase):
    """Тесты для программы пограничного контроля"""
    
    def setUp(self):
        """Инициализация тестовых данных перед каждым тестом"""
        self.manufacturers, self.parts, self.parts_manufacturers = init_data()
    
    def test_get_parts_with_vaz(self):
        """Тест 1: Проверка поиска деталей с 'ВАЗ' в названии"""
        # Действие
        result = get_parts_with_vaz(self.manufacturers, self.parts)
        
        # Проверки
        self.assertGreater(len(result), 0, "Должны быть найдены детали с 'ВАЗ' в названии")
        
        for name, price, manufacturer in result:
            self.assertIn('ВАЗ', name, f"Деталь '{name}' должна содержать 'ВАЗ' в названии")
            self.assertGreater(price, 0, f"Цена детали '{name}' должна быть положительной")
        
        # Ожидаем 4 детали с 'ВАЗ' в названии
        expected_names = ['Двигатель ВАЗ-2108', 'Поршень ВАЗ-2108', 'Карбюратор ВАЗ']
        result_names = [name for name, price, manufacturer in result]
        
        for expected_name in expected_names:
            self.assertIn(expected_name, result_names, 
                         f"Деталь '{expected_name}' должна быть в результатах")
    
    def test_get_manufacturers_sorted_by_avg_price(self):
        """Тест 2: Проверка сортировки производителей по средней цене"""
        # Действие
        result = get_manufacturers_sorted_by_avg_price(self.manufacturers, self.parts)
        
        # Проверки
        self.assertEqual(len(result), 5, "Должны быть представлены все 5 производителей")
        
        # Проверяем сортировку по возрастанию
        prices = [avg_price for name, avg_price in result]
        self.assertEqual(prices, sorted(prices), "Список должен быть отсортирован по возрастанию")
        
        # Проверяем правильность вычисления средней цены
        for name, avg_price in result:
            manufacturer = next(m for m in self.manufacturers if m.name == name)
            manufacturer_parts = [p for p in self.parts if p.manufacturer_id == manufacturer.id]
            
            if manufacturer_parts:  # только если есть детали
                expected_avg = sum(p.price for p in manufacturer_parts) / len(manufacturer_parts)
                self.assertAlmostEqual(avg_price, expected_avg, places=2,
                                      msg=f"Некорректная средняя цена для {name}")
    
    def test_get_manufacturers_starting_with_a(self):
        """Тест 3: Проверка поиска производителей на букву 'А'"""
        # Действие
        result = get_manufacturers_starting_with_a(
            self.manufacturers, self.parts, self.parts_manufacturers
        )
        
        # Проверки
        self.assertEqual(len(result), 2, "Должны быть найдены 2 производителя на букву 'А'")
        
        manufacturer_names = [item['manufacturer'] for item in result]
        self.assertIn('АвтоВАЗ', manufacturer_names, "Должен быть найден АвтоВАЗ")
        self.assertIn('АЗЛК', manufacturer_names, "Должен быть найден АЗЛК")
        
        # Проверяем детали АвтоВАЗ
        avtovaz = next(item for item in result if item['manufacturer'] == 'АвтоВАЗ')
        self.assertGreater(len(avtovaz['parts']), 0, "У АвтоВАЗ должны быть детали")
        
        # Проверяем, что есть хотя бы одна ожидаемая деталь
        expected_parts = ['Двигатель ВАЗ-2108', 'Карбюратор ВАЗ', 'Поршень ВАЗ-2108']
        has_expected = any(part in avtovaz['parts'] for part in expected_parts)
        self.assertTrue(has_expected, "У АвтоВАЗ должна быть хотя бы одна ожидаемая деталь")


class TestEdgeCases(unittest.TestCase):
    """Тесты граничных случаев"""
    
    def test_empty_data(self):
        """Тест с пустыми данными"""
        empty_manufacturers = []
        empty_parts = []
        empty_pm = []
        
        # Тест 1
        result1 = get_parts_with_vaz(empty_manufacturers, empty_parts)
        self.assertEqual(result1, [], "При пустых данных должен возвращаться пустой список")
        
        # Тест 2
        result2 = get_manufacturers_sorted_by_avg_price(empty_manufacturers, empty_parts)
        self.assertEqual(result2, [], "При пустых данных должен возвращаться пустой список")
        
        # Тест 3
        result3 = get_manufacturers_starting_with_a(empty_manufacturers, empty_parts, empty_pm)
        self.assertEqual(result3, [], "При пустых данных должен возвращаться пустой список")
    
    def test_no_vaz_parts(self):
        """Тест, когда нет деталей с 'ВАЗ' в названии"""
        manufacturers = [Manufacturer(1, 'Test')]
        parts = [
            Part(1, 'Двигатель Test', 10000, 1),
            Part(2, 'Коробка передач', 20000, 1),
        ]
        
        result = get_parts_with_vaz(manufacturers, parts)
        self.assertEqual(len(result), 0, "Если нет деталей с 'ВАЗ', должен быть пустой список")
    
    def test_no_manufacturers_starting_with_a(self):
        """Тест, когда нет производителей на букву 'А'"""
        manufacturers = [
            Manufacturer(1, 'Test1'),
            Manufacturer(2, 'Test2'),
            Manufacturer(3, 'Test3'),
        ]
        parts = [Part(1, 'Test Part', 1000, 1)]
        parts_manufacturers = [PartManufacturer(1, 1)]
        
        result = get_manufacturers_starting_with_a(manufacturers, parts, parts_manufacturers)
        self.assertEqual(len(result), 0, "Если нет производителей на 'А', должен быть пустой список")


# ============================================================================
# ЗАПУСК ПРОГРАММЫ И ТЕСТОВ
# ============================================================================

if __name__ == '__main__':
    import sys
    
    # Если переданы аргументы командной строки для тестов
    if len(sys.argv) > 1 and 'test' in sys.argv[1]:
        # Запускаем тесты
        print("Запуск модульных тестов...")
        print("="*60)
        unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
        print("="*60)
        print("Тестирование завершено!")
    else:
        # Запускаем основную программу
        main()
        
        # После основной программы показываем возможность запуска тестов
        print("\nДля запуска тестов выполните: python border_control_tdd.py test")