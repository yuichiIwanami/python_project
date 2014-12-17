__author__ = 'gaudi8'

import random

def merge_sort(n, list):
  if n <= 1:
    return

  m = n / 2
  merge_sort(m, list)
  merge_sort(n - m, list + m)

  for i in range(0, m):
    buffer[i] = list[i]

  j = m
  i = k = 0

  while i < m and j < n:
    if buffer[i] <= list[j]:
      list[k] = buffer[i]
    else:
      list[k] = list[j]
    k += 1
    i += 1

  while i < m:
    list[k] = buffer[i]


NUM = 10
# 
sort = []

for i in range(0, NUM):
  sort[i] = random.randint(0, 100)

merge_sort(NUM, sort)








