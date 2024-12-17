public class Solution {
    public bool IsAnagram(string s, string t) {
        int x = s + t;
        Array.sort(s, t);
        for (int i = 1; i < )
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