import textwrap
import json


def format_title_message(input_str: str, max_len: int = 80) -> str:
    a_str = f" {(input_str + " Messages").title()} "
    for i in range(max_len - (len(input_str + " Messages") + 2)):
        if i & 1 == 0:
            a_str = "=" + a_str
        else:
            a_str = a_str + "="
    return a_str


def format_message(message: str, max_len: int = 80) -> str:
    try:
        json_dict = json.loads(message)
        return json.dumps(json_dict, indent=4, ensure_ascii=False)
    except:
        return textwrap.fill(
            message, width=max_len, break_long_words=False, break_on_hyphens=False
        )
