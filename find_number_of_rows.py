import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f=open(data, 'r')
    reader=csv.reader(f)
    a=0
    for i in reader:
        a+=1
    return a-1
print(find_number_of_rows('data.csv'))

# Read the csv file
