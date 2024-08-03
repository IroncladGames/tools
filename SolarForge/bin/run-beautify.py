import argparse
import json
import sys
import re
import jsonsafeload
import icbeautifier

#test example:
#py run-beautify.py d:/sins2_data/data/entities/players/advent_player/advent_loyalist.player     

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file_path")    
    args = parser.parse_args()
                    
    with open(args.file_path, "rt") as read_file:                
        #jsonsafeload is used because some of our old json files have lines that end with "-". 
        #need to make sure we can load them so we can rebeautify them to fix the problem.
        content = read_file.read()
        data = jsonsafeload.load(content) 

    # https://stackoverflow.com/questions/53110610/json-dump-in-python-writing-newline-character-and-carriage-returns-in-file
    with open(args.file_path, "w", newline="\n") as write_file:  
        print(f"Beautifying {args.file_path}")
        write_file.write(icbeautifier.beautify(data))


if __name__ == "__main__":
    sys.exit(main())
