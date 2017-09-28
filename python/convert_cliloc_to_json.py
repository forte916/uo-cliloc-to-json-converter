# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import struct
import glob
import json

"""
Description:
    Convert multiple Cliloc files to a json file for easy to translate.
    This python script takes a very long time.

Input:
    Multiple Cliloc files stored in `input` folder.
    Then, run this script without argument.

    A example of folder tree.
        +--cliloc2json.py
        +--input
        |    +--Cliloc.deu
        |    +--Cliloc.enu
        |    +--Cliloc.jpn
        |
        +--json

Output:
    A json file merged from all languages into `json` folder.

    A sample of output.
        {
            "500001": {
                "DEU": "Ich reagiere nicht.",
                "ENU": "I have no reaction to you.",
                "JPN": "何もないよ。"
            },
            "500002": {
                "DEU": "Ich gehe nach Hause.",
                "ENU": "I am going home.",
                "JPN": "家に帰ります。"
            }
        }
"""

inputClilocs = []
allLanguages = []
outdict = {}

def usage():
    print("Usage:")
    print("  1. Prepare Cliloc files in input folder.")
    print("  2. $ %s" % sys.argv[0])
    sys.exit(1)

def ReadCliloc(infile, extension):
    print("Reading %s... " % infile)

    try:
        fin  = open(infile, 'rb')
    except IOError as e:
        print('%s: %s' % (type(e).__name__, str(e)), file=sys.stderr)
        return
    try:
        fin.seek(6) # header, 6 bytes
        while True:
            buf = fin.read(4)
            if buf == "":
                break

            number = struct.unpack("<L", buf)          # message ID
            delim  = fin.read(1)                       # delimiter
            length = struct.unpack("<H", fin.read(2))  # message length
            if length[0] > 0:
                text = fin.read(length[0])             # message text
            else:
                text = ''

            if not outdict.get(str(number[0])):
                outdict[str(number[0])] = {}
            outdict[str(number[0])][extension] = text
    finally:
        fin.close()
    print("OK!")


def ReadInputDir(entries):
    for entry in entries:
        extension = os.path.splitext(entry)[1][1:].strip().upper()
        inputClilocs.append({'filePath':entry, 'language':extension})

    for cliloc in inputClilocs:
        allLanguages.append(cliloc['language'])

    for cliloc in inputClilocs:
        ReadCliloc(cliloc['filePath'], cliloc['language'])

    #TODO: fill blank string if unfilled.

    # `ensure_ascii=False` will assume utf-8
    if len(outdict) > 0:
        try:
            fout = open(os.path.join('json', 'Cliloc.json'), "w+")
            json.dump(outdict, fout, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
            #json.dump(outdict, codecs.getwriter('utf-8')(fout), ensure_ascii=False, indent=4, sort_keys=True)

            #with io.open("json\Cliloc_utf8.json", "w+", encoding='utf-8') as fout2:
            #    fout2.write(json.dumps(outdict, ensure_ascii=False, indent=4, sort_keys=True))

            print('Done! Cliloc.json has been saved in json folder. You can open and edit it using any text editor.')
        except Exception as e:
            print('%s: %s' % (type(e).__name__, str(e)), file=sys.stderr)
            print('Error! Cliloc.json could not be saved.')
            return
        finally:
            fout.close()


#
# main
#
if __name__ == '__main__':
    entries = glob.glob(os.path.join('input', 'Cliloc.*'))
    print(entries)
    if len(entries) < 1:
        usage()

    ReadInputDir(entries)

