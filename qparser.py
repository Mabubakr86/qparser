""" simple module to transfer copied network headers from
    browser into dictionary.

    usage:

        python parser.py <filename.txt>

"""

# import required packages
import json
import sys
import os

def get_headers(filename):
    """ a function to convert copied headers from
        net work tab into dictionary for feeding scrapy
        or requests libraries.
    args:
        filename:str, name of txt file in same directory
    returns:
        headers : as dictionary. 
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = (line.strip() for line in f.readlines())   # create generator object to get lines
            headers = {line.split(':')[0]:line.split(':')[1]
                        for line in lines }                    # create dictionary
            print(json.dumps(headers, indent=2))               # print headers as json
            return headers
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_headers(sys.argv[1])                        # pass file name as command line arg.

