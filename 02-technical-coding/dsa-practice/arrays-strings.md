# DSA Practice: Arrays & Strings

Core algorithmic patterns and fully solved Python implementations commonly tested in Accenture technical coding assessments.

---

## Pattern 1: Two Pointers (Valid Palindrome)

- **Problem**: Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
- **Code Solution (Python)**:
```python
def isPalindrome(s: str) -> bool:
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
```

---

## Pattern 2: Sliding Window (Maximum Sum Subarray of Size K)

- **Problem**: Given an array of integers and a number $k$, find the maximum sum of any contiguous subarray of size $k$.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
- **Code Solution (Python)**:
```python
def maxSubarraySum(arr, k):
    if len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

---

## Pattern 3: Hashing / Frequency Map (Two Sum)

- **Problem**: Find indices of two numbers in an array that add up to a target value.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
- **Code Solution (Python)**:
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```
