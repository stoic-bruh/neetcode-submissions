class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.d.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr = self.d[key]
        l = 0
        r = len(arr) - 1
        if timestamp<arr[0][0]:
            return ""
        
        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] > timestamp:
                r = mid - 1

            elif arr[mid][0] < timestamp:
                l = mid + 1

            elif arr[mid][0] == timestamp:
                return arr[mid][-1]
        if arr[mid][0]>timestamp:
            return arr[mid-1][-1]
        else:      
            return arr[mid][-1]