#!/usr/bin/env python
import glob
import os
import re
import sys


class NoMatchingThemeFoundException(Exception):
    pass


THEME_DIR = os.path.expanduser('~/.mintty/themes')
THEMES = glob.glob(os.path.join(THEME_DIR, '*.minttyrc'))

ESCAPE_BEGIN = '\033]'
ESCAPE_END = '\a'

COLORS = dict(
    foregroundcolour='10;',
    backgroundcolour='11;',
    cursorcolour='12;',
    black='4;0;',
    blue='4;4;',
    cyan='4;6;',
    green='4;2;',
    magenta='4;5;',
    red='4;1;',
    white='4;7;',
    yellow='4;3;',
    boldblack='4;8;',
    boldblue='4;12;',
    boldcyan='4;14;',
    boldgreen='4;10;',
    boldmagenta='4;13;',
    boldred='4;9;',
    boldwhite='4;15;',
    boldyellow='4;11;',
)


def set_color(color_name, value):
    print('{begin}{color_name}{value}{end}'.format(
        begin=ESCAPE_BEGIN,
        color_name=COLORS[color_name.lower()],
        value=value,
        end=ESCAPE_END), end='')


def select_theme(query):
    pattern = re.compile(query)
    for theme in THEMES:
        (name, _) = os.path.splitext(os.path.basename(theme))
        if pattern.search(name):
            with open(theme) as theme_file:
                for line in theme_file:
                    stripped_line = line.strip()
                    parts = stripped_line.split('=')
                    color_name = parts[0]
                    value = parts[1]
                    set_color(color_name, value)
                return
    raise NoMatchingThemeFoundException()


def main():
    if len(sys.argv) != 1:
        try:
            select_theme(sys.argv[1])
            exit(0)
        except NoMatchingThemeFoundException:
            sys.stderr.write('No matching theme found\n')
            exit(2)
    else:
        sys.stderr.write('Must specify one argument\n')
        exit(1)


if __name__ == '__main__':
    main()
