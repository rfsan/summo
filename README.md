# Summo

Summo is a Python package to summarize a dataset information

```python
import summo
import pandas as pd

df = pd.DataFrame(
    {
        "a": [1, 2, None, 2, None],
        "b": [4, 5, 6, 5, None],
        "c": ["a", "b", None, "d", None],
    }
)
summary = summo.summary(df)
```

`summary` is a `dict` that looks like

```python
{
    "table": {
        "rows": 5,
        "columns": 3,
        "rows_duplicated": 0,
        "rows_all_na_count": 1,
        "rows_all_na_pct": 0.2,
    },
    "columns": {
        "a": {
            "na_count": 2,
            "na_pct": 0.4,
            "unique": False,
            "dtype": "float64",
        },
        "b": {
            "na_count": 1,
            "na_pct": 0.2,
            "unique": False,
            "dtype": "float64",
        },
        "c": {
            "na_count": 2,
            "na_pct": 0.4,
            "unique": False,
            "dtype": "object",
        },
    },
}
```

## Installation

- `pip install summo`