import os
import asyncio
from shazamio import Shazam
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TDRC

async def recognize_song(file_path):
    shazam = Shazam()
    out = await shazam.recognize(file_path)
    if out and 'track' in out:
        return {
            'title': out['track'].get('title'),
            'album': out['track']['sections'][0]['metadata'][0]['text'],
            'artist': out['track'].get('subtitle'),
            'year': out['track']['sections'][0]['metadata'][2]['text']
        }
    return None

def get_current_metadata(file_path):
    audio = MP3(file_path, ID3=ID3)

    try:
        tags = audio.tags
        if not tags:
            tags = ID3()
    except:
        tags = ID3()

    return {
        'title': str(tags.get('TIT2', [''])[0]),
        'album': str(tags.get('TALB', [''])[0]),
        'artist': str(tags.get('TPE1', [''])[0]),
        'year': str(tags.get('TDRC', [''])[0])
    }

def update_metadata(file_path, new_metadata):
    audio = MP3(file_path, ID3=ID3)
    
    if audio.tags is None:
        audio.tags = ID3()

    if new_metadata['title']:
        audio.tags['TIT2'] = TIT2(encoding=3, text=new_metadata['title'])
    if new_metadata['album']:
        audio.tags['TALB'] = TALB(encoding=3, text=new_metadata['album'])
    if new_metadata['artist']:
        audio.tags['TPE1'] = TPE1(encoding=3, text=new_metadata['artist'])
    if new_metadata['year']:
        audio.tags['TDRC'] = TDRC(encoding=3, text=new_metadata['year'])

    audio.save()

async def process_file(file_path):
    print(f"Processing: {file_path}")

    # Get current metadata
    current_metadata = get_current_metadata(file_path)

    # Recognize the song
    recognized_info = await recognize_song(file_path)

    # Update metadata if recognition was successful
    if recognized_info:
        print(f"Recognized: {recognized_info['title']} by {recognized_info['artist']}")
        update_metadata(file_path, recognized_info)
    else:
        print(f"Could not recognize: {file_path}")

async def main():
    music_directory = './library'
    
    tasks = []

    print("hello")
    # go through every file and every directory
    for root, dirs, files in os.walk(music_directory):
        if 'CVS' in dirs:
            dirs.remove('CVS') # don't visit CVS directories

    for root, dirs, files in os.walk(music_directory):
        for file in files:
            if file.endswith('.mp3'):
                file_path = os.path.join(root, file)
                tasks.append(process_file(file_path))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
