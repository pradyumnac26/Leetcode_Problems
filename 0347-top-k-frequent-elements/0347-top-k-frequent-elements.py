class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        ctr = Counter(nums)
        print(ctr)
        common = ctr.most_common(k)
        print(common)
        for c in common:
            output.append(c[0])
        return output
        