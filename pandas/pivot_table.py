def pivot_table(data, values=None, index=None, columns=None, aggfunc='mean',
                fill_value=None, margins=False, dropna=True,
                margins_name='All'):
    """
    Create a spreadsheet-style pivot table as a DataFrame. The levels in the
    pivot table will be stored in MultiIndex objects (hierarchical indexes) on
    the index and columns of the result DataFrame
    Parameters
    ----------
    data : DataFrame
    values : column to aggregate, optional
    index : column, Grouper, array, or list of the previous
        If an array is passed, it must be the same length as the data. The list
        can contain any of the other types (except list).
        Keys to group by on the pivot table index.  If an array is passed, it
        is being used as the same manner as column values.
    columns : column, Grouper, array, or list of the previous
        If an array is passed, it must be the same length as the data. The list
        can contain any of the other types (except list).
        Keys to group by on the pivot table column.  If an array is passed, it
        is being used as the same manner as column values.
    aggfunc : function or list of functions, default numpy.mean
        If list of functions passed, the resulting pivot table will have
        hierarchical columns whose top level are the function names (inferred
        from the function objects themselves)
    fill_value : scalar, default None
        Value to replace missing values with
    margins : boolean, default False
        Add all row / columns (e.g. for subtotal / grand totals)
    dropna : boolean, default True
        Do not include columns whose entries are all NaN
    margins_name : string, default 'All'
        Name of the row / column that will contain the totals
        when margins is True.
    Examples
    --------
    >>> df
       A   B   C      D
    0  foo one small  1
    1  foo one large  2
    2  foo one large  2
    3  foo two small  3
    4  foo two small  3
    5  bar one large  4
    6  bar one small  5
    7  bar two small  6
    8  bar two large  7
    >>> table = pivot_table(df, values='D', index=['A', 'B'],
    ...                     columns=['C'], aggfunc=np.sum)
    >>> table
              small  large
    foo  one  1      4
         two  6      NaN
    bar  one  5      4
         two  6      7
    Returns
    -------
    table : DataFrame
    See also
    --------
    DataFrame.pivot : pivot without aggregation that can handle
        non-numeric data
    """
    index = _convert_by(index)
    columns = _convert_by(columns)
