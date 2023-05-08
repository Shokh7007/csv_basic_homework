#Define function,Get coloumn names from a csv file
import csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f=open(data, 'r')
    reader=csv.reader(f)
    z=list(reader)
    a=[] 
    for i in z:
        a.append(i[1])
    return a[1:]
print(get_column_names('data.csv'))
    
# Read the csv file