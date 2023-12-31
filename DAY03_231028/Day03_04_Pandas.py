# 10 minutes to pandas
import numpy as np
import pandas as pd

# Object creation
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype = "int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)

df2.dtypes

df2.<TAB>       # noqa: E225, E999
df2.A
df2.abs

# Viewing data
df.head()

df.tail(3)

df.index

df.columns

df.to_numpy()

df.describe()

df.T

df.sort_index(axis=1, ascending=False)

df.sort_values(by="B")


# Selection
df["A"]
df[0:3]
df["20130102":"20130104"]