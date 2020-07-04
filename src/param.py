from src import ROOT_DIR


class PARAMS(object):
    # for video_combine.py
    W, H = 960, 540
    RIGHT_VIEW_PATH = ROOT_DIR + '/videos/right.mp4'
    LEFT_VIEW_PATH = ROOT_DIR + '/videos/left.mp4'
    OUTPUT_VIDEO = ROOT_DIR + '/videos/output.avi'

    # for app.py
    ALLOWED_EXTENSIONS = {"mp4"}
    UPLOAD_FOLDER = './videos'
