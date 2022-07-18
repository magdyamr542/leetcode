from typing import List

def longestConsecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    nums_set = set(nums)
    # build a graph where a node can have an edge to only one node if their diff is 1 e.g [2->3] [4->5]
            

    root_nodes = [] # nodes without incoming edges. we begin traversing the graph from these nodes
    for num in nums:
        if  num - 1 not in nums_set:
            root_nodes.append(num)
            

    # traverse the graph in O(n). The graph is asyclic and each node is visited one time
    result = 0 # the longes sequence is 0 at the beginning
    for root_node in root_nodes:
        # start a search for a consequtive subsequence beginning from this root node
        longest_ss = 1
        curr = root_node
        while curr + 1 in nums_set:
            longest_ss += 1
            curr = curr + 1
        result = max(result , longest_ss)
    
    return result
    

#https://leetcode.com/problems/longest-consecutive-sequence/
if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))
