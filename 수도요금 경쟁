t = int(input())

for i in range(t):
  p, q, r, s, w = map(int, input().split())
  sum_a, sum_b = 0, 0

  sum_a = p * w
  sum_b = q if w <= r else s * (w - r) + q
  
  result = sum_a if sum_a < sum_b else sum_b

  print(f"#{i + 1} {result}")
