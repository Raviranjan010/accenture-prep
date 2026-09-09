# Coding Round: C Language — Complete Practice Bank

## What this is
C language problems in Accenture coding assessments focus on explicit memory management, pointer arithmetic, string manipulation (`char*`), array bounds, and fundamental algorithms without high-level abstractions.

---

## 10 Solved C Language Problems

### Problem 1: Second Largest Element in Array
```c
#include <stdio.h>
#include <limits.h>

int getSecondLargest(int arr[], int n) {
    if (n < 2) return -1;
    int first = INT_MIN, second = INT_MIN;
    for (int i = 0; i < n; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] > second && arr[i] != first) {
            second = arr[i];
        }
    }
    return (second == INT_MIN) ? -1 : second;
}
```

---

### Problem 2: Palindrome String Check
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char s[]) {
    int l = 0, r = strlen(s) - 1;
    while (l < r) {
        while (l < r && !isalnum(s[l])) l++;
        while (l < r && !isalnum(s[r])) r--;
        if (tolower(s[l]) != tolower(s[r])) return 0;
        l++; r--;
    }
    return 1;
}
```

---

### Problem 3: Reverse String in Place
```c
#include <stdio.h>
#include <string.h>

void reverseString(char str[]) {
    int l = 0, r = strlen(str) - 1;
    while (l < r) {
        char temp = str[l];
        str[l] = str[r];
        str[r] = temp;
        l++; r--;
    }
}
```

---

### Problem 4: Move Zeroes to End
```c
#include <stdio.h>

void moveZeroes(int arr[], int n) {
    int pos = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != 0) {
            arr[pos++] = arr[i];
        }
    }
    while (pos < n) {
        arr[pos++] = 0;
    }
}
```

---

### Problem 5: Find Frequency of Characters
```c
#include <stdio.h>

void countFrequency(char str[]) {
    int freq[256] = {0};
    for (int i = 0; str[i] != '\0'; i++) {
        freq[(unsigned char)str[i]]++;
    }
    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            printf("%c: %d\n", i, freq[i]);
        }
    }
}
```

---

### Problem 6: Check Prime Number
```c
#include <stdio.h>

int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}
```

---

### Problem 7: Maximum Subarray Sum (Kadane's Algorithm)
```c
#include <stdio.h>

int maxSubArray(int arr[], int n) {
    int maxSoFar = arr[0], currMax = arr[0];
    for (int i = 1; i < n; i++) {
        currMax = (arr[i] > currMax + arr[i]) ? arr[i] : currMax + arr[i];
        maxSoFar = (maxSoFar > currMax) ? maxSoFar : currMax;
    }
    return maxSoFar;
}
```

---

### Problem 8: Swap Two Numbers Using Bitwise XOR (No Temp Var)
```c
#include <stdio.h>

void swap(int *a, int *b) {
    if (*a != *b) {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
    }
}
```

---

### Problem 9: Merge Two Sorted Arrays
```c
#include <stdio.h>

void mergeSorted(int a[], int m, int b[], int n, int res[]) {
    int i = 0, j = 0, k = 0;
    while (i < m && j < n) {
        if (a[i] <= b[j]) res[k++] = a[i++];
        else res[k++] = b[j++];
    }
    while (i < m) res[k++] = a[i++];
    while (j < n) res[k++] = b[j++];
}
```

---

### Problem 10: Nth Fibonacci Number (Iterative)
```c
#include <stdio.h>

int fib(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

---

## Where this appears in the real Accenture test
Appears in Stage 3: Coding Round.

---

## Recommended videos
- [Naukri Code360 Accenture Coding Practice](https://www.naukri.com/code360/interview-bundle/accenture) — C problems.
