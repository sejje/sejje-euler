'''
Someone else's code
This records the length of a sequence per number
like 13:10 (digit 13, sequence length 10)
Then if a number is already in the table it doesn't have
to compute the rest of the sequence.

About 7 times faster than mine.
'''


import time
t=time.time()

nums = {1:1}
nums_cur = {}
# n - number we start to count until 1, cur - current number, count - current item number
n=1
cur=1
count=1
max=0
while n < 1000000:
    #if not n%100000: print 'n=', n
    #print 'n='+str(n), 'cur='+str(cur), 'count='+str(count), 'max='+str(max)
    if cur in nums:
        tmp=count+nums[cur]
        if tmp-1 > max:
            print 'New max:', tmp-1, 'num:', n, time.time()-t
            max=tmp-1
        for i in nums_cur.keys():
            nums[i]=nums[cur]+count-nums_cur[i]
        nums_cur={}
        # Increase n until it doesn't appear in the checked-numbers array
        while n in nums:
            n+=1
        cur=n
        count=1
    nums_cur[cur]=count
    count+=1
    if cur%2: cur=3*cur+1
    else: cur/=2
print 'Done.', time.time()-t
