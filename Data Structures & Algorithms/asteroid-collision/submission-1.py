class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while stack and stack[-1]>0 and a<0:
                if abs(stack[-1])>abs(a):
                    alive = False
                    break
                elif abs(stack[-1])<abs(a):
                    stack.pop()
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(a)
        return stack