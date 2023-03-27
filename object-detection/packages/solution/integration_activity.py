from typing import Tuple

IMAGE_SIZE = 416

def DT_TOKEN() -> str:
    # TODO: change this to your duckietown token
    dt_token = "dt1-3nT8KSoxVh4MkRCyEK79pFCgYz8Ri7FXyo4PnjwrcRheHtg-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfV7iYbnY1yVpaGUmJ4KFSsu7PosRt7GM2x"
    return dt_token


def MODEL_NAME() -> str:
    # TODO: change this to your model's name that you used to upload it on google colab.
    # if you didn't change it, it should be "yolov5n"
    return "yolov5n"


def NUMBER_FRAMES_SKIPPED() -> int:
    # TODO: change this number to drop more frames
    # (must be a positive integer)
    return 5


def filter_by_classes(pred_class: int) -> bool:
    """
    Remember the class IDs:

        | Object    | ID    |
        | ---       | ---   |
        | Duckie    | 0     |
        | Cone      | 1     |
        | Truck     | 2     |
        | Bus       | 3     |


    Args:
        pred_class: the class of a prediction
    """
    # Right now, this returns True for every object's class
    # TODO: Change this to only return True for duckies!
    # In other words, returning False means that this prediction is ignored.
    if pred_class == 0:
        return True
    else:
        return False

def filter_by_scores(score: float) -> bool:
    """
    Args:
        score: the confidence score of a prediction
    """
    # Right now, this returns True for every object's confidence
    # TODO: Change this to filter the scores, or not at all
    # (returning True for all of them might be the right thing to do!)

    if score > 0.6:
        return True
    else:
        return False


def filter_by_bboxes(bbox: Tuple[int, int, int, int]) -> bool:
    """
    Args:
        bbox: is the bounding box of a prediction, in xyxy format
                This means the shape of bbox is (leftmost x pixel, topmost y, rightmost x, bottommost y)
    """
    # TODO: Like in the other cases, return False if the bbox should not be considered.
    if bbox[0] < int(IMAGE_SIZE/3):
        return False
        
    side_1 = bbox[2]-bbox[0]
    side_2 = bbox[3]-bbox[1]
    
    area = side_1*side_2

    print(f"The area of the bounding box is: {area}")

    if area>5000/10:
        return True
    else:
        return False
