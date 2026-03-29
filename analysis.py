def average(data: list) -> float:
    total = 0
    for num in data:
        total += num
    return float(total / len(data))


def median(data: list) -> float:
    sorted_data = sorted(data)
    mid = len(data)// 2
    if len(data)%2 == 0:
        return (sorted_data[mid-1]+ sorted_data[mid])/2
    return float(sorted_data[mid])


def range(data: list) -> float:
   
    return float(max(data) - min(data))
    
    


def rolling_avg(data: list, k: int) -> float:
    ### I checked online I had an easy solution
    ### Pandas will change my data (Series)
    ### so I can use the calculation rolling(windows()).mean()
    import pandas as pd
    
    rolling_avg = pd.Series(data).rolling(window=k).mean()
    
    print(rolling_avg)
    return rolling_avg