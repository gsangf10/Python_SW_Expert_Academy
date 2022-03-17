def is_cal(mm, dd):
  
  if mm == 2:
    if dd >= 1 and dd <= 28:
      return True
  elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    if dd >= 1 and dd <= 30:
      return True
  elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    if dd >= 1 and dd <= 31:
      return True
  else:
    return False
  
  return False

t = int(input())
for i in range(t):
  ymd = input()
  result = ymd[0:4] + '/' + ymd[4:6] + '/' + ymd[6:8] if is_cal(int(ymd[4:6]), int(ymd[6:8])) else -1
  print("#{} {}".format(i+1,result))
