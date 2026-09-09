# Coding Round: C++ — Complete Practice Bank

## What this is
C++ (STL) is a favorite programming language choice in competitive coding assessments due to fast runtime execution speed and rich standard template library (`std::vector`, `std::unordered_map`, `std::algorithm`).

---

## 10 Solved C++ Coding Problems

### Problem 1: Second Largest Element in Array
```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int getSecondLargest(const vector<int>& arr) {
    if (arr.size() < 2) return -1;
    int first = INT_MIN, second = INT_MIN;
    for (int num : arr) {
        if (num > first) {
            second = first;
            first = num;
        } else if (num > second && num != first) {
            second = num;
        }
    }
    return (second == INT_MIN) ? -1 : second;
}
```

---

### Problem 2: Palindrome String Check
```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool isPalindrome(string s) {
    int l = 0, r = s.length() - 1;
    while (l < r) {
        while (l < r && !isalnum(s[l])) l++;
        while (l < r && !isalnum(s[r])) r--;
        if (tolower(s[l]) != tolower(s[r])) return false;
        l++; r--;
    }
    return true;
}
```

---

### Problem 3: Two Sum (Hash Map $O(N)$)
```cpp
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> mp;
    for (int i = 0; i < nums.size(); i++) {
        int diff = target - nums[i];
        if (mp.find(diff) != mp.end()) return {mp[diff], i};
        mp[nums[i]] = i;
    }
    return {};
}
```

---

### Problem 4: Move Zeroes to End
```cpp
#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int pos = 0;
    for (int num : nums) {
        if (num != 0) nums[pos++] = num;
    }
    while (pos < nums.size()) nums[pos++] = 0;
}
```

---

### Problem 5: First Non-Repeating Character
```cpp
#include <string>
#include <vector>
using namespace std;

int firstUniqChar(string s) {
    vector<int> freq(26, 0);
    for (char c : s) freq[c - 'a']++;
    for (int i = 0; i < s.length(); i++) {
        if (freq[s[i] - 'a'] == 1) return i;
    }
    return -1;
}
```

---

### Problem 6: Reverse Words in a Sentence
```cpp
#include <string>
#include <sstream>
#include <vector>
using namespace std;

string reverseWords(string s) {
    stringstream ss(s);
    string word, res = "";
    vector<string> words;
    while (ss >> word) words.push_back(word);
    for (int i = words.size() - 1; i >= 0; i--) {
        res += words[i];
        if (i != 0) res += " ";
    }
    return res;
}
```

---

### Problem 7: Maximum Subarray Sum (Kadane's Algorithm)
```cpp
#include <vector>
#include <algorithm>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int maxSoFar = nums[0], currMax = nums[0];
    for (size_t i = 1; i < nums.size(); i++) {
        currMax = max(nums[i], currMax + nums[i]);
        maxSoFar = max(maxSoFar, currMax);
    }
    return maxSoFar;
}
```

---

### Problem 8: Longest Substring Without Repeating Characters
```cpp
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> mp;
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); right++) {
        char ch = s[right];
        if (mp.find(ch) != mp.end() && mp[ch] >= left) {
            left = mp[ch] + 1;
        }
        mp[ch] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

---

### Problem 9: Merge Two Sorted Arrays
```cpp
#include <vector>
using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
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
```

---

### Problem 10: Fibonacci Series (Tabulation)
```cpp
#include <iostream>
using namespace std;

int fib(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

---

## Where this appears in the real Accenture test
Appears in Stage 3: Coding Round.

---

## Recommended videos
- [Naukri Code360 Accenture Coding Practice](https://www.naukri.com/code360/interview-bundle/accenture) — C++ problems.
