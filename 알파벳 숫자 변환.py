s = input().strip()

for i in s:
  if ord(i) >= 65 and ord(i) <= 90:
    result = ord(i) - 64
  elif ord(i) >= 97 and ord(i) <= 122:
    result = ord(i) - 96
  print(result, end=' ')
