#https://leetcode.com/problems/daily-temperatures/
#using monotonic decresing stack approach

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((t, i))
        return result