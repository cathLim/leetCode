func shuffle(nums []int, n int) []int {
	j := 2*n - 1

	for i := 0; i < len(nums); i++ {
		nums[i] = (nums[i] << 10) | nums[i+n]
	}

	for i := n - 1; i >= 0; i-- {
		y := nums[i] & ((1 << 10) - 1)
		x := nums[i] >> 10

		nums[j] = y
		nums[j-1] = x
		j -= 2
	}

	return nums
}
