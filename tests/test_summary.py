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
                "row_count": 4,
                "column_count": 2,
                "rows_duplicated": 1,
                "rows_all_na": 0,
            },
            "columns": {
                "a": {"na_count": 0},
                "b": {"na_count": 0},
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
                "row_count": 5,
                "column_count": 3,
                "rows_duplicated": 0,
                "rows_all_na": 1,
            },
            "columns": {
                "a": {"na_count": 2},
                "b": {"na_count": 1},
                "c": {"na_count": 2},
            },
        },
    ),
]


@pytest.mark.parametrize("df, expected", dataframes)
def test_summary(df, expected):
    result = summo.summary(df)
    assert expected == result
