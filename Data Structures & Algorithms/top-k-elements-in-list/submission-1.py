class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        out = []
        val = list(freq.values())
        val.sort(reverse=True)
        
        val = val[:k]
        for key,value in freq.items():
            if value in val:
                out.append(key)

        return out