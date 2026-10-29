class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        answer=[]
        for item in nums:
            if item in count:
                count[item]+=1
            else:
                count[item]=1
        
        sorted_count=dict(sorted(count.items(),key=lambda                  item:item[1],reverse=True))
        for key in sorted_count.keys():
            if k==0:
                break
            answer.append(key)
            k-=1
        
        return answer

            
            



        