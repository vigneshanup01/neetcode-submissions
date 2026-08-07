class Solution {

    public String encode(List<String> strs) {
            StringBuilder sb=new StringBuilder();
            for(String str:strs)
            {
                sb.append(str.length());
                sb.append('#');
                sb.append(str);
            }
            return sb.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> result=new ArrayList<>();
        int i=0;
        while(i<str.length())
        {
            int j=i;

            while(str.charAt(j)!='#')
            {
                j++;
            }
            
            int len=Integer.parseInt(str.substring(i,j));
            j++;

            String s=str.substring(j,j+len);

            result.add(s);

            i=j+len;

        }
        return result;
    }
}
