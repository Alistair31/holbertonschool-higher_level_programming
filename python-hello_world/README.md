# Python String and Output Practice Scripts 🐍

This documentation provides detailed explanations and usage notes for a set of Python files focusing on string manipulation, printing outputs, and a fun "Easter egg". Each script is designed to help beginners understand core Python concepts.

---

## 2-print.py

This script demonstrates how to print a string with special characters, specifically quotes, using Python's `print` function.

```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

- **Purpose:** Teaches how to handle special characters (escaping quotes) within a string.
- **Key concept:** Escape sequences in strings.

**Output:**
```
"Programming is like building a multilingual puzzle
```

---

## 3-print_number.py

This script shows how to print an integer embedded within a string using formatted string literals (f-strings).

```python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

- **Purpose:** Prints an integer variable as part of a message.
- **Key concept:** f-string for inline variable substitution.

**Output:**
```
98 Battery street
```

---

## 4-print_float.py

This file prints a floating-point number with a specific formatting: two decimal places.

```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

- **Purpose:** Shows how to format floats in output.
- **Key concept:** f-string formatting for floats (`.2f` means two decimal places).

**Output:**
```
Float: 3.14
```

---

## 5-print_string.py

This script demonstrates string repetition and slicing using f-strings for formatted output.

```python
#!/usr/bin/python3
str = "Holberton School"
print(f"{str}{str}{str}")
print(f"{str:.9}")
```

- **Purpose:** Repeats a string three times, then prints the first nine characters.
- **Key concept:** String repetition and slicing with formatting.

**Output:**
```
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

---

## 6-concat.py

This file concatenates two strings with a space and then prints a welcome message.

```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

- **Purpose:** Combines two strings with a space and uses the result in a message.
- **Key concept:** String concatenation and formatted output.

**Output:**
```
Welcome to Holberton School!
```

---

## 7-edges.py

This script slices a string to obtain its first three letters, last two letters, and all but the first and last letters.

```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

- **Purpose:** Teaches string slicing operations.
- **Key concept:** Indexing and slicing in Python strings.

**Output:**
```
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

---

## 8-concat_edges.py

This script shows advanced string slicing and concatenation by selecting specific sections of a sentence and joining them in a new order.

```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:-17] + str[:6]
print(str)
```

- **Purpose:** Demonstrates complex slicing and concatenation to create a new message from existing string parts.
- **Key concept:** String slicing with start and end indices; combining non-contiguous segments.

**Breakdown:**
- `str[39:66]` → "object-oriented programming"
- `str[106:-17]` → "with very clear "
- `str[:6]` → "Python"

**Output:**
```
object-oriented programmingwith very clear Python
```

---

## 9-easter_egg.py 🎁

This script is a Python "Easter egg." When run, it prints "The Zen of Python" by Tim Peters, a set of aphorisms for writing good Python code.

```python
#!/usr/bin/python3
import this
```

- **Purpose:** Introduces users to Pythonic principles and culture.
- **Key concept:** Hidden Python modules ("Easter eggs").

**Output:**  
When run, this script prints the Zen of Python, such as:
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
```

---

## Comparison Table

| Filename              | Main Concept                   | Demonstrates                  | Output Example (short)                |
|-----------------------|-------------------------------|-------------------------------|---------------------------------------|
| 2-print.py            | Escape Sequences              | Printing special characters   | `"Programming is like building...`    |
| 3-print_number.py     | f-Strings                     | Number in strings             | `98 Battery street`                   |
| 4-print_float.py      | Float Formatting              | Two decimal places            | `Float: 3.14`                         |
| 5-print_string.py     | String Repetition/Slicing     | Repeat & slice strings        | `Holberton... Holberton`              |
| 6-concat.py           | String Concatenation          | Joining strings               | `Welcome to Holberton School!`        |
| 7-edges.py            | String Slicing                | Various slices                | `First 3 letters: Hol`                |
| 8-concat_edges.py     | Advanced Slicing/Concat       | Reordering string parts       | `object-oriented programming...`      |
| 9-easter_egg.py       | Python Culture                | Zen of Python                 | `Beautiful is better than ugly.`      |

---

## Summary

These scripts are excellent introductory exercises for learning how to manipulate strings, format outputs, and use unique Python features. They encourage experimentation with string operations and introduce some of the whimsical elements of Python's culture.
