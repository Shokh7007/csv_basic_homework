import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   f=open(data, 'r')
   reader=csv.reader(f)
   z=list(reader) 
   return z[0]

print(get_first_row('data.csv'))

# Read the csv file