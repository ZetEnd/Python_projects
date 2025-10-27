import sys
from functools import lru_cache

n = int(sys.stdin.readline())
orders = [sys.stdin.readline().strip() for _ in range(n)]
    
# Предварительно вычисляем для каждого заказа:
# (s_odd, s_even) - S в нечётных и чётных позициях при добавлении этого заказа
order_stats = []
for order in orders:
    s_odd = 0
    s_even = 0
    for i in range(len(order)):
        if order[i] == 'S':
            if i % 2 == 0:
                s_odd += 1
            else:
                s_even += 1
    order_stats.append((s_odd, s_even, len(order)))
    
# Мемоизация для перебора всех вариантов
@lru_cache(maxsize=None)
def dfs(pos, used, last_parity):
    if pos == n:
        return 0
        
    max_s = 0
    for i in range(n):
        if not (used & (1 << i)):
            s_odd, s_even, length = order_stats[i]
            if last_parity == 0:  # последний был чётный (Маша)
                added = s_odd
            else:  # последний был нечётный (Вася)
                added = s_even
                
            new_parity = (last_parity + length) % 2
            current = dfs(pos + 1, used | (1 << i), new_parity) + added
            if current > max_s:
                max_s = current

    #print(order_stats)
    #print(orders)
    #return(current)
    return max_s
    
# Начинаем с чётного дня (день 0 - перед первым заказом)
print(dfs(0, 0, 0))