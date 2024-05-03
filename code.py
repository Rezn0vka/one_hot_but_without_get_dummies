import pandas as pd
import random
from sklearn.preprocessing import OneHotEncoder
#надеюсь сделал то что нужно
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

encoder = OneHotEncoder(sparse=False)
one_hot_encoded = encoder.fit_transform(data[['whoAmI']])

one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.categories_[0])

data = pd.concat([data, one_hot_df], axis=1)

data.head()
