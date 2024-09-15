To complete the assignment "Exploring Python List Methods," here's a detailed guide for the methods specified in the assignment. You can use the structure below to create your document in Google Docs or Microsoft Word.

---

**Assignment Title: Exploring Python List Methods**

**Objective:**  
In this document, various methods associated with Python lists will be explained, including their descriptions, syntax, parameters, and return types.

---

### 1. **`append()`**

- **Description:**  
  Adds a single element to the end of the list.
  
- **Syntax:**  
  ```python
  list.append(element)
  ```
  - `element`: The item to be added to the list.

- **Return Type:**  
  `None` (modifies the original list in place).

- **Example:**
  ```python
  numbers = [1, 2, 3]
  numbers.append(4)
  print(numbers)  # Output: [1, 2, 3, 4]
  ```

---

### 2. **`extend()`**

- **Description:**  
  Extends the list by appending all elements from another iterable (such as a list or tuple).
  
- **Syntax:**  
  ```python
  list.extend(iterable)
  ```
  - `iterable`: Any iterable (list, tuple, set, etc.) whose elements will be added to the list.

- **Return Type:**  
  `None` (modifies the original list).

- **Example:**
  ```python
  numbers = [1, 2, 3]
  more_numbers = [4, 5]
  numbers.extend(more_numbers)
  print(numbers)  # Output: [1, 2, 3, 4, 5]
  ```

---

### 3. **`insert()`**

- **Description:**  
  Inserts an element at a specific position in the list.
  
- **Syntax:**  
  ```python
  list.insert(index, element)
  ```
  - `index`: The position at which the element is to be inserted.
  - `element`: The item to be inserted.

- **Return Type:**  
  `None` (modifies the original list).

- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  fruits.insert(1, 'orange')
  print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']
  ```

---

### 4. **`remove()`**

- **Description:**  
  Removes the first occurrence of the specified element from the list.
  
- **Syntax:**  
  ```python
  list.remove(element)
  ```
  - `element`: The item to be removed.

- **Return Type:**  
  `None` (modifies the original list).

- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  fruits.remove('banana')
  print(fruits)  # Output: ['apple', 'cherry']
  ```

---

### 5. **`pop()`**

- **Description:**  
  Removes and returns the element at the specified position (or the last element if no index is specified).
  
- **Syntax:**  
  ```python
  list.pop([index])
  ```
  - `index` (optional): The position of the element to be removed. If not specified, the last element is removed.

- **Return Type:**  
  The removed element.

- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  last_item = numbers.pop()
  print(last_item)  # Output: 4
  print(numbers)    # Output: [1, 2, 3]
  ```

---

### 6. **`clear()`**

- **Description:**  
  Removes all elements from the list, leaving it empty.
  
- **Syntax:**  
  ```python
  list.clear()
  ```

- **Return Type:**  
  `None` (modifies the original list).

- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  fruits.clear()
  print(fruits)  # Output: []
  ```

---

### 7. **`index()`**

- **Description:**  
  Returns the index of the first occurrence of the specified element.
  
- **Syntax:**  
  ```python
  list.index(element, [start], [end])
  ```
  - `element`: The item to search for.
  - `start` (optional): The position to start the search.
  - `end` (optional): The position to end the search.

- **Return Type:**  
  An integer (the index of the element).

- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  index = fruits.index('banana')
  print(index)  # Output: 1
  ```

---

### 8. **`count()`**

- **Description:**  
  Returns the number of times the specified element appears in the list.
  
- **Syntax:**  
  ```python
  list.count(element)
  ```
  - `element`: The item to count.

- **Return Type:**  
  An integer.

- **Example:**
  ```python
  numbers = [1, 2, 2, 3, 4]
  count = numbers.count(2)
  print(count)  # Output: 2
  ```

---

### 9. **`sort()`**

- **Description:**  
  Sorts the list in ascending order by default. You can also sort in descending order by using the `reverse` parameter.
  
- **Syntax:**  
  ```python
  list.sort(key=None, reverse=False)
  ```
  - `key` (optional): A function to customize the sort order.
  - `reverse` (optional): If `True`, the list is sorted in descending order.

- **Return Type:**  
  `None` (modifies the original list).

- **Example:**
  ```python
  numbers = [4, 2, 3, 1]
  numbers.sort()
  print(numbers)  # Output: [1, 2, 3, 4]
  ```

---

### 10. **`reverse()`**

- **Description:**  
  Reverses the elements of the list in place.
  
- **Syntax:**  
  ```python
  list.reverse()
  ```

- **Return Type:**  
  `None` (modifies the original list).

- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  numbers.reverse()
  print(numbers)  # Output: [4, 3, 2, 1]
  ```

---

### 11. **`copy()`**

- **Description:**  
  Returns a shallow copy of the list.
  
- **Syntax:**  
  ```python
  list.copy()
  ```

- **Return Type:**  
  A new list.

- **Example:**
  ```python
  numbers = [1, 2, 3]
  new_list = numbers.copy()
  print(new_list)  # Output: [1, 2, 3]
  ```