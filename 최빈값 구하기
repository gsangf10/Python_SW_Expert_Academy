t = int(input())

for i in range(1,t+1):
  t_num = int(input())
  score = list(map(int, input().strip().split()))
  result = [0, 0]
  count = 0
  for j in range(101):
    count = score.count(j)
    if count >= result[1]:
      result[0], result[1] = j, count
  print("#{} {}".format(t_num,result[0]))
