# How Much Time You Spent Listening Music On Spotify ?
Honestly i was wondering this question for sometime and finally decided to make a python script to answer this question. 
There are easier ways of learning your listening time like downloading an app on your phone but they don't take the listening time prior to the apps installation into account so i just wanted to make my own version.

In this readme file i will be teaching you how to get your data from Spotify and learn your listening time.
## How to get your listening data from Spotify?
1. To get your data go to this adress https://www.spotify.com/us/account/privacy/

2. Request your data by following the steps under 'Download your data' headline.

## How to calculate your total listening time?
1. Download your data by going to your mailbox and finding the mail from Spotify that contains your data.

2. Open the file and go to 'MyData' and select every file that starts with 'StreamingHistory' and put them in the folder named 'your-data' in the folder of script. You can also put every file in there too but this looks better

3. Open the terminal 

4. Type or copy paste this command ```python listening_time_calculator.py``` then run the script by hitting enter 

5. It will print a line that contains your listening time data as hours and days.

## Result Screenshot
![image](https://user-images.githubusercontent.com/25200573/218332185-544babb2-94f9-4e96-b7ae-2e4a3295e38a.png)
