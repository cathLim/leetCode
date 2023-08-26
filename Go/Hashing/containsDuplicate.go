//https://leetcode.com/problems/contains-duplicate/
/*
There is no built-in hashset for Go
Hence, we use map, where keys are type int and values are type bool
map is a built-in-function to create a new instance of a map, slice or channel with a specified type.
*/
func containsDuplicate(nums []int) bool {
	hashset := make(map[int] bool) //create an empty map

	//_ is a throwaway variable
	//that allows us to discard values that we're not interested
	//which for this case, use to ignore the index of the current element in this loop
	//iteration, the value of each element is assigned to variable n
	for _, n := range nums{
		if hashset[n]{
			return true //If found, return true indicating a duplicate
		}
		hashset[n] = true // to add a new element to the hashset and mark the element seen by assigning the value true to it. 
	}
    return false //If not found, return false
}