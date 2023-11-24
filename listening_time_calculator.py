import json, pathlib

total = 0 # A variable to collect the total listening time

try: # Going through each StreamingHistory file and gathering listening time data for each song
    for path in pathlib.Path('your-data').iterdir():
        if path.is_file() and path.name.startswith('Streaming_History'):
            print('Going through {}'.format(path.name))
            currentFile = open(path, 'r', encoding='UTF-8')
            for item in json.loads(currentFile.read()):
                total += int(item['ms_played'])
            currentFile.close()
finally: # Calculating total listening time
    print(f'Your total listening time is {total/3600000:.2f} hours which is {total/86400000:.2f} days!')
