import pandas as pd
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)


def seventh():
    california_data = fetch_california_housing()
    df = pd.DataFrame(california_data.data, columns=california_data.feature_names)

    print(df.info())

    print('----------------------------')

    print(df.isna().sum())

    print('----------------------------')

    filtered_data = df.loc[(df['Population'] > 2500) & (df['HouseAge'] > 50)]
    print(filtered_data)

    print('----------------------------')

    max_median_value = california_data.target.max()
    min_median_value = california_data.target.min()

    print('Макс. значение медианной стоимости дома =', max_median_value)
    print('Мин. значение медианной стоимости дома =', min_median_value)

    print('----------------------------')

    mean_values = df.apply(lambda x: (x.name, x.mean()))
    print(mean_values)

    print('----------------------------')


if __name__ == "__main__":
    seventh()
