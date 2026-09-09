# Coding Round: Python — Complete Practice Bank

## What this is
The Accenture Coding Round (Stage 3) evaluates your hands-on problem solving, data structure manipulation, and algorithmic efficiency. Candidates can choose their preferred programming language (Python, Java, C++, C, JavaScript, or SQL). Python is widely chosen due to its concise syntax and rich standard library.

---

## Formula / Rule / Pattern & Shortcut

> [!TIP]
> ### The Dual-Pass Strategy (Brute-Force $\rightarrow$ Optimal)
> Always state your brute-force logic first (even mentally), write working code that passes base test cases, and then apply optimal data structures (Hash Maps for $O(1)$ lookup, Two Pointers for $O(N)$ array traversal, Sliding Window for substring problems).
> 
> *Why it works*: Partial credit exists in automated coding environments for correct solutions even if time complexity is sub-optimal. Securing a working solution first prevents 0-score timeouts.

---

## 10 Solved Coding Problems (Easy to Medium)

### Problem 1: Second Largest Element in Array
- **Task**: Given an array of integers, find the second largest distinct element without sorting the array.
- **Brute-Force ($O(N \log N)$)**: Sort array in descending order, return 2nd element.
- **Optimized Python Solution ($O(N)$ Time, $O(1)$ Space)**:
```python
def find_second_largest(arr):
    if len(arr) < 2:
        return -1
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else -1

# Test
print(find_second_largest([12, 35, 1, 10, 34, 1])) # Output: 34
```

---

### Problem 2: Valid Palindrome (Ignoring Special Characters & Case)
- **Task**: Check if a string is a palindrome considering only alphanumeric characters.
- **Optimized Python Solution ($O(N)$ Time, $O(1)$ Space)**:
```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Test
print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True
```

---

### Problem 3: Two Sum (Target Pair)
- **Task**: Return indices of two numbers that add up to a target.
- **Optimized Python Solution ($O(N)$ Time, $O(N)$ Space)**:
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9)) # Output: [0, 1]
```

---

### Problem 4: Move Zeroes to End
- **Task**: Move all 0s in an array to the end while maintaining relative order of non-zero elements.
- **Optimized Python Solution ($O(N)$ Time, $O(1)$ Space)**:
```python
def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums

# Test
print(move_zeroes([0, 1, 0, 3, 12])) # Output: [1, 3, 12, 0, 0]
```

---

### Problem 5: First Non-Repeating Character
- **Task**: Find the first non-repeating character in a string and return its index.
- **Optimized Python Solution ($O(N)$ Time, $O(1)$ Auxiliary Space)**:
```python
from collections import Counter

def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

# Test
print(first_uniq_char("accenture")) # Output: 0 ('a')
```

---

### Problem 6: Reverse Words in a Sentence
- **Task**: Reverse the order of words in a given string.
- **Python Solution ($O(N)$ Time, $O(N)$ Space)**:
```python
def reverse_words(s: str) -> str:
    words = s.strip().split()
    return " ".join(words[::-1])

# Test
print(reverse_words("  hello world  ")) # Output: "world hello"
```

---

### Problem 7: Maximum Subarray Sum (Kadane's Algorithm)
- **Task**: Find the contiguous subarray with the largest sum.
- **Optimized Python Solution ($O(N)$ Time, $O(1)$ Space)**:
```python
def max_sub_array(nums) -> int:
    max_so_far = current_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
    return max_so_far

# Test
print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6 ([4, -1, 2, 1])
```

---

### Problem 8: Longest Substring Without Repeating Characters
- **Task**: Find length of longest substring without duplicate characters.
- **Optimized Python Solution ($O(N)$ Time, $O(K)$ Space)**:
```python
def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = max_len = 0
    for right, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= left:
            left = char_map[ch] + 1
        char_map[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Test
print(length_of_longest_substring("abcabcbb")) # Output: 3 ("abc")
```

---

### Problem 9: Merge Two Sorted Arrays Without Extra Space
- **Task**: Merge two sorted arrays `nums1` and `nums2` in-place.
- **Python Solution ($O(M+N)$ Time, $O(1)$ Space)**:
```python
def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]
    return nums1

# Test
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)) # Output: [1, 2, 2, 3, 5, 6]
```

---

### Problem 10: Fibonacci Series (Dynamic Programming - Tabulation)
- **Task**: Compute Nth Fibonacci number efficiently.
- **Optimized Python Solution ($O(N)$ Time, $O(1)$ Space)**:
```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test
print(fib(10)) # Output: 55
```

---

## Where this appears in the real Accenture test
Appears in Stage 3: Coding Round (2 problems, 45 minutes total).

---

## Recommended videos
- [Naukri Code360 Accenture Interview Bundle](https://www.naukri.com/code360/interview-bundle/accenture) — Accenture coding practice bank.
