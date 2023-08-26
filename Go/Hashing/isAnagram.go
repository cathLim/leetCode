//https://leetcode.com/problems/valid-anagram/
/*
    using HashMap approach
    1. creates two hashmap, s and t
    2. compare both value
    3. make sure both have the same length

Time complexity: O(s+t)
Space complexity: O(s+t)
*/
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
    //rune data type is used to represent a Unicode code point
	//suitable for handling char
	smap := make(map[rune]int)
	tmap := make(map[rune]int)

	for _, ch := range s {
		smap[ch]++
	}

	for _, ch := range t {
		tmap[ch]++
	}

	for ch, count := range smap {
		if tmap[ch] != count {
			return false
		}
	}

	return true
}

func main() {
	s := "anagram"
	t := "nagaram"
	result := isAnagram(s, t)
	fmt.Println("Are strings anagrams?", result) // Should print "Are strings anagrams? true"
}
