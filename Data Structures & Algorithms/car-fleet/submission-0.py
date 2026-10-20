class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)   # closest to the target first
        stack = []                                          # arrival time of each fleet

        for pos, spd in cars:
            time = (target - pos) / spd                     # hours to reach the target
            if not stack or time > stack[-1]:
                stack.append(time)                          # arrives later: it's a new fleet
            # else: it catches up to the fleet ahead and merges, so nothing to add

        return len(stack)