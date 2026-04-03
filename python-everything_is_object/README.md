# Python: Everything is an Object

## 1 - Introduction

In this project, I answer what seems to be basic and easy questions about python objects. Those questions revealed some misconceptions I had about what an object is, what its id is, how it is stored in memory and what affected it or not.

---

## 2 - ID and Type

I had already learned the type() function to determine the type of an object ( Int, List, etc..) and the concept is known.
However the ID part wasn’t a thing that I really worked on, only with a similar concept with C language helped me to get the basics.
But even with that, a couple of errors made me search further about it. I found several interesting thing:


```python
a = 89
b = 89
print(type(a))   # <class 'int'>
print(id(a))     # e.g. 140234567891234
print(id(b))     # same as id(a) !
print(a is b)    # True
```

**Key findings:**

- For **small integers** (from `-5` to `256`), Python caches and reuses the same object. So if `a = 89` and `b = 89`, both variables point to the **same object in memory** — they share the same `id`.

- For **lists**, the behaviour depends on *how* you modify them:

```python
my_list = [1, 2, 3]
print(id(my_list))   # e.g. 140234500000001

my_list += [4]       # modifies in-place
print(id(my_list))   # same id — the object itself was modified

my_list = my_list + [5]  # creates a new object
print(id(my_list))       # different id — a brand new list was assigned
```

`+=` modifies the existing object (in-place), while `= list + [...]` creates a **new object** and rebinds the variable to it.

---

## 3 - Mutable Objects

A **mutable** object is one that can be modified after its creation — its content can change without creating a new object.

```python
my_list = [1, 2, 3]
print(id(my_list))   # e.g. 140234500000001
my_list.append(4)
print(id(my_list))   # same id — the list was mutated, not replaced
print(my_list)       # [1, 2, 3, 4]
```

Common mutable types in Python:

| Type | Mutable |
|------|---------|
| `list` | ✅ Yes |
| `dict` | ✅ Yes |
| `set` | ✅ Yes |
| `bytearray` | ✅ Yes |

> A simple rule of thumb: mutable objects are generally **containers** — they hold references to other objects and can be updated without being replaced.

---

## 4 - Immutable Objects

An **immutable** object cannot be modified after its creation. Any operation that appears to "change" it actually creates a **new object**.

```python
a = "hello"
print(id(a))      # e.g. 140234511111111

a = a + " world"
print(id(a))      # different id — a new string was created
print(a)          # "hello world"
```

```python
t = (1, 2, 3)
# t[0] = 99     # ❌ TypeError: 'tuple' object does not support item assignment
```

Common immutable types in Python:

| Type | Immutable |
|------|-----------|
| `int` | ✅ Yes |
| `float` | ✅ Yes |
| `str` | ✅ Yes |
| `tuple` | ✅ Yes |
| `bool` | ✅ Yes |
| `frozenset` | ✅ Yes |

> Because immutable objects can never change, Python can safely reuse them in memory — which is why small integers and short strings are often cached and shared across variables.

---

## 5 - How They Interact with Each Other

Understanding mutability becomes especially important when objects reference each other or are passed to functions.

### Assignment and references

In Python, variables are not boxes — they are **labels** pointing to objects. When you assign `b = a`, both labels point to the **same object**.

```python
a = [1, 2, 3]
b = a            # b points to the same list as a
b.append(4)
print(a)         # [1, 2, 3, 4] — a was also affected!
print(a is b)    # True
```

To avoid this, use a **copy**:

```python
b = a.copy()     # or list(a) or a[:]
b.append(99)
print(a)         # [1, 2, 3] — a is unchanged
print(a is b)    # False
```

### Function arguments

Python passes objects **by reference**. Mutable objects can therefore be modified inside a function:

```python
def add_item(lst):
    lst.append(99)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)   # [1, 2, 3, 99] — modified in place
```

Immutable objects, on the other hand, cannot be changed — any reassignment inside the function simply rebinds the local variable:

```python
def try_change(n):
    n = n + 10
    print("inside:", n)

x = 5
try_change(x)
print("outside:", x)   # 5 — unchanged
```

### A subtle trap with mutable default arguments

One classic Python gotcha: using a mutable object as a **default argument** in a function definition. The default is created **once**, not on every call.

```python
def append_to(element, lst=[]):   # ⚠️ dangerous!
    lst.append(element)
    return lst

print(append_to(1))   # [1]
print(append_to(2))   # [1, 2]  — not [2]!
```

The correct pattern:

```python
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

---

## Conclusion

Python's object model is both elegant and occasionally surprising. The key takeaways:

- **Everything in Python is an object**, with a type and an identity (`id`).
- **Mutable objects** (lists, dicts, sets) can be changed in place; their `id` stays the same.
- **Immutable objects** (ints, strings, tuples) cannot be changed; any "modification" produces a new object.
- Variables are **references**, not containers — understanding this prevents many subtle bugs when objects are shared or passed to functions.
