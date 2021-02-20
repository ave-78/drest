import pandas as pd
import numpy as np

# l_1 = []
# for row in range(10):
#     d = {}
#     for col in range(5):
#         d[f'col_{col}'] = col
#     l_1.append(d)
l_2 = [{f'col_{col}': row for col in range(5)} for row in range(10)]
l_3 = l_2

# print(l_1)
print(l_2)
l_3 = pd.DataFrame(l_3)
l_2 = pd.DataFrame(l_2)
l_2['col_1'] = np.NaN
l_3['col_0'] = 10
l_3['col_3'] = 30
l_3['col_4'] = np.NaN
print(l_2)
print(l_3)

