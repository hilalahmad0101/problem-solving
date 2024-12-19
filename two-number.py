class Solution:
    def sum_number(self,value):
        a=0
        # for i in value:
        a=a+value
        return a


    def sum(self,nums,target):
        nums2=[1,2,3,4,5]
        target=6
        nums2_list=[]
        i=0

        # print(len(nums2))

        while(i < len(nums2)):
            # nums2[i]
            # print(self.sum_number(nums2[i]))
            if(self.sum_number(nums2[i]) == target):
                nums2_list.append(i)
            else:
                self.sum_number(nums2[i])
                nums2_list.append(i)

                
            # if target == nums[i]:
            #     print(i)
            # else: 
            i +=1

        print(nums2_list)
        # for i in nums2:
        #     if target == i:
        #         print(nums2.index(i))
        #     else:
        #         i +=i
                
   

s=Solution()

s.sum([1,2,3,4,5],4)

# [0,2,3]