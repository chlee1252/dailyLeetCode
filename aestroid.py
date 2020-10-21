class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        # scan each star
        for star in asteroids:
            
            stack.append( star )
            
            # check for possible collision
            while len(stack) >= 2:
                
                # one pair of stars, a and b collide
                if stack[-2] > 0 and stack[-1] < 0:
                    
                    a = stack.pop()
                    b = stack.pop()
                    
                    if a + b:
                        # a and b have different size, the bigger one remains
                        stack.append( max(a, b, key = abs) )
                        
                else:
                    
                    # exit checking while loop
                    break
                    
        return stack