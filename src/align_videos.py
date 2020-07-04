import cv2
import numpy as np
from src.param import PARAMS


def combine():
    print("Start combining the videos...")
    cap_right = cv2.VideoCapture(PARAMS.RIGHT_VIEW_PATH)
    cap_left = cv2.VideoCapture(PARAMS.LEFT_VIEW_PATH)
    out = cv2.VideoWriter(PARAMS.OUTPUT_VIDEO, cv2.VideoWriter_fourcc(*"MJPG"), 30, (PARAMS.W, PARAMS.H))

    while cap_right.isOpened():
        ret_right, frame_right = cap_right.read()
        ret_left, frame_left = cap_left.read()
        # sometimes we don't get anything out of .read() above...
        if frame_left is not None and frame_right is not None:
            img = np.concatenate((frame_left, frame_right), axis=1)
            img = cv2.resize(img, (PARAMS.W, PARAMS.H))
            cv2.imshow("a", img)
            out.write(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap_right.release()
    cap_left.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    combine()
