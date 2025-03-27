public class PrefixSum {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int[] prefixSum = new int[arr.length];
        
        // Construct prefix sum array
        prefixSum[0] = arr[0];
        for (int i = 1; i < arr.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }
        
        // Range [2, 4]
        int left = 2;
        int right = 4;
        int sum;
        
        if (left == 0) {
            sum = prefixSum[right];
        } else {
            sum = prefixSum[right] - prefixSum[left - 1];
        }
        
        // Print the result
        System.out.println("Sum of elements in range [" + left + ", " + right + "] is: " + sum);
    }
}
