func getConcatenation(nums []int) []int {
    var ans []int

    for i := 0; i < 2; i++ {
        for _, n := range nums { // Use underscore (_) to ignore the index
            ans = append(ans, n) // Append the element n to ans
        }
    }
    return ans
}

