class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer>dq=new ArrayDeque<>();

        int[] ans=new int[nums.length-k + 1];
        int idx=0;

        for(int right=0;right<nums.length;right++)
        {
            while(!dq.isEmpty() && dq.peekFirst()<=right-k)
            {
                dq.pollFirst();
            }
            while(!dq.isEmpty() && nums[dq.peekLast()]<nums[right])
            {
                dq.pollLast();
            }
            dq.offerLast(right);

            if(right>=k-1)
            {
                ans[idx++]=nums[dq.peekFirst()];
            }
        }
        return ans;
    }
}
