def victorina():
    item = int(input("Загадайте число от 1 до 10: "))
    
    if item > 10:
        print("1-10")
        exit()
        
    if item < 1:
        print("1-10")
        exit()
    
    low = 0 
    high = 9
    
    list_of_items = [i for i in range(1, 11)]
    
    while low < high:
        mid = (low + high) // 2 
        guess = list_of_items[mid]
        
        ans = input(f"Вы загадали число {guess}?[N\y]")
        if ans.lower() != "y":
            if guess < item:
                low = mid + 1 
            else:
                high = mid - 1    
        else:
            break    

    
victorina()
