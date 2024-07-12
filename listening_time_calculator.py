import json, pathlib
# import time
# startTime = time.time()

total = 0 # A variable to collect the total listening time
allSongs = [] # A list to collect all the songs that have been listened to
try: # Going through each StreamingHistory file and gathering listening time data for each song
    for path in pathlib.Path('your-data').iterdir():
        # Look for both naming conventions of the file to take the new naming convention into account 
        if path.is_file() and path.name.startswith(("Streaming_History", "StreamingHistory")):
            print('Going through {}'.format(path.name))
            currentFile = open(path, 'r', encoding='UTF-8')
            for item in json.loads(currentFile.read()):
                # Look for both naming conventions of the file to take the new naming convention into account 
                total += int(item.get("msPlayed", item.get("ms_played", 0)))
                allSongs.append({"Track Name": item.get("trackName", item.get("track_name", "Unknown song")), "Listening Time": int(item.get("msPlayed", item.get("ms_played", 0)))/60000 })
            currentFile.close()
            # endTime = time.time()
finally: # Calculating total listening time in minutes, hours and days
    print(f'Your total listening time is:\n\t\x1b[1;36m{total/60000:.2f} minutes\033[0m which is \x1b[1;36m{total/3600000:.2f} hours\033[0m which is \x1b[1;36m{total/86400000:.2f} days\033[0m!')
    allSongs.sort(key=lambda song: song["Listening Time"], reverse=True)
    print(f'Your most listened to song is:\n\t\x1b[1;36m{allSongs[0]["Track Name"]}\033[0m with \x1b[1;36m{allSongs[0]["Listening Time"]:.2f} minutes\033[0m of listening time!')
    # print("This script took {:.5f} seconds to run.".format(endTime - startTime))
