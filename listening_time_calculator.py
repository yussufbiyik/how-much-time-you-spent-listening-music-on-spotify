import json, pathlib
# import time
# startTime = time.time()

total = 0 # A variable to collect the total listening time

try: # Going through each StreamingHistory file and gathering listening time data for each song
    for path in pathlib.Path('your-data').iterdir():
        # Look for both naming conventions of the file to take the new naming convention into account 
        if path.is_file() and path.name.startswith(("Streaming_History", "StreamingHistory")):
            print('Going through {}'.format(path.name))
            currentFile = open(path, 'r', encoding='UTF-8')
            for item in json.loads(currentFile.read()):
                # Look for both naming conventions of the file to take the new naming convention into account 
                total += int(item.get("msPlayed", item.get("ms_played", 0)))
            currentFile.close()
            # endTime = time.time()
finally: # Calculating total listening time in minutes, hours and days
    print(f'Your total listening time is {total/60000:.2f} minutes which is {total/3600000:.2f} hours which is {total/86400000:.2f} days!')
    # print("This script took {:.5f} seconds to run.".format(endTime - startTime))
