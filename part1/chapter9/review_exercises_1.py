desserts = ['ice cream', 'cookies']
desserts.sort()

print 'the index number of "ice cream" is:' , desserts.index('ice cream')

food = desserts[:]

food.extend(['broccoli', 'turnips'])

print desserts
print food

food.remove('cookies')

print food[0:2]


string = 'cookies, cookies, cookies'
cookies = string.split(',')
print cookies


def nums_function(nums):
    for i in range(0, len(nums)):
        if nums[i] < 20:
            print nums[i]

nums_function([2, 4, 8, 16, 32, 64])
