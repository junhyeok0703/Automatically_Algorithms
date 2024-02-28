class Solution {
    public int[] solution(int[] num_list) {
       int [] reversearr = new int[num_list.length];
        for (int i = num_list.length - 1, j = 0; i >= 0; i--, j++) {
            reversearr[j] = num_list[i];
            System.out.println(reversearr[j]);
        }
        return reversearr;
}
}