# -*- coding: utf-8 -*-
"""Testing_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zzJ3OQ_rCPYgbsbHti_ndWbIzHjtfGKP

### Test data for sign_test() and paired_permute() functions:

* Pine_stand data from Lake Louise Field Station in Lowndes County, Georgia.
  * Subset Species column and select dbh vector.
"""

import pandas as pd
from scipy.stats import norm

# If stored on Google Drive (or other path)
# Adjust as required
url = "/content/drive/MyDrive/Resources/Pine_stand.csv"

# To read via pandas DataFrame
df = pd.read_csv(url)

# Extract dbh columns for each subset species as a list.
lob_dbh = df[df["Species"] == "Loblolly pine"].dbh.to_list()
slash_dbh = df[df["Species"] == "Slash pine"].dbh.to_list()

# Actual medians for testing
print("Loblolly median dbh:")
print(df[df["Species"] == "Loblolly pine"].dbh.median())
print("Slash median dbh:")
print(df[df["Species"] == "Slash pine"].dbh.median())

"""* Simulate data from normal distribution.
  * Use this to evaluate paired tests.
"""

# Test data for paired sign test or paired permute
test1 = norm.rvs(size = 10, loc = 5, scale = 1)
test2 = norm.rvs(size = 10, loc = 5, scale = 1)
test3 = norm.rvs(size = 10, loc = 8, scale = 1)

"""#### One sample sign test:"""

sign_test(lob_dbh, md = 45)  # default is "two_sided"
sign_test(lob_dbh, md = 30)

"""### Paired sign test:"""

sign_test(x = test1, y = test2)
sign_test(x = test1, y = test2, alternative = "greater")
sign_test(x = test1, y = test2, alternative = "less")
sign_test(x = test1, y = test3)

"""### Paired permutation test:"""

paired_permute(test1, test2)
paired_permute(test1, test2, alternative = "greater")
paired_permute(test1, test2, alternative = "less")
paired_permute(test1, test2, alternative = "less", nsims = 9999)
paired_permute(test1, test3, alternative = "less")