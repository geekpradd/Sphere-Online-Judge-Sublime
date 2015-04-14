##Sphere Online Judge Sublime Plugin 

This is a Sublime Text plugin to view Sphere Online Judge problem contents directly in Sublime Text in a Textarea.

To make the plugin lightweight, the core functionality, that is parsing and scraping, is done in an online API hosted on Heroku. The source of the API is in the api branch.

The plugin connects to the API and displays the problem content using the Problem ID. The problem ID is a unique identifier for problems on Sphere Online Judge.

For example, the Prime Generator problem has the following URL:
```
http://www.spoj.com/problems/PRIME1/
```

The unique ID of the Prime Generator problem is PRIME1, which is used by Sphere Online Judge to track submissions and display data.

You need to enter this ID in a input panel for the plugin to work.

This plugin is under development.

###To-Do

1. Search the current View to get the problem ID (from a docstring) to display problem content without using an input panel 
2. API search integration (No problem ID required)
3. Image Support

###About

Created By Pradipta (geekpradd). Copyright 2015. MIT Licensed.