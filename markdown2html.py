#!/usr/bin/python3
'''This script takes two arguments: first is a markdown file name and the
    second is an html output filename
'''


if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    sym_map = {
            '# ': ('<h1>', '</h1>\n'),
            '## ': ('<h2>', '</h2>\n'),
            '### ': ('<h3>', '</h3>\n'),
            '#### ': ('<h4>', '</h4>\n'),
            '##### ': ('<h5>', '</h5>\n'),
            '###### ': ('<h6>', '</h6>\n')
        }

    with open(sys.argv[1]) as rf:
        read_lines = rf.readlines()
        with open(sys.argv[2], 'a') as wf:
            for line in read_lines:
                for k, v in sym_map.items():
                    if line.startswith(k):
                        html_line = line.replace(k, v[0]).replace('\n', v[1])
                        break
                wf.write(html_line)

    sys.exit(0)
