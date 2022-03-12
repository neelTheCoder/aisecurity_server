!pip install pandas

#importing libararies
import pandas as pd
import csv
from google.colab import files
 
#have roster.csv file uploaded
data = pd.read_csv("roster.csv")
results = pd.read_csv('roster.csv')

#adds all student ids to list to be used in their respective picture filepaths
ids = data['Student #'].tolist()

#asks the user what the filepath to the photo directory is (up to the image itself)
pictures_filepath = input("What is the file path to the student photo directory? (ex. /home/kiosk/Downloads/PowerSchool/JPG/): ")

#creating a new column in csv file called "Picture Filepath"
default_text = 'Picture Filepath'
with open('roster.csv', 'r') as read_obj, \
        open('new_roster.csv', 'w', newline='') as write_obj:
    csv_reader = csv.reader(read_obj)
    csv_writer = csv.writer(write_obj)
    for row in csv_reader:
        row.append(default_text)
        csv_writer.writerow(row)

#using the id list earlier, adds unique filepath to each student's photo (depending on their id)
i = 0
with open('new_roster.csv') as f:
    data=[row for row in csv.reader(f)] 
with open('new_roster.csv', 'w') as f:
    w=csv.writer(f)
    for i in range(len(results)):
      data[i+1][3]=pictures_filepath  + str(ids[i]) + ".jpg"
      i += 1
    for row in data:
        w.writerow(row)

#downloads updated roster.csv ONLY WORKS IN GOOGLE COLAB
files.download('new_roster.csv') 
