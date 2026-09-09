# Coding Round: JavaScript — Complete Practice Bank

## What this is
JavaScript coding problems in Accenture technical assessments test modern ES6+ array manipulation methods (`map`, `filter`, `reduce`), string algorithms, object keys, and logic functions.

---

## 10 Solved JavaScript Coding Problems

### Problem 1: Second Largest Element in Array
```javascript
function getSecondLargest(arr) {
    if (arr.length < 2) return -1;
    let first = -Infinity, second = -Infinity;
    for (let num of arr) {
        if (num > first) {
            second = first;
            first = num;
        } else if (num > second && num !== first) {
            second = num;
        }
    }
    return second === -Infinity ? -1 : second;
}

// Test
console.log(getSecondLargest([12, 35, 1, 10, 34, 1])); // 34
```

---

### Problem 2: Palindrome String Check
```javascript
function isPalindrome(s) {
    let cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    let reversed = cleaned.split('').reverse().join('');
    return cleaned === reversed;
}

// Test
console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
```

---

### Problem 3: Two Sum (Hash Map $O(N)$)
```javascript
function twoSum(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];
        if (map.has(diff)) {
            return [map.get(diff), i];
        }
        map.set(nums[i], i);
    }
    return [];
}
```

---

### Problem 4: Move Zeroes to End
```javascript
function moveZeroes(nums) {
    let pos = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[pos++] = nums[i];
        }
    }
    while (pos < nums.length) {
        nums[pos++] = 0;
    }
    return nums;
}
```

---

### Problem 5: First Non-Repeating Character
```javascript
function firstUniqChar(s) {
    const counts = {};
    for (let ch of s) counts[ch] = (counts[ch] || 0) + 1;
    for (let i = 0; i < s.length; i++) {
        if (counts[s[i]] === 1) return i;
    }
    return -1;
}
```

---

### Problem 6: Reverse Words in a Sentence
```javascript
function reverseWords(s) {
    return s.trim().split(/\s+/).reverse().join(' ');
}
```

---

### Problem 7: Maximum Subarray Sum (Kadane's Algorithm)
```javascript
function maxSubArray(nums) {
    let maxSoFar = nums[0], currMax = nums[0];
    for (let i = 1; i < nums.length; i++) {
        currMax = Math.max(nums[i], currMax + nums[i]);
        maxSoFar = Math.max(maxSoFar, currMax);
    }
    return maxSoFar;
}
```

---

### Problem 8: Group Anagrams
```javascript
function groupAnagrams(strs) {
    const map = {};
    for (let str of strs) {
        let sorted = str.split('').sort().join('');
        if (!map[sorted]) map[sorted] = [];
        map[sorted].push(str);
    }
    return Object.values(map);
}
```

---

### Problem 9: Flatten Nested Array
```javascript
function flattenArray(arr) {
    return arr.reduce((flat, toFlatten) => 
        flat.concat(Array.isArray(toFlatten) ? flattenArray(toFlatten) : toFlatten), []);
}
```

---

### Problem 10: Fibonacci (Memoized DP)
```javascript
function fib(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
}
```

---

## Where this appears in the real Accenture test
Appears in Stage 3: Coding Round.

---

## Recommended videos
- [Naukri Code360 Accenture Coding Practice](https://www.naukri.com/code360/interview-bundle/accenture) — JavaScript coding questions.
