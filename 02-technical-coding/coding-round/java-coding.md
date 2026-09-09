# Coding Round: Java — Complete Practice Bank

## What this is
Java is one of the most widely used languages in Accenture Coding Rounds (Stage 3). This module covers 10 high-frequency DSA coding problems implemented in Java (JDK 8+) with time/space complexity tradeoffs.

---

## 10 Solved Coding Problems (Easy to Medium)

### Problem 1: Second Largest Element in Array
```java
public class SecondLargest {
    public static int getSecondLargest(int[] arr) {
        if (arr.length < 2) return -1;
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
        for (int num : arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second && num != first) {
                second = num;
            }
        }
        return (second == Integer.MIN_VALUE) ? -1 : second;
    }
    public static void main(String[] args) {
        System.out.println(getSecondLargest(new int[]{12, 35, 1, 10, 34, 1})); // Output: 34
    }
}
```

---

### Problem 2: Palindrome String Check
```java
public class PalindromeCheck {
    public static boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
            l++; r--;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama")); // true
    }
}
```

---

### Problem 3: Two Sum (Hash Map $O(N)$)
```java
import java.util.HashMap;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

---

### Problem 4: Move Zeroes to End
```java
public class MoveZeroes {
    public static void moveZeroes(int[] nums) {
        int pos = 0;
        for (int num : nums) {
            if (num != 0) nums[pos++] = num;
        }
        while (pos < nums.length) nums[pos++] = 0;
    }
}
```

---

### Problem 5: First Non-Repeating Character
```java
import java.util.HashMap;

public class FirstUniqChar {
    public static int firstUniqChar(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1) return i;
        }
        return -1;
    }
}
```

---

### Problem 6: Reverse Words in a Sentence
```java
public class ReverseWords {
    public static String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]);
            if (i != 0) sb.append(" ");
        }
        return sb.toString();
    }
}
```

---

### Problem 7: Maximum Subarray Sum (Kadane's Algorithm)
```java
public class Kadane {
    public static int maxSubArray(int[] nums) {
        int maxSoFar = nums[0], currMax = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(nums[i], currMax + nums[i]);
            maxSoFar = Math.max(maxSoFar, currMax);
        }
        return maxSoFar;
    }
}
```

---

### Problem 8: Longest Substring Without Repeating Characters
```java
import java.util.HashMap;

public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (map.containsKey(ch) && map.get(ch) >= left) {
                left = map.get(ch) + 1;
            }
            map.put(ch, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

---

### Problem 9: Merge Two Sorted Arrays
```java
public class MergeSortedArrays {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1, p2 = n - 1, p = m + n - 1;
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }
        while (p2 >= 0) nums1[p--] = nums2[p2--];
    }
}
```

---

### Problem 10: Fibonacci Series (Dynamic Programming)
```java
public class Fibonacci {
    public static int fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}
```

---

## Where this appears in the real Accenture test
Appears in Stage 3: Coding Round.

---

## Recommended videos
- [Naukri Code360 Accenture Interview Bundle](https://www.naukri.com/code360/interview-bundle/accenture) — Java coding questions.
