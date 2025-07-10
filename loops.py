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

def add_greetings(names):
  name_list = []
  for name in names:
    name_list.append('Hello, ' + name)
  for i in range(len(name_list)):
    print(name_list[i])


def delete_starting_events(my_list):
  while my_list and my_list[0] % 2 == 0:
    my_list.pop(0)
  print(my_list)
  return None


odd_nums([4, 7, 9, 10, 13])
divisible_by_ten([20, 25, 30, 35, 40])
add_greetings(["Bob", "Pete", "Smitty"])
delete_starting_events([4, 8, 10, 11, 12, 15])