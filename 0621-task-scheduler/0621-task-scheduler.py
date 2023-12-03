class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time: O(n) + O(log26), where n is when we count each task in tasks and generate count, log26 since we can't
        have more than 26 chars and max_heap will have 26 tasks at most, each task being count of chars/tasks
        Space: O(n)

        Steps:
        1. We first need to get the count of each letter (tasks).
        2. We then need to start with the most frequent task. Here's the intuition:
        Eg: Let's say we have tasks = [A, A, A, B, B, C], n=1
        If we start with the most frequent task:
        A -> B -> A -> B -> A -> C
        This is one of the scenarios and we have no idle time.

        If we start with B or C:
        B -> A -> B -> C -> A -> idle -> A 
        We have an idle time in this scenario since in this case, we are not using the most frequent task
        first and we are not able to kinda cancel out the idle time by using another less frequent task (since 
        we already have used them before). So, we are left with only the most frequent task instances and hence, 
        we have to have idle time since we can't use the same task one after the other if n > 0.

        3. We will keep track of which task to execute by using the task count. We will start by using the most 
        frequent task and then go one by one. Heapify the task count and create a max heap out of it so that 
        we can get the max value in O(logn) time.
        4. Use a queue to keep track of tasks which are in cooldown and when we can use them next.

        *************************************************************************************
        TL;DR:
        Heap: Keeps track of which task to execute currently.
        Queue: Keeps track of which tasks are idled and which ones to push to the heap next.        
        *************************************************************************************
        """
        task_count = {}
        queue = deque([])
        time = 0

        # Get the task count
        for task in tasks:  # O(n) time
            task_count[task] = 1 + task_count.get(task, 0)

        max_heap = [-count for count in list(task_count.values())]  
        heapq.heapify(max_heap)  # O(26) time

        # Max Heap or Queue can both be empty. If max heap is empty but queue has values, it means that time is
        # still ticking but we are stuck in idle time and not popping from queue and adding it to the heap and 
        # executing the task.
        while max_heap or queue:  # O(max(m, n)) time, where m = len(max_heap)=26, n = len(queue)
            time += 1  # time will go ahead if either max_heap or queue is non empty
            if max_heap:  # heap can be empty and all the tasks might be idled in queue
                task = heapq.heappop(max_heap)  # O(logm) time
                task += 1  # since this is max heap, we have -ve integers and we want to increase it till 0
                if task < 0:
                    queue.appendleft((task, time+n))  # O(1), time+n is the time when task won't be idled anymore
            if queue:  # check if there are any idled tasks
                if time == queue[-1][1]:  # if the time matches the time of the idled task in queue
                    idled_task, _ = queue.pop()  # O(1) time
                    heapq.heappush(max_heap, idled_task)  # add the task back to the heap 
        return time

        
