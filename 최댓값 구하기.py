t = int(input())

for i in range(t):
  num = list(map(int, input().split()))
  max_num = 0
  for j in num:
    if j > max_num:
      max_num = j
  print("#{} {}".format(i+1, max_num))
