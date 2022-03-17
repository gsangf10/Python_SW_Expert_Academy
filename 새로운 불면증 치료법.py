
def num_digits(n):
  if n == 0:
    return 0
  while n != 0:
    return 1 + num_digits(n//10)
  return 0;

t = int(input())
for i in range(t):
  n = int(input())
  check_num = [False] * 10
  x = 0
  while True:
    x += 1
    xn = x * n
    digits = num_digits(xn)
    for j in range(digits - 1,-1,-1):
      num = xn // (10 ** j)
      xn -= num * (10 ** j)
      check_num[num] = True
    if check_num.count(False) == 0:
      break
  print("#{} {}".format(i+1, x*n))
