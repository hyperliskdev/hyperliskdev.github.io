---
layout: post
title:  "Code Snippet #1"
date:   2023-05-22
categories: rust leetcode programming dynamic code coding 
---

As an introduction, I want to start doing Leetcode and other problem styles and posting them to my website. Each one will be a single problem, I will go through the problem and take out bits and bytes that interest me and will be useful to solving the problem. Then, I want to work through writing the code and hopefully I can do this for some amount of time before abandoning it.


The first code snippet will be LeetCode #703 - Kth Largest Element in a Stream. The goal is to design a class called KthLargest with memebers k (kth largest) and nums (of this array).

```rust
struct KthLargest {
    k: i32,
    nums: Vec<i32>
}
```

LeetCode gives us this impl for the KthLargest 
```rust
impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {}
    
    fn add(&self, val: i32) -> i32 {}
}
```

Basically, the concept of the solution seems straight forward. Use the new function to initalize a new KthLargest object and use the add function to apend a value to to nums array and then return the kth largest value in the array.

```rust
    fn new(k: i32, nums: Vec<i32>) -> Self {
        KthLargest {
            k,
            nums
        } 
    }
    
    fn add(&mut self, val: i32) -> i32 {
        self.nums.push(val);
        self.nums.sort();

        self.nums[self.nums.len() - self.k as usize]
    }

```

Very basic solution, just changed the reference in add to mutable so that I can push the value and then sort. `self.nums.len() - self.k as usize` would take for example the length of 9 and subtract k (the 3rd largest) --> 9 - 3 = 6 --> self.nums[6]. 6 is the index of the 3rd largest num in the sorted array.

Thanks for reading, this was mostly a test post but problem solving is always fun.
