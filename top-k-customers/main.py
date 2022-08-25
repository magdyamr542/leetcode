from typing import List
import heapq


class Node(object):
    def __init__(self, name : str , freq : int):
        self.name = name
        self.freq = freq

    def __repr__(self):
        return self.name

    def __lt__(self, other : 'Node'):
        ourFreq = self.freq
        otherFreq = other.freq
        if ourFreq < otherFreq:
            return False
        elif ourFreq == otherFreq:
            return self.name > other.name
        return False


def topKCustomers(orders : List[str] , k:int) -> List[str]:
    freq_map = {}
    for order in orders:
        if freq_map.get(order , None):
            freq_map[order] += 1
        else:
            freq_map[order] = 1
    print(freq_map)
    heap = list(map(lambda order : Node(order , freq_map[order]) , orders))
    heapq.heapify(heap)
    while len(heap) > k:
        heapq.heappop(heap)
    return list(map(lambda node: node.name , heap))



        
        
        
        

# https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-internship-on-campus-2022/
if __name__ == "__main__":
    orders = ["xy","yz","xy","zz","yz","xy","zz","yz","xy" , "zz" , "zz" , "zz"]
    k=2
    print(topKCustomers(orders , k))
