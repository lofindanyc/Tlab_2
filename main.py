import cleaning 
import analysis



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
    
    data = cleaning.clean_heartrate_data(data)
    avg = analysis.average(data)
    med = analysis.median(data)
    rg = analysis.range(data)
    print(avg, med, rg) 
    #
    # rolling_avg(data,3)
    return (avg,med,rg)


    

    # open file using file I/O and read it into the `data` list
    

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
   

    # calculate the average, median, and range of this file using the functions you've wrote
    
    
    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
    run("data/phase4.txt")
