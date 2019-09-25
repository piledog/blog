#!/usr/local/bin/python3

from collections import namedtuple
from json import load, loads, dump
from argparse import ArgumentParser
import time

FILE = open('./nagging.json', 'r+')
N = namedtuple('N', ['ts', 'saliva'])

def new(content):
    try:
        data = load(FILE)
    # 空文件, 初始为化空json
    except ValueError as error:
        data = loads('[]')

    item = N(int(time.time()), content)._asdict()
    data.append(item)
    
    FILE.seek(0, 0)
    dump(data, FILE)

def remove_recent():
    try:
        data = load(FILE)
    except:
        print('file not exists. create new nag first')
        return

    if len(data) == 0:
        print('empty file, add new nag first')
        return
    
    recent = N(**data[-1])
    
    # 仅对发布时间超过1day时提醒
    elapsed = (time.time() - recent.ts) / 60
    if input(f'Are you sure to remove "{recent.saliva}" {int(elapsed)} mins ago? enter "y" to confirm: ') == 'y':
        del data[-1]
        FILE.seek(0, 0)
        dump(data, FILE)
        FILE.truncate()
        # 英语不及格
        print(f'nag has been removed.({len(data)} nag pieces in the file)')
    else:
        print(f'operation canceled.({len(data)} nag pieces in the file)')

def main():
    parser = ArgumentParser(description='add/remove nag in the json file')
    parser.add_argument('-n', help='add new nag', metavar='content')
    parser.add_argument('-r', help='remove the most recent nag', action='store_true')
    
    args = parser.parse_args()

    if args.r:
        remove_recent()
    if args.n:
        new(args.n)

    FILE.close()

if __name__ == "__main__":
    main()
