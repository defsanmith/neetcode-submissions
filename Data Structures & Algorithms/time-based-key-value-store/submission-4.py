class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            return self.timeMap[key].append((value, timestamp))
        self.timeMap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        result = ""
        left, right = 0, len(self.timeMap[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            v, t = self.timeMap[key][mid]

            if timestamp < t:
                right = mid - 1
            else:
                result = v
                left = mid + 1
                
        return result
        
