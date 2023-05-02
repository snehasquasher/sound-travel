import csv 

#create dict of valid names 
valid_names = set()
with open('sound_files_namings.txt', 'r') as file:
    for line in file:
        valid_names.add(line)

print(valid_names)


# #creating a dictionary with the audio ids and file names 
# with open('audio_id_file_name.csv','r') as file: 
#     reader = csv.reader(file)
#     #skip the header row 
#     next(reader)
#     #create dict to store data 
#     audio_ids = {}
#     #traverse each row in the CSV file and add them to the dict 
#     for row in reader: 
#         audio_id = int(row[0])
#         file_name = row[1]
#         if file_name in valid_names: 
#             audio_ids[audio_id] = file_name



# with open('recordings.csv','r') as file: #read recordings.csv 
#     reader = csv.reader(file)
#     #skip the header row 
#     next(reader)
    
#     #create dict to store data 
#     sound_directory = {}
    
#     #traverse each row in the CSV file and add them to the dict 
#     for row in reader: 
#         region = row[6]
#         location = row[7]
#         sound_id = row[16]
#         values = [float(row[4]),float(row[5]),region,location] #latitude,longitude,location
#         if sound_id != '' and int(sound_id) in audio_ids: 
#             file_name = audio_ids[int(sound_id)]
#             sound_directory[file_name] = values
        
#     #write to a csv file 
#     for key,value in sound_directory.items(): 
#         print(key,value)
        
#     with open('output.csv','w',newline = '') as file: 
#         writer = csv.writer(file)
#         writer.writerow(zip(sound_directory.keys(),sound_directory.values()))