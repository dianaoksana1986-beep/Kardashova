import time
def climb_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)

def climb_iterative(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1

values_of_n = [10, 20, 30, 35]

print("Результати порівняння часу роботи:")
print(f"{'n':<5} | {'Результат':<12} | {'Рекурсивний (сек)':<20} | {'Ітеративний (сек)':<20}")
print("-" * 65)

for n in values_of_n:
    start_rec = time.time()
    res_rec = climb_recursive(n)
    end_rec = time.time()
    time_rec = end_rec - start_rec

    start_iter = time.time()
    res_iter = climb_iterative(n)
    end_iter = time.time()
    time_iter = end_iter - start_iter

    print(f"{n:<5} | {res_iter:<12} | {time_rec:<20.6f} | {time_iter:<20.6f}")