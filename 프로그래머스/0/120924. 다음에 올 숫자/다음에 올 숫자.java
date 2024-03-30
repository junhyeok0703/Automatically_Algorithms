class Solution {
    public int solution(int[] common) {
        int len = common.length;
         int answer = 0;
        
        int c1 = common[1]-common[0];
        int c2 = common[2]-common[1];
        if(c1 == c2){
            answer = common[len-1]+c1;
        }
        else{
            int a = common[1]/common[0];
             answer=common[len-1]* a;
        }
     
       
        return answer;
    }
}