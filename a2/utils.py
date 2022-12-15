import json
import operator
import os
from functools import reduce
from glob import glob
from typing import Optional, List, TypeVar

V = TypeVar("V")


def get_directory_content(directory_path: str, extension: Optional[str] = None) -> List[str]:
    directory_content_wildcard = "*"
    if extension is not None:
        directory_content_wildcard += f".{extension}"
    lookup_pattern = os.path.join(directory_path, directory_content_wildcard)
    return glob(lookup_pattern)


def flatten_lists(lists: List[List[V]]) -> List[V]:
    return reduce(operator.add, lists, [])


def safe_create_path_parent(path: str) -> None:
    path_parent = os.path.dirname(path)
    os.makedirs(path_parent, exist_ok=True)


def dump_to_json(target_path: str, content: dict) -> None:
    safe_create_path_parent(target_path)
    with open(target_path, 'w') as outfile:
        json.dump(content, outfile, indent=4)
