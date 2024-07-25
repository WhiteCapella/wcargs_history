import pandas as pd
def read_data():
    df = pd.read_parquet('~/data/parquet')
    return df


def top(cnt, dt):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(cnt)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)
    return r


def count():
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    print(cnt)
