---
layout: post
title:  "Code Snippet #2"
date:   2023-06-14
categories: python leetcode programming dynamic code coding 
---



Welcome to Code Snippet #2, this one is for LeetCode #530 - Minimum Absolute Difference in BST (Binary Search Tree).

The problem contains a single sentence in the description that says --> 

> Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the [tree.](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

A very basic example:

![Binary Search Tree](/assets/img/bst.png)

Basically, what is the smallest difference in nodes in the entire binary tree. In this case, we can find that out by going the bst with an inorder traversal and storing the values in an array. Then taking the difference and finding the smallest difference.

Here is that into python3 code.


```python
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        // Return the maxsize if no root node
        if root is None:
            return MAX_SIZE
        
        // hold the values for sorting and subtractions
        values = []
        
        // Sort time
        inorder(root, values)
        
        n = len(values)

        // First subtraction will always be smaller than the largest integer
        minDiff = sys.maxsize
        
        // go through each pair in the values array, finding the smallest difference.
        for i in range(1, n):
            diff = values[i] - values[i-1]
            if diff < minDiff:
                minDiff = diff
        
        return minDiff


```


Thank you for reading and I hope this helped.