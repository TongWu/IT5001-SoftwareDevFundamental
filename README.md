# IT5001 - Software Development Fundamentals

## 0. Introductions

### 0.0 Disclaimer and References

- This repo is the self-organized warehouse for National University of Singapore, School of Computing, Course IT5001: Software Development Fundamentals.

- This is the self-written note for National University of Singapore, School of Computing, Course IT5001: Software Development Fundamentals. The materials and references used in this note are for revision and organization use only.

- > The content in this kind of block means which is not in the aspect of this course, which may from references, or self-understanding/translations. The understanding for them are not required under this course regulation.

- The most of the content and material used in this repo are referred from the National University of Singapore. Few of contents in the block as mentioned before, are referenced from the University of Manchester, Columbia University, website or/and self-organized. 

- **Do not share any content in this repo to anyone without permission, including course material, video, lab assignment and notes.**

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

#### Built-in

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

### 2.1 Abstraction

![image-20230912192717225](https://images.wu.engineer/images/2023/09/12/image-20230912192717225.png)

- Function is useful, especially when a code piece will be used few times
- User only needs to know input arguments and output data types
  - As known as ‘Blackbox’, it is not necessary for users to understand the code in each function

![image-20230912192957777](https://images.wu.engineer/images/2023/09/12/image-20230912192957777.png)

#### Type of functions

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

### 2.2 Python Modules and Packages

#### 2.2.1 Functions in Python

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

#### 2.2.2 Import Modules and Packages

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

#### 2.2.3 Namespaces: Importing Modules

**Import Single Module**

![image-20230912195105773](https://images.wu.engineer/images/2023/09/12/image-20230912195105773.png)

**Import Multiple Modules**

![image-20230912195157145](https://images.wu.engineer/images/2023/09/12/image-20230912195157145.png)

**Import Objects from Modules**

![image-20230912195248752](https://images.wu.engineer/images/2023/09/12/image-20230912195248752.png)

> 总结：
>
> 在导入整个模块时，会导入整个模块的namespace，这个namespace在global namespace当中。然而当导入一个模块中的某个或多个函数时，这些函数会被导入到global namespace。

### 2.3 User-Defined Functions

![image-20230912195454207](https://images.wu.engineer/images/2023/09/12/image-20230912195454207.png)

#### 2.3.1 Arguments

- Arguments is the input of the function, it allows function to receive data from the outside environment

![image-20230912200422206](https://images.wu.engineer/images/2023/09/12/image-20230912200422206.png)

##### Type of Arguments

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

#### 2.3.2 Return Statement

- It does two things
  1. Terminates the function
  2. Return statement pass the output of function to the calling function

![image-20230912200356522](https://images.wu.engineer/images/2023/09/12/image-20230912200356522.png)

![image-20230912200403892](https://images.wu.engineer/images/2023/09/12/image-20230912200403892.png)

#### 2.3.3 Function Tracing

##### Namespace

![image-20230912201313110](https://images.wu.engineer/images/2023/09/12/image-20230912201313110.png)

##### Tracing 1

![image-20230912201410351](https://images.wu.engineer/images/2023/09/12/image-20230912201410351.png)

![image-20230912201420789](https://images.wu.engineer/images/2023/09/12/image-20230912201420789.png)

##### Tracing 2

![image-20230912201541315](https://images.wu.engineer/images/2023/09/12/image-20230912201541315.png)

![image-20230912201550111](https://images.wu.engineer/images/2023/09/12/image-20230912201550111.png)

#### 2.3.4 Doc String

- Contains information about the function
  - Describes how to use the function
  - Can access it using help/doc methods

![image-20230912200531566](https://images.wu.engineer/images/2023/09/12/image-20230912200531566.png)

### 2.4 Pure Functions

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

## 3. Control Structure (Selections and Loops)

![image-20230912205854358](https://images.wu.engineer/images/2023/09/12/image-20230912205854358.png)

### 3.1 Selection

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

### 3.2 Repetition

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

### 3.3 Iteration

**The act of repeating a process with the aim of approaching a desired goal, target or result**

- There are three types of loops
  1. Must run exactly N times
  2. Run many number of times
  3. Run at most N times
     - Check all True (or check all False)
     - Find any True (or False)

#### 3.3.1 For loop (Must run exactly N times)

- Use iterable objects to repeatedly execute a series of tasks
- Number of repetitions are equal to number of items provided by iterable object

##### Iterable and Iterators

![image-20230912222536678](https://images.wu.engineer/images/2023/09/12/image-20230912222536678.png)

##### Built-in iterable: `range()`

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

#### 3.3.2 Run many number of times

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

#### 3.3.3 Run at most N times (check all True)

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

#### 3.3.4 When use `for` and `while`?

- `for`
  - You know how many times the loop will run
  - Namely, anything in the body of the loop will NOT change the number of times you repeat the loop
  - E.g., printing all the data in a spreadsheet
- `while`
  - You may not know how many times you need to repeat
  - The number of times is depended on the “condition”, in which, may change unpredictably inside the loop
  - E.g., while the player haven’t guess the right answer, keep guessing

### 3.4 `break` & `continue`

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

## 4. Functions Scope and Recursion

### 4.1 Scope

#### 4.1.1 Global & Local Variables

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

##### Global Variable

![image-20230913001202988](https://images.wu.engineer/images/2023/09/12/image-20230913001202988.png)

##### Global Variable vs. Local Variable

![image-20230913001239224](https://images.wu.engineer/images/2023/09/12/image-20230913001239224.png)

![image-20230913001314239](https://images.wu.engineer/images/2023/09/12/image-20230913001314239.png)

#### 4.1.2 Crossing Boundary (change global variable in the function)

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

### 4.2 Generator Functions

![image-20230913001719005](https://images.wu.engineer/images/2023/09/12/image-20230913001719005.png)

#### 4.2.1 Return vs. Yield

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

### 4.3 Calling Other Functions

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

#### 4.3.1 Stack

![image-20230913002638704](https://images.wu.engineer/images/2023/09/12/image-20230913002638704.png)

![image-20230913002643679](https://images.wu.engineer/images/2023/09/12/image-20230913002643679.png)

![image-20230913002704069](https://images.wu.engineer/images/2023/09/12/image-20230913002704069.png)

![image-20230913002711167](https://images.wu.engineer/images/2023/09/12/image-20230913002711167.png)

#### 4.3.2 Namespaces

![image-20230913010918426](https://images.wu.engineer/images/2023/09/12/image-20230913010918426.png)

![image-20230913010928747](https://images.wu.engineer/images/2023/09/12/image-20230913010928747.png)

> When the function is executed and returned the result value, the namespace of this function will be vanished.

### 4.4 Recursion

- A function that calls itself

- Solve a big problem by solving a smaller version of itself

  - > Divide and conquer

#### 4.4.1 Recursive Function

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

#### 4.4.2 Namespaces

![image-20230913011227729](https://images.wu.engineer/images/2023/09/12/image-20230913011227729.png)

![image-20230913011236255](https://images.wu.engineer/images/2023/09/12/image-20230913011236255.png)

## 5. Recursion VS. Iteration

### 5.1 Reversing a String

#### 5.1.1 Iterative Version 1

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

#### 5.1.2 Iterative Version 2

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

#### 5.1.3 Recursive Version

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

### 5.2 Code Refactoring

- Refactoring is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior.

![image-20230913210337455](https://images.wu.engineer/images/2023/09/13/image-20230913210337455.png)

### 5.3 Nested Functions

![image-20230913210544963](https://images.wu.engineer/images/2023/09/13/image-20230913210544963.png)

![image-20230913210551383](https://images.wu.engineer/images/2023/09/13/image-20230913210551383.png)

- Inner functions **can access** global variables **but cannot modify** them.

#### 5.3.1 Global Keyword

![image-20230913210657898](https://images.wu.engineer/images/2023/09/13/image-20230913210657898.png)

## 6. Bugs and Debugging

- Syntax Error
  - A syntax error is an error in the source code of a program. Since computer programs **must follow strict syntax** to compile correctly, any aspects of the code that do not conform to the syntax of the programming language will produce a syntax error

### 6.1 Debugging

- Means to remove errors from a program
- After debugging, the program is **not necessarily error-free**
  - It just means that whatever errors remain are harder to find
  - This is especially true for large applications

#### 6.2 IDLE Debugger

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

### 6.2 Common Types of Errors

![image-20230913212833106](https://images.wu.engineer/images/2023/09/13/image-20230913212833106.png)

![image-20230913212837957](https://images.wu.engineer/images/2023/09/13/image-20230913212837957.png)

![image-20230913212846231](https://images.wu.engineer/images/2023/09/13/image-20230913212846231.png)

![image-20230913212853484](https://images.wu.engineer/images/2023/09/13/image-20230913212853484.png)

![image-20230913212858595](https://images.wu.engineer/images/2023/09/13/image-20230913212858595.png)

![image-20230913212903939](https://images.wu.engineer/images/2023/09/13/image-20230913212903939.png)

### 6.3 Summary

- Compound data helps us to reason at a higher conceptual level
- Abstraction barriers separate usage of a compound data from its implementation
- Only functions at the interface should be used
- We can choose between different implementations as long as contract is fulfilled

## 7. Sequences



## 8. Anonymous Functions



## 9. High Order Functions



