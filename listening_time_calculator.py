import json, pathlib

total_listening_time = [] # A variable to collect each milisecond of listening time

try: # Going through each StreamingHistory file and gathering listening time data for each song
    for path in pathlib.Path('your-data').iterdir():
        if path.is_file():
            if path.name.startswith('StreamingHistory'):
                print('Going through {}'.format(path.name))
                currentFile = open(path, 'r', encoding='UTF-8')
                for item in json.loads(currentFile.read()):
                    total_listening_time.append(item)
                currentFile.close()
finally: # Calculating total listening time
    total = 0
    for item in total_listening_time:
        total += int(item['msPlayed'])
    print(f'Your total listening time is {total/3600000:.2f} hours which is {total/86400000:.2f} days!')