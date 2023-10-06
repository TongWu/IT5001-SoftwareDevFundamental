

| Data Type | iterable | mutable | indexable | hashable |
| --------- | -------- | ------- | --------- | -------- |
| int       | No       | No      | No        | Yes      |
| float     | No       | No      | No        | Yes      |
| str       | Yes      | No      | Yes       | Yes      |
| tuple     | Yes      | No      | Yes       | Yes      |
| list      | Yes      | Yes     | Yes       | No       |
| set       | Yes      | Yes     | No        | No       |
| dict      | Yes      | Yes     | Yes       | No       |



## Built-in Functions

`round()` 函数在Python中对浮点数进行四舍五入时，遵循了称为“银行家舍入”或“偶数舍入”的规则。

当一个数正好位于两个整数之间时（例如 2.5，位于 2 和 3 之间），这种规则指定应舍入到最近的偶数。这种舍入方式的好处是，在多次舍入运算时可以避免总体的累积偏差。



## 逻辑运算和计算

- `or`运算符返回第一个为`True`的操作数（即非零值）
  - 例如`bool(4) + int(True) or float(False)`,`bool(4)+int(True)=2`,则`or`会返回2

- 逻辑运算符（如 `or`）是短路求值的。这意味着如果左边的操作数已经确定了整个表达式的值，那么右边的操作数就不会被评估。
  - 例如 `1>1+1 or 3>7-6 or 6>7/0` ，第二个操作数为True，那么python不会计算之后的操作数，所以不会识别到ZeroDivisionError：
- 逻辑运算符中，`and`的运算顺序要优于`or`

- `11&4`: 这个表达式使用了按位与运算符 `&` 来计算两个整数 11 和 4 的二进制按位与结果。 `1011 & 0100 = 0000 = 0`
- 在多重比较时, 会从左到右进行评估
  - 例如`False == True == False`，其实是`False == True and True == False`
- 连续的正负号会按照它们的顺序进行评估。每个`+`操作符不改变数的正负性，而每个`-`操作符会翻转数的正负性。
  - 例如`9-+-+-+-9`,第一个`-`将`9`变为`-9`,每个`+`不改变数值,之后的每个`-`翻转数字的正负性，所以最终是`9+9=18`




## List

复杂的list表达式例子：

1. `[ 5, [3], [2, 3] ] [ [2,[1]] [1] ] [ :[1,2][1] ]`, 即三个部分: `[5, [3], [2, 3]]`, `[[2,[1]] [1]]`, `[:[1,2][1]]`
   - 第二个部分: `[[2,[1]] [1]]`，即是`[2,[1]]`的第二个元素，所以返回`[[1]]`
   - 第三个部分: `[:[1,2][1]]`, 即是`[:2]`
   - 然而`[5, [3], [2, 3]][[1]]`不合法，所以此表达式会抛出错误
2. `[ 5, [3], [2, 3] ] [ [2,[1]] [0] ] [ :[1,2][1] ]`
   - 第二个部分: `[[2,[1]] [0]]`，即是`[2,[1]]`的第一个元素，所以返回`[2]`
   - 其余和第一个例子相同
   - `[5, [3], [2, 3]][2]`为`[2,3]`
   - `[2,3][:2]`为`[2]`，此为答案

- 当创建一个对象（例如列表）并将其赋值给一个变量时，该变量实际上只是一个指向对象的引用，而不是对象本身。这意味着，当你在函数中修改一个可变对象（如列表、字典或集合）时，你实际上是修改了该对象的内容，而不是引用。也就是说，函数内可以修改函数外的list。



## Dictionary

- 不能在迭代过程中修改正在迭代的容器的大小或结构，但可以修改字典中现有键的值。在您给出的代码中，您试图在迭代字典`a`的过程中删除其键。这会导致一个运行时错误。
- 如果在插入键值对时，键已经存在；那么此键对应的值会被覆写为新的值

- `set` (e.g., `d[k] = v`)：设置一个键值对 - O*(1)
- `get` (e.g., `d[k]`)：获取一个键的值 - O(1)
- `del`：删除一个键值对 - O(1)
- `in`：检查键是否存在 - *O*(1)
- `len`：返回键值对数量 - *O*(1)
- `keys`：返回所有键 - *O*(*n*)
- `values`：返回所有值 - *O*(*n*)
- `items`：返回所有键值对 - *O*(*n*)
- 当你将一个字典转换为列表时`list(dict)`，Python实际上是将字典的**键**转换为列表。
  - `list({1:2, 3:4})`的输出为[1,3]




## `map()` & `filter()`

- map和filter函数都返回一个可迭代的对象，只能读取一次



## Lambda Function

- Lambda函数的输入如果在for loop中，那么他只会捕获for loop的最终值
  - 例如`lambda x: i + x for i in range(3)`，此处的i只会是3
- 



## OOP

- 当一个类使用了多重继承时，那么`__init__`函数会调用在括号内的第一个父类的`__init__`函数
  - 例如`class Paladin(Fighter, Cleric)`, 如果`Paladin`类中要打印一个`self`对象的值，那么这个值是继承自`Fighter`父类



## Read File

| Modes | Description                                                  |
| ----- | ------------------------------------------------------------ |
| r     | Opens a file for **reading only**. The file pointer is placed at the beginning of the file. This is the **default mode** |
| rb    | Opens a file for reading only in **binary format**. The file pointer is placed at the beginning of the file. This is the default mode. |
| r+    | Opens a file for **both reading and writing**. The file pointer placed at the beginning of the file. |
| rb+   | Opens a file for both reading and writing in **binary format**. The file pointer placed at the beginning of the file. |
| w     | Opens a file for **writing only**. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. |
| wb    | Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. |
| w+    | Opens a file for **both writing and reading**. Overwrites the file if the file exists. If the file does not exist, creates a new file for reading and writing. |
| wb+   | Opens a file for both writing and reading in **binary format**. Overwrites the file if the file exists. If the file does not exist, creates a new file for reading and writing. |
| a     | Open a file for **appending**. The file pointer is at the **end of the file** if the file exists. That is, the file is in append mode. If the file does not exist, it creates a new file for writing |
| ab    | Open a file for **appending in binary format**. The file pointer is at the **end of the file** if the file exists. That is, the file is in append mode. If the file does not exist, it creates a new file for writing |
| a+    | Open a file for **appending and reading**. The file pointer is at the **end of the file** if the file exists. That is, the file is in append mode. If the file does not exist, it creates a new file for reading and writing |
| ab+   | Open a file for **appending and reading in binary format**. The file pointer is at the **end of the file** if the file exists. That is, the file is in append mode. If the file does not exist, it creates a new file for reading and writing |

 

## Time complexity

1. **Bubble Sort**:
   - **最优情况**：*O*(*n*) — 当输入数组已经是排序好的状态时。
   - **最坏情况**：*O*(*n*2) — 当输入数组是逆序的时候。
2. **Merge Sort**:
   - **最优情况**：*O*(*n*log*n*) — 这是在所有情况下的时间复杂度，因为合并排序总是将列表分为两半，然后合并这些部分。
   - **最坏情况**：*O*(*n*log*n*) — 同上。
3. **Breadth-First Search (BFS)**:
   - **最优情况**：*O*(1) — 当起始节点就是目标节点时。
   - **最坏情况**：*O*(*V*+*E*) — 其中 V 是顶点数，E 是边数。
4. **Depth-First Search (DFS)**:
   - **最优情况**：*O*(1) — 当起始节点就是目标节点时。
   - **最坏情况**：*O*(*V*+*E*) — 其中 V 是顶点数，E 是边数。
5. **Dijkstra's Algorithm**:
   - **最优情况**：与最坏情况相同，因为 Dijkstra 总是考虑所有的边和节点。
   - **最坏情况**：当使用简单的数组/列表作为优先队列时：*O*(*V*2)；当使用堆或者优先队列数据结构时：*O*(*V*log*V*+*E*log*V*)。

| Algorithm   | Best Case    | Worst Case                               |
| ----------- | ------------ | ---------------------------------------- |
| Bubble Sort | $O(n)$       | $O(n^2)$                                 |
| Merge Sort  | $O(nlog\ n)$ | $O(nlog\ n)$                             |
| BFS         | $O(1)$       | $O(V+E)$, V for node num, E for edge num |
| DFS         | $O(1)$       | $O(V+E)$                                 |
| Dijkstra    | $O(V^2)$     | $O(V^2)$                                 |

### Deep Count

```python
def deepcount(seq):
	if seq == []:
		return 0
	elif type(seq) != list:
		return 1
	else:
		return deepcount(seq[0]) + deepcount(seq[1:])
```

### Deep Map

```python
def deepMap(func,seq):
	if seq == []:
		return seq
	elif type(seq) != list
		return func(seq)
	else:
		return [deepSquare(func,seq[0])] + deepSquare(func,seq[1:])
```

### **Change list to tuple deeply**

```python
def deep_tuple(s):
	if not isinstance(s, list): return s
	return tuple(deep_tuple(i) for i in s)
```

### Flatten

```python
def flatten(seq):
	if seq == []:
		return seq
	elif type(seq) != list:
		return [seq]
	else:
		return flatten(seq[0]) + flatten(seq[1:])
```

| Type of Exception | Description                                            |
| ----------------- | ------------------------------------------------------ |
| NameError         | If an identifier is used before assignment             |
| TypeError         | If wrong type of parameter is sent to a function       |
| ValueError        | If function parameter has invalid value (Eg: log(-1) ) |
| ZeroDivisionError | If 0 is used as divisor                                |
| StopIteration     | Raised by next(iter)                                   |
| IndexError        | If index is out of bound for a sequence                |
| KeyError          | If non-existent key is requested for set or dictionary |
| IOError           | If I/O operation fails (Eg: opening a file)            |
| EOFError          | If end of file is reached for console of file input    |
| AttributeError    | If an undefined attribute of an object is used         |