class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = []
        # numberOfDays = len(temperatures)
        # for i in range(numberOfDays):
        #     j = i+1
        #     while j < numberOfDays:
        #         if temperatures[j] > temperatures[i]:
        #             result.append(j-i)
        #             break
        #         j+=1
        #     else: 
        #         result.append(0)
        # return result

        result =[0] * len(temperatures)
        waiting_stack = []

        for today, temp in enumerate(temperatures):
            while waiting_stack and temp > temperatures[waiting_stack[-1]]:
                colder_day = waiting_stack.pop()
                result[colder_day] = today - colder_day
            waiting_stack.append(today)
        
        return result




