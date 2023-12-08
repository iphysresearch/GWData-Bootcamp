# Pandas quiz

## 1.

Selecting a single column from a DataFrame returns?

```text
A: Another DataFrame
B: A series
C: A numpy array
D: A list
```

## 2.

What happens when you multiply a DataFrame like df*20?

```text
A: Returns a DataFrame with rows doubled
B: Returns a DataFrame with columns doubled
C: Raises a bad operand type error
D: Returns a DataFrame with element-wise application of df*20
```

## 3.

Which of these commands will sort DataFrame df by column name?


```text
A: df.sort_index()
B: df.sort()
C: df.sort_index(axis=1)
D: df.sort(axis=‘columns’)
```

## 4.

A series is a one-dimensional array which is labelled and can hold any datatype.

```text
A: True
B: False
```

## 5.

Which method iterates over DataFrame columns, returning a tuple with the column name and the content as a Series?

```text
A: iterrows()
B: iteritems()
C: mod()
D: None of the above
```

## 6

How do you convert the datatype of a column ‘x’ in df from an object to an integer?

```text
A: df[‘x’].astype(‘integer’)
B: int(df[‘x’])
C: df[‘x’].int
D: df[‘x’].astype(int)
```

## 7.

By default, the pandas dropna() method returns a new DataFrame and will not change the original.

```text
A: True
B: False
```

## 8.

What is a correct method to discover if a row is a duplicate?

```text
A: df.duplicates()
B: df.duplicate()
C: df.duplicated()
D: df.delete_duplicates()
```

## 9.

```python
import numpy as np

a = np.array([[0, 1, 2], [3, 4, 5]])
b = a.sum(axis=1)
print (b)
```

上面代码的输出结果是？

```text
A: 3
B: 12
C: [3, 12]
D: [3, 5, 7]
E: An exception is thrown
```

## 10.

Given DataFrame df with three columns x, y and z which of these would not return the rows where column x is greater than column y and column y is greater than column z?


```text
A: df.query(‘x>y & y>z’)
B: df.query(‘(x>y)’ & ‘(y>z)’)
C: df.query(‘x>y and y>z’)
D: df.query(‘x>y>z’)
```

## 11.

Index of a DataFrame cannot be non-numeric.


```text
A: True
B: False
```

## 12.

The groupby method on DataFrame is associated with what types of operations?

```text
A: split-align-combine
B: split-apply-combine
C: sort-align-combine
D: sort-apply-collate
```
