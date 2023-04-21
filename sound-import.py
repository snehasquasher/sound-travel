import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the CSV file into a pandas dataframe
df = pd.read_csv('recordings.csv')

# Iterate over each row of the dataframe
for index, row in df.iterrows():
    # Get the ID and slug values from the row
    recording_id = row['ID']
    slug = row['slug']
    
    # Construct the URL to the recording website
    url = f'https://earth.fm/recordings/{slug}'
    
    # Send a GET request to the recording website
    response = requests.get(url)
    
    # Use BeautifulSoup to extract the audio file URL from the website HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    audio_element = soup.find('audio')
    audio_url = audio_element['src']
    
    # Send a GET request to the audio file URL to download the file
    response = requests.get(audio_url)
    
    # Write the file to disk using the ID as the filename
    with open(f'{recording_id}.mp3', 'wb') as f:
        f.write(response.content)