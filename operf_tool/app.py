from collections import namedtuple
from itertools import islice

import baker

Entry = namedtuple('Entry', ['samples', 'percent', 'image_name', 'symbol_name'])

def parse_line(line):
    toks = line.split()
    toks = toks[:3] + [' '.join(toks[3:])]
    return Entry(
        *(t(x) for t,x in zip((int, float, str, str), toks)))

def entries(filename):
    with open(filename, 'r') as f:
        for e in map(parse_line, islice(f, 3, None)):
            yield e

@baker.command
def sample_count(filename):
    "Count total number of samples in FILENAME."
    print(sum(e.samples for e in entries(filename)))

@baker.command
def image_summary(filename):
    "Sample counts per image."
    rslt = {}
    for e in entries(filename):
        rslt[e.image_name] = rslt.setdefault(e.image_name, 0) + e.samples

    for c, n in sorted((count, image_name) for image_name, count in rslt.items()):
        print('{}\t{}'.format(c, n))

@baker.command
def images(filename):
    "List images in profile."
    for name in sorted({e.image_name for e in entries(filename)}):
        print(name)

def main():
    baker.run()

if __name__ == '__main__':
    main()