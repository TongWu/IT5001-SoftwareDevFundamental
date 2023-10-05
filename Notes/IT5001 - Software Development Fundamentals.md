# 0. Introductions

## 0.0 Disclaimer and References

- This repo is the self-organized warehouse for National University of Singapore, School of Computing, Course IT5001: Software Development Fundamentals.

- This is the self-written note for National University of Singapore, School of Computing, Course IT5001: Software Development Fundamentals. The materials and references used in this note are for revision and organization use only.

- > The content in this kind of block means which is not in the aspect of this course, which may from references, or self-understanding/translations. The understanding for them are not required under this course regulation.

- The most of the content and material used in this repo are referred from the National University of Singapore. Few of contents in the block as mentioned before, are referenced from the University of Manchester, Columbia University, website or/and self-organized. 

- **Do not share any content in this repo to anyone without permission, including course material, video, lab assignment and notes.**

## 0.1 Software Development

![image-20230911144254896](https://images.wu.engineer/images/2023/09/11/image-20230911144254896.png)

- Programming languages provide tools to:
  1. Build data structures
  2. Do reasoning
- Representations
  - Numbers, Strings, Arrays, Multi-dimensional arrays, Graphs, Trees

## 0.2 Algorithm

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

# 1. Python and Basic Types

## 1.1 Introduction to Built-in Types

![image-20230911145105876](https://images.wu.engineer/images/2023/09/11/image-20230911145105876.png)

![image-20230911145144304](https://images.wu.engineer/images/2023/09/11/image-20230911145144304.png)

> immutable = cannot been modified 变量被赋值后不可以被修改
>
> primitive types = original types 原始变量

> 在python中，不存在primitive types这一概念，但是在其他语言例如C++中存在primitive types。这些数据类型是语言本身提供的，不是由用户自由定义的数据结构。例如int, long, char, bool, void, float等。
>
> 在python中，这一概念通常被built-in types所包含

## 1.2 Numbers: Numeric Types

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

## 1.3 Boolean Type

![image-20230911151419691](https://images.wu.engineer/images/2023/09/11/image-20230911151419691.png)

> 以上内容介绍了真值测试。
>
> **真值测试**：在Python中，几乎任何对象都可以进行真值测试，以确定其是否可以解释为`True`或`False`。
>
> - 所有非零的数字都被认为是`True`。
> - 任何非空的对象，如字符串、列表、字典等，都被认为是`True`。
> - 常见的被解释为`False`的值有：`None`、`0`、`0.0`、`0j`、`""`（空字符串）以及`[]`、`()`、`{}`（空的容器）等。

## 1.4 Identifiers (Variable Names)

- User-defined names for objects, can enhance readability

- Rules:

  - First character should be an alphabet or underscore(\_)
  - Other characters can be numbers and underscore
  - Special characters are not allowed
  - Names are **case sensitive**

  ![image-20230911152057055](https://images.wu.engineer/images/2023/09/11/image-20230911152057055.png)

## 1.5 Multiple Assignment

![image-20230911152125356](https://images.wu.engineer/images/2023/09/11/image-20230911152125356.png)

## 1.6 Keywords

![image-20230911152243220](https://images.wu.engineer/images/2023/09/11/image-20230911152243220.png)

- Keyword cannot be name of variables

## 1.7 Operators

### Arithmetic Operators

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

### Comparison Operators

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

### Logical/Boolean Operators

![image-20230911153328300](https://images.wu.engineer/images/2023/09/11/image-20230911153328300.png)

#### `and` Operator

![image-20230911153359818](https://images.wu.engineer/images/2023/09/11/image-20230911153359818.png)

#### `or` Operator

![image-20230911153457176](https://images.wu.engineer/images/2023/09/11/image-20230911153457176.png)

#### `not` Operator

![image-20230911153521444](https://images.wu.engineer/images/2023/09/11/image-20230911153521444.png)

### Augmented Assignment Operators

![image-20230911153702919](https://images.wu.engineer/images/2023/09/11/image-20230911153702919.png)

## 1.8 Expressions

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

## 1.9 Standard IO

### Input

![image-20230911154316848](https://images.wu.engineer/images/2023/09/11/image-20230911154316848.png)

### Output

![image-20230911154329910](https://images.wu.engineer/images/2023/09/11/image-20230911154329910.png)

## 1.10 Strings

- Strings are **indexed sequence of characters**

### Single quotes

```python
>>> 'It is IT5001'
'It is IT5001'
>>> '"It is IT5001," said Alice'
'"It is IT5001," said Alice'
>>> 'It\'s IT5001'
"It's IT5001"
```

### Double quotes

```python
>>> "It is IT5001"
'It is IT5001'
>>> "It's IT5001"
"It's IT5001"
>>> "\"It is IT5001,\" said Alice"
'"It is IT5001," said Alice'
```

### Triple quotes and triple double quotes

```python
>>> '''"It is IT5001," said Alice. So, it's IT5001.'''
'"It is IT5001," said Alice. So, it's IT5001.'
```

### String Operators

![image-20230911155000848](https://images.wu.engineer/images/2023/09/11/image-20230911155000848.png)

![image-20230911155012775](https://images.wu.engineer/images/2023/09/11/image-20230911155012775.png)

### Built-in Sting Functions

![image-20230911161859090](https://images.wu.engineer/images/2023/09/11/image-20230911161859090.png)

### Lexicographical Ordering

![image-20230911161949960](https://images.wu.engineer/images/2023/09/11/image-20230911161949960.png)

Lexicographical Ordering 词典排序

- First, the first two letters are compared, and if they differ this determines the outcome of the comparison
- If they are equal, the next two letters are compared, and so on. Until either sequence is exhausted

> 在词典排序中，元素是基于它们的组成部分逐一进行比较的。对于字符串，这意味着它们是基于各自的字符按字母顺序进行排序的。
>
> 让我们通过以下几点来解释词典排序：
> 
>1. **字符比较**：字符串中的字符按其ASCII值（或其他相关的字符编码，如Unicode）进行比较。
> 2. **顺序性**：从左到右逐字符地比较两个字符串。在遇到第一个不同的字符时，比较就会结束，返回的结果取决于这个不同字符的顺序。
>3. **字符串长度**：如果两个字符串在某个位置的字符都相同，但一个字符串较短并且是另一个字符串的前缀（例如，“abc”和“abcd”），那么较短的字符串在词典排序中将位于前面。
> 4. **应用范围**：词典排序不仅适用于字符串，还可应用于其他可以按元素逐一比较的数据结构，如列表或元组。

### String Indexing and Slicing

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

### Immutability of Strings

![image-20230911162804966](https://images.wu.engineer/images/2023/09/11/image-20230911162804966.png)

### String Methods

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

### f-strings

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

### Raw Strings

- Strings prefixed with literal ‘r’

```python
>>> print('This is \nIT5001')
This is
IT5001
>>> print(r'This is \nIT5001')
This is \nIT5001
```

## 1.11 Namespaces

![image-20230911163754381](https://images.wu.engineer/images/2023/09/11/image-20230911163754381.png)

### Built-in

- Contains names of `_builtin_` module
  - Datatypes
    - int, floats, etc.
  - Functions
    - print, input, etc.
  - Exceptions
    - NameError, SyntaxError, etc.
- Check `dir(_builtins_)`
- Will be created (destoryed) when Python interpreter starts (closes)

### Global

![image-20230911164036586](https://images.wu.engineer/images/2023/09/11/image-20230911164036586.png)

### How objects stored?

![image-20230911164101046](https://images.wu.engineer/images/2023/09/11/image-20230911164101046.png)

- Interpreter first searches names in Global Namespace
- If name is not in Global, then searches in builtin namespace
- If name is also not in builtin, throws `NameError`

## 1.12 Memory Management

- Python does memory management automatically
- Private heap to store objects
- Memory management depends on object type

## 1.13 Data Model: Objects, Values and Types

- Objects are Python’s abstraction for data
- Data in program is represented by objects and relation between objects

![image-20230911164403158](https://images.wu.engineer/images/2023/09/11/image-20230911164403158.png)

# 2. Functions

## 2.1 Abstraction

![image-20230912192717225](https://images.wu.engineer/images/2023/09/12/image-20230912192717225.png)

- Function is useful, especially when a code piece will be used few times
- User only needs to know input arguments and output data types
  - As known as ‘Blackbox’, it is not necessary for users to understand the code in each function

![image-20230912192957777](https://images.wu.engineer/images/2023/09/12/image-20230912192957777.png)

### Type of functions

- Pure functions

  - Function without side-effects
  - Only mapping
  - Outputs depend only on inputs

- Functions with side-effects

  - Side-effects: I/O tasks
    - Taking input from keyboard, reading data from files, etc.
    - Printing output to screen, writing data to files, etc.

- Higher-order Functions

  - Functions that accepts functions as inputs and/or return functions as outputs

  $$
  h(x) = f(g(x))
  $$

## 2.2 Python Modules and Packages

### 2.2.1 Functions in Python

- Built-in functions
  - Built-in module is loaded automatically
  - Examples: `print()`, `input()`, `id()`
- Functions from Python modules and packages
  - Not loaded automatically
  - Need to `import` when needed
  - Example: `turtle`, `math`
- User-defined Functions
- Special function
  - `main()`

### 2.2.2 Import Modules and Packages

1. `import <module_name>`
2. `from <module_name> import <names>`

```python
import math
from math import sin, pi
```

> 对于`import math`和`from math import *`，在导入方式和随后的使用方式上有所不同：
>
> 1. **`import math`**:
>    - 这种方式导入整个`math`模块。
>    - 当你想使用`math`模块中的任何函数或变量时，你需要使用`math.`前缀。例如，要使用正弦函数，你会这样写：`math.sin(90)`
> 2. **`from math import *`**:
>    - 这种方式导入`math`模块中的所有函数和变量。
>    - 这意味着你可以直接使用`math`模块中的函数或变量，而无需加`math.`前缀。例如，你可以直接写`sin(90)`而不是`math.sin(90)`。
>    - 使用这种方式存在一个潜在的问题：如果其他模块或你的代码中有与`math`模块中的函数或变量同名的项，那么它们可能会被覆盖。这可能导致意外的行为和难以追踪的错误。
>
> 总之，虽然`from math import *`可以使你的代码看起来更简洁，但由于可能导致的命名冲突和代码的可读性问题，许多开发者推荐避免使用这种导入方式，而是选择`import math`或只导入所需的特定函数，例如`from math import sin, cos`。

### 2.2.3 Namespaces: Importing Modules

**Import Single Module**

![image-20230912195105773](https://images.wu.engineer/images/2023/09/12/image-20230912195105773.png)

**Import Multiple Modules**

![image-20230912195157145](https://images.wu.engineer/images/2023/09/12/image-20230912195157145.png)

**Import Objects from Modules**

![image-20230912195248752](https://images.wu.engineer/images/2023/09/12/image-20230912195248752.png)

> 总结：
>
> 在导入整个模块时，会导入整个模块的namespace，这个namespace在global namespace当中。然而当导入一个模块中的某个或多个函数时，这些函数会被导入到global namespace。

## 2.3 User-Defined Functions

![image-20230912195454207](https://images.wu.engineer/images/2023/09/12/image-20230912195454207.png)

### 2.3.1 Arguments

- Arguments is the input of the function, it allows function to receive data from the outside environment

![image-20230912200422206](https://images.wu.engineer/images/2023/09/12/image-20230912200422206.png)

#### Type of Arguments

1. **位置参数（Positional Arguments）**:

   - 这是最常见的参数类型。它们是基于它们在函数定义中的位置来传递的。

   ```python
   def add(x, y):
   	return x+y
   ```

   在上面这个例子中，`x` `y`是位置参数。即我们需要对应参数在括号中的位置传入参数，例如`add(3,4)`，其中x就是3，y就是4

2. **关键字参数（Keyword Arguments）**:

   - 当调用函数时，可以使用参数的名称来为其提供值，这称为关键字参数。这种调用方法可以提高代码的可读性，并允许我们在调用函数时更加灵活地排列参数。

   ```python
   add(x=5, y=3)
   ```

   在使用关键字参数时，可以无视顺序。

3. **默认参数（Default/optional Arguments）**:

   - 函数定义时可以为参数设置默认值。如果调用函数时没有提供该参数的值，则使用默认值。

   ```python
   def greet(name, greeting="Hello"):
       print(greeting, name)
   
   greet("Alice")  # 输出: Hello Alice
   greet("Bob", greeting="Hi")  # 输出: Hi Bob
   ```

> **Extra types of argument**
>
> 1. **可变位置参数（\*args）**:
>
> - 这允许函数接收任意数量的位置参数。这在函数内部被表示为一个元组(tuple)。
>
> ```python
> def multiply(*nums):
>     result = 1
>     for num in nums:
>         result *= num
>     return result
> ```
>
> 2. **可变关键字参数（\*\*kwargs）**
>
>    - 这允许函数接收任意数量的关键字参数。这在函数内部被表示为一个字典。
>
>    ```python
>    def display_data(**data):
>        for key, value in data.items():
>            print(key, ":", value)
>    ```
>
> 3. **参数类型注解（Type Annotations）**:
>
>    - 从Python 3.5开始，函数参数可以包括类型注解，这可以增加代码的可读性。
>
>    ```python
>    def add(x: int, y: int) -> int:
>        return x + y
>    ```

### 2.3.2 Return Statement

- It does two things
  1. Terminates the function
  2. Return statement pass the output of function to the calling function

![image-20230912200356522](https://images.wu.engineer/images/2023/09/12/image-20230912200356522.png)

![image-20230912200403892](https://images.wu.engineer/images/2023/09/12/image-20230912200403892.png)

### 2.3.3 Function Tracing

##### Namespace

![image-20230912201313110](https://images.wu.engineer/images/2023/09/12/image-20230912201313110.png)

##### Tracing 1

![image-20230912201410351](https://images.wu.engineer/images/2023/09/12/image-20230912201410351.png)

![image-20230912201420789](https://images.wu.engineer/images/2023/09/12/image-20230912201420789.png)

##### Tracing 2

![image-20230912201541315](https://images.wu.engineer/images/2023/09/12/image-20230912201541315.png)

![image-20230912201550111](https://images.wu.engineer/images/2023/09/12/image-20230912201550111.png)

### 2.3.4 Doc String

- Contains information about the function
  - Describes how to use the function
  - Can access it using help/doc methods

![image-20230912200531566](https://images.wu.engineer/images/2023/09/12/image-20230912200531566.png)

## 2.4 Pure Functions

> Recall:
>
> Side-effects: I/O tasks
>
> - Taking input from keyboard, reading data from files, etc.
> - Printing output to screen, writing data to files, etc.

- Pure functions has no side-effects, only mapping. The output of the pure function depends only on inputs

```python
x = 2
y = 4
def sum_two(x, y):
	return x+y
z = sum_two(3,6)
print(z)
```

```python
x = 2
y = 4
def sum_two(x):
	return x+y
z = sum_two(3)
print(z)
```

> Pure function的定义为：该函数没有任何的副作用(Side-effects)，包含获取额外的输入和有额外的输出。并且该函数的输出是否只取决于输入。
>
> 对于第一段函数，该函数的输出只取决于输入参数`x`, `y`而不依赖任何外部的变量或者状态。故该函数为纯函数pure function
>
> 对于第二段函数，该函数取决于输入参数`x`和外部参数`y`。所以他不是一个pure function

# 3. Control Structure (Selections and Loops)

![image-20230912205854358](https://images.wu.engineer/images/2023/09/12/image-20230912205854358.png)

## 3.1 Selection

```python
if (condition): # If the condition is true, do the expression below
	{expression}
	if (condition): # Nested selection
		{expression}
elif (condition): # AKA. else if. The selection is still legal without "elif"
else: # The selection is still legal without "else"
	{expression}
```

- In python, strongly follow the indentation (缩进)

## 3.2 Repetition

```python
while (condition): # Do the expression in the indentation if the condition is true
    {expression}
```

- Infinity Repetition:

```python
while True:
	{expression}
```

##### `<=` or `<`?

```python
n = 5
while n < 10:
	print(n)
	n += 1
    
# Output:
5
6
7
8
9
# Final n=10
```

```python
n = 5
while n <= 10:
	print(n)
	n += 1
    
# Output:
5
6
7
8
9
10
# Final n=11
```

> 在执行while loop时，程序会先判断条件，若条件为真则运行loop中的代码。

## 3.3 Iteration

**The act of repeating a process with the aim of approaching a desired goal, target or result**

- There are three types of loops
  1. Must run exactly N times
  2. Run many number of times
  3. Run at most N times
     - Check all True (or check all False)
     - Find any True (or False)

### 3.3.1 For loop (Must run exactly N times)

- Use iterable objects to repeatedly execute a series of tasks
- Number of repetitions are equal to number of items provided by iterable object

#### Iterable and Iterators

![image-20230912222536678](https://images.wu.engineer/images/2023/09/12/image-20230912222536678.png)

#### Built-in iterable: `range()`

- `range({start}, {stop}, {step})`
  - Generate sequence of numbers from `start` (inclusive) to `stop` (exclusive), incremented by `step`
  - `start` and `step` are optional arguments
    - Default values:
      - `start = 0`
      - `step = 1`

- Example:

```python
for i in range(5): # same as range(0, 5), range(0, 5, 1)
	print(i)

Output: 
0
1
2
3
4
```

### 3.3.2 Run many number of times

```python
def sumNumber():
    sumSoFar = 0
    print('Please enter a number or type \'bye\' to sum:')
    num = input()
    while num != 'bye':
        sumSoFar += int(num)
        print('Please enter a number or type \'bye\' to sum:')
        num = input()
    print(f'The sum of all numbers is {sumSoFar}')
    
sumNumber()
```

- We do not know how many numbers will the user enter
- Line 3,4 and Line 7,8 are repeated
  - Because the first time run the function will through line 3,4 to enter the while loop
  - Then the line 7,8 will run many times as user want
- While loop terminate condition: `num = 'bye'`
  - If `num = 'bye'`, exit the while loop

### 3.3.3 Run at most N times (check all True)

```python
def checkAllAlpha(string):
    l = len(string)
    for i in range(l):
        if not isAlphabet(string[i]):
            return False
    return True
```

- The function input a string variable `string`
- Get the length of the `string` as a iterator
- For each character in `string`, check if this character is alphabet:
  - If not alphabet, terminate the function and return `False`
  - If all characters are alphabet, terminate the function and return `True`

- **In this case, the loop will most run `l` times, but it may less than `l` times.**

### 3.3.4 When use `for` and `while`?

- `for`
  - You know how many times the loop will run
  - Namely, anything in the body of the loop will NOT change the number of times you repeat the loop
  - E.g., printing all the data in a spreadsheet
- `while`
  - You may not know how many times you need to repeat
  - The number of times is depended on the “condition”, in which, may change unpredictably inside the loop
  - E.g., while the player haven’t guess the right answer, keep guessing

## 3.4 `break` & `continue`

```python
for j in range(10):
    print(j)
    if j == 3:
        break # break out the loop
print('done')
# Output:
0
1
2
3
done
```

```python
for j in range(10):
    if j == 3:
        continue # Skip the expression below, jump to the next loop with j++
    print(j)
print('done')

# Output:
0
1
2
4
5
6
7
8
9
done
```

# 4. Functions Scope and Recursion

## 4.1 Scope

### 4.1.1 Global & Local Variables

- A variable which is defined in the main body of a file is called a **global variable**. It will be **visible throughout the file**, and also inside any file which imports that file
- A variable which is defined inside a function is **local** to that function. It is accessible **from the point at which it is defined until the end of the function**, and exists for as long as the function is executing
- The parameter names in the function definition behave like local variables, but they contain the values that we pass into the function when we call it.

```python
a = 2
b = 3 # Global variables
def hello():
    a = 4
    b = 5 # Local variables
```

![image-20230913001120532](https://images.wu.engineer/images/2023/09/12/image-20230913001120532.png)

#### Global Variable

![image-20230913001202988](https://images.wu.engineer/images/2023/09/12/image-20230913001202988.png)

#### Global Variable vs. Local Variable

![image-20230913001239224](https://images.wu.engineer/images/2023/09/12/image-20230913001239224.png)

![image-20230913001314239](https://images.wu.engineer/images/2023/09/12/image-20230913001314239.png)

### 4.1.2 Crossing Boundary (change global variable in the function)

- Use `global` keyword to pass the global variable into the function

```python
x = 0
def foo():
	global x
	x = 999
	print(x)

foo()
print(x)

# Output:
999
999
```

```python
x = 0
def foo():
	print(x) # This will throw an ERROR, since no local variable called `x`
	x = 999
	print(x)

foo()
```

## 4.2 Generator Functions

![image-20230913001719005](https://images.wu.engineer/images/2023/09/12/image-20230913001719005.png)

### 4.2.1 Return vs. Yield

- With `return` statement:
  - State is not retained after the function returns the value
- With `yield` statement:
  - State of the function is retained between the calls
  - Can have many `yield` statements in sequence

> `return` 和 `yield ` 的主要区别：
>
> 1. **函数类型**:
>    - **return** 用在普通的函数中，这些函数被称为“函数”（functions）。
>    - **yield** 用在生成器中，这些函数被称为“生成器函数”（generator functions）。
> 2. **返回值**:
>    - 使用 **return** 的函数返回一个单一的值（这可以是任何数据类型，如整数、字符串、列表、字典等）。
>    - 使用 **yield** 的函数返回一个生成器对象，这个对象可以用于迭代，每次迭代都返回一个值。
> 3. **执行流程**:
>    - 当函数遇到 **return** 时，它会返回一个值，并且函数的执行结束。下次再调用这个函数时，它会从头开始执行。
>    - 当生成器函数遇到 **yield** 时，它会返回一个值，并“暂停”函数的执行，而不是结束它。下次再迭代生成器时，它会从上次暂停的地方继续执行，而不是从头开始。
> 4. **内存效率**:
>    - 生成器（使用 **yield**）在处理大量数据时特别有用，因为它们是在每次迭代时产生一个值，而不是一次性产生所有的值并存储在内存中。这对于大数据流和懒加载序列特别有用。
>
> ```python
> def generate_numbers(n):
>     for i in range(n):
>         yield i
>         
> for number in generate_numbers(5):
>     print(number)
>     
> # Output:
> 0
> 1
> 2
> 3
> 4
> ```

![image-20230913002243050](https://images.wu.engineer/images/2023/09/12/image-20230913002243050.png)

## 4.3 Calling Other Functions

```python
def hypotenuse(a,b):
	return sqrt((a*a) + (b*b))
```

```python
def hypotenuse(a, b):
	return sqrt(sum_of_squares(a,b))
	
def sum_of_squares(x, y):
	return square(x) + square(y)
	
def square(x):
	return x*x
```

- Two examples above are equilibrium.
- The order of enter and exit the function follows the principle of heap

### 4.3.1 Stack

![image-20230913002638704](https://images.wu.engineer/images/2023/09/12/image-20230913002638704.png)

![image-20230913002643679](https://images.wu.engineer/images/2023/09/12/image-20230913002643679.png)

![image-20230913002704069](https://images.wu.engineer/images/2023/09/12/image-20230913002704069.png)

![image-20230913002711167](https://images.wu.engineer/images/2023/09/12/image-20230913002711167.png)

### 4.3.2 Namespaces

![image-20230913010918426](https://images.wu.engineer/images/2023/09/12/image-20230913010918426.png)

![image-20230913010928747](https://images.wu.engineer/images/2023/09/12/image-20230913010928747.png)

> When the function is executed and returned the result value, the namespace of this function will be vanished.

## 4.4 Recursion

- A function that calls itself

- Solve a big problem by solving a smaller version of itself

  - > Divide and conquer

### 4.4.1 Recursive Function

- Function calls itself

```python
def factorial(n):
	if n==1:
		return 1
	else:
		return n*fractorial(n-1) # Calling itself
print(fractorial(4))
```

![image-20230913011204651](https://images.wu.engineer/images/2023/09/12/image-20230913011204651.png)

### 4.4.2 Namespaces

![image-20230913011227729](https://images.wu.engineer/images/2023/09/12/image-20230913011227729.png)

![image-20230913011236255](https://images.wu.engineer/images/2023/09/12/image-20230913011236255.png)

# 5. Recursion VS. Iteration

## 5.1 Reversing a String

### 5.1.1 Iterative Version 1

```python
def reverseStringI(s):
	output = ''
	l = len(s)
	for i in range(l):
		output += s[l-i-1]
	return output

>>> reverseString('abcde')
'edcba'
```

![image-20230913011726729](https://images.wu.engineer/images/2023/09/12/image-20230913011726729.png)

### 5.1.2 Iterative Version 2

```python
def reverseString(s):
	output = ''
	for c in s:
		output = c + output
	return output
	
>>> reverseString('abcde')
'edcba'
```

![image-20230913200315114](https://images.wu.engineer/images/2023/09/13/image-20230913200315114.png)

### 5.1.3 Recursive Version

```python
def reverseString(s):
	if not s:
		return ''
	return reverseString(s[1:])+s[0]
```

![image-20230913204445164](https://images.wu.engineer/images/2023/09/13/image-20230913204445164.png)

>1. **迭代 (Iterative)**:
>   - 迭代方法是通过使用循环（例如 `for` 或 `while`）来反复执行某些操作直到满足某个条件。
>   - 迭代通常更直观，尤其是对于那些习惯于思考“步骤”的人。
>2. **递归 (Recursive)**:
>   - 递归方法是函数自己调用自己来解决问题的小部分，直到满足终止条件或基本情况。
>   - 递归往往可以用更少的代码来实现
>3. **何时使用迭代或递归**:
>   - 如果问题可以简单地分解为重复的相似任务，那么迭代可能是一个更好的选择。
>   - 如果问题可以自然地分解为更小的子问题，递归可能更适合。但要注意，深度递归可能导致栈溢出。
>
>4. 性能与效率
>
>   - 在python中，由于函数的调用导致了额外的运行时间，故递归通常比迭代慢。此外，深度递归可能会导致栈溢出错误
>   - 迭代通常更高效，因为其不涉及函数调用的开销
>
>5. 示例
>
>   1. 斐波那契数列
>
>   ```python
>   def fibonacci_iterative(n):
>       if n <= 1:
>           return n
>       a, b = 0, 1
>       for _ in range(2, n+1):
>           a, b = b, a + b
>       return b
>       
>   def fibonacci_recursive(n):
>       if n <= 1:
>           return n
>       return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
>   ```
>
>   尽管递归版本更为简洁，但是面对非常大的`n`值，其运行速度会非常慢，因为他重复计算了许多相同的值。递归问题一般可以通过使用缓存或动态规划（DP）来优化

> 总结：
>
> 一般来说，现阶段优选迭代(iterative)。然而对于一个问题能够拆分为许多个小问题的情况下(divide and conquer)，递归(recursive)更有逻辑意义，然而这并不代表递归是最好的选择。事实上，对于分而治之的问题，动态规划(dynamic programming)是更好的选择。

## 5.2 Code Refactoring

- Refactoring is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior.

![image-20230913210337455](https://images.wu.engineer/images/2023/09/13/image-20230913210337455.png)

## 5.3 Nested Functions

![image-20230913210544963](https://images.wu.engineer/images/2023/09/13/image-20230913210544963.png)

![image-20230913210551383](https://images.wu.engineer/images/2023/09/13/image-20230913210551383.png)

- Inner functions **can access** global variables **but cannot modify** them.

## 5.3.1 Global Keyword

![image-20230913210657898](https://images.wu.engineer/images/2023/09/13/image-20230913210657898.png)

# 6. Bugs and Debugging

- Syntax Error
  - A syntax error is an error in the source code of a program. Since computer programs **must follow strict syntax** to compile correctly, any aspects of the code that do not conform to the syntax of the programming language will produce a syntax error

## 6.1 Debugging

- Means to remove errors from a program
- After debugging, the program is **not necessarily error-free**
  - It just means that whatever errors remain are harder to find
  - This is especially true for large applications

## 6.2 IDLE Debugger

![image-20230913211915969](https://images.wu.engineer/images/2023/09/13/image-20230913211915969.png)

![image-20230913211924635](https://images.wu.engineer/images/2023/09/13/image-20230913211924635.png)

![image-20230913211948845](https://images.wu.engineer/images/2023/09/13/image-20230913211948845.png)

- Go
  - Clicking this will run the program until the next break point is reached. You can insert break points in your code by right clicking and selecting Set Breakpoint. Lines that have break points set on them will be highlighted in yellow.
- Step
  - This executes the next statement. If the statement is a function call, it will enter the function and stop at the first line.
- Over
  - This executes the next statement just as Step codes. But it does not enter into functions. Instead, it finishes executing any function in the statement and stops at the next statement in the same scope.
- Out
  - This exits the current functions and stops in the caller of the current function.
  - After using Step to step into a function, you can use Out to quickly execute all the statements in the function and get back out to the outer function
- Quit: This terminates execution

![image-20230913212751620](https://images.wu.engineer/images/2023/09/13/image-20230913212751620.png)

## 6.3 Common Types of Errors

![image-20230913212833106](https://images.wu.engineer/images/2023/09/13/image-20230913212833106.png)

![image-20230913212837957](https://images.wu.engineer/images/2023/09/13/image-20230913212837957.png)

![image-20230913212846231](https://images.wu.engineer/images/2023/09/13/image-20230913212846231.png)

![image-20230913212853484](https://images.wu.engineer/images/2023/09/13/image-20230913212853484.png)

![image-20230913212858595](https://images.wu.engineer/images/2023/09/13/image-20230913212858595.png)

![image-20230913212903939](https://images.wu.engineer/images/2023/09/13/image-20230913212903939.png)

## 6.4 Summary

- Compound data helps us to reason at a higher conceptual level
- Abstraction barriers separate usage of a compound data from its implementation
- Only functions at the interface should be used
- We can choose between different implementations as long as contract is fulfilled

# 7. Data Collections (Sequences)

## 7.1 Indexed Collection

- Lists and Tuples are both belongs to a type of data structure called arrays
- **Lists are mutable (can modify the data) and is dynamic arrays**
- **Tuples are immutable (cannot modify the data) and is static arrays**

### 7.1.1 Strings

- Mentioned in previous chapter

### 7.1.2 Lists

- Ordered sequence of data types
  - Homogeneous sequence. Lists can be:
    1. Sequence of integers `[1, 2, 3, 4]`
    2. Sequence of floats `[1.0, 2.0, 3.0, 4.0]`
    3. Sequence of strings `['a', 'b', 'c', 'd']`
    4. Sequence of lists `[[1,2,3,4], [1.0, 2.0, 3.0, 4.0], ['a', 'b', 'c', 'd']]`
    5. Sequence of functions, etc.
  - Heterogeneous sequence
    - Mix of integers, floats, strings, etc.
- Lists defined using square brackets `[]`

![image-20230913225204556](https://images.wu.engineer/images/2023/09/13/image-20230913225204556.png)

![image-20230913225218016](https://images.wu.engineer/images/2023/09/13/image-20230913225218016.png)

![image-20230913225341543](https://images.wu.engineer/images/2023/09/13/image-20230913225341543.png)

#### Mutable

- Elements can be replaced
- Elements can be added `append()`
- Elements can be removed `remove()`
  - Can remove a specific element (If element occurs multiple times, removes the first occurrence)
  - Can remove element at a specific location (index)
  - Can remove from the end of the list
- Elements can be sorted
  - `sort()`
  - `sorted()`
- Elements can be reversed

#### Dynamic-size Arrays

![image-20230913225814915](https://images.wu.engineer/images/2023/09/13/image-20230913225814915.png)

#### `append()` vs. concatenation 级联

```python
my_list_1 = [1,2,3,4]
my_list_2 = [5,6,7,8]
my_list_1.append(my_list_2) # Append
my_list_1
# Output: [1,2,3,4, [5,6,7,8]]
```

```python
my_list_1 = [1,2,3,4]
my_list_2 = [5,6,7,8]
my_list_1 = my_list_1 + my_list_2 # Concatenation
my_list_1
# Output: [1,2,3,4,5,6,7,8]
```

> 当讨论`append`和`级联`（通常指的是连接）时，我们通常是在讨论列表（list）的操作。下面是`append`和`级联（连接）`之间的主要区别：
>
> 1. **定义**：
>    - `append()`: 是一个列表方法，用于在列表的末尾添加一个元素。
>    - `级联（连接）`: 指的是将两个或多个列表连接在一起，创建一个新的列表。在Python中，可以使用`+`运算符来连接列表。
> 2. **结果**：
>    - `append()`: 修改原始列表并在其末尾添加一个元素。它不返回一个新列表，而是在原地进行修改。
>    - `级联（连接）`: 创建一个新的列表，它是两个列表的组合。
> 3. **使用场景**：
>    - 当你想在列表的末尾添加一个元素时，使用`append()`。
>    - 当你想将两个列表组合成一个新的列表时，使用`级联（连接）`。

#### String to Lists (and vice-versa)

```python
my_string = "IT5001"
my_list = list(my_string)
```

![image-20230913230453239](https://images.wu.engineer/images/2023/09/13/image-20230913230453239.png)

```python
my_list = ['a', 'b', 'c', 'd']
my_string = str(my_list)
a = my_string[0]
```

![image-20230913230553213](https://images.wu.engineer/images/2023/09/13/image-20230913230553213.png)

#### Aliasing vs Cloning

![image-20230913230747490](https://images.wu.engineer/images/2023/09/13/image-20230913230747490.png)

> 在Python的`list`中，`aliasing`和`cloning`是两个重要的概念，涉及对象的引用和复制。
>
> 1. **Aliasing（别名）**:
>
>    - 当两个变量指向同一个列表对象时，我们称这种现象为别名。
>    - 因为列表是可变的，所以当其中一个变量对列表进行修改时，另一个变量引用的列表内容也会随之改变，因为它们都指向同一个列表对象。
>
>    示例：
>
>    ```python
>    a = [1, 2, 3]
>    b = a  # b 是 a 的别名，它们都指向同一个列表对象
>    b[0] = 10
>    print(a)  # 输出：[10, 2, 3]，因为修改 b 也会影响 a
>    ```
>
> 2. **Cloning（克隆）**:
>
>    - 克隆是创建列表的一个完整拷贝或副本。
>    - 这意味着原始列表和克隆后的列表是两个不同的对象。对其中一个列表的修改不会影响另一个列表。
>    - 克隆可以使用切片、`copy`方法或其他方法来实现。
>
>    示例：
>
>    ```python
>    a = [1, 2, 3]
>    c = a[:]  # 使用切片克隆列表
>    d = a.copy()  # 使用copy方法克隆列表
>    c[0] = 10
>    d[1] = 20
>    print(a)  # 输出：[1, 2, 3]，a 的内容没有改变
>    print(c)  # 输出：[10, 2, 3]
>    print(d)  # 输出：[1, 20, 3]
>    ```
>
> **为什么这些概念重要？**
>
> 理解`aliasing`和`cloning`在编程中非常重要，因为对列表的错误操作可能会导致预期之外的结果。例如，当你无意中使用了列表的别名并进行了修改，这可能会影响到程序的其他部分，导致难以追踪的错误。

#### `sort()` vs `sorted()`

![image-20230913230954159](https://images.wu.engineer/images/2023/09/13/image-20230913230954159.png)

> `sort()` 和 `sorted()` 都是用来对集合进行排序的，但它们之间有一些关键的不同。
>
> 1. **方法 vs 函数**：
>    - `sort()` 是列表（list）的一个方法。因此，你只能在列表上调用它，如 `my_list.sort()`.
>    - `sorted()` 是一个内置函数，可以对任何可迭代的对象进行操作（如列表、元组、字符串等），并且总是返回一个新的排序列表。
> 2. **返回值**：
>    - `sort()` 不返回任何值（即返回 `None`）。它直接修改原始列表。
>    - `sorted()` 返回一个新的排序列表，并且不会修改原始的可迭代对象。
> 3. **应用对象**：
>    - `sort()` 只适用于列表。
>    - `sorted()` 可以应用于任何可迭代的对象。
> 4. **不变性**：
>    - 使用 `sort()` 时，原始列表会被修改。
>    - 使用 `sorted()` 时，原始可迭代对象保持不变。

#### `reverse()`

![image-20230913231044029](https://images.wu.engineer/images/2023/09/13/image-20230913231044029.png)

#### List of anything

![image-20230913231117499](https://images.wu.engineer/images/2023/09/13/image-20230913231117499.png)

![image-20230913231125413](https://images.wu.engineer/images/2023/09/13/image-20230913231125413.png)

#### Iterable

```python
for i in [0,1,2,3,4]:
	print(i)
    
my_list = [1,2,3,4]
for i,j in enumerate(my_list):
    print(f'Element at index {i} is {j}')
    
# Output
Element at index 0 is 1
Element at index 1 is 2
Element at index 2 is 3
Element at index 3 is 4
```

#### Mutation and Iteration

- Avoid mutating a list while iterating over the list

```python
myList = [1,2,3,4]

for element in myList:
	myList.remove(element)
```

- `next()` method uses an index to retrieve the elements from `myList`
- `remove()` method mutates the `myList`, but the index in `next()` method will not be updated

> 在Python中，直接在遍历列表的过程中修改它（例如通过删除其元素）是一种常见的错误做法，因为这会干扰迭代过程并导致意外的结果。
>
> 以下是修改列表时可能遇到的问题：
>
> 1. **索引偏移**： 当你从列表中删除一个元素时，后面的元素的索引都会减少1。这可能导致跳过一些元素或出现索引错误。
> 2. **长度变化**： 列表的长度在迭代过程中发生变化，可能导致某些元素未被处理或循环出现超出范围的错误。
> 3. **递归复杂性**： 当结合递归时，这种行为会变得更加复杂和难以预测，因为你可能在递归的每一层都在修改列表。
>
> 为了避免这些问题，通常采用以下策略之一：
>
> 1. **创建新的列表**： 而不是修改原始列表，你可以创建一个新的列表，其中包含所有你想保留的元素。
> 2. **反向迭代**： 通过反向迭代列表，从末尾开始，可以确保即使在删除元素时，也不会干扰尚未处理的元素的索引。
> 3. **标记待删除的元素**： 在迭代期间，你可以标记要删除的元素（例如，将其添加到另一个列表中），然后在迭代结束后删除它们。
>
> 如果你需要使用递归来处理列表（例如，处理嵌套的列表结构），通常最安全的方法是创建新的列表或其他数据结构来存储结果，而不是尝试修改原始列表。

![image-20230913231946718](https://images.wu.engineer/images/2023/09/13/image-20230913231946718.png)

> 1. **空列表**： 如果`lst`是一个空列表，那么`lst[0]`会导致`IndexError`。函数在被调用前应该确保列表不为空，或者在函数内部进行检查。
> 2. **非数值元素**： 如果列表中含有非数值元素（例如字符串、列表或其他对象），而这些元素之间不能进行比较，则`i > maxSofar`可能会导致`TypeError`。
> 3. **非列表输入**： 尽管函数名是`findMax`，这个函数实际上可以处理任何可迭代的输入，如元组、集合等。考虑是否需要对输入类型进行检查或者更改函数名称以反映其更广泛的功能。
> 4. **内置函数**： Python已经提供了一个内置的`max`函数来获取可迭代对象中的最大值。除非有特定的原因（例如，你需要自定义比较逻辑或其他操作），否则通常推荐使用内置的`max`函数。

#### List Comprehensions

- Provides a concise way to apply an operation to the items in iterable object and store the result as a list
- Syntax
  - `[{expression} for {element} in {iterable} if {condition}]`
- Returns an iterable

```python
#TODO: Create a list my_list = [1,2,3,...,100]
my_list = [i for i in range(1, 101)]

#TODO: Create a list of first 10 squared numbers
my_list2 = [i*i for i in range(1,11)]

#TODO: Create a list of odd numbers less than 100
my_list3 = [i for i in range(1,101,2)]

#TODO: Create a list of prime numbers less than 50
for i in range(2,8):
    print([j for j in range(i*2, 50, i)])
```

> 1. **"Provides a concise way to apply an operation to the items in iterable object and store the result as a list"**:
>    - 这句话解释了列表推导式的核心用途。它提供了一种简洁的方法来对可迭代对象中的每个项目进行操作，并将结果存储为一个列表。
> 2. **Syntax**:
>    - 这是一个子标题，指的是以下内容将描述列表推导式的语法。
> 3. **"{expression} for {element} in {iterable} if {condition}"**:
>    - 这是列表推导式的基本语法。
>      - `{expression}` 是对每个元素进行的操作。
>      - `{element}` 是当前从`{iterable}`中取出的元素。
>      - `{iterable}` 是你要迭代的对象，例如列表、元组或任何可迭代的对象。
>      - `if {condition}` 是一个可选部分，表示只有当条件为`True`时，才会对`{element}`进行`{expression}`操作。
> 4. **"Returns an iterable"**:
>    - 这意味着列表推导式的结果是一个可迭代的对象，具体来说，就是一个列表。

#### Generator Expressions

- Provides a generator that can be used to iterate over without explicitly generating the list of items
- Syntax:
  - `({expression} for {element} in {iterable} if {condition})`
- Returns an iterator
- Requires less memory than list

```python
num = 4
square_list = [x**2 for x in range(num)]
square_generator = (x**2 for x in range(num))
# Two approaches' output are same
print(f'Size of list {sys.getsizeof(square_list)}') # Output: 87624
print(f'Size of generator {sys.getsizeof(square_generator)}') # Output: 120
```

> 1. **"Provides a generator that can be used to iterate over without explicitly generating the list of items"**:
>    - 这句话描述了生成器表达式的核心用途。生成器表达式提供了一个生成器，允许你逐项迭代，而不需要事先生成整个列表。这意味着不像列表推导式，它不会一次性产生所有的项，而是每次产生一个项。
> 2. **Syntax**:
>    - 这是一个子标题，指的是以下内容将描述生成器表达式的语法。
> 3. **"{expression} for {element} in {iterable} if {condition}"**:
>    - 这是生成器表达式的基本语法，与列表推导式非常相似。
>      - `{expression}` 是对每个元素进行的操作。
>      - `{element}` 是当前从`{iterable}`中取出的元素。
>      - `{iterable}` 是你要迭代的对象，例如列表、元组或任何可迭代的对象。
>      - `if {condition}` 是一个可选部分，表示只有当条件为`True`时，才会对`{element}`进行`{expression}`操作。
> 4. **"Returns an iterator"**:
>    - 这意味着生成器表达式的结果是一个迭代器，你可以使用例如`next()`函数来逐一获取项。
> 5. **"Requires less memory than list"**:
>    - 由于生成器表达式不会一次性生成所有的结果，而是在每次迭代时按需生成，因此它比等效的列表推导式占用更少的内存。

### 7.1.3 Tuples

- A static and an immutable array/list
- Syntax:
  - `int_tuple = (1,2,3)`
  - `float_tuple = (1.0,2.0,3.0)`
  - `str_tuple = ('a','b','c')`
  - `mixed_tuple = (1, 1.0, 'a')`

![image-20230913233323539](https://images.wu.engineer/images/2023/09/13/image-20230913233323539.png)

![image-20230913233330326](https://images.wu.engineer/images/2023/09/13/image-20230913233330326.png)

![image-20230913233340146](https://images.wu.engineer/images/2023/09/13/image-20230913233340146.png)

#### Lists and Tuples

- Similarities:
  - List and tuple are:
    - indexed
    - iterable
  - Both can store same or mixed data types
- Differences:
  - List is mutable
  - Tuple is immutable

![image-20230913233522261](https://images.wu.engineer/images/2023/09/13/image-20230913233522261.png)

#### Tuple with only one element

```python
tuple1 = (3,)
print(tuple1) # Output: (3,)
tuple1[0] # Output: 3
```

### 7.1.4 Lists vs Tuples

- List
  - Usually stores a large collection of data with the same type
- Tuple
  - Usually stores a small collections of items with various data types

## 7.2 Non-indexed Collection

### 7.2.1 Sets

- A set is an **unordered** collection of **immutable** elements with **no duplicate** elements
  - Unordered: Cannot get a single element by its index, like `s[2]`
  - No duplicate: every element exists only once in a set

![image-20230913233940367](https://images.wu.engineer/images/2023/09/13/image-20230913233940367.png)

![image-20230913233955144](https://images.wu.engineer/images/2023/09/13/image-20230913233955144.png)

![image-20230913234008743](https://images.wu.engineer/images/2023/09/13/image-20230913234008743.png)

```python
>>> setA = {1,2,3,4}
>>> setB = {3,4,5,6}
>>> setA | setB #Union
{1,2,3,4,5,6}
>>> setA & setB #Intersection
{3,4}
>>> setA - setB #A-B
{1,2}
>>> setA ^ setB #(A|B)-A&B
{1,2,5,6}
>>> setA.remove(1)
>>> setA
{2,3,4}
>>> setA.remove(1) #error if element missing
error
>>> setA.discard(1) #use discard instead
```

```python
# Sets are iterable
my_set = {1,2,3}
for i in my_set:
	print(i)
	
#Output:
1
2
3
```

#### Set from list and Vice-versa

![image-20230913234439182](https://images.wu.engineer/images/2023/09/13/image-20230913234439182.png)

### 7.2.2 Dictionary

- You search for the key in the dictionary
- Each key has a **correspondent** 相应的 value

![image-20230913234659258](https://images.wu.engineer/images/2023/09/13/image-20230913234659258.png)

![image-20230913234640692](https://images.wu.engineer/images/2023/09/13/image-20230913234640692.png)

- Each pair has a key and a value

![image-20230913234749847](https://images.wu.engineer/images/2023/09/13/image-20230913234749847.png)

- Key is on the left, value on the right
- Can store any type

```python
>>> my_dict = {'a':1, 'b':2}
>>> my_dict['b']
2
```

- AKA **hashtable** in other languages

![image-20230913234957817](https://images.wu.engineer/images/2023/09/13/image-20230913234957817.png)

![image-20230913235055853](https://images.wu.engineer/images/2023/09/13/image-20230913235055853.png)

![image-20230913235106770](https://images.wu.engineer/images/2023/09/13/image-20230913235106770.png)

![image-20230913235112190](https://images.wu.engineer/images/2023/09/13/image-20230913235112190.png)

- Other dict methods
  - `clear()` clear all
  - `copy()` make a copy
  - `keys()` return all keys
  - `values()` return all values
  - `items()` return all keys + values

![image-20230913235219858](https://images.wu.engineer/images/2023/09/13/image-20230913235219858.png)

## 7.3 Hashability and Immutability

![image-20230914145311450](https://images.wu.engineer/images/2023/09/14/image-20230914145311450.png)

> 在Python中，"Hashability"和"Immutability"是两个非常重要的概念，尤其是在处理集合类型（例如`set`和`dict`）时。
>
> 1. **不可变性 (Immutability)**
>
>    不可变性意味着对象的状态或值在其生命周期内不能被修改。这意味着，一旦对象被创建，我们就不能改变它。对于不可变对象，任何修改或更新的尝试都将导致创建一个新的对象。
>
>    例如，Python中的字符串和元组都是不可变的。这意味着一旦你创建了这些对象，你不能改变它们的值。例如：
>
>    ```python
>    my_str = "hello"
>    # 以下操作是非法的，会抛出异常
>    # my_str[0] = "H"
>    
>    my_tuple = (1, 2, 3)
>    # 以下操作也是非法的，会抛出异常
>    # my_tuple[0] = 4
>    ```
>
> 2. **可散列性 (Hashability)**
>
>    一个对象如果是可散列的，意味着它有一个固定的哈希值，这个哈希值在该对象的生命周期内不会改变。在Python中，这通常意味着对象需要满足以下条件：
>
>    - 该对象有一个`__hash__()`方法，这个方法返回一个整数，这个整数在对象的整个生命周期内都是固定的。
>    - 该对象还需要有一个`__eq__()`方法，可以用来判断两个对象是否相等。
>    - 如果两个对象在`__eq__()`方法中被认为是相等的，那么它们的哈希值必须相同。
>
>    哈希值是数据结构，如`dict`和`set`，用来快速定位一个元素的关键工具。例如，当你在一个字典中查找一个键时，Python首先计算键的哈希值，然后使用这个哈希值来直接定位相关联的值，而不需要检查字典中的每一个键。
>
>    因为可变对象的内容可能会改变，所以它们通常不是可散列的。例如，列表和字典是不可散列的，而字符串、整数和元组是可散列的。
>
> 3. **联系**：
>
>    在Python中，所有不可变的原生数据类型（如`int`、`float`、`str`和`tuple`）都是可散列的。这也意味着，这些类型的对象可以被用作集合的键或元素。但这并不意味着所有不可变对象都是可散列的，或者所有可散列的对象都是不可变的。不过，在常见的原生数据类型中，这两个特性往往是同时出现的。

### 7.3.1 Return Multiple Values

![image-20230914145509171](https://images.wu.engineer/images/2023/09/14/image-20230914145509171.png)

### 7.3.2 If don’t know the number of argument

![image-20230914145541870](https://images.wu.engineer/images/2023/09/14/image-20230914145541870.png)

![image-20230914145606792](https://images.wu.engineer/images/2023/09/14/image-20230914145606792.png)

### 7.3.3 Accessing Global Variables

- Can a function access(read-only) a global variable?
  - Yes, for both mutable and immutable variables

![image-20230914145702904](https://images.wu.engineer/images/2023/09/14/image-20230914145702904.png)

### 7.3.4 Modifying Global Variables

- Can a function modify a global variable with variable declared **global** within local function?
  - Yes, for both mutable and immutable variables

![image-20230914145812587](https://images.wu.engineer/images/2023/09/14/image-20230914145812587.png)

- Can a function modify a global variable with variable **not declared** as global within local function?
  - No for immutable variables
  - Yes for mutable variables with **only** the methods that mutate data(`append()`, `sort()`, etc)

![image-20230914145947096](https://images.wu.engineer/images/2023/09/14/image-20230914145947096.png)

![image-20230914150009942](https://images.wu.engineer/images/2023/09/14/image-20230914150009942.png)

## 7.4 Argument passed to Functions

- Pass by value (regular method)
  - An independent (duplicate) copy of argument is passed as input
  - Not good if the argument size is very large
    - Requires additional memory and execution time
- Pass by reference (pass a pointer)
  - Address of argument is passed and function access the value from the address
  - Efficient for arguments of very large size



- **Python use neither of them above, python use pass by assignment**

- The only exception is with global keyword

  - ```python
    def square():
    	global x # This is equivalent to pass by reference (pointer)
    	x = x**2
    	
    x = 2
    square()
    ```

> 在Python中，参数传递的方式经常被描述为“pass by assignment”或“pass by object reference”。这种方式与其他编程语言中的“pass by value”和“pass by reference”略有不同。
>
> 要理解"pass by assignment"，你需要首先了解Python中的变量和对象是如何工作的：
>
> 1. **Python中的变量与对象**：在Python中，所有的数据（无论是数字、字符串、列表等）都是以对象的形式存储的。当你创建一个变量（例如，`a = 3`），实际上是发生了两件事：首先，一个`int`类型的对象`3`被创建；然后，变量`a`被分配给这个对象，使得`a`引用该对象。
> 2. **参数传递的过程**：当你传递一个变量作为函数的参数时，实际上是将这个变量的引用（或说，指向对象的指针）传递给函数。也就是说，函数中的参数变量和外部传入的变量引用的是同一个对象。
> 3. **不可变性与可变性**：这种传递方式在不可变对象（如`int`、`str`、`tuple`）和可变对象（如`list`、`dict`）中的行为是不同的。对于不可变对象，由于对象本身不可更改，所以任何更改尝试实际上会创建一个新对象；而对于可变对象，可以在函数内部直接修改对象的内容。
>
> 下面是一些示例来说明这一点：
>
> ```python
> def modify(x):
>     x += 1
>     return x
> 
> a = 3
> b = modify(a)
> print(a)  # 输出：3
> print(b)  # 输出：4
> ```
>
> 在上面的例子中，虽然`x`在`modify`函数内部被修改了，但由于`int`是不可变的，所以`a`的值并没有改变。
>
> 再来看一个关于列表的例子：
>
> ```python
> def modify_list(lst):
>     lst.append(4)
>     return lst
> 
> my_list = [1, 2, 3]
> new_list = modify_list(my_list)
> 
> print(my_list)    # 输出：[1, 2, 3, 4]
> print(new_list)   # 输出：[1, 2, 3, 4]
> ```
>
> 在这个例子中，`my_list`在函数内部被修改，因为`list`是一个可变对象，所以原始的`my_list`也受到了影响。
>
> “pass by assignment”意味着函数参数接收的是原始变量引用的复制，而不是对象本身或对象的复制。

> 总结：
>
> - pass by assignment类似于C++中传递一个指针的做法，但不完全相同
> - 当你传递一个对象给函数时，你传递的是这个对象引用的一个拷贝(copy of object reference)。这意味着，函数内部的参数变量和外部的变量都指向同一个对象。
> - 对于不可变对象（如`int`、`str`、`tuple`），由于它们的值不能更改，任何修改尝试都会创建新对象。因此，函数外部的原始变量不会受到影响。
> - 对于可变对象（如`list`、`dict`），你可以在函数内部修改这个对象，从而也影响到函数外部的变量。
> - 这种传递方式与C/C++的“pass by reference”有一些相似之处，但在Python中不使用“引用”或“值”这样的术语，因为每个变量都是一个对象的引用。所以，我们使用“pass by assignment”这个术语来描述Python的参数传递机制。

![image-20230914153211704](https://images.wu.engineer/images/2023/09/14/image-20230914153211704.png)

- Immutable Variable
  - Can access global variable
  - Cannot modify global variable unless declared global `global x`
- Mutable Variable
  - Can access global variable
  - Can modify the variable
    - Need to use `global   ` keyword that do not mutate objects
    - No need to use `global ` keyword for methods that mutate objects

## 7.5 Lists append and concatenation

### 7.5.1 How are lists resized with append

![image-20230914153529951](https://images.wu.engineer/images/2023/09/14/image-20230914153529951.png)

![image-20230914153541330](https://images.wu.engineer/images/2023/09/14/image-20230914153541330.png)

> 与C++中的`std::vector`原理非常相似
>
> Python的`list`是一个动态数组实现，它提供了平均时间复杂度为�(1)*O*(1)的尾部插入操作，即`append`方法。其背后的原理和C++的`std::vector`类似。以下是`list`的`append`操作的基本原理：
>
> 1. **预分配存储空间**：当你创建一个新的列表或向列表添加元素时，Python可能不仅仅为当前的元素分配空间，而是预分配额外的空间。这意味着，列表的内部存储容量可能比它当前持有的元素数量要大。
> 2. **动态调整大小**：当向一个已经填满预分配空间的列表中再添加元素时，Python会为列表分配一个新的内存块，并可能比当前的内存块大一些。然后，Python会将旧的元素复制到新的内存块中，并释放旧的内存块。
> 3. **平均时间复杂度**：由于预分配的存储空间和动态的大小调整，大多数`append`操作都是常数时间复杂度。但在某些情况下（例如，当需要动态调整大小时），`append`操作可能会需要更多的时间。然而，考虑到所有`append`操作，其平均时间复杂度仍然是�(1)*O*(1)。
>
> C++的`std::vector`也是一个动态数组实现，其原理非常类似。当你向`std::vector`中添加元素，导致其容量不足时，它会分配一个新的、更大的内存块，将旧的元素复制到新的内存块，并释放旧的内存块。因此，尽管单个`push_back`操作可能会花费更多的时间，但从平均意义上看，其时间复杂度也是�(1)*O*(1)。
>
> 因此，Python的`list`和C++的`std::vector`在实现上有很多相似之处，特别是它们如何动态地调整大小以支持快速的尾部插入操作。

### 7.5.2 How are lists resized with concatenation 级联

![image-20230914153918687](https://images.wu.engineer/images/2023/09/14/image-20230914153918687.png)

### 7.5.3 Append vs Concatenation

![image-20230914153943329](https://images.wu.engineer/images/2023/09/14/image-20230914153943329.png)

### 7.5.4 Insertion/Deletion

![image-20230914154008117](https://images.wu.engineer/images/2023/09/14/image-20230914154008117.png)

## 7.6 List vs Tuple Conclusion

![image-20230914154028809](https://images.wu.engineer/images/2023/09/14/image-20230914154028809.png)

# 8. Anonymous Functions

- Traditional Form:
  - `square(x) -> x^2`
- Anonymous Form:
  - `x -> x^2`
- Anonymous Functions also known as **lambda($\lambda$) Functions**
  - Function without name
- Python Syntax:
  - `lambda args: {expression}`

## 8.1 Functions: Traditional Math vs $\lambda$-Calculus vs Python

![image-20230914160209922](https://images.wu.engineer/images/2023/09/14/image-20230914160209922.png)

![image-20230914160236309](https://images.wu.engineer/images/2023/09/14/image-20230914160236309.png)

```python
>>> (lambda x:x)('abc') # Identity function
'abc'
>>> (lambda x:x)(10) # Identity function
10
>>> (lambda x: 'abc')(5) # Constant function
‘abc'
>>> (lambda x,y,z: x+y+z)(4,5,9) # Multiple arguments
18
```

```python
(lambda args: {expressions})
# input args (x,y,z), then output the result of the expressions
```

# 9. High Order Functions

## 9.1 Functions in Python

- Functions can be
  - Assigned to variables
  - Passed as arguments to functions
  - Returned from functions

> 这段话描述的是Python中函数的一等公民（first-class citizen）特性。在计算机科学中，如果一个语言的函数被视为一等公民，这意味着函数可以被像其他基本数据类型（如整数、字符串）那样使用。

## 9.2 Functions can be assigned to variables

### 9.2.1 Callability

- Normal variables are not **callability**

![image-20230914190310747](https://images.wu.engineer/images/2023/09/14/image-20230914190310747.png)

- A function is **callable**

![image-20230914190336830](https://images.wu.engineer/images/2023/09/14/image-20230914190336830.png)

### 9.2.2 Variable store a function

- Normal variables can store values
- Variable can also store a function

![image-20230914190436636](https://images.wu.engineer/images/2023/09/14/image-20230914190436636.png)

> **Assigned to variables**: 在Python中，你可以将一个函数赋值给一个变量。这个变量现在可以像原始的函数那样被调用。
>
> ```python
> def greet():
>     return "Hello!"
> 
> say_hello = greet
> print(say_hello())  # 输出: Hello!
> ```
>
> 在上面的示例中，我们定义了一个函数`greet`，然后将它赋值给`say_hello`变量。现在，`say_hello`也可以被调用并执行与`greet`相同的功能。

![image-20230914190510841](https://images.wu.engineer/images/2023/09/14/image-20230914190510841.png)

> 当把函数赋给变量时，函数名称后带不带括号`()`有很大的区别
>
> 1. **`say_hello = greet`**:
>
>    这里你将`greet`函数本身赋值给了`say_hello`变量。此后，你可以使用`say_hello()`来调用这个函数。在这种情况下，`say_hello`变成了`greet`函数的一个引用或别名。
>
>    ```python
>    def greet():
>        return "Hello!"
>    
>    say_hello = greet
>    print(say_hello())  # 输出: Hello!
>    ```
>
> 2. **`say_hello = greet()`**:
>
>    这里你首先调用了`greet`函数，并将它的**返回值**赋值给了`say_hello`变量。如果`greet`函数的返回值是一个字符串"Hello!"，那么`say_hello`将会存储这个字符串值。
>
>    ```python
>    def greet():
>        return "Hello!"
>                         
>    say_hello = greet()
>    print(say_hello)  # 输出: Hello!
>    ```
>
>    注意这里的差异：`say_hello`是一个字符串，而不是一个函数，所以你不需要括号来访问它的值。
>
> 总结：`say_hello = greet`是函数引用的赋值，使`say_hello`成为一个函数；而`say_hello = greet()`是函数调用的结果的赋值，使`say_hello`持有这个结果。
>
> 如果`greet`函数需要参数，当您尝试`say_hello = greet()`（没有提供所需的参数）时，您会收到一个错误，因为在调用函数时没有提供必要的参数。

- When a function assigned to a variable, their ID are identical

```python
def inc_func(x):
	return x+1
	
my_func = inc_func

print( id(my_func) == id(inc_func) ) # Output: True
```

### 9.2.3 Functions stored in variables

```python
>>> from math import cos, sin, tan
>>> f_1 = cos
>>> f_1(0) # Equivalent to cos(0)
1.0
>>> print(f_1) # The type is function
<built-in function cos>
 
>>> def f():
		print("Hello")
>>> print(f)
<function f at 0x000000F9F93F4950>
```

### 9.2.4 Functions as elements in Lists/Tuples

```python
from math import cos, sin, tan
def inc_func(x):
	return x+1
mylist = [cos, sin, tan, inc_func, print]
x = my_list[3](1) # Equilavent to int_func(1)
print(x) # Output: 2
```

```python
from math import cos, sin, tan
my_func_list = [cos, sin, tan]
theta = pi/3
output = [func(theta) for func in my_func_list]
print(output) # Output: [0.5000000000000001, 0.866025..., 1.7320...]
```

### 9.2.5 Functions as elements in dictionaries

```python
def square(n):
	return n**2
	
def power(n,k):
	return n**k
	
my_func_dict = {square: None, power: 5} # Function as key

output = []
for func, parameter in my_func_dict.items():
	output.append(func(2) if parameter == None else func(2, parameter))
	
pirnt(output)
```

## 9.3 Functions can be passed as arguments to functions

![image-20230914192207363](https://images.wu.engineer/images/2023/09/14/image-20230914192207363.png)

> **Passed as arguments to functions**: 函数可以作为参数传递给其他函数。这在函数式编程中尤其有用，例如使用`map()`或`filter()`函数。
>
> ```python
> def square(x):
>     return x * x
> 
> numbers = [1, 2, 3, 4]
> squared_numbers = list(map(square, numbers))
> print(squared_numbers)  # 输出: [1, 4, 9, 16]
> ```
>
> 在此示例中，我们将`square`函数作为第一个参数传递给`map()`函数。

## 9.4 Functions can be returned from functions

> **Returned from functions**: 函数可以从其他函数中返回。这使我们可以创建所谓的“高阶函数”。
>
> ```python
> def power(n):
>     def compute(x):
>         return x ** n
>     return compute
> 
> square = power(2)
> cube = power(3)
> 
> print(square(4))  # 输出: 16
> print(cube(2))    # 输出: 8
> ```
>
> 在上面的示例中，`power`函数返回了一个内部函数`compute`。根据`power`函数接收的参数，返回的函数具有不同的行为。
>
> 总的来说，这段话突出了Python中函数的灵活性和功能性。由于函数在Python中是一等公民，你可以像处理其他对象一样处理它们，这为各种编程模式和技术提供了可能性。

- Functions can return inner functions as output

- Inner functions serves many purpose

  - Closures

    - Returns inner functions
    - Function plus the environment (state) in which they execute together
    - Preserve function state across function calls
    - Example:

    ![image-20230914192757812](https://images.wu.engineer/images/2023/09/14/image-20230914192757812.png)

  - Decorators

    - Decorator is a closure
      - Additionally, outer function accepts a function as input argument
    - Modifying input function’s behavior with an inner function without explicitly changing input function’s code

    - Example:

      ![image-20230914193121622](https://images.wu.engineer/images/2023/09/14/image-20230914193121622.png)

> 内部函数在Python中有多种用途。以下描述了其中的两种主要用途：闭包和装饰器。
>
> 1. **Closures**:
>
>    闭包是一个特殊类型的函数，它记住了创建它的环境的状态。
>
>    - **Returns inner functions**: 闭包的外部函数返回一个内部函数。
>    - **Function plus the environment (state) in which they execute together**: 这意味着闭包不仅仅是一个函数；它还包括函数执行时的环境或状态。
>    - **Preserve function state across function calls**: 尽管函数通常在调用结束后不保留状态，但闭包允许我们在连续的调用之间保留一些状态。
>
>    ```python
>    def counter():
>        count = 0
>        def increment():
>            nonlocal count
>            count += 1
>            return count
>        return increment
>    
>    c = counter()
>    print(c())  # 1
>    print(c())  # 2
>    ```
>
>    在上面的例子中，每次调用`c()`时，它都会记住`count`的状态。
>
> 2. **Decorators**:
>
>    装饰器是一种特殊类型的闭包，用于修改或增强其他函数的行为，而无需修改那些函数的代码。
>
>    - **Decorator is a closure**: 所有的装饰器都是闭包，因为它们都返回函数并记住自己的环境状态。
>    - **Additionally, outer function accepts a function as input argument**: 装饰器的外部函数接受一个函数作为输入参数。
>    - **Modifying input function’s behavior with an inner function without explicitly changing input function’s code**: 这是装饰器的主要用途。它允许我们增强或修改一个函数的行为，而无需修改该函数的源代码。
>
>    ```python
>    def simple_decorator(f):
>        def wrapper():
>            print("Before function call")
>            f()
>            print("After function call")
>        return wrapper
>                         
>    @simple_decorator
>    def say_hello():
>        print("Hello!")
>                         
>    say_hello()
>                         
>    ```
>
>    输出：
>
>    ```python
>    Before function call
>    Hello!
>    After function call
>                         
>    ```
>
>    在上面的例子中，装饰器`simple_decorator`修改了`say_hello`函数的行为，使其在调用前后都打印了额外的信息。

## 9.5 Function Composition

- In math, we can do something like: $log(sin(x))$
- In python, we can also done this

![image-20230914193812464](https://images.wu.engineer/images/2023/09/14/image-20230914193812464.png)

## 9.6 Lambda in functions

> `lambda`在Python中用于创建匿名函数，也就是没有名称的简短函数。`lambda`函数的语法结构非常简洁，只包含一个表达式。这种函数在需要短暂使用函数对象的地方非常有用。
>
> ### 基本语法：
>
> ```
> lambda arguments: expression
> ```
>
> 注意：
>
> - `lambda`定义的函数可以接受任意数量的参数，但只能有一个表达式。
> - 表达式的值就是该函数的返回值。

![image-20230914194846415](https://images.wu.engineer/images/2023/09/14/image-20230914194846415.png)

```python
>>> f = lambda a,b: lambda x: b(b(a))
>>> f('b', lambda a: a*3)(lambda a: a[:1])
'''
('b', lambda a: a*3) are two argument for the first lambda argument a and b
The argument a has character 'b', and the argument b has lambda expression 'lambda a: a*3'
(lambda a: a[:1]) is the argument for the second lambda argument x
So in this case, the expression b(b(a)) will be first executed
The result will be: 
- The inner b(a) = 'b' * 3 = 'bbb'
- The outer b() = 'bbb' * 3 = 'bbbbbbbbb'
Then, the lambda x will be executed, which is 'bbbbbbbbb'[:1] = 'b'
The output is 'b'
'''
```

![image-20230914195713852](https://images.wu.engineer/images/2023/09/14/image-20230914195713852.png)

![image-20230914195720379](https://images.wu.engineer/images/2023/09/14/image-20230914195720379.png)

![image-20230914195725746](https://images.wu.engineer/images/2023/09/14/image-20230914195725746.png)

# 9b. Sequences and Higher Order Functions

## 9b.1 `map()`: Scaling a Sequence

- Scale by 2 use iteration and recursion:
  - `[5,1,4,9,11,22,12,55]` to `[10,2,8,18,22,44,24,110]`

```python
def seqScaleI(seq, n):
	output = []
	for i in seq:
		output.append(i*n)
	return output
	
def seqScaleR(seq, n):
	if not seq:
		return seq
	return [seq[0]*n]+seqScaleR(seq[1:],n)
```

- Use `map()`:

```python
>>> lst = [5,1,4,9,11,22,12,55]
>>> list(map(lambda x:2*x, lst))
[10,2,8,18,22,44,24,110]
```

> **用途**：`map` 函数用于将指定函数应用于给定序列的每个元素。
>
> **语法**：
>
> ```python
> map(function, iterable, ...)
> ```
>
> - `function`: 是一个函数，将应用于每个项上。
> - `iterable`: 是一个或多个迭代对象。

- The map object is actually an ‘iterable’
  - After you took out items from the map object, the items will be ‘gone’
  - Conversion from a map object to a tuple or list for only once

```python
>>> tup = (1,-2,3)
>>> map1 = map(abs,tup)
>>> map1
<map object at 0x112e61438>
>>> type(map1)
<class 'map'>
>>> map1Tuple = tuple(map1)
>>> map1Tuple
(1,2,3)
>>> map1List = list(map1)
>>> map1List
[]
```

## 9b.2 `filter()`: filter out items

- Python’s `map()`: Apply a function `f` to every item `x` in the sequence
- Python’s `filter()`:
  - Apply a predicate function `f` to every item `x` in the sequence
    - A predicate is a function that return `True` or `False`
  - Return an iterable that
    - Keep the item if `f(x)` returns `True`
    - Remove the item otherwise

```python
>>> l = [1,2,3,'a',(1,2),('b',3)]
>>> filter(lambda x:type(x)==int, l)
<filter object at 0x112e618d0>
>>> list(filter(lambda x:type(x)==int, l))
[1,2,3]
>>> l = [1,2,'a',(1,2),6,('b',3),999]
>>> list(filter(lambda x:type(x)==int, l))
[1,2,6,999]
>>> list(filter(lambda x:type(x)==str, l))
['a']
>>> l2 = [1,4,5,-4,9,-99,0,32,-9]
>>> list(filter(lambda x:x<0, l2))
[-4,-99,-9]
```

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
print(list(result))  # 输出：[2, 4, 6]
```

## 9b.3 Counting a Sequence: Shallowly or Deeply

### Shallow Count

- How to count the number of element in a sequence?

```python
>>> lst = [5,1,4,9,11,22,12,55]
>>> len(lst)
8
```

- Of course we can use `len()`
- But what if we want to implement it ourselves?

```python
def seqCountR(seq):
	if not seq:
		reurn 0
	return 1+seqCountR(seq[1:])
```

- However, it’s shallow
- Total count = count of the **first item + count of the rest**
  - But the count of the first item is always 1

```python
>>> lst2 = [1,2,3,[4,5,6,7]]
>>> seqCountR(lst2)
4
>>> len(lst2)
4
```

### Deep Count

- Total count = count of the first item + count of the rest
  - But the count of the first item is only 1 if it is not a sequence
- `[1,2,3,4,[2,3,4],[1]]`
  - The first item has a count 1
- [[1,2],3,4,5]
  - The first item does not has a count 1 since it is a list
- How to check the first item is a list or not?
  - `type(seq[0]) == list`
- What to do if the first item is a sequence?
  - recursively compute `deepcount()` of the first item

```python
def deepcount(seq):
	if seq == []:
		return 0
	elif type(seq) != list:
		return 1
	else:
		return deepcount(seq[0]) + deepcount(seq[1:])
```

![image-20231003162600192](https://images.wu.engineer/images/2023/10/03/image-20231003162600192.png)

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

## 9b.4 Copy sequence shallowly or deeply

### `copy()` and `DeepCopy()`

- `copy()`

```python
>>> l = [1,2,3,[1,2],[2,3,4,[1,2,3]],[3,4,5]]
>>> l2 = l.copy()
>>> l2
[1,2,3,[1,2],[2,3,4,[1,2,3]],[3,4,5]]
>>> l[3][0] = 999
>>> l2
[1,2,3,[999,2],[2,3,4,[1,2,3]],[3,4,5]]
>>> l
[1,2,3,[999,2],[2,3,4,[1,2,3]],[3,4,5]]
```

- `DeepCopy()`

```python
>>> l2 = deepMap(lambda x:x.copy() if type(x)==list else x,l)
>>> l2
[1,2,3,[1,2],[2,3,4,[1,2,3]],[3,4,5]]
>>> l[3][0] = 999
>>> l
[1,2,3,[999,2],[2,3,4,[1,2,3]],[3,4,5]]
>>> l2
[1,2,3,[1,2],[2,3,4,[1,2,3]],[3,4,5]]
```

## 9b.5 `flatten()`: Just be shallow

```python
def flatten(seq):
	if seq == []:
		return seq
	elif type(seq) != list:
		return [seq]
	else:
		return flatten(seq[0]) + flatten(seq[1:])
		
l = [1,2,3,[1,2],[2,3,4,[1,2,3]],[3,4,5]]
print(flatten(l))
# Output: [1,2,3,1,2,2,3,4,1,2,3,3,4,5]
```



# 10. File I/O

## 10.1 Writing a file

![image-20230927205318692](https://images.wu.engineer/images/2023/09/27/image-20230927205318692.png)

```python
# Output:
This is my first lineThis is my second line
```

![image-20230927205411010](https://images.wu.engineer/images/2023/09/27/image-20230927205411010.png)

```python
def writing_something():
	with open('my_file.txt', 'w') as f:
		f.write('This is my first line' + '\n')
		f.write('This is my second line' + '\n')

write_something()
```

```python
# Output:
This is my fist line
This is my second line
```

### 10.1.1 Different file opening mode

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

## 10.2 Reading a file

### 10.2.1 Read the whole file

![image-20230927210425743](https://images.wu.engineer/images/2023/09/27/image-20230927210425743.png)

Use the function `split()` to separate the string into a list of strings by a separater

- If you do not put any argument for `split()`, the default separators are space and newline `\n`

```python
>>> with open('student_marks.txt') as f:
	data = f.read() # Read the whole file into the variable 'data'
>>> data
'John 70\nMary 50\nJoe 67\nFrank 90\nGru 99\nKiki 63'
# \n is new line character
>>> data.split()
['John', '70', 'Mary', '50', 'Joe', '67', 'Frank', '90', 'Gru', '99', 'Kiki', '63']
```

- Extract all the scores

```python
>>> data.split()
['John', '70', 'Mary', '50', 'Joe', '67', 'Frank', '90', 'Gru', '99', 'Kiki', '63']
>>> max(data.split())
'Mary'
>>> all_score = [int(i) for i in data.split()[1::2]] # Starting from the second position and step two
>>> all_score
[70, 50, 67, 90, 99, 63]
>>> max(all_score)
99
```

- Reading one whole file into a string is not ‘healthy’
  - Your file can be a few MB or even GB
  - Then this line of code will run in a very long time, may even end in crashing the whole program or even the system
  - Better way to do is to read the file line-by-line

### 10.2.2 Read the file line-by-line

```python
def read_line_by_line():
	with open('student_marks.txt') as f:
		for line in f:
			print(line)
# Output:
John 70
Mary 50
Joe 67
Frank 90
Gru 99
Kiki 63
```

- If do it in Python shell:

```python
>>> with open('student_marks.txt') as f:
		for line in f:
			print(line)
			
'John 70\n'
'Mary 50\n'
'Joe 67\n'
'Frank 90\n'
'Gru 99\n'
'Kiki 63\n'
```

- The file variable `f` is iterable
- When do it in Python Shell, annoying newline character `\n` consist

> 当你使用`print`函数打印字符串时，它默认会添加一个换行符。而当你从文件读取每一行时，每行本身就包含一个换行符。因此，当你直接打印读取的行时，它会显示两个换行符。
>
> 为了避免打印额外的换行符，你可以使用`str.strip()`方法来去除每行末尾的换行符。这样，`print`函数只会在打印后添加一个换行符。
>
> 这是修改后的代码：
>
> ```python
> with open('student_marks.txt') as f:
>     for line in f:
>         print(line.strip())
> ```
>
> 通过这种方式，输出的结果不会有额外的换行符。

### 10.2.3 `rstrip()`: Strip characters on the right

```python
>>> with open('crude-birth-rate.csv') as f:
		line1 = f.readline().rstrip('\n')
		line2 = f.readline().rstrip('\n')
		line3 = f.readline().rstrip('\n')
		print(line1)
		print(line2)
		print(line3)
year,level_1,value
1960,Crude Birth Rate,37.5
1961,Crude Birth Rate,35.2
```

> `rstrip()` 是一个Python字符串方法，用于删除字符串末尾的指定字符。当不传递任何参数给该方法时，它默认会删除字符串末尾的所有空白字符，其中包括空格、制表符、换行符和回车符。
>
> 示例：
>
> 1. **删除末尾空白字符**：
>
>    ```python
>    text = "Hello, World!   \n"
>    stripped_text = text.rstrip()
>    print(stripped_text)  # 输出："Hello, World!"
>    ```
>
> 2. **删除末尾特定字符**： 如果你提供了一个参数，`rstrip()` 将会删除字符串末尾的所有这些指定字符。
>
>    ```python
>    text = "example.com///"
>    stripped_text = text.rstrip('/')
>    print(stripped_text)  # 输出："example.com"
>    ```
>
> 注意：`rstrip()` 只会删除字符串**末尾**的字符，并不会删除字符串中间的字符。此外，它返回一个新的字符串（因为字符串在Python中是不可变的），并不会修改原始字符串。

### 10.2.4 String `rstrip()` and `split()`

```python
>>> string = '555555 Hello Everybody!!! 55555'
>>> string.rstrip('5')
'555555 Hello Everybody!!! '
>>> string.lstrip('5')
' Hello Everybody!!! 55555'
>>> string.lstrip('5').rstrip('5')
' Hello Everybody!!! '
>>>
>>> string.split()
['555555', 'Hello', 'Everybody!!!', '55555']
>>> string.split('o')
['555555 Hell', 'Everyb', 'dy!!! 55555']
```

> 1. **strip()**:
>
>    - **目的**：删除字符串的首尾字符。
>
>    - **默认行为**：如果没有指定任何参数，它将删除字符串的首尾空白字符（如空格、制表符、换行符等）。
>
>    - **使用方法**：
>
>      ```python
>      text = "  Hello, World!  "
>      stripped_text = text.strip()
>      print(stripped_text)  # 输出："Hello, World!"
>      ```
>
>    - 如果指定了参数，它将删除字符串首尾的所有这些指定字符：
>
>      ```python
>      text = "###Hello, World!###"
>      stripped_text = text.strip('#')
>      print(stripped_text)  # 输出："Hello, World!"
>      ```
>
> 2. **split()**:
>
>    - **目的**：将字符串分割成多个子字符串。
>
>    - **默认行为**：如果没有指定任何参数，它将按空白字符（如空格、制表符、换行符等）来分割字符串。
>
>    - **使用方法**：
>
>      ```python
>      text = "Hello, World! How are you?"
>      split_text = text.split()
>      print(split_text)  # 输出：['Hello,', 'World!', 'How', 'are', 'you?']
>      ```
>
>    - 如果指定了分隔符作为参数，它将使用该分隔符来分割字符串：
>
>      ```python
>      text = "apple,banana,grape"
>      split_text = text.split(',')
>      print(split_text)  # 输出：['apple', 'banana', 'grape']
>      ```
>
> **总结**：
>
> - `strip()` 用于删除字符串的首尾字符。
> - `split()` 用于将字符串分割成一个列表，其中包含多个子字符串。

### 10.2.5 Reading CSV Files

```python
>>> birth_file = open('crude-birth-rate.csv')
>>> birth_file_reader = csv.reader(birth_file)
>>> birth_data = list(birth_file_reader)
>>> pprint(birth_data)
```

Output:

![image-20231003143916618](https://images.wu.engineer/images/2023/10/03/image-20231003143916618.png)

# 11. Multi-dimensional Array

![image-20231003191808401](https://images.wu.engineer/images/2023/10/03/image-20231003191808401.png)

## 11.1 2-Dimensional Array in Python

```python
# 1-D array
>>> l = [1,2,3,4,5]
>>> l[3]
4
```

```python
# 2-D array
>>> m = [[1,2],[3,4]]
>>> m[0][0]
1
>>> m[0][1]
2
>>> m[1][0]
3
>>> m[1][1]
4
```

### Create an N x N identical matrix

```python
def identityMatrix(N):
	output = []
	for i in range(N):
		row = []
		for j in range(N):
			row.append(1 if i==j else 0)
		output.append(row)
	return output
	
pprint(identityMatrix(10))
```

- Output:

![image-20231003194202777](https://images.wu.engineer/images/2023/10/03/image-20231003194202777.png)

### 2-D looping

- Let’s say we just want to print 0 and 1

```python
def mTightPrint(m):
	for i in range(len(m)):
		line = ''
		for j in range(len(m[0])):
			line += str(m[i][j])
		print(line)

mTightPrint(m1)
```

- Output:

![image-20231003194346235](https://images.wu.engineer/images/2023/10/03/image-20231003194346235.png)

### R x C Zero Matrix

```python
def createZeroMatrix(r, c):
	output = []
	for i in range(N):
		row = []
		for j in range(N):
			row.append(1 if i==j else 0)
		output.append(row)
	return output
	
>>> m = identityMatrix(4,9)
>>> pprint(m)
[[0,0,0,0,0,0,0,0,0]
 [0,0,0,0,0,0,0,0,0]
 [0,0,0,0,0,0,0,0,0]
 [0,0,0,0,0,0,0,0,0]]
>>> m[1][3] = 9
>>> m[3][7] = 6
>>> pprint(m)
[[0,0,0,0,0,0,0,0,0]
 [0,0,0,9,0,0,0,0,0]
 [0,0,0,0,0,0,0,0,0]
 [0,0,0,0,0,0,0,6,0]]
```

### Matrix Addition, Multiplication, Transpose

```python
def sumMatrices(m1,m2):
	r = len(m1)
	c = len(m1[0])
	output = createZeroMatrix(r,c)
	for i in range(r):
		for j in range(c):
			output[i][j] = m1[i][j] + m2[i][j]
	return output
	
def multiplyMatrices(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    result = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                result[i][j] += m1[i][k] * m2[k][j]
    return result
    
def matrix_transpose(m):
    result = [[0 for j in range(len(m))] for i in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result
```

## 11.2 Tables

![image-20231003195910289](https://images.wu.engineer/images/2023/10/03/image-20231003195910289.png)

```python
>>> records = [['John', 'A1000000A', 90, 80, 100, 70],
			   ['Peter', 'A1000009D', 60, 100, 60, 90],
			   ['Paul', 'A1000003C', 80, 80, 70, 90],
			   ['Mary', 'A1000001B', 100, 70, 80, 80]]
>>> records[2][5] = 100
>>> pprint(records)
[['John', 'A1000000A', 90, 80, 100, 70],
 ['Peter', 'A1000009D', 60, 100, 60, 90],
 ['Paul', 'A1000003C', 80, 80, 70, 100],
 ['Mary', 'A1000001B', 100, 70, 80, 80]]
>>> colIndex = {'name': 0, 'SN':1, 'eng':2, 'math':3, 'sci':4, 'sos':5}
>>> records[3][colIndex['eng']] = 0
>>> pprint(records)
[['John', 'A1000000A', 90, 80, 100, 70],
 ['Peter', 'A1000009D', 60, 100, 60, 90],
 ['Paul', 'A1000003C', 80, 80, 70, 100],
 ['Mary', 'A1000001B', 0, 70, 80, 80]]
>>> records.append(['Seon', 'A1000004Z', 70, 80, 70, 80])
>>> pprint(records)
[['John', 'A1000000A', 90, 80, 100, 70],
 ['Peter', 'A1000009D', 60, 100, 60, 90],
 ['Paul', 'A1000003C', 80, 80, 70, 100],
 ['Mary', 'A1000001B', 0, 70, 80, 80]
 ['Seon', 'A1000004Z', 70, 80, 70, 80]]
>>> scoreSumEng = 0
>>> for i in range(len(records)):
		scoreSumEng += records[i][colIndex['eng']]
>>> print(scoreSumEng/len(records))
60.0
```

## 11.3 2D-Array with CSV

![image-20231003200814131](https://images.wu.engineer/images/2023/10/03/image-20231003200814158.png)

# 12. Object Oriented Programming (OOP)

## 12.1 Class and Instance

- Class:
  - Specifies the common behavior of entities
  - a *blueprint* that defines properties and behavior of an object
- Instance:
  - A particular object of entity of a given class
  - A concrete, usable object created from the blueprint

![image-20231004135135588](https://images.wu.engineer/images/2023/10/04/image-20231004135135588.png)

```python
>>> s = 'abc'
>>> type(s)
<class 'str'>
```

- The variable `s` above is an **instance** of the class `str`
- Each instance will store different values

> **class:**
>
> 使用class关键字定义一个类，后跟类名和冒号。类名通常采用驼峰命名法。
> ```python
> class MyClass:
>     pass
> ```
> **instance:**
> 类的对象或实例是根据类定义创建的实体。可以使用类名和括号来创建它，就像调用函数一样。
>
> ```python
> obj = MyClass("Some value")
> ```
>
> **attribute:**
>
> 属性是与对象关联的变量。它们表示对象的状态或数据。
>
> 类中可以有两种类型的属性：实例属性和类属性。
>
> 实例属性：与特定的对象实例关联。每个对象实例都可以有其自己的值。
>
> ```python
> class MyClass:
>     def __init__(self, value):
>         self.instance_attribute = value
> ```
> 类属性：与类自身关联，而不是实例。所有对象实例共享同一个类属性。
>
> ```python
> class MyClass:
>     class_attribute = "I'm a class attribute"
> ```
> **method:**
>
> 方法是与对象关联的函数，定义了对象可以执行的操作。
> 类的方法需要至少一个参数，通常命名为self，它引用对象实例本身。
> ```python
> class MyClass:
>     def my_method(self):
>         print("This is a method!")
> ```
>
> **构造函数 `__init__`:**
>
> 当创建类的新对象时，__init__ 方法会自动调用。它常用于初始化对象的属性。
> ```python
> class MyClass:
>     def __init__(self, value):
>         self.attribute = value
> ```

```python
class StudentRecord():
    # __init__ 函数类似于C++中的构造函数，当创建类的新对象时，构造函数会自动调用。
    def __init__(self):
        self.name = ''
        self.sn = ''
        self.gender = ''
        self.year = 0
        self.eng = 0
        self.math = 0
        self.sci = 0
        self.ss = 0
```

- In a student record, we want to store name, student number...
    - These are created automatically using the class above if a new object is created

### `self` variable

- Every class definition has access to a `self` variable
- `self` is a reference to the entire instance
- `self` variable will not disappear when the function exits
- The variable “name” will disappear after the completion of the function `__init__()`
- The variable “self.name” will remain after the completion of the function `__init__()`

### `__init__()`

- `def __init__(self):`
  - called when the object is first initialized
  - `self` argument is a reference to the object calling the method
  - It allows the method to reference properties and other methods of the class
- Special methods have `__` in front and behind the name

### Create an Instance

```python
alan = StudentRecord()
alan.name
```

- When you create a new instance, the **constructor** function is called
  - aka., `__init__()`

### Store values into an instance

```python
alan.name = 'Alan'
alan.sn = 'A1000001A'
alan.gender = 'M'
alan.eng = 90
alan.math = 100
alan.sci = 80
alan.ss = 10
```

### Initialization the object through constructor

```python
class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
myAcc = BankAccount('Alan', 1000)
johnAcc = BankAccount('John Wick', 100000000)
myAcc.name # Output: Alan
myAcc.balance # Output: 1000
myAcc.balance += 999
myAcc.balance # Output: 1999
```

## 12.2 Methods

```python
class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Money not enough! You do not have ${amount}")
            return 0
        else:
            self.balance -= amount
            return amount
    def showBalance(self):
        print(f'Your balance is ${self.balance}')
```

```python
>>> myAcc = BankAccount('Alan', 1000)
>>> myAcc.showBalance()
Your balance is $1000
>>> myAcc.withdraw(123)
123
>>> myAcc.showBalance()
Your balance is $877
>>> myAcc.withdraw(99999)
Money not enough! You do not have $99999
0
```

## 12.3 Inheritance

> 一个类可以继承另一个类的属性和方法，使代码重用变得简单。
> ```python
> class ParentClass:
>     pass
> 
> class ChildClass(ParentClass):
>     pass
> ```

```python
class Vehicle:
    def __init__(self, pos):
        self.pos = pos
        self.velocity = (0,0)
    def setVelocity(self, vx, vy):
        self.velocity = (vx, vy)
    def move(self):
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
        print(f"Move to {self.pos}")

class Sportscar(Vehicle):
    def turnOnTurbo(self):
        print("VROOOOOOM...")
        self.velocity = (self.velocity[0]*2, self.velocity[1]*2)
        print(f'Velocity increased to {self.velocity}')
```

### Change the initialization of the inheritance

1. Overriding. Redefining the method will override the one in Vehicle
2. Calling super class. Redefine a constructor, but call the constructor in super() (Vehicle class) instead

```python
class Lorry(Vehicle):
    # Overriding
    def __init__(self, pos):
        self.pos = pos
        self.velocity = (0,0)
        self.cargo = []
        
class Lorry(Vehicle):
    # Call super class
    def __init__(self, pos):
        super().__init__(pos)
        self.cargo = []
```

### `super()`

A way to access a method in your parent/higher classes

- Usually we prefer use `super()` because no duplication of code
- Calling super class: redefine a constructor, but call the constructor in `super()` instead

> super() 函数在Python中用于调用父类（或超类）的方法。它常用于两种情况：覆盖类方法时，以及多重继承中。使用 super() 可以确保父类中的适当方法被调用，特别是在存在多个继承层次或多重继承的情况下。
>
> 为什么要使用 super()?
> 当你在子类中重写某个方法，但仍然希望调用父类中的原始版本时，super() 就派上用场了。最常见的情况是在子类的 __init__ 方法中，你可能希望扩展或修改父类的初始化行为，而不是完全替换它。
>
> 在条件允许的情况下，优先使用super函数而不是重载

### Overriding

- When you re-define a same method that was in your parent class
- You own class will call your new re-defined method
  - Instead of your parent’s one

![image-20231004141616027](https://images.wu.engineer/images/2023/10/04/image-20231004141616027.png)

## 12.4 Multiple Inheritance

- We have a vehicle and a cannon class, now we want to create a tank class, which is inheritance from both vehicle and cannon class

![image-20231004141809455](https://images.wu.engineer/images/2023/10/04/image-20231004141809455.png)

- Which constructor should tank class call?

```python
class Cannon:
	def __init__(self):
		self.numAmmo = 0
			
class Vehicle:
	def __init__(self):
		self.pos = pos
		self.velocity = (0,0)
```

- Wee need to call BOTH:

```python
class Tank(Vehicle, Cannon):
	def __init__(self):
		Vehicle.__init__(self, pos)
		Cannon.__init__(self)
```

- In case we want to use use Cannon and Bisarca class to build BattleBisarca class, which `load()` function should we called from? Bisarca or Lorry?

![image-20231004142145869](https://images.wu.engineer/images/2023/10/04/image-20231004142145869.png)

- The nearest one will be called

![image-20231004142201808](https://images.wu.engineer/images/2023/10/04/image-20231004142201808.png)

- Complication arises when the same method is available in two distinct superclasses

- Diamond inheritance

  > “Diamond inheritance”（有时也被称为“diamond problem”或“diamond paradox”）是一个在面向对象编程中的常见问题，特别是在支持多重继承的语言中，如C++。这个问题描述了当两个基类继承自一个公共基类，然后另一个类从这两个派生类继承时，可能会出现的继承冲突。

![image-20231004142304906](https://images.wu.engineer/images/2023/10/04/image-20231004142304906.png)

- MI causes more trouble sometime because you may call the unexpected method in a complicated inheritance structure
- Recommendation is, only use MI if the parents are very different
  - e.g. Vehicle and Cannon
  - Or Tablet + calling device = smart phone

## 12.5 Private vs Public

- add `__` before the method name to convert the method from public to private
- The function can be used inside of the class but cannot be called from the outside

![image-20231004142739350](https://images.wu.engineer/images/2023/10/04/image-20231004142739350.png)

- However, you can still add `_` and the class name to access it

```python
>>> myDadTruck._Bisarca__convertCargo()
['Sportcar', 'Lorry']
```

### Private Methods

- Originally, in  a low of other OOP Languages, a private method/variable will NOT be accessible by anyone other than the class itself

- The purpose is to prevent any programmers to access the method/variable in a wrong way

  - E.g. directly change the balance of a bank account like

    ```python
    myAcc.balance = 10000000
    ```

- However, Python does not have that “full protection”

## 12.6 Conclusions

### Benefits of OOP

- Pros:
  - Simplification of complex, possibly hierarchical structures
  - Easy reuse of code
  - Easy code modifiability
  - Intuitive methods
  - Hiding of details through message passing and polymorphism
- Cons:
  - Overhead associated with the creation of classes, methods and instances

![image-20231004143243118](https://images.wu.engineer/images/2023/10/04/image-20231004143243118.png)

> Python 支持 OOP，但它并不是一个“纯粹”的面向对象编程语言。Python 也支持其他编程范式，例如过程式编程和函数式编程。这使得 Python 成为一种多范式的编程语言，允许开发者选择适合他们问题的编程风格。

# 13. Image Processing (Optional)



# 14. Order of Growth and Memoization

## 14.1 Fibonacci

> 对于算法，"running time"（运行时间）和"running space"（运行空间）是两个关键的度量指标，用于评估算法的效率。
>
> 1. **Running Time (运行时间)**：
>    - 描述了算法执行所需的时间，常常与输入大小（通常用 �*n* 表示）相关。
>    - 运行时间经常使用“大O表示法”（Big O notation）来描述，它给出了算法性能的上界。
>    - 常见的时间复杂度有：�(1)*O*(1)（常数时间）、�(log⁡�)*O*(log*n*)（对数时间）、�(�)*O*(*n*)（线性时间）、�(�log⁡�)*O*(*n*log*n*)、�(�2)*O*(*n*2)、�(�3)*O*(*n*3) 以及 �(2�)*O*(2*n*)，等等。
> 2. **Running Space (运行空间)**：
>    - 描述了算法在执行过程中所需的额外存储空间（不包括输入数据本身的存储空间）。
>    - 与运行时间类似，运行空间通常也使用“大O表示法”来描述。
>    - 常见的空间复杂度有：�(1)*O*(1)（常数空间）、�(log⁡�)*O*(log*n*)、�(�)*O*(*n*)（线性空间）、等等。
>
> 算法的运行时间和运行空间如何增长，取决于算法的设计和实现。某些算法可能会牺牲空间来获得更快的速度（即使用更多的内存来减少计算时间），而其他算法可能会做相反的选择。

1. **递归方法**：
   - **时间复杂度**：简单的递归算法具有指数级的时间复杂度，即 $O(2^n)$。这是因为每一个元素都被计算两次。
   - **空间复杂度**：由于递归的深度是 $n$，空间复杂度为$O(n)$。这主要是因为每次递归调用都会在调用栈上消耗空间。
2. **循环方法 (迭代)**：
   - **时间复杂度**：循环方法通常使用两个变量来保存前两个斐波那契数，并用它们来计算下一个斐波那契数。这种方法只需要线性的时间，即 $O(n)$。
   - **空间复杂度**：由于我们只需要保存前两个斐波那契数，空间复杂度为常数，即 $O(1)$。

![image-20231004144604165](https://images.wu.engineer/images/2023/10/04/image-20231004144604165.png)

## 14.2 Searching in a list of $n$ items

### Linear search

- \# comparison proportional to $n$

- Because in average, the expected number search is $n/2$

### Binary Search

- \# comparisons proportional to $log(n)$
- Because we divide the list into half for at most $log(n)$ items

> **二分搜索**（也称为二分查找或折半查找）是一种在排序数组中查找特定元素的算法。每次迭代，它都会将搜索的区间减半，直到找到所需的元素或搜索区间为空。
>
> 1. **Running Time (运行时间)**：
>
>    - **时间复杂度**：每次都将搜索区间减半，因此需要 log⁡�log*n* 次迭代来缩小到只包含一个元素的区间。因此，时间复杂度是 $O(log(n))$。
>
> 2. **Running Space (运行间)**：
>
>    - **空间复杂度**：二分搜索算法不需要额外存储整个数组或其部分，只需要几个指针或索引来跟踪当前的搜索范围（例如，low, high）。因此，空间复杂度是$O(1)$，也就是常数空间。
>
> 3. **为什么时间复杂度是 $O(log(n))$？**
>
>    每次迭代，我们都会将搜索的范围减少一半。这意味着，经过第一次迭代后，搜索范围减少到原来的一半；第二次迭代后，减少到原来的四分之一；第三次迭代后，减少到原来的八分之一，依此类推。
>
>    假设我们最多需要 $k$ 次迭代来找到目标值或确定目标值不在数组中。在这 $k$ 次迭代后，搜索范围最多被减少到原始大小的 $1/2^k$。这意味着原始大小 $n$ 最多减少到 $n/2^k$。
>
>    为了确定 $k$ 的最大值，我们可以设 $n/2^k=1$（当搜索范围减少到1时，搜索结束）。从中解出 $k$，我们得到 $k=log_2n$。
>
>    因此，我们最多需要 $log_2n$ 次迭代，所以二分搜索的时间复杂度是 $O(log\ n)$。

### Bubble Sort & Merge Sort

```python
def bubble(my_list):
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            
def bubbleSort(my_list):
    for i in range(len(my_list)-1):
        bubble(my_list)
        
my_list_1 = [38,2,10,3,1]
bubbleSort(my_list_1)
print(my_list_1)
```

> 冒泡排序是一种简单的排序算法，其基本思想是：通过比较相邻的两个元素并进行交换（如果它们的顺序是错误的），从而将最大（或最小）的元素“浮动”到其正确的位置。这个过程重复执行，每次减少需要考虑的未排序元素的数量，直到整个列表被排序。
>
> 1. `bubble` 函数：
>    - 它遍历列表，并对相邻的两个元素进行比较。如果当前元素大于其下一个元素，则交换它们。这确保了在经过一次完整的迭代后，最大的元素会被移动到列表的末尾。
>    - 请注意，这个函数只执行一次迭代，并不保证完全排序整个列表。
> 2. `bubbleSort` 函数：
>    - 它反复调用 `bubble` 函数，确保整个列表被排序。
>    - 对于长度为 $n$ 的列表，它会调用 `bubble` 函数 �−1*n*−1 次，确保每个元素都到达其正确的位置。
>
> 现在，考虑你提供的 `my_list_1` 示例：
>
> 初始列表为: [38,2,10,3,1]
>
> - **第1次**调用 `bubble` 后: [2,10,3,1,38]
> - **第2次**调用 `bubble` 后: [2,3,1,10,38]
> - **第3次**调用 `bubble` 后: [2,1,3,10,38]
> - **第4次**调用 `bubble` 后: [1,2,3,10,38]
>
> 在4次迭代后，列表被完全排序。因此，`print(my_list_1)` 的输出是: [1,2,3,10,38]
>
> 要注意的是，虽然这个冒泡排序实现是正确的，但它不是最优的。在最坏情况下，冒泡排序的时间复杂度为 $O(n^2)$，其中 $n$ 是列表的长度。这意味着，对于大的输入数据，这个算法可能会变得非常慢。

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    # 分解步骤
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # 递归排序
    left = merge_sort(left)
    right = merge_sort(right)

    # 合并步骤
    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # 如果有剩余的元素，将它们添加到结果中
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged
```

> **归并排序（Merge Sort）**是一种分而治之的排序算法。它的基本思想是将一个大问题分解成若干小问题，解决这些小问题，然后将它们的结果合并以解决原始的大问题。具体到排序问题，归并排序将一个大列表分成两个（或更多的）子列表，递归地排序这些子列表，然后合并它们以产生一个完全排序的列表。
>
> 以下是归并排序的基本步骤：
>
> 1. **分解**：将当前列表分成两个（大致）相等长度的子列表。
> 2. **递归排序**：递归地对这两个子列表进行归并排序。
> 3. **合并**：将两个已排序的子列表合并成一个单一的已排序列表。
>
> **合并**是归并排序中的关键步骤。当我们有两个已排序的子列表时，我们可以通过线性时间的操作来合并它们。
>
> **时间复杂度**： 归并排序的时间复杂度为 $O(nlog\ n)$，其中 $n$ 是要排序的元素数量。这使得归并排序在大多数情况下都比如冒泡排序、插入排序或选择排序等简单排序算法更有效。
>
> **空间复杂度**： 由于归并排序在合并过程中需要额外的空间来存储左右子列表的拷贝，其空间复杂度为$ O(n)$，其中 $n$ 是要排序的元素数量。

![image-20231004150005094](https://images.wu.engineer/images/2023/10/04/image-20231004150005094.png)

## 14.3 Optimization

### Memoization

![image-20231004150054034](https://images.wu.engineer/images/2023/10/04/image-20231004150054034.png)

- Create a dictionary to remember the answer if `fibm(n)` is computed before
- If the `ans` was computed before, get the answer from the dictionary
- Otherwise, compute the `ans` and put it into the dictionary for later use

```python
fibans = {}

def fibm(n):
	if n in fibans.keys():
		return fibans[n]
	if (n == 0):
		ans = 0
	elif (n == 1):
		ans = 1
	else:
		ans = fibm(n-1) + fibm(n-2)
	fibans[n] = ans
	return ans
```

### Recursion Removal

- Store all the answers in an array
- Add new `fib(i)`, as `fib(i-1) + fib(i-2)`

- And only keep `fib(n-1)` and `fib(n-2)`

```python
def fibi(n):
	if n<3:
		return 1
	fibminus1, fibminus2 = 1,1
	for i in range(3, n+1):
		fibminus2, fibminus1 = fibminus1, fibminus1 + fibminus2
	return fibminus1
```

# 15. Exceptions

## 15.1 Types of Errors

- There are two kinds of errors in Python:
  1. Syntax Errors
  2. Exceptions

### 15.1.1 Syntax Errors

```python
>>> while True print('Hello world')
SyntaxError: invalid syntax
```

### 15.1.2 Exceptions

- Errors detected during execution are called exceptions
- Examples:

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

#### NameError

```python
>>> 4 + spam*3
Traceback (most recent call last):
	File "<pyshell#4>", line 1, in <module>
		4 + spam*3
NameError: name 'spam' is not defined
```

#### TypeError

```python
>>> '2' + 2
Traceback (most recent call last):
	File "<pyshell#5>", line 1, in <module>
        '2' + 2
TypeError: Can't convert 'int' object to str implicitly
```

#### ValueError

```python
>>> int('one')
Traceback (most recent call last):
	File "<pyshell#2>", line 1, in <module>
		int('one')
ValueError: invalid literal for int() with base 10: 'one'
```

#### ZeroDivisionError

```python
>>> 10 * (1/0)
Traceback (most recent call last):
	File "<pyshell#3>", line 1, in <module>
		10 * (1/0)
ZeroDivisionError: division by zero
```

#### Other Common Errors

![image-20231004224533019](https://images.wu.engineer/images/2023/10/04/image-20231004224533019.png)

## 15.2 Handling Exceptions

1. Use Guard Clauses
2. Use Try-Except-Else constructs

### 15.2.1 Guard Clauses

- Guard is a Boolean expression that must evaluate to `True` if the program execution is to continue in the branch in question

#### Raising Exceptions

- The `raise` statement allows the programmer to force a specific exception to occur

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
	File "<stdin>", line 1, in ?
NameError: HiThere
```

```python
def add_two_integers(x,y):
    if not isinstance(x,int):
        raise TypeError('First argument must be of type integer')
    if not isinstance(y,int):
        raise TypeError('Second argument must be of type integer')
    return x+y
```

```python
def add_two_numbers(x,y):
    if not isinstance(x,(int,float)): # Checking for multiple types
        raise TypeError('First argument must be numerics')
    if not isinstance(y,(int,float)):
        raise TypeError('Second argument must be numerics')
    return x+y
```

#### Use with caution

- Python can raise exceptions without explicit guard clauses
- Checking for a specific exception may consume resources
  - Especially if it is done within a loop with several iterations

### 15.2.2 Try-Except-Else Constructs

- The simplest way to catch and handle exceptions is with a try-except block:

```python
x, y = 5, 0
try:
	z = x/y
except ZeroDivisionError:
	print('divide by zero')
```

- The `try` clause is executed
- If an exception occurred, skip the rest of the `try` clause, to a matching `except` clause
- If no exception occurs, the `except` clause is skipped (go to the `else` clause, if it exists)
- The `finally` clause is always executed before leaving the `try` statement, whether an exception has occurred or not

#### Try-Except

- A `try` clause may have more than 1 `except` clause, to specify handlers for different exception
- At most one handler will be executed
- Similar to if-elif-else
- `finally` will always be executed

![image-20231004225801594](https://images.wu.engineer/images/2023/10/04/image-20231004225801594.png)

```python
def divide_test(x,y):
	try:
		result = x/y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print('result is', result)
	finally:
		print("executing finally clause")
		
>>> divide_test(2,1)
result is 2.0
executing finally clause

>>> divide_test(2,0)
division by zero!
executing finally clause

>>> divide_test("2","1")
executing finally clause
Traceback (most recent call last):
	File "<stdin>", line 1, in ?
	File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

#### Multiple Exceptions

```python
import math
def my_function(x,y):
	try:
		return math.log(x)/y
	except ValueError:
		print('First argument must be nonzero positive; returning nan')
		return float("NaN")
	except ZeroDivisionError:
		print('Second argument must be nonzero; returning nan')
		return float("NaN")
```

```python
import math
def my_function_1(x,y):
	try:
		return math.log(x)/y
	except (ZeroDivisionError, ValueError):
		print('First argument must be nonzero positive; returning nan')
		print('Second argument must be nonzero; returning nan')
		return float("NaN")
```

#### Checking for ALL exceptions

```python
import math
def my_function(x,y):
	try:
		return math.log(x)/y
	except Exception as e:
		print(e)
		return float("NaN")
```

## 15.3 User-defined Exceptions

```python
class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
```

```python
try:
	raise MyError(2*2)
except MyError as e:
	print('Exception value:', e.value)
# Output: Exception value: 4
```

```python
raise MyError('oops!')
Traceback (most recent call last):
	File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'
```

## 15.4 Assertion

- If the statement in the assertion is False, then EXCEPTIONS
  - Raises an `AssertionError`

> 在编程中，`assertion`（断言）是一种运行时的检查，用于测试程序中的某些假设是否为真。如果该假设为真，则程序继续执行；如果为假，则程序会引发一个特定的异常（在Python中是`AssertionError`）。
>
> 断言常用于调试和开发阶段，以确保程序的某些部分按预期运行。它们不应用于处理运行时错误，因为断言可以在全局优化标志下被禁用。
>
> 在Python中，你可以使用`assert`语句来添加断言：
>
> ```python
> def add_positive_numbers(a, b):
>    	assert a > 0 and b > 0, "Both numbers should be positive"
>    	return a + b
> ```
>
> 在上述函数中，`assert`语句检查两个数字是否都为正数。如果不是，它会引发一个`AssertionError`，并附带给定的错误消息 "Both numbers should be positive"。
>
> 需要注意的是，虽然断言在开发和调试时非常有用，但在生产代码中依赖断言来处理错误可能不是一个好主意，因为：
>
> 1. 断言可以通过使用`-O`（优化）标志来禁用Python解释器而被关闭。
> 2. 使用专门的异常处理机制（例如`try`/`except`块）更加明确和灵活。

# 16. Data Visualization

![image-20231005155338054](https://images.wu.engineer/images/2023/10/05/image-20231005155338054.png)

## 16.1 Numpy

- Create a list of numbers from 0 to pi(3.14) with split 0.1
- Without Numpy:

```python
x = [i/100 for i in range(0,314)]
```

- With Numpy:

```python
import numpy as np
x1 = np.arange(0, 3.14, 0.1)
```

- Split 100 elements for range(0,3.14) using Numpy:

```python
x2 = np.linspace(0,3.14,100)
```

## 16.2 Matplotlib

```py
import numpy as np
import matplotlib.pyplot as plt

x2 = np.linspace(0,3.14,100)
plt.plot(x2)
plt.show()
```

![image-20231005160511253](https://images.wu.engineer/images/2023/10/05/image-20231005160511253.png)

### Plotting cos(x)

- Without Numpy:

```python
y = [cos(i) for i in x1]
```

- With Numpy:

```python
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0,3.14,100)
y1 = np.cos(x1)
plt.plot(y1)
plt.show()
```

### More Curves

![image-20231005162030381](https://images.wu.engineer/images/2023/10/05/image-20231005162030381.png)

![image-20231005162036979](https://images.wu.engineer/images/2023/10/05/image-20231005162036979.png)

![image-20231005162043328](https://images.wu.engineer/images/2023/10/05/image-20231005162043328.png)

![image-20231005162053644](https://images.wu.engineer/images/2023/10/05/image-20231005162053644.png)

![image-20231005162107939](https://images.wu.engineer/images/2023/10/05/image-20231005162107939.png)

### Multiple Figures

```python
# Plot sin and cos functions
plt.subplot(211)
plt.plot(x, y1, "-g")
plt.title('Sine Curve')
plt.subplot(212)
plt.plot(x, y2, "--b")
plt.title('Cosine Curve')

# Limit the y axis to -1.5 to 1.5
plt.ylim(-1.5,1.5)
plt.show()
```

![image-20231005162258721](https://images.wu.engineer/images/2023/10/05/image-20231005162258721.png)

![image-20231005162304387](https://images.wu.engineer/images/2023/10/05/image-20231005162304387.png)

![image-20231005162315459](https://images.wu.engineer/images/2023/10/05/image-20231005162315459.png)

### Bar Chart

```python
N = 18
x = [i for i in range(0, N+1)]
y = [nChooseK(N,i) for i in range(0,N+1)]

plt.bar(x,y)
plt.show()
```

![image-20231005162425105](https://images.wu.engineer/images/2023/10/05/image-20231005162425105.png)

```python
plt.barh(x,y)
plt.show()
```

![image-20231005162444800](https://images.wu.engineer/images/2023/10/05/image-20231005162444800.png)

### Histogram

- Similar to bar chart, but a histogram groups numbers into ranges
- Bar charts has gap, but Histogram has no gaps

![image-20231005162623860](https://images.wu.engineer/images/2023/10/05/image-20231005162623860.png)

```python
N = 100000
def roll_dice():
	return random.randint(1,6)
	
dice_stat = []
for i in range(N):
	dice_stat.append(roll_dice()+roll_dice()+roll_dice())
    
plt.hist(dice_stat, 16) # 16 for number of bins
plt.show()
```

![image-20231005162835634](https://images.wu.engineer/images/2023/10/05/image-20231005162835634.png)

### Pie Chart

```python
labels = ['Python', 'Java', 'C++', 'C#', 'C', 'JavaScript']
sizes = [26.7, 22.6, 9.9, 9.4, 7.37, 6.9, 5.9, 11.23]

plt.pie(sizes, shadow=True, startangle=90)
plt.legend(labels, loc="best")

plt.axis('equal') # Otherwise, becomes "oval" chart
plt.title('Programming Languages Used in 2016')
plt.tight_layout()
plt.show
```

![image-20231005163125737](https://images.wu.engineer/images/2023/10/05/image-20231005163125737.png)

### Saving a graph

```python
fig.savefig('plot.png') # or,
fig.savefig('plot.pdf')
# Or any format that is supported by matplotlib
```

# 17. Algorithms (Optional)



# 18. Programming Design

## 18.1 Manage Complexity

### Establish Level of Complexity

![image-20231005164751076](https://images.wu.engineer/images/2023/10/05/image-20231005164751076.png)

## 18.2 Make Good Abstraction

### 1. Makes it more natural to think

![image-20231005164913415](https://images.wu.engineer/images/2023/10/05/image-20231005164913415.png)

### 2. Makes program easier to understand

![image-20231005164935522](https://images.wu.engineer/images/2023/10/05/image-20231005164935522.png)

### 3. Captures Common Patterns

![image-20231005165005357](https://images.wu.engineer/images/2023/10/05/image-20231005165005357.png)

### 4. Allows for code reuse

![image-20231005165022073](https://images.wu.engineer/images/2023/10/05/image-20231005165022073.png)

### 5. Hides irrelevant details (blackbox)

![image-20231005165045036](https://images.wu.engineer/images/2023/10/05/image-20231005165045036.png)

### 6. Separates specifications from implementations

![image-20231005165106129](https://images.wu.engineer/images/2023/10/05/image-20231005165106129.png)

### 7. Makes debugging easier

![image-20231005165130860](https://images.wu.engineer/images/2023/10/05/image-20231005165130860.png)

## 18.3 Program Design Top-down Approach

### Sequence of writing

![image-20231005165208271](https://images.wu.engineer/images/2023/10/05/image-20231005165208271.png)

### Formulate the problem

![image-20231005165308046](https://images.wu.engineer/images/2023/10/05/image-20231005165308046.png)

![image-20231005165303040](https://images.wu.engineer/images/2023/10/05/image-20231005165303040.png)

![image-20231005165314273](https://images.wu.engineer/images/2023/10/05/image-20231005165314273.png)

![image-20231005165320899](https://images.wu.engineer/images/2023/10/05/image-20231005165320899.png)

![image-20231005165327678](https://images.wu.engineer/images/2023/10/05/image-20231005165327678.png)

### Coping with changes

- What if the starting fare is increased to $3.2?
- What if 385m is increased to 400m?

### Avoid magic numbers

- It is a terrible idea to hardcode constants
  - Hard to make changes in the future
- Define abstractions to hide them

![image-20231005165459120](https://images.wu.engineer/images/2023/10/05/image-20231005165459120.png)
