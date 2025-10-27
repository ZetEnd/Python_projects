import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.max_tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        # Строим дерево
        for i in range(self.n):
            self.max_tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[2 * i], self.max_tree[2 * i + 1])

    def _apply(self, v, val):
        self.max_tree[v] += val
        if v < self.size:  # Не лист
            self.lazy[v] += val

    def _push(self, v):
        self._apply(2 * v, self.lazy[v])
        self._apply(2 * v + 1, self.lazy[v])
        self.lazy[v] = 0

    def _add(self, l, r, val, x, lx, rx):
        if r < lx or l > rx:
            return
        if l <= lx and rx <= r:
            self._apply(x, val)
            return
        self._push(x)
        m = (lx + rx) // 2
        self._add(l, r, val, 2 * x, lx, m)
        self._add(l, r, val, 2 * x + 1, m + 1, rx)
        self.max_tree[x] = max(self.max_tree[2 * x], self.max_tree[2 * x + 1])

    def add(self, l, r, val):
        self._add(l, r, val, 1, 0, self.size - 1)

    def _max_query(self, l, r, x, lx, rx):
        if r < lx or l > rx:
            return -float('inf')
        if l <= lx and rx <= r:
            return self.max_tree[x]
        self._push(x)
        m = (lx + rx) // 2
        s1 = self._max_query(l, r, 2 * x, lx, m)
        s2 = self._max_query(l, r, 2 * x + 1, m + 1, rx)
        return max(s1, s2)

    def query(self, l, r):
        return self._max_query(l, r, 1, 0, self.size - 1)


# Чтение ввода
N = int(input())
A = list(map(int, input().split()))
M = int(input())

# Создаем дерево
st = SegmentTree(A)
res = []

for _ in range(M):
    parts = input().split()
    if parts[0] == 'a':
        l, r, x = map(int, parts[1:])
        st.add(l - 1, r - 1, x)
    elif parts[0] == 'm':
        l, r = map(int, parts[1:])
        res.append(str(st.query(l - 1, r - 1)))

print(' '.join(res))
