'''
Sample input
'''
array = [1, 3, -2, 1, 4, -3]
K=2

hash_map = {}
hash_map[0] = [-1]
prefix_sum = 0
for ind in range(0, len(array)):
  prefix_sum += array[ind]
  if prefix_sum - K in hash_map:
    start_list = hash_map[prefix_sum - K]
    for start_index in start_list:
      print start_index+1, ind
  if prefix_sum not in hash_map:
    hash_map[prefix_sum] = [ind]
  #else:
    #start_list2 = hash_map[prefix_sum]
    #start_list2.append(ind)
