def odd_nums(my_list):
  for item in my_list:
    if item % 2 == 1:
      print(item)

def divisible_by_ten(nums):
  i = 0
  for num in nums:
    if num % 10 == 0:
      i += 1
  print(i)




odd_nums([4, 7, 9, 10, 13])
divisible_by_ten([20, 25, 30, 35, 40])