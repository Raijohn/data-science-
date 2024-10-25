import pandas as pd
info = {"Name":["bob","jeff","jerry"],"Age":[10,20,30]}
info_df = pd.DataFrame(info)
print(info_df)
print(type(info_df))