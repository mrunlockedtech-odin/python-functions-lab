import re
# Exercise 1

# def sum_to(n):
#   sum = 0
#   for num in range(1,n+1):
#     sum += num
#   return sum

# print(sum_to(10))

# Exercise 2

# def largest(nums):
#   nums.sort()
#   return nums[-1]
# print(largest([1,2,3,4,0]))
# print(largest([10,4,2,231,91,54]))

# Exercise 3

def occurrences(total_string, sub_string):
  return len(re.findall(sub_string,total_string))
  
print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))