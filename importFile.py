# This script, opens a CSV file with football data
# Save it on a DICT
# And present it as you wish
def open_csv_file(file, mode):
  try:
    with open(file, mode) as openfile:
      line = openfile.readlines()
      return line
  except FileNotFoundError:
    print('File Not Found')
  except:
    print('Unknown error')

mydata=open_csv_file('2000-01.csv','r')

print(mydata)
