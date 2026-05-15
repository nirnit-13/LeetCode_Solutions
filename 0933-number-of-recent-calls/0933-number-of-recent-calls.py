from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        # Step 1: Add the current ping
        self.q.append(t)
        
        # Step 2: Remove pings that fall outside the [t - 3000, t] window
        while self.q[0] < t - 3000:
            self.q.popleft()
            
        # Step 3: The size of the queue is the number of valid pings
        return len(self.q)