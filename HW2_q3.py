import pandas as pd
import numpy as np

data_frame = pd.DataFrame(np.random.randint(10, 40, size=60).reshape(-1, 4))
rows_with_sum_over_100 = data_frame[data_frame.sum(axis=1) > 100]
print(rows_with_sum_over_100)
