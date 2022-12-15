import argparse
import os

from roboflow import Roboflow

from a2.consts import SUPPORTED_IMAGE_FORMATS
from a2.utils import flatten_lists, get_directory_content, dump_to_json


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
        "--api_key", "-k",
        help="Your Roboflow API key",
        type=str,
        required=True
    )
    parser.add_argument(
        "--project_id", "-p",
        help="Roboflow project id",
        type=str,
        required=True
    )
    parser.add_argument(
        "--project_version", "-v",
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


if __name__ == "__main__":
    args = get_cli_arguments()
    image_source_paths = flatten_lists([
        get_directory_content(directory_path=args.source_image_directory, extension=extension)
        for extension
        in SUPPORTED_IMAGE_FORMATS
    ])
    rf = Roboflow(api_key=args.api_key)
    project = rf.workspace().project(args.project_id)
    model = project.version(args.project_version).model

    for image_source_path in image_source_paths:
        annotations = model.predict(
            image_path=image_source_path,
            confidence=args.detection_confidence_threshold,
            overlap=args.detection_iou_threshold
        ).json()
        source_image_file_name = os.path.basename(image_source_path)
        file_name = os.path.splitext(source_image_file_name)[0]
        target_json_file_name = f"{file_name}.json"
        target_json_path = os.path.join(args.target_annotation_directory, target_json_file_name)
        dump_to_json(target_json_path, annotations)
