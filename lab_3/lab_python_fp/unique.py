class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)

            if self.ignore_case and isinstance(item, str):
                check_item = item.lower()
            else:
                check_item = item

            if check_item not in self.seen:
                self.seen.add(check_item)
                return item

    def __iter__(self):
        return self

if __name__ == "__main__":
    print("Тест 1 - числа:")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data1):
        print(item, end=" ")
    print()

    print("Тест 2 - строки c ignore_case = False:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data2):
        print(item, end=" ")
    print()

    print("Тест 3 - строки с ignore_case = True:")
    for item in Unique(data2, ignore_case = True):
        print(item, end=" ")
    print()
