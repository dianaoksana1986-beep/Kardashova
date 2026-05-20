class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)


def is_palindrome(phrase: str) -> bool:
    clean_chars = [char.lower() for char in phrase if char.isalnum()]
    
    deque = Deque()
    for char in clean_chars:
        deque.add_rear(char)
        
    still_equal = True
    while deque.size() > 1 and still_equal:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            still_equal = False
            
    return still_equal

phrases = [
    "А роза упала на лапу Азора",
    "Привіт, світ!",
    "Я несу гусеня",
    "Racecar"
]

print("\nПеревірка на паліндром:")
for p in phrases:
    print(f"'{p}' -> {is_palindrome(p)}")