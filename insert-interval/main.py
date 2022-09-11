from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]):
    result = []
    new = newInterval # will be none once merged
    newStart , newEnd = new
    for interval in intervals:
        currStart , currEnd = interval
        if new:
            # comes before current
            if currStart > newStart and  currStart > newEnd:
                result.append(new)
                result.append(interval)
                new = None
            # overlaps
            elif (currStart >=  newStart and  currStart <= newEnd) or (newStart >=  currStart and  newStart <= currEnd):
                # it can be merged
                result.append([min(currStart , newStart) ,max(currEnd , newEnd)])
                new = None
            else:
                # it can not be merged
                result.append(interval)
        else:
            top = result[-1]
            topStart , topEnd = top
            if currStart > topStart and currStart > topEnd:
                result.append(interval)
            elif currStart >= topStart and currStart <= topEnd:
                # it can be merged
                result[-1] = [min(currStart , topStart) ,max(currEnd , topEnd)]

    if new:
        result.append(new)

    return result


# https://leetcode.com/problems/insert-interval/
def main():
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
    newInterval = [4,8]
    print(insert(intervals , newInterval))

if __name__ == "__main__":
    main()
