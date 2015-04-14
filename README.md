##Sphere Online Judge Sublime Plugin 

This is a Sublime Text plugin to view Sphere Online Judge problem contents directly in Sublime Text in a Textarea.

To make the plugin lightweight, the core functionality, that is parsing and scraping, is done in an online API hosted on Heroku. The source of the API is in the api branch.

###Installation

####Package Control

Search for Sphere Online Judge on Package Control and press enter. The plugin will be installed.

####Zip File 

Download the following zip: <a href="https://github.com/geekpradd/Sphere-Online-Judge-Sublime/archive/master.zip">Sphere Online Judge Sublime Text</a> and extract it to your Packages Directory (Click on Preferences - Browse packages)

###Usage

You can click on the Tools Menu, then Sphere Online Judge-> Respective Options (there are two).
The Command Pallete also has these options.

The first option, reads the first 5 lines of your current opened file for a problem id. The probem ID is used by Sphere Online Judge for submissions and serving content.

For example, the prime generator problem's URL is : http://www.spoj.com/problems/PRIME1/
and here the problem ID is PRIME1

You can declare the problem ID in your codefile as a docstring parameter.

In Python, you can do:

```python
"""
@problem: PRIME1
"""
```

In Java, C, C++

```java
/*
* @problem: PRIME1
*/
```

If the plugin can't find the ID, it will automatically prompt you for the ID.

The second option does the same, it just does not check the view for the ID and implicitly asks you for the ID.

Once you submit the ID, a textarea should pop up in 1-2 seconds (depending on your internet connection) with the problem. If you entered an invalid ID, you will recieve an error dialog.

###To-Do

1. API search integration (No problem ID required)
2. Image Support

###About

Created By Pradipta (geekpradd). Copyright 2015. MIT Licensed.