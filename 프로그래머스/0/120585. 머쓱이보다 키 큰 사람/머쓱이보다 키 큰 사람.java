import java.util.Arrays;
class Solution {
    public int solution(int[] array, int height) {
       Arrays.sort(array);
        int cnt = 0;
       for(int i =0 ;i<array.length;i++){
           if(height<array[i]){
               cnt++;
           }
       }
        return cnt;
    }
}