from pandas import DataFrame

def truncate_date(df: DataFrame, datestring: str, datecol: str) -> None:

    row = df.loc[df[datecol] == datestring]

    print(row.index)
