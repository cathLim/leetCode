func search(nums []int, target int) int {
    L, R := 0, len(nums)-1

    for L <= R{
        M := (L+R)/2

        if target > nums[M]{
            L = M + 1
        }else if target < nums[M]{
            R = M - 1
        }else{
            return M
        }
    }
    return -1
}
    