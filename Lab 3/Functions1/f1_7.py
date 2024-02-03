def has_33(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 3:
            k = 0
        if nums[i] == 3:
            k += 1
        if k == 2:
            print(True)
            break
    if k != 2:
        print(False)

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])