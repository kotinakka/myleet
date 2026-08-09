class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i ,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stack_t,stack_ind=stack.pop()
                k= i-stack_ind
                res[stack_ind] = k
            stack.append([t,i])
        return res
        