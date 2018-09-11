class Solution(object):
    def merge(self, intervals):

        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda interval: interval[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], current[1])
            else:
                res.append(current)

        return res


obj = Solution()
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 2], [2, 3], [3, 4], [5, 7]]
# intervals = [[1, 2], [2, 3], [3, 4], [4, 8]]
# intervals = [[1, 4], [2, 3]]
intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
print(obj.merge(intervals=intervals))



