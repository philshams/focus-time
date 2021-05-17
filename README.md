# focus time

Focus time is an application in python to help you focus for a set amount of time

## Installation

- All testing was done on Windows 10 with Anaconda 3 in a conda environment with Python 3.8
```
pip install focus-time
```


## Usage

Open any terminal and activate  the environment where you installed focus-time (tested on Anaconda prompt, powershell, command prompt). _Recommended: right-click the title bar of the terminal GUI, click properties, and uncheck QuickEdit Mode. Otherwise, certain clicking actions may cause the terminal to freeze_

### Focus sessions
To start a focus session, simply turn on your sound, turn off your phone, and write the command (the commands _focus_, _focus-session_, and _python -m focus.session_ all work as well):
```
focus-time
```
write how long you would like to focus for in minutes and press enter
```
How long would you like to focus for? (minutes)   # e.g. write 60 here to do a one-hour focus session 
```
make sure you have more than that amount of time available, in case you are not focused for some of the time:
```
starting focus session for 60.0 to 90.0 minutes
```
Every once and a while, a prompt will pop up along with a doorbell sound, asking if you were actually doing what you set out to focus on (e.g. work) as opposed to something else (e.g. texting). If you are focusing for work, it is recommended to do as it says (make sure the terminal is selected when you press a key); this will not count the previous period toward your total, ensuinge that you end up focusing for the amount of time you wanted to focus. If you are focusing for meditation, it is recommended to use the doorbell tone as a reminder to focus, without pressing any buttons.
```
Were you focusing? If yes, carry on. If no, press any key within 10 seconds
```
Once you pass the amount of time you wanted to successfully focus, you will be notified of your success. If you pass the maximum amount of time (here, 90 minutes), you will be notified of that as well.

### Focus days

To go for a day's worth of focus time, enter the following command instead (_python -m focus.day_ works as well):
```
focus-day
```
Write how long you'd like to focus for today, to be spread throughout multiple focus sessions, and press enter:
```
How long would you like to focus for today? (hours)
```
This will trigger a series of focus sessions. Upon completion of each session, you'll be notified of how much time you have to go, and you can start a new session whenever you're ready.
```
You have 6.3 hours to go. When you're ready let's start session number 2!
```
If, upon completion of one of these focus sessions, you surpass your goal for the day, you will be notified and congratulated.