def spy_game(nums):
    check = False
    n_0 = 0
    n_7 = 0
    for i in range(len(nums)):
        if nums[i] == 0 and n_7 == 0:
            n_0 += 1
        if n_0 == 2 and nums[i] == 7:
            print(True)
            check = True
    if check == False:
        print(False)

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 