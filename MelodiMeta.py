#!/usr/bin/env python3

import os
import sys
import mutagen

def update_track_metadata(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.flac', '.mp3')):
            file_path = os.path.join(directory, filename)
           
            # Extract track number from filename
            try:
                track_number = int(filename.split()[0])
            except ValueError:
                print(f"Couldn't extract track number from {filename}")
                continue
           
            # Update metadata
            try:
                audio = mutagen.File(file_path)
                if isinstance(audio, mutagen.flac.FLAC):
                    audio['tracknumber'] = str(track_number)
                elif isinstance(audio, mutagen.mp3.MP3):
                    audio['TRCK'] = mutagen.id3.TRCK(encoding=3, text=[str(track_number)])
                audio.save()
                print(f"Updated track number for {filename}")
            except Exception as e:
                print(f"Error updating {filename}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        album_path = sys.argv[1]
    else:
        album_path = r"C:\Users\sharvinzlife\Music\Top 100 USA 2024"
    
    print(f"Processing album at: {album_path}")
    update_track_metadata(album_path)
    print("Process completed.")