struct KthLargest {
    k: i32,
    nums: Vec<i32>
}

impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {
        KthLargest {
            k,
            nums
        } 
    }
    
    fn add(&self, val: i32) -> i32 {
        self.nums.push(val);
        self.nums.sort();

        self.nums[self.nums.len() - self.k as usize]
    }
}
