import pandas as pd
import numpy as np

PATH_CSV = 'https://raw.githubusercontent.com/edlich/eternalrepo/' \
           'master/DS-WAHLFACH/dsm-beuth-edl-demodata-dirty.csv'

# Read data from source into dataframe
df = pd.read_csv(PATH_CSV)

# Display first 5 rows
print(df.head())

# Display first row to see detailed information
print(df.iloc[0])

# There are some entries with missing email addresses
print(df.email)

# Assuming that an entry without email address is not useful,
# all entries without it will be dropped.
# Therefore, empty email strings are converted to NaNs.
df.email.replace('', np.nan, inplace=True)
df.dropna(subset=['email'], inplace=True)

# Remove duplicates by email address
df.drop_duplicates(subset=['email'], ignore_index=True, inplace=True)

# Check if the given ages have a proper format or range.
print(pd.unique(df.age))

# The ages are given as strings. It should be numeric.
# Rows with improper ages will be kept as NaN.
df.age = pd.to_numeric(df.age, errors='coerce', downcast='float')
df.age = df.age.loc[(df.age > 0) & (df.age < 110)]  # False is interpreted as NaN

# Check gender column: It looks nice except one NaN.
# Let's change it to 'Unknown'. So NaNs won't be bothering.
print(pd.value_counts(df.gender, dropna=False))
df.gender.fillna('Unknown', inplace=True)

# There is an id missing
print(df[pd.isna(df.id)])

# Data without id are still useful. We also have dropped some rows.
# So the id column can be dropped:
df.drop(columns=['id'], inplace=True)

# The cleaned dataframe looks like this:
# It still contains a few NaNs in the age column and
# contains 19 rows.
print(df)
