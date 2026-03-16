from pandas import DataFrame

def truncate_date(df: DataFrame, datestring: str, datecol: str, ahead: bool) -> None:

    # Take input date string and locate matching row
    row = df.loc[df[datecol] == datestring]

    # Slice df ahead of given date, or before given date.
    if ahead:
        df = df.loc[row.index[0]:]
    else:
        df = df.loc[:row.index[0]]

    return df

