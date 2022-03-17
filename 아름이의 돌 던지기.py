t = int(input())
for i in range(t):
  ple_cnt = int(input())
  dist = list(map(int, input().strip().split()))
  result = 100000
  for pi in range(len(dist)):
    dist_abs = abs(dist[pi])
    if result > dist_abs:
      result = dist_abs
  result_cnt = dist.count(result)
  result_cnt += dist.count(result * -1)
  print(f"#{i + 1} {result} {result_cnt}")
