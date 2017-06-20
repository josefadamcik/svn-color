#!/usr/bin/env python3

"""
 Author: Saophalkun Ponlu (http://phalkunz.com)
 Contact: phalkunz@gmail.com
 Date: May 23, 2009
 Modified: June 15, 2009

 Additional modifications:
 Author: Phil Christensen (http://bubblehouse.org)
 Contact: phil@bubblehouse.org
 Date: February 22, 2010
"""

import sys, subprocess

colorizedSubcommands = (
	'status',
	'stat',
	'st',
	'add',
	'remove',
	'diff',
	'di',
    'log',
)

statusColors = {
    'M '     : "31",
    '? '    : "37",
    'A '     : "32",
    'X '     : "33",
    'C '     : "30;41",
    'D '     : "31;1",
    '----'   : "34",
    '---'    : "31",
    '-'     : "31",
    '+++'    : "32",
    '+'    : "32",
    '@'     : "36",
    'Index:': "33;1",
    '='     : "34",
    'r'     : "33;1",
    '   M'  : "32",
    '   A'  : "33",
    '   D'  : "33",
}

def colorize(line):
    for status in statusColors:
        if line.startswith(status):
            return ''.join(("\033[", statusColors[status], "m", line, "\033[m"))
    else:
        return line

if __name__ == '__main__':
    command = sys.argv
    command[0] = '/usr/bin/svn'

    if len(command) > 1:
        subcommand = (command[1], '')[len(command) < 2]
    else:
        subcommand = ''
    if subcommand in colorizedSubcommands: # and sys.stdout.isatty():
        task = subprocess.Popen(command, stdout=subprocess.PIPE)
        while True:
            line = task.stdout.readline()
            if not line:
                break
            sys.stdout.write(colorize(line.decode()))
            sys.stdout.flush()
    else:
        task = subprocess.Popen(command)
    task.communicate()
    sys.exit(task.returncode)
