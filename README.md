# Stock-Price-Alarm-Bot

Based on tutorial by Neuralnine:
https://www.youtube.com/watch?v=qkphpFhkHTs

Requirements:

 - pandas-datareader
 - winotify (windows only)
 - notify (all OS)

Resources:

Notify: https://pypi.org/project/notify-py/

Notify is very limited in functionality but is enoguh for now
Sadly the more complete notification modules are all OS/Desktop 
specific, ie Windows only or Mac only or Gnome/KDE only

Will need to create a custom notification box module later with
either TKinter or imgui for python, or just imgui for C++ extended
for python for a custom cross platform solution

Will need to messa round with this later, stocks do not update over the weekend so it's not a good time to test this now, will have to make a custom function to test notifier, then have it run on a weekday, need to do this tomorrow and Tuesday!