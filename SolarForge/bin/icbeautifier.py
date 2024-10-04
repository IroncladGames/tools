import os
import jsbeautifier
import json
import re
import functools


# exclude lists where order in data matters
EXCLUDE_SORT_LIST_KEYS = [
    "in_game_musics",
    "abilities",
    "behaviors",
    "strikecraft_kinds",
    "ship_roles",
    "tags",
    "skins",
    "build_kinds",
    "ship_components",
    "planet_components",
    "structures",
    "buildable_units",
    "buildable_strikecraft",
    "faction_research_subjects",
    "faction_buildable_units",
    "attack_target_type_groups",
    "attack_target_type_group_ids",
    "pickable_players"
]


def make_options():
    options = jsbeautifier.default_options()
    options.indent_size = 4
    options.brace_style = "expand"
    options.end_with_newline = True # github always complains if there is no newline at end of file
    options.wrap_line_length = 100
    return options
    

def is_hex(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def is_list_of_sortable_strings(obj):
    if isinstance(obj, list) and len(obj) > 0:
        are_all_hex = True
        are_all_strings = True
        
        for item in obj:
            if not isinstance(item, str):
                are_all_strings = False
            else:
                if not is_hex(item):
                    are_all_hex = False

        # don't sort hex values (colors) as the order matters in data
        return are_all_strings and not are_all_hex
    
    return False

# if strings ends with digits returns a tuple of the (prefix,enddigits)
# ex. 'foo_123' -> ('foo', 123)
def split_string_with_end_digits(s):
    # https://stackoverflow.com/questions/14471177/python-check-if-the-last-characters-in-a-string-are-numbers    
    m = re.search(r'\d+$', s)
    if m is not None:
        d = m.group(0)
        return (s[:-len(d)], int(d))
    return (s, 0)
           
def cmp_strings(a, b):
    split_a = split_string_with_end_digits(a)
    split_b = split_string_with_end_digits(b)
    cmp = 0
    if split_a[0] == split_b[0]:
        cmp = -1 if split_a[1] < split_b[1] else 1
    else:
        cmp = -1 if split_a[0] < split_b[0] else 1
    return cmp

def sort_lists(obj_key, json_obj):
    if obj_key in EXCLUDE_SORT_LIST_KEYS:
        return json_obj

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():            
            sort_lists(key, value)
    elif isinstance(json_obj, list):
        if is_list_of_sortable_strings(json_obj):
            # sort so that lower numbers appear before higher numbers e.g. advent_2 before advent_13
            json_obj.sort(key=functools.cmp_to_key(cmp_strings))
        else:            
            for value in json_obj:          
                sort_lists(None, value)

    return json_obj
    
# convenient for testing as you iterate through the characters
def print_current_line(text, index, level):
    next_newline_index = text.find('\n', index)
    if next_newline_index == -1:
        # if there is no newline character after the current index, print the rest of the text
        print(f"level {level}: " + text[index:])
    else:
        # print the characters from the current index up to (but not including) the newline character
        print(f"level {level}: " + text[index:next_newline_index])
        
def post_beautify(text):
    # this relies heavily on the predictable behavior of jsbeautify.
    # will likely not work well for json text from another source
    
    # jsbeautify has a bug where it will create a corrupt json file by
    # splitting up a negative number across a new line if it is within a big list of numbers.
    # [1, 2, 3, -4]
    # ->
    # [1, 2, 3, -
    #   4]
    # fix it up the best we can here be moving the negative sign next to the value after the newline
    text = re.sub(r'-\n(?P<whitespace>\s*)', r'\n\g<whitespace>-', text)
    
    text = re.sub(r'", ', '",\n', text)
    text = re.sub(r'": \["', '": [\n"', text)
    text = re.sub(r'","', '",\n', text)
    text = re.sub(r'"\],\n', '"\n],\n', text) # put-closing-list-bracket-on-newline
    level = 0
    prev_was_newline = False
    new_text = ""
    for i in range(len(text)):
        c = text[i]   

        if i > 0 and c == "\"" and text[i-1] == "\n":            
            #print_current_line(text, i, level)
            new_text += " " * (level + 1) * 4

        # put-closing-list-bracket-on-newline (indent closing bracket properly)
        if i > 0 and c == ']' and text[i-1] == "\n":            
            #print_current_line(text, i, level)
            new_text += " " * (level) * 4

        if c == '{':
            level += 1
        elif c == '}':
            level -= 1        
        new_text += c
    return new_text       
        

def beautify(json_data):
    options = make_options()       
    json_data = sort_lists(None, json_data)
    output_text = jsbeautifier.beautify(json.dumps(json_data), options)
    return post_beautify(output_text)