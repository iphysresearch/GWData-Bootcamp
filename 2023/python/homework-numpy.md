# Numpy quiz


## 1.

```python
import numpy as np

ary = np.array([1,2,3,5,8])

ary = ary + 1

print (ary[1])
```

上面代码的输出结果是？

```text
A: 1
B: 2
C: 3
D: 4
E: 5
```


## 2.

```python
import numpy as np

a = np.array([1,2,3,5,8])
b = np.array([0,3,4,2,1])
c = a + b
c = c*a

print (c[2])
```

上面代码的输出结果是？

```text
A: 7
B: 12
C: 10
D: 21
E: 28
```

## 3.

```python
import numpy as np

a = np.array([1,2,3,5,8])
print (a.ndim)
```

上面代码的输出结果是？

```text
A: 0
B: 1
C: 2
D: 3
E: 5
```

## 4.

```python
import numpy as np

a = np.array([[1,2,3],[0,1,4]])
print (a.size)
```

上面代码的输出结果是？

```text
A: 0
B: 1
C: 2
D: 5
E: 6
```

## 5.

```python
import numpy as np

a = np.array([[1,2,3],[0,1,4]])
b = np.zeros((2,3), dtype=np.int16)
c = np.ones((2,3), dtype=np.int16)
d = a + b + c
print (d[1,2] )
```

上面代码的输出结果是？

```text
A: 0
B: 1
C: 5
D: 8
E: An exception is thrown
```

## 6.

```python
import numpy as np

a = np.array([1,2,3,4,5])
b = np.arange(0,10,2)
c = a + b
print (c[4])
```

上面代码的输出结果是？

```text
A: 4
B: 5
C: 13
D: 15
E: An exception is thrown
```

## 7.

```python
import numpy as np

a = np.zeros(6)
b = np.arange(0,10,2)
c = a + b
print (c[4])
```

上面代码的输出结果是？

```text
A: 0
B: 2
C: 8
D: 10
E: An exception is thrown
```

## 8.

```python
import numpy as np

a = np.array([[0, 1, 0], [1, 0, 1]])
a += 3
b = a + 3
print (a[1,2] + b[1,2])
```

上面代码的输出结果是？

```text
A: 2
B: 8
C: 11
D: 14
E: An exception is thrown
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

```python
import numpy as np

a = np.array([[0, 1, 2], [3, 4, 5]])
b = a.ravel()
print (b[0,0])
```

上面代码的输出结果是？

```text
A: 0
B: 3
C: 9
D: 10
E: An exception is thrown
```
