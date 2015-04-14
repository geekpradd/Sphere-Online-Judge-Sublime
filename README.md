##Sphere Online Judge Sublime Plugin 

This is a Sublime Text plugin to view Sphere Online Judge problem contents directly in Sublime Text in a Textarea.

To make the plugin lightweight, the core functionality, that is parsing and scraping, is done in an online API hosted on Heroku. The source of the API is in the api branch.

This plugin is under development.

###Usage

There are two ways to use this plugin.
Firstly, you can directly use the command from the Command Pallete. Doing so, there will be an input panel where you need to enter the problem ID.

The plugin connects to the API and displays the problem content using the Problem ID. The problem ID is a unique identifier for problems on Sphere Online Judge.

For example, the Prime Generator problem has the following URL:
```
http://www.spoj.com/problems/PRIME1/
```

The unique ID of the Prime Generator problem is PRIME1, which is used by Sphere Online Judge to track submissions and display data.

You need to enter this ID in the input panel and press enter. A textarea will pop up in 1-2 seconds (depends on your internet speed) showing the problem. The problem is cached so accessing the same problem again happens quickly.

You can also embed a docstring to the current view so that the problem is loaded automatically without having to enter the problem ID. The plugin will check the first 5 lines for the ID and if present, the input panel will be skipped.

You have to embed the problem id in a docstring like this at the top of your file (optional):

```python
"""
Python example. The line only include the problem id and nothing else
@problem: PRIME1
"""
```

```java
/*
* Java, C++, C example
* @problem: VFMUL
*/
```
###To-Do

1. API search integration (No problem ID required)
2. Image Support

###About

Created By Pradipta (geekpradd). Copyright 2015. MIT Licensed.