import pandas as pd
import numpy as np

np.random.seed(42)
n = 10000

data = {
    'date_rptd': pd.date_range(start='2020-01-01', periods=n, freq='h'),
    'date_occ': pd.date_range(start='2020-01-01', periods=n, freq='h'),
    'time_occ': np.random.randint(0, 2400, size=n),
    'vict_age': np.random.normal(35, 15, size=n),
    'lat': np.random.normal(34, 1, size=n),
    'lon': np.random.normal(-118, 1, size=n),
    'crm_cd_desc': np.random.choice(['BURGLARY', 'ROBBERY', 'ASSAULT', 'THEFT', 'VANDALISM'], size=n),
    'string_col': np.random.choice([' A ', 'B', ' C', 'D '], size=n)
}

df = pd.DataFrame(data)
# Add some missing values and outliers
df.loc[0:100, 'vict_age'] = np.nan
df.loc[101:200, 'vict_age'] = 150 # Outlier
df.loc[201:300, 'vict_age'] = -10 # Negative age
df.to_csv('crime dataset.csv', index=False)
