t = int(input())
arr_num = list(map(int, input().split()))

# ver 1
for i in range(t-1, -1, -1):
  for j in range(i):
    if arr_num[j] > arr_num[j+1]:
      arr_num[j], arr_num[j+1] = arr_num[j+1], arr_num[j]

# ver 2
# arr_num.sort()
      
print(arr_num[t//2])
