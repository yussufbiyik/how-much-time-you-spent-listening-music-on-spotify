import json, pathlib

total_listening_time = [] # A variable to collect each milisecond of listening time

try: # Going through each StreamingHistory file and gathering listening time data for each song
    for path in pathlib.Path('your-data').iterdir():
        if path.is_file() and path.name.startswith('Streaming_History'):
            print('Going through {}'.format(path.name))
            currentFile = open(path, 'r', encoding='UTF-8')
            for item in json.loads(currentFile.read()):
                # Append the listening time to total_listening_time variable
                total_listening_time.append(item['ms_played'])
            currentFile.close()
finally: # Calculating total listening time
    total = 0
    for ms in total_listening_time:
        total += int(ms)
        # Divide the total to these specific numbers in order to get hour and day equivalent of the total miliseconds 
    print(f'Your total listening time is {total/3600000:.2f} hours which is {total/86400000:.2f} days!')
