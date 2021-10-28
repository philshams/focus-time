# focus time [![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) ![github-actions](https://github.com/philshams/focus-time/actions/workflows/github-actions.yml/badge.svg) [![codecov](https://codecov.io/gh/philshams/focus-time/branch/master/graph/badge.svg?token=47QYGC78KA)](https://codecov.io/gh/philshams/focus-time) [![Maintainability](https://api.codeclimate.com/v1/badges/1ad02bb99ec75481e422/maintainability)](https://codeclimate.com/github/philshams/focus-time/maintainability)

Focus time is an application in python to help you focus for a set amount of time

## Installation
```
pip install focus-time
```
- Tested for use with Python 3.8. Currently working on Windows 10; support for Linux and MacOS upcoming. 
- Focus time can be run through any terminal that can run Python packages (tested on Anaconda prompt, powershell, command prompt).
- In Windows: right-click the title bar of the terminal GUI, click properties, and uncheck QuickEdit Mode if applicable. With QuickEdit Mode, certain clicking actions cause the terminal to freeze

## Focus session
1. To start a focus session, simply turn on your sound, turn off your phone, and write the command in your terminal, within the environment in which focus-time is installed ('focus-time', 'focus-session', and 'python -m focus.session' all work as well):
```py
focus
```
2. Type in how long you would like to focus for in minutes (e.g. 60) and press enter. Note that this is the amount of _focusing_ time; if you are distracted for some of it, the session will take longer in real time
```
How long would you like to focus for? (minutes)     60

starting focus session for 60.0 to 90.0 minutes
```
3. Every once and a while, a prompt will pop up along with a "ding-dong!", asking if you were actually focusing (e.g. writing your book) as opposed to something else (e.g. texting). If you were not focusing, make sure the terminal is selected when you press a key; this will not count the previous period toward your total amount of focus time. If you were focusing, just carry on!
- The inter-ding-dong interval is randomly selected from an (approximately) exponentially decaying distribution. This means that at any point in time, the probability that the timer will end soon is about the same, regardless of how long it has been since the last ding-dong.
- If you are using this as a meditation timer, it is recommended to use the sounds as a reminder to focus without pressing any anything.
```
Were you focusing? If yes, carry on. If no, press any key within 10 seconds
```
4. Once you pass the amount of time you wanted to successfully focus, you will be notified of your success. If you pass the maximum amount of time (here, 90 minutes), you will be notified of that as well.
```
You did it!!!
```

## Focus day

1. How about a whole day's worth of focus time? Enter the following command instead ('python -m focus.day' works as well):
```
focus-day
```
2. Write how long you'd like to focus for today and press enter. This will be spread throughout multiple focus sessions.
```
How long would you like to focus for today? (hours)
```
3. This will trigger a series of focus sessions (see above). Upon completion of each session, you'll be notified of how much time you have to go, and you can start a new session whenever you're ready.
```
You have 6.3 hours to go. When you're ready let's start session number 2!

How long would you like to focus for? (minutes) 
```
4. If, upon completion of one of these focus sessions, you surpass your goal for the day, you will be notified and congratulated.
