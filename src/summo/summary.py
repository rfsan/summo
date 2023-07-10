import pandas as pd
from typing import Any


def summary(df: pd.DataFrame) -> dict[str, Any]:
    # Table summary
    rows, columns = df.shape
    rows_all_na_count = df.isna().all(axis=1).sum()

    # Column summary
    # all columns
    cols_na_count = df.isna().sum()
    cols_na_pct = cols_na_count / rows
    # numerical columns
    num_cols = df.select_dtypes("number")
    num_agg_funcs = [
        ("median", lambda s: s.quantile(0.5)),
        ("mean", "mean"),
        # ("count", "count"),
    ]
    num_summ = num_cols.groupby([-1] * df.shape[0]).agg(num_agg_funcs)  # type: ignore
    num_summ = num_summ.stack(0).droplevel(0)

    columns_summary = pd.concat(
        [
            cols_na_count.to_frame("na_count"),
            cols_na_pct.to_frame("na_pct"),
            (df.nunique() == rows).to_frame("unique"),
            df.dtypes.apply(str).to_frame("dtype"),
            num_summ,
        ],
        axis=1,
    )
    columns_dict = {
        colname: series.dropna().to_dict() for colname, series in columns_summary.iterrows()
    }

    return {
        "table": {
            "rows": rows,
            "columns": columns,
            "rows_duplicated": df.duplicated().sum(),
            "rows_all_na_count": rows_all_na_count,
            "rows_all_na_pct": rows_all_na_count / rows,
        },
        "columns": columns_dict,
    }
