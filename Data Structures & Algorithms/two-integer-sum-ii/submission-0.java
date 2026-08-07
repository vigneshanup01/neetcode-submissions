class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer,Integer> prev= new HashMap<>();
        for(int i=0;i<numbers.length;i++)
        {
            int num=numbers[i];
            int diff=target-num;
            
                if(prev.containsKey(diff))
                {
                    return new int[]{prev.get(diff)+1,i+1};
                }
                prev.put(num,i);
        }
        return new int[]{};
    }
}
