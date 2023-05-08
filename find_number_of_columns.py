import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open(data, 'r')
    reader=csv.reader(f)
    z=list(reader)
    return len(z[0])
    
print(find_number_of_columns('data.csv'))

# Read the csv file