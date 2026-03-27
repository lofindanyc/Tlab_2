def clean_heartrate_data(data: list) -> tuple:
    cleaned = []
    for line in data :
        if line.replace('\n', '') != '' and line.replace('\n', '') != 'NO DATA':
        
            cleaned.append(int(line.replace('\n','')))
    return cleaned
        


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
    
    print(rolling_avg,'dwdwddd')
    return rolling_avg


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    
    file_data_heart = open(file)
    data=file_data_heart.readlines()
    
    data = clean_heartrate_data(data)
    avg = average(data)
    med = median(data)
    rg = range(data)
    print(avg, med, rg) 
    rolling_avg(data,3)
    return avg,med,rg


    

    # open file using file I/O and read it into the `data` list
    

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
   

    # calculate the average, median, and range of this file using the functions you've wrote
    
    
    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


if __name__ == "__main__":
    #run("data/phase0.txt")
    #run("data/phase1.txt")
    #run("data/phase2.txt")
    run("data/phase3.txt")
    #run("data/phase4.txt")
