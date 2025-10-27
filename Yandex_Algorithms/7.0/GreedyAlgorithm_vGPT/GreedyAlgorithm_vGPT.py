from collections import defaultdict
import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(10000)
    N, K = map(int, sys.stdin.readline().split())
    bricks = []
    by_color = defaultdict(list)

    for idx in range(N):
        L, C = map(int, sys.stdin.readline().split())
        bricks.append((L, C, idx))
        by_color[C].append((L, idx))

    # Переберем возможные ширины w от 1 до 5000
    # и найдем такую, что для каждого цвета можно набрать w
    max_sum = sum(l for l, _, _ in bricks)
    for target_w in range(1, max_sum // 2 + 1):
        first_wall = []
        used = set()
        ok = True

        for color in range(1, K + 1):
            arr = by_color[color]
            n = len(arr)
            dp = [None] * (target_w + 1)
            dp[0] = []
            for l, idx in arr:
                for s in range(target_w, l - 1, -1):
                    if dp[s - l] is not None and dp[s] is None:
                        dp[s] = dp[s - l] + [idx]
            if dp[target_w] is None:
                ok = False
                break
            else:
                first_wall.extend(dp[target_w])
                used.update(dp[target_w])

        if ok:
            # теперь пытаемся построить вторую стену такой же ширины из оставшихся кирпичей
            second_ok = True
            second_wall = []
            for color in range(1, K + 1):
                arr = [x for x in by_color[color] if x[1] not in used]
                dp = [None] * (target_w + 1)
                dp[0] = []
                for l, idx in arr:
                    for s in range(target_w, l - 1, -1):
                        if dp[s - l] is not None and dp[s] is None:
                            dp[s] = dp[s - l] + [idx]
                if dp[target_w] is None:
                    second_ok = False
                    break
                else:
                    second_wall.extend(dp[target_w])

            if second_ok:
                print("YES")
                print(' '.join(str(i + 1) for i in first_wall))
                return

    print("NO")

threading.Thread(target=main).start()

