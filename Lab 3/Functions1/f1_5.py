def permut(string):
    string_list = list(string)
    end = 0
    while end != len(string): 
        for i in range(len(string) - 1):
            string_list[i], string_list[i + 1] = string_list[i + 1], string_list[i]
            print(string_list)
        end += 1
permut("123")