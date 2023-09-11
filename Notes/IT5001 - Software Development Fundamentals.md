# IT5001 - Software Development Fundamentals

## 0. Introductions

### 0.1 Software Development

![image-20230911144254896](https://images.wu.engineer/images/2023/09/11/image-20230911144254896.png)

- Programming languages provide tools to:
  1. Build data structures
  2. Do reasoning
- Representations
  - Numbers, Strings, Arrays, Multi-dimensional arrays, Graphs, Trees

### 0.2 Algorithm

- An **Algorithm** is a well-defined computational procedure consisting of **a set of instructions**, that takes some value or set of values as **input**, and produces some value or set of values as **output**.
- The desired I/O relationship is specified by the statement of the **computational problem** for which the algorithm is designed.
- An algorithm is **correct** if, *for every input*, it **halts** with the correct output.

![image-20230911144644686](https://images.wu.engineer/images/2023/09/11/image-20230911144644686.png)

> 算法是一个被明确定义的计算过程。它将一组输入值转换为一组新的输出值。
>
> 期望的输入输出关系由设计算法的计算问题所声明指定。
>
> 对于每个输入，都能以正确的输出作为停止，则算法是正确的。

#### **Representing Algorithm**

1. Flowchart
2. Pseudo-code

![image-20230911144821860](https://images.wu.engineer/images/2023/09/11/image-20230911144821860.png)

> Algorithms are **ideas**, program is the **final code on a machine**.

## 1. Python and Basic Types

### 1.1 Introduction to Built-in Types

![image-20230911145105876](https://images.wu.engineer/images/2023/09/11/image-20230911145105876.png)

![image-20230911145144304](https://images.wu.engineer/images/2023/09/11/image-20230911145144304.png)

> immutable = cannot been modified 变量被赋值后不可以被修改
>
> primitive types = original types 原始变量

> 在python中，不存在primitive types这一概念，但是在其他语言例如C++中存在primitive types。这些数据类型是语言本身提供的，不是由用户自由定义的数据结构。例如int, long, char, bool, void, float等。
>
> 在python中，这一概念通常被built-in types所包含

### 1.2 Numbers: Numeric Types

- Integers: `int`
- Floats: `float`
  - `float` stores real numbers as binary fractions
  - 64-bit double precision

```python
>>> 2
2
>>> type(2)
<class 'int'>
>>> 2.0
2.0
>>> type(2.0)
<class 'float'>
```

> `a = 0x1a` 这是16进制，属于`int`类型
>
> `b =  0b1010` 这是2进制，属于`int`类型
>
> `c = 2.5e3` 这是科学计数法，等于`2.5*10^3=2500.0`。属于`float`类型
>
> 由于浮点数的舍入误差，对 `float` 进行算术操作时需要小心。比如 `0.1 + 0.2` 在许多系统上并不等于 `0.3`，而是接近这个值的一个稍微不同的浮点数。

### 1.3 Boolean Type

![image-20230911151419691](https://images.wu.engineer/images/2023/09/11/image-20230911151419691.png)

> 以上内容介绍了真值测试。
>
> **真值测试**：在Python中，几乎任何对象都可以进行真值测试，以确定其是否可以解释为`True`或`False`。
>
> - 所有非零的数字都被认为是`True`。
> - 任何非空的对象，如字符串、列表、字典等，都被认为是`True`。
> - 常见的被解释为`False`的值有：`None`、`0`、`0.0`、`0j`、`""`（空字符串）以及`[]`、`()`、`{}`（空的容器）等。

### 1.4 Identifiers (Variable Names)

- User-defined names for objects, can enhance readability

- Rules:

  - First character should be an alphabet or underscore(\_)
  - Other characters can be numbers and underscore
  - Special characters are not allowed
  - Names are **case sensitive**

  ![image-20230911152057055](https://images.wu.engineer/images/2023/09/11/image-20230911152057055.png)

### 1.5 Multiple Assignment

![image-20230911152125356](https://images.wu.engineer/images/2023/09/11/image-20230911152125356.png)

### 1.6 Keywords

![image-20230911152243220](https://images.wu.engineer/images/2023/09/11/image-20230911152243220.png)

- Keyword cannot be name of variables

### 1.7 Operators

#### Arithmetic Operators

![image-20230911152402632](https://images.wu.engineer/images/2023/09/11/image-20230911152402632.png)

**Mixed mode arithmetic**

```python
>>> 2 + 3.0
5.0
```

- There are narrower and wider types
  - Float is wider (more general than integer)
  - Since all integers is floats, but not vice-versa
- Narrower types is promoted to wider type
  - Integer is promoted to float

#### Comparison Operators

![image-20230911152714292](https://images.wu.engineer/images/2023/09/11/image-20230911152714292.png)

> 比较运算符中`==`和`is`的区别（`!=`和`is not`同理）
>
> 1. **`==` (相等比较运算符)**:
>
>    - 检查两个对象的**值**是否相等。
>    - 如果对象内容相同，即使它们是不同的对象实例，它们也被视为相等。
>    - 例如，`[1, 2, 3] == [1, 2, 3]` 返回 `True`，即使这两个列表在内存中的位置不同。
>
> 2. **`is` (身份比较运算符)**:
>
>    - 检查两个对象是否是**同一对象**，即它们是否有相同的内存地址。
>    - 即使两个对象具有相同的内容，但它们位于不同的内存地址，使用 `is` 也会返回 `False`。
>    - 例如，`a = [1, 2, 3]` 和 `b = [1, 2, 3]`，尽管 `a == b` 返回 `True`，但 `a is b` 返回 `False`，因为它们在内存中是两个不同的对象。
>
>    ![image-20230911153052941](https://images.wu.engineer/images/2023/09/11/image-20230911153052941.png)
>
>    ![image-20230911153132919](https://images.wu.engineer/images/2023/09/11/image-20230911153132919.png)
>
> 但是，对于某些小的整数值和字符串，Python为了优化会使用相同的对象。例如：
>
> ```python
> >>> x = 5
> >>> y = 5
> >>> print(x is y)
> True
> ```

#### Logical/Boolean Operators

![image-20230911153328300](https://images.wu.engineer/images/2023/09/11/image-20230911153328300.png)

##### `and` Operator

![image-20230911153359818](https://images.wu.engineer/images/2023/09/11/image-20230911153359818.png)

##### `or` Operator

![image-20230911153457176](https://images.wu.engineer/images/2023/09/11/image-20230911153457176.png)

##### `not` Operator

![image-20230911153521444](https://images.wu.engineer/images/2023/09/11/image-20230911153521444.png)

#### Augmented Assignment Operators

![image-20230911153702919](https://images.wu.engineer/images/2023/09/11/image-20230911153702919.png)

### 1.8 Expressions

- Expressions is a piece of syntax evaluated to some value
- Combination of operators and operands
  - Value is an expression
  - Variable is an expression
  - Combination of values, variables and operators is also an expression

```python
>>> 1
1
>>> x = 1
>>> x
1
>>> x + 1*2
3
```

> 表达式是一个语法片段，它在评估时会产生某个值。换句话说，当你在程序中使用一个表达式，它将为你返回一个结果，这个结果是一个值。
>
> 表达式是有运算符(+,-,\*,\\)和操作数(5, 2.0, x)构成的
>
> 变量，数值，其二者的组合都可以是表达式

### 1.9 Standard IO

#### Input

![image-20230911154316848](https://images.wu.engineer/images/2023/09/11/image-20230911154316848.png)

#### Output

![image-20230911154329910](https://images.wu.engineer/images/2023/09/11/image-20230911154329910.png)

### 1.10 Strings

- Strings are **indexed sequence of characters**

#### Single quotes

```python
>>> 'It is IT5001'
'It is IT5001'
>>> '"It is IT5001," said Alice'
'"It is IT5001," said Alice'
>>> 'It\'s IT5001'
"It's IT5001"
```

#### Double quotes

```python
>>> "It is IT5001"
'It is IT5001'
>>> "It's IT5001"
"It's IT5001"
>>> "\"It is IT5001,\" said Alice"
'"It is IT5001," said Alice'
```

#### Triple quotes and triple double quotes

```python
>>> '''"It is IT5001," said Alice. So, it's IT5001.'''
'"It is IT5001," said Alice. So, it's IT5001.'
```

#### String Operators

![image-20230911155000848](https://images.wu.engineer/images/2023/09/11/image-20230911155000848.png)

![image-20230911155012775](https://images.wu.engineer/images/2023/09/11/image-20230911155012775.png)

#### Built-in Sting Functions

![image-20230911161859090](https://images.wu.engineer/images/2023/09/11/image-20230911161859090.png)

#### Lexicographical Ordering

![image-20230911161949960](https://images.wu.engineer/images/2023/09/11/image-20230911161949960.png)

> Lexicographical Ordering 词典排序
>
> - First, the first two letters are compared, and if they differ this determines the outcome of the comparison
> - If they are equal, the next two letters are compared, and so on. Until either sequence is exhausted
>
> 在词典排序中，元素是基于它们的组成部分逐一进行比较的。对于字符串，这意味着它们是基于各自的字符按字母顺序进行排序的。
>
> 让我们通过以下几点来解释词典排序：
>
> 1. **字符比较**：字符串中的字符按其ASCII值（或其他相关的字符编码，如Unicode）进行比较。
> 2. **顺序性**：从左到右逐字符地比较两个字符串。在遇到第一个不同的字符时，比较就会结束，返回的结果取决于这个不同字符的顺序。
> 3. **字符串长度**：如果两个字符串在某个位置的字符都相同，但一个字符串较短并且是另一个字符串的前缀（例如，“abc”和“abcd”），那么较短的字符串在词典排序中将位于前面。
> 4. **应用范围**：词典排序不仅适用于字符串，还可应用于其他可以按元素逐一比较的数据结构，如列表或元组。

#### String Indexing and Slicing

![image-20230911162725147](https://images.wu.engineer/images/2023/09/11/image-20230911162725147.png)

```python
>>> string_example = 'This is IT5001'
>>> string_example[0:3:2]
'TI'
>>> string_example[-1]
'1'
>>> string_example[1:len(string_example)]
'his is IT5001'
>>> string_example[-12:-4]
'is is IT'
>>> string_example[-12:-4:2]
'i sT'
```

#### Immutability of Strings

![image-20230911162804966](https://images.wu.engineer/images/2023/09/11/image-20230911162804966.png)

#### String Methods

![image-20230911163157281](https://images.wu.engineer/images/2023/09/11/image-20230911163157281.png)

- Case Conversion

```python
>>> 'abcd'.upper()
'ABCD'
>>> 'ABCD'.lower()
'abcd'
>>> 'abcd'.title()
'Abcd'
```

#### f-strings

- Strings prefixed with ‘f’
  - `f'Hi {name}'`
- ‘f’ stands for formatted strings
- Expressions can be embedded in strings
  - Expressions evaluated at run time
- Contains replacement fields, delimited by curly braces

```python
>>> module_code = 'IT5001'
>>> module_name = "Software Development Fundamentals"
>>> f"Welcome to {module_code} : {module_name}"
'Welcome to IT5001 : Software Development Fundamentals'

>>> print(f'23/2')
23/2
>>> print(f'{23/2}')
11.5
```

#### Raw Strings

- Strings prefixed with literal ‘r’

```python
>>> print('This is \nIT5001')
This is
IT5001
>>> print(r'This is \nIT5001')
This is \nIT5001
```

### 1.11 Namespaces

![image-20230911163754381](https://images.wu.engineer/images/2023/09/11/image-20230911163754381.png)

#### Builtin

- Contains names of `_builtin_` module
  - Datatypes
    - int, floats, etc.
  - Functions
    - print, input, etc.
  - Exceptions
    - NameError, SyntaxError, etc.
- Check `dir(_builtins_)`
- Will be created (destoryed) when Python interpreter starts (closes)

#### Global

![image-20230911164036586](https://images.wu.engineer/images/2023/09/11/image-20230911164036586.png)

#### How objects stored?

![image-20230911164101046](https://images.wu.engineer/images/2023/09/11/image-20230911164101046.png)

- Interpreter first searches names in Global Namespace
- If name is not in Global, then searches in builtin namespace
- If name is also not in builtin, throws `NameError`

### 1.12 Memory Management

- Python does memory management automatically
- Private heap to store objects
- Memory management depends on object type

### 1.13 Data Model: Objects, Values and Types

- Objects are Python’s abstraction for data
- Data in program is represented by objects and relation between objects

![image-20230911164403158](https://images.wu.engineer/images/2023/09/11/image-20230911164403158.png)

## 2. Functions



## 3. Selections and Loops



## 4. Functions Scope and Recursion



## 5. Recursion VS. Iteration



## 6. Debugging



## 7. Sequences



## 8. Anonymous Functions



## 9. High Order Functions



