class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length()>s2.length())
        {
            return false;
        }

        int[] s1Count = new int[26];
        int[] windowCount = new int[26];

        for(int i=0;i<s1.length();i++)
        {
            s1Count[s1.charAt(i)-'a']++;
            windowCount[s2.charAt(i)-'a']++;
        }

        if(Arrays.equals(s1Count,windowCount))
        {
            return true;
        }

        for(int right=s1.length();right<s2.length();right++)
        {
            windowCount[s2.charAt(right)-'a']++;

            windowCount[s2.charAt(right-s1.length())-'a']--;

            if(Arrays.equals(s1Count,windowCount))
            {
                return true;
            }
        }
        return false;

    }
}
