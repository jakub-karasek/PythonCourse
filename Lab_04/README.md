# ASSIGNMENT 4

## Conversion of a Jupyter Notebook file to Python.

Write a program that reads a .ipynb file (actually in JSON format), the name of which will be provided as a command-line argument. After loading, the list of cells should be transformed into a list of strings in the following way: each line of text from a "markdown" cell should be preceded by a comment character # , while from "code" cells, only lines with the source code should be kept, omitting everything else (especially any output). The translation should be done using the map function (the content of one cell translates to one string—presumably multiline). To concatenate the list of lines of text, you can use the construction "separator".join(list). It is also worth adding additional newline characters "\n" here and there. Additionally, at the beginning of the text coming from each markdown (or code), a special comment "#%%\n" can be added—popular IDEs treat Python files with such comments as if they consist of cells for the next execution. The resulting strings should be saved to an output file with the same name as the input file, but with the .py extension instead of .ipynb. You can use the construction print(*list, file=file) for saving, possibly with the appropriate sep= and/or end=. The resulting file should be a valid Python file.

In addition to the above, the program should print the number of exercises present in the notebook's content. Exercises are found in markdown cells that contain the string # Exercise in the first line. This part should be done using filter or reduce. If you use filter, remember that instead of creating a list just to count its length, you can use a trick similar to counting vowels in the example with sorted(..., key=...). If you want to use reduce, you should add 1 or 0 to the counter depending on the result of the "exercise" test (or the result of the test itself—using a similar trick).

For the example input file file.ipynb (sample content):

```code
<markdown cell>
   This program prints "A kuku".
<code cell>
   <code> 
      print("A kuku")
   <output>
      A kuku
<markdown cell>
   ### Exercise 1
   Write a program that prints "Ala has a cat" twice on separate lines.
<code cell>
   <code> 
     print("Ala has a cat")
     print("Ala has a cat")
   <output>
     Ala has a cat
     Ala has a cat
```

an output file file.py should be created with the following content:

```python
# This program prints "A kuku".

print("A kuku")

# ### Exercise 1
# Write a program that prints "Ala has a cat" twice on separate lines.

print("Ala has a cat")
print("Ala has a cat")
```

The program should also print:

```
Number of exercises: 1
```

The details of the task specification should be refined independently, for example, by inspecting the notebook file from today's classes.

## Running script
You can run script with
python3 ipynb_to_py.py [path_to_input_file]
for example:
```bash
python3 ipynb_to_py.py Zajecia4.ipynb
```

