import numpy as np
import pandas as pd

a = [1.3, 2.2, 2.7, 3.1, 3.3, 3.7]

# q = np.quantile(a, 0.2)
#
# print(a)
# print(q)

df = pd.DataFrame(a)
df.quantile([.1, .25, .5, .75])

print(a)
