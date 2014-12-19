# coding=utf-8
__author__ = 'gaudi8'

import random
import math

# ソートするリストの要素数
NUM = 10

# ソート関数
def merge_sort(given_list):
  """

  :rtype : list
  """
  given_length = len(given_list)
  if given_length <= 1:
    return given_list

  half_length = int(math.ceil(given_length / 2))
  first_list = merge_sort(given_list[:half_length])
  last_list = merge_sort(given_list[half_length:given_length])

  result_list = []
  while len(first_list) * len(last_list):
    if first_list[0] <= last_list[0]:
      result_list.append(first_list[0])
      first_list.pop(0)
    else:
      result_list.append(last_list[0])
      last_list.pop(0)

  if len(first_list):
    result_list.extend(first_list)
  if len(last_list):
    result_list.extend(last_list)

  return result_list


# def test(list):
# list = [1,2]
# ソートするリスト
sort = []

# ソートするリストの作成
for i in range(0, NUM):
  sort.append(random.randint(0, NUM * 10))

print(sort)
sort = merge_sort(sort)
# test(sort)
print(sort)


