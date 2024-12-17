
public class Solution {
    public bool HasDuplicate(int[] nums) {
        Array.Sort(nums);
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Solution solution = new Solution();
        
        int[] nums = { 1, 2, 3, 4, 2 };
        bool result = solution.HasDuplicate(nums);
        
        Console.WriteLine($"{result}");
    }
}