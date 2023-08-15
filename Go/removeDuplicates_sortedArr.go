//https://leetcode.com/problems/remove-duplicates-from-sorted-array/

func removeDuplicates(nums []int) int{
	
	var j int = 1 // to keep track of the position of non-duplicates element

	for i := 1; i<len(nums); i++{
		if nums[i] != nums[i-1]{
			nums[j] = nums[i]
			j++
		}
	}
	return j
}