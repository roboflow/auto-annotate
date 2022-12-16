import argparse
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


def get_cli_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Roboflow API a2")
    parser.add_argument(
        "--source_image_directory", "-s",
        help="Path to directory containing source images",
        type=str,
        required=True
    )
    parser.add_argument(
        "--target_annotation_directory", "-t",
        help="Path to directory that will store result annotations",
        type=str,
        required=True
    )
    parser.add_argument(
        "--roboflow_api_key", "-k",
        help="Your Roboflow API key",
        type=str,
        required=False
    )
    parser.add_argument(
        "--roboflow_project_id", "-p",
        help="Roboflow project id",
        type=str,
        required=True
    )
    parser.add_argument(
        "--roboflow_project_version", "-v",
        help="Roboflow project version",
        type=int,
        required=True
    )
    parser.add_argument(
        "--detection_confidence_threshold", "-c",
        help="Roboflow detection API confidence threshold",
        type=int,
        default=40
    )
    parser.add_argument(
        "--detection_iou_threshold", "-i",
        help="Roboflow detection API IoU threshold",
        type=int,
        default=30
    )
    return parser.parse_args()