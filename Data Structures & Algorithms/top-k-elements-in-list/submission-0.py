class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        arr=[]
        for i ,cnt in d.items():
            arr.append([cnt,i])
        arr.sort()

        res=[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res