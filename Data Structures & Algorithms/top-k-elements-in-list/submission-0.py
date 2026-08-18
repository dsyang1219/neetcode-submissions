class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for i, num in enumerate(nums):
            if num in counts.keys():
                counts[num] += 1
            else:
                counts[num] = 1

        pairs = sorted(counts.items(), key=lambda p: p[1], reverse=True)
        result = [p[0] for p in pairs] 

        return result[:k]

        




    

        

            
            
            