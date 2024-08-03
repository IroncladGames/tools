import json
import re

def strip_whitespace_not_in_quotes(text):
    # Pattern to match spaces outside quotes
    pattern = r'\s+(?=([^"]*"[^"]*")*[^"]*$)'

    # Replace the matched spaces with empty string
    stripped_text = re.sub(pattern, '', text)

    return stripped_text

def load(json_string):
    # line wraps introduced by beautification may make the json unparsable (e.g. -5.6 gets split into "-" on one line
    # and "5.6" on the next line. we need to strip out all whitespace (not in quotes) before loading the json.
    #
    # NOTE: This is not usable for localized_text, it effectively deadlocks when running the regex on all the nested strings.
    safe_string = strip_whitespace_not_in_quotes(json_string)

    return json.loads(safe_string)
