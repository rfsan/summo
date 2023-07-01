import pandas as pd


def summary(df: pd.DataFrame):
    return {
        "table": {
            "row_count": df.shape[0],
            "column_count": df.shape[1],
            "rows_duplicated": df.duplicated().sum(),
            "rows_all_na": df.isna().all(axis=1).sum(),
        },
        "columns": pd.concat(
            [df.isna().sum()],
            axis=1,
            keys=["na_count"],
        ).to_dict("index"),
    }
