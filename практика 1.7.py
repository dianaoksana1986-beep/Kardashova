class PhoneBook:
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]
        
    def _hash(self, key: str) -> int:
        hash_value = 0
        prime = 31
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % self.capacity
        return hash_value

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]
        
        for bucket in old_table:
            for k, v in bucket:
                self.add(k, v)

    def add(self, key: str, value: str):
        if self.size / self.capacity > 0.75:
            self._resize()
            
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index][i] = (key, value)
                return
                
        self.table[index].append((key, value))
        self.size += 1

    def get(self, key: str) -> str:
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return "Контакт не знайдено"

    def delete(self, key: str) -> bool:
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                self.size -= 1
                return True
        return False

    def contains(self, key: str) -> bool:
        index = self._hash(key)
        for k, _ in self.table[index]:
            if k == key:
                return True
        return False

    def count(self) -> int:
        return self.size

pb = PhoneBook()
pb.add("Анна", "+380671111111")
pb.add("Іван", "+380932222222")
pb.add("Марія", "+380503333333")

print("\nТестування PhoneBook:")
print("Кількість контактів:", pb.count())
print("Пошук 'Іван':", pb.get("Іван"))
print("Чи є 'Анна'?:", pb.contains("Анна"))
pb.delete("Анна")
print("Чи є 'Анна' після видалення?:", pb.contains("Анна"))
print("Нова кількість контактів:", pb.count())