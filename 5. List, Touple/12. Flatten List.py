lst = [[1, 2], [3, 4], [5, 6]]

flatten_lst = []

# for sub_list in lst:
#     for item in sub_list:
#         flatten_lst.append(item)

# import numpy as np
# flatten_lst = np.concatenate(lst).tolist()

flatten_lst = sum(lst, [])

print(flatten_lst)