"""
Created on Sun Mar 19 2022

How to run it:
python3 ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv >combined.csv
@author: Forta
"""

import os
import sys


def main(argv):
     file_counter = 1
     new_header = '"filename"'
     for dir_file_name in argv:
        try:
            # cuts path from file name
            file_name_start = dir_file_name.rindex('/') +1
            file_name = dir_file_name[file_name_start:]
            file_name = '"' + file_name + '"'
            # adds filename to each row
            with open(dir_file_name) as f:
                line_counter = 1
                for l in f.readlines():
                    if (file_counter == 1) and (line_counter == 1):
                        print("{},{}".format(l.strip(),new_header))
                    elif line_counter == 1:
                        pass
                    else:
                        print("{},{}".format(l.strip(), file_name))

                    line_counter = line_counter+1

            file_counter = file_counter+1

        except Exception as e:
            pass


if __name__ == "__main__":
    main(sys.argv[1:])