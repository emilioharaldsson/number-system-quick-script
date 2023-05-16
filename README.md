
About
=====

This python script provides all the chords in the number system of a key based in
the major scale. If set up as instructed, the script will provide a quick way to 
learn the confines of their current key for writting/composing. 


Requirements
============


* Python 3.6
* sys library 


Set up 

------

Instructions assumes bash is running on terminal and a .bash_profile is set up.

Open up a terminal and add path to script to .bash_profile

```sh
$ nano ~/.bash_profile

# Add the following 

alias run_chords='python /path/to/the/project/folder/main.py'
# * might have to replave python for python3 if on mac
```

Ensure that you have the Python interpreter in your PATH

Find the location of your Python interpreter: 
```sh
$ which python 
# * might have to replave python for python3 if on mac
```

Next, add this python interpreter location to your PATH

```sh
$ nano ~/.bash_profile

export PATH="/usr/local/bin/python:$PATH"
# * might have to replave python for python3 if on mac
```



To Run
======
------

Simply open a terminal and type "run_chords" or whatever
you chose to name the script in your .bash_profile. 

Example 

```sh
$ run_chords f#

```

Output: 

I major - ['F#', 'A#', 'C#']
II minor - ['G#', 'B', 'D#']
III minor - ['A#', 'C#', 'F']
IV major - ['B', 'D#', 'F#']
V major - ['C#', 'F', 'G#']
VI minor - ['D#', 'F#', 'A#']
VII dim - ['F', 'G#', 'B']
