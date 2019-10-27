class Sol:
    def array_partition_I(self,arr):
        arr.sort()
        sum=0
        for i in range(len(arr)):
            if i%2==0:
                sum+=arr[i]
        return sum
