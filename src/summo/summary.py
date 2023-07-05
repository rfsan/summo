import pandas as pd
from typing import Any


def summary(df: pd.DataFrame) -> dict[str, Any]:
    rows, columns = df.shape
    rows_all_na_count = df.isna().all(axis=1).sum()
    cols_na_count = df.isna().sum()
    cols_na_pct = cols_na_count / rows
    return {
        "table": {
            "rows": rows,
            "columns": columns,
            "rows_duplicated": df.duplicated().sum(),
            "rows_all_na_count": rows_all_na_count,
            "rows_all_na_pct": rows_all_na_count / rows,
        },
        "columns": pd.concat(
            [cols_na_count, cols_na_pct, df.nunique() == rows, df.dtypes.apply(str)],
            axis=1,
            keys=["na_count", "na_pct", "unique", "dtype"],
        ).to_dict("index"),
    }
