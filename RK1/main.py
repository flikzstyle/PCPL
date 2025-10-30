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
    PartManufacturer(1, 1), PartManufacturer(8, 1), PartManufacturer(4, 1), # АвтоВАЗ
    PartManufacturer(2, 2), PartManufacturer(5, 2),                         # ГАЗ
    PartManufacturer(3, 3), PartManufacturer(7, 3),                         # УАЗ
    PartManufacturer(6, 4),                                                 # КАМАЗ
    PartManufacturer(9, 5),                                                 # АЗЛК
    PartManufacturer(1, 2),                                                 # Двигатель ВАЗ-2108 произв на ГАЗ
    PartManufacturer(9, 1),                                                 # Двигатель Москвич-412 произв на АвтоВАЗ
]

def main():
    print('--- Задание Д1 ---')
    
    one_to_many = [
        (p.name, p.price, m.name)
        for p in parts
        for m in manufacturers
        if p.manufacturer_id == m.id
    ]
    
    query1_result = [item for item in one_to_many if 'ВАЗ' in item[0]]
    
    print("Список деталей, содержащих 'ВАЗ' в названии, и их производители:")
    for name, price, manufacturer_name in query1_result:
        print(f'{name} (Цена: {price}) - Производитель: {manufacturer_name}')
    print('\n' + '='*40 + '\n')

    print('--- Задание Д2 ---')

    grouped_prices = {}
    for m in manufacturers:
        prices = [p.price for p in parts if p.manufacturer_id == m.id]
        if prices: 
            grouped_prices[m.name] = prices
            
    avg_prices = [
        (name, sum(prices) / len(prices))
        for name, prices in grouped_prices.items()
    ]
    
    query2_result = sorted(avg_prices, key=lambda item: item[1])
    
    print("Список производителей, отсортированный по средней цене их деталей:")
    for name, avg_price in query2_result:
        print(f'Производитель: {name}, Средняя цена деталей: {avg_price:.2f}')
    print('\n' + '='*40 + '\n')
    
    print('--- Задание Д3 ---')

    parts_by_id = {p.id: p for p in parts}
    manufacturers_by_id = {m.id: m for m in manufacturers}

    filtered_manufacturers = filter(lambda m: m.name.startswith('А'), manufacturers)

    print("Список производителей на 'А' и их детали:")
    for m in filtered_manufacturers:
        part_ids = [pm.part_id for pm in parts_manufacturers if pm.manufacturer_id == m.id]
      
        part_names = [parts_by_id[pid].name for pid in part_ids]
        
        print(f'\nПроизводитель: {m.name}')
        if part_names:
            for part_name in part_names:
                print(f'  - {part_name}')
        else:
            print('  - Деталей не найдено.')
            
if __name__ == '__main__':
    main()