def sum_to(n):
  sum = 0
  for num in range(1,n+1):
    sum += num
  return sum

print(sum_to(10))