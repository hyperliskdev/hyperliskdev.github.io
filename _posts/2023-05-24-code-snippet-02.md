---
layout: post
title:  "Code Snippet #2"
date:   2023-05-22
categories: java leetcode programming dynamic code coding code-snippet
---

Welcome to Code Snippet #2. Today we will be doing LeetCode #2542 - Maximum Sequence Score.


Given two arrays (num1, nums2) and a length k, find all ***subsequences*** of length k in nums1.

The score of a specific set of indexes is given by this equation -->
`(nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1])`


```
class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
    }
}
```

Firstly, bruteforcing this problem for larger values of n and k becomes very hard, very quickly. As a simplification step we will sort the nums2 array in decresing order. This will allow for a quicker identification of the minimum portion of the score product. 

```
int n = nums1.length;

int[][]  = new int[n][2];

for (int i = 0; i < n; ++i) {
    pairs[i] = new int[]{nums1[i], nums2[i]};
}

Arrays.sort(pairs, (a, b) -> b[1] - a[1]);
```

Since we need to keep the relationship of nums1 to nums2 we are sorting this and the nums1 array in the same fasion. Thereforce the minimum is fixed at num2[i].

```

PriorityQueue<Integer> topKHeap = new PriorityQueue<>(k, (a, b) -> a - b);
long topKSum = 0;
for (int i = 0; i < k; ++i) {
    topKSum += pairs[i][0];
    topKHeap.add(pairs[i][0]);
}

long answer = topKSum * pairs[k - 1][1];

```

The next k num1 values get added to the PriorityQueue and the sum is updated aswell.

```        
// Iterate over every nums2[i] as minimum from nums2.
for (int i = k; i < n; ++i) {

    topKSum += pairs[i][0] - topKHeap.poll();
    topKHeap.add(pairs[i][0]);
    
    answer = Math.max(answer, topKSum * pairs[i][1]);
}

return answer;
```

Finally, the we iterate over nums2[i] and compute the answer from topKSum and num2[i].

Using `Math.max` to make sure the highest computed value makes it to the answer variable.


Thanks for reading this Code Snippet. This one was alot harder to understand but I liked reading the information that was provided and other answers contained recursion and bruteforced it.