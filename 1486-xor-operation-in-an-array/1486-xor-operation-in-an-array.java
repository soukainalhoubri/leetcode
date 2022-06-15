class Solution {
    public int xorOperation(int n, int start) {
        int[] nums=new int[n];
        for(int i=0;i<n;i++){
            nums[i]=start+2*i;
        }
        
        int ans=nums[0];
        for(int k=1;k<n;k++){
            ans=ans^nums[k];
        }
        return ans;
        
    }
}