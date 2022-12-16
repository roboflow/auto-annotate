import os

from roboflow import Roboflow
from tqdm import tqdm

from a2.consts import SUPPORTED_IMAGE_FORMATS, ROBOFLOW_API_KEY
from a2.utils import flatten_lists, get_directory_content, dump_to_json, get_cli_arguments


def annotate(
        source_image_directory: str,
        target_annotation_directory: str,
        roboflow_api_key: str,
        roboflow_project_id: str,
        roboflow_project_version: int,
        detection_confidence_threshold: int = 40,
        detection_iou_threshold: int = 30
) -> None:
    image_source_paths = flatten_lists([
        get_directory_content(directory_path=source_image_directory, extension=extension)
        for extension
        in SUPPORTED_IMAGE_FORMATS
    ])
    rf = Roboflow(api_key=roboflow_api_key)
    project = rf.workspace().project(roboflow_project_id)
    model = project.version(roboflow_project_version).model

    for image_source_path in tqdm(image_source_paths):
        annotations = model.predict(
            image_path=image_source_path,
            confidence=detection_confidence_threshold,
            overlap=detection_iou_threshold
        ).json()
        source_image_file_name = os.path.basename(image_source_path)
        file_name = os.path.splitext(source_image_file_name)[0]
        target_json_file_name = f"{file_name}.json"
        target_json_path = os.path.join(target_annotation_directory, target_json_file_name)
        dump_to_json(target_json_path, annotations)


if __name__ == "__main__":
    args = get_cli_arguments()

    roboflow_api_key = args.roboflow_api_key if args.roboflow_api_key else os.environ.get(ROBOFLOW_API_KEY)
    if roboflow_api_key is None:
        raise Exception("Please set ROBOFLOW_API_KEY environment variable.")

    annotate(
        source_image_directory=args.source_image_directory,
        target_annotation_directory=args.target_annotation_directory,
        roboflow_api_key=roboflow_api_key,
        roboflow_project_id=args.roboflow_project_id,
        roboflow_project_version=args.roboflow_project_version,
        detection_confidence_threshold=args.detection_confidence_threshold,
        detection_iou_threshold=args.detection_iou_threshold
    )
