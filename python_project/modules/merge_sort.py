# coding=utf-8
__author__ = 'gaudi8'

import random
import math

# ソートするリストの要素数
NUM = 10


def merge_sort(n, given_list):
  """

  :rtype : list
  """
  if n <= 1:
    return given_list

  m = int(math.ceil(n / 2))
  first_list = merge_sort(m, given_list[:m])
  last_list = merge_sort(n - m, given_list[m:n])

  return_list = []
  while len(first_list) * len(last_list):
    if first_list[0] <= last_list[0]:
      return_list.append(first_list[0])
      first_list.pop(0)
    else:
      return_list.append(last_list[0j])

  if m < n:
    return_list.append(last_list[-1])

  return return_list


# def test(list):
# list = [1,2]
# ソートするリスト
sort = []

for i in range(0, NUM):
  sort.append(random.randint(0, 100))

print(sort)
sort = merge_sort(NUM, sort)
# test(sort)
print(sort)








