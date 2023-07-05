import pandas as pd
import pytest
import summo


dataframes = [
    (
        pd.DataFrame(
            {
                "a": [1, 2, 3, 2],
                "b": [4, 5, 6, 5],
            }
        ),
        {
            "table": {
                "rows": 4,
                "columns": 2,
                "rows_duplicated": 1,
                "rows_all_na_count": 0,
                "rows_all_na_pct": 0,
            },
            "columns": {
                "a": {"na_count": 0, "na_pct": 0, "unique": False, "dtype": "int64"},
                "b": {"na_count": 0, "na_pct": 0, "unique": False, "dtype": "int64"},
            },
        },
    ),
    (
        pd.DataFrame(
            {
                "a": [1, 2, None, 2, None],
                "b": [4, 5, 6, 5, None],
                "c": ["a", "b", None, "d", None],
            }
        ),
        {
            "table": {
                "rows": 5,
                "columns": 3,
                "rows_duplicated": 0,
                "rows_all_na_count": 1,
                "rows_all_na_pct": 1 / 5,
            },
            "columns": {
                "a": {
                    "na_count": 2,
                    "na_pct": 2 / 5,
                    "unique": False,
                    "dtype": "float64",
                },
                "b": {
                    "na_count": 1,
                    "na_pct": 1 / 5,
                    "unique": False,
                    "dtype": "float64",
                },
                "c": {
                    "na_count": 2,
                    "na_pct": 2 / 5,
                    "unique": False,
                    "dtype": "object",
                },
            },
        },
    ),
]


@pytest.mark.parametrize("df, expected", dataframes)
def test_summary(df, expected):
    result = summo.summary(df)
    assert expected == result
