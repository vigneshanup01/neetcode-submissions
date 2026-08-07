class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer>dq=new LinkedList<>();

        int result[]=new int[nums.length-k+1];

        int index=0;

        for(int right=0;right<nums.length;right++)
        {
            while(!dq.isEmpty() && nums[dq.peekLast()]<=nums[right])
            {
                dq.pollLast();
            }
            dq.offerLast(right);

            if(dq.peekFirst()<=right-k)
            {
                dq.pollFirst();
            }
            if(right>=k-1)
            {
                result[index]=nums[dq.peekFirst()];
                index++;
            }
        }
        return result;
    }
}
