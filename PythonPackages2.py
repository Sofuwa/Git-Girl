import pandas as pd
import numpy as np
mf = pd.read_csv("movies_metadata - movies_metadata.csv")
mf.head()
mf1 = mf.sort_values('release_date')[[ 'title', 'release_date', 'budget', 'revenue', 'runtime']]
mf1
mf1["revenue"] = pd.to_numeric(mf1["revenue"], errors='err')
mf1[((mf1["revenue"] > 2000000) & (mf1["budget"] < 1000000))]
