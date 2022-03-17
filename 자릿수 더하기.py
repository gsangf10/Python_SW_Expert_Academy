def num_digits(n):
  if n == 0:
    return 0
  while n != 0:
    return 1 + num_digits(n//10)
  return 0;

n = int(input())
sum = 0
for i in range(num_digits(n)-1,-1,-1):
  q = n // (10 ** i)
  n -= q * (10 ** i)
  sum += q
print(sum)
