import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open(data, 'r')
    reader=csv.reader(f)
    z=list(reader)
    a=[]
    for i in z:
        a.append(i[0])
    return a[1:]
print(get_first_column('data.csv'))
    
# Read the csv file