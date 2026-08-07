class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character,Integer> windowMap=new HashMap<>();
        HashMap<Character,Integer> targetMap=new HashMap<>();

        int left=0;

        for(char c:s1.toCharArray())
        {
            targetMap.put(c,targetMap.getOrDefault(c,0)+1);
        }
        for(int right=0;right<s2.length();right++)
        {
            char rightChar=s2.charAt(right);
            windowMap.put(rightChar,windowMap.getOrDefault(rightChar,0)+1);

            if(right-left+1>s1.length())
            {
                char leftChar=s2.charAt(left);
                windowMap.put(leftChar,windowMap.get(leftChar)-1);
                if(windowMap.get(leftChar)==0)
                {
                    windowMap.remove(leftChar);
                }
                left++;
            }
            if(windowMap.equals(targetMap))
            {
                return true;
            }
        }
        return false;
    }
}
