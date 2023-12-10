class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Time: O(n), where n is len(operations)
        Space: O(n), since we are using the record list
        """
        record = []

        for op in operations:
            if op not in ['+', 'D', 'C']:
                record.append(int(op))
            else:
                if op == '+':
                    record.append(record[-1] + record[-2])
                elif op == 'D':
                    record.append(2*record[-1])
                elif op == 'C':
                    record.pop()
        
        return sum(record)