class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character,Integer> need=new HashMap<>();
        HashMap<Character,Integer> window=new HashMap<>();

        for(char c:t.toCharArray())
        {
            need.put(c,need.getOrDefault(c,0)+1);

        }

        int have=0;
        int required=need.size();

        int left=0;

        int minLen=Integer.MAX_VALUE;
        int start=0;

        for(int right=0;right<s.length();right++)
        {
            char rightChar=s.charAt(right);
            window.put(rightChar,window.getOrDefault(rightChar,0)+1);

            if(need.containsKey(rightChar) && window.get(rightChar).intValue()==need.get(rightChar).intValue())
            {
                have++;
            }

        

            while(have==required)
            {
                if(right-left+1<minLen)
                {
                    minLen=right-left+1;
                    start=left;
                }
                char leftChar=s.charAt(left);

                window.put(leftChar,window.get(leftChar)-1);

                if(need.containsKey(leftChar) && window.get(leftChar)<need.get(leftChar))
                {
                    have--;
                }
                left++;
            }
        }
            if(minLen==Integer.MAX_VALUE)
            {
                return "";
            }
            return s.substring(start,start+minLen);
    }
        
}
