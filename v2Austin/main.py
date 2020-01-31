import cv2

BINARY_GRAPH_NAME = "handtrackinggpu.binarypb"
INPUT_VIDEO_STREAM_NAME = "input_video"
OUTPUT_VIDEO_STREAM_NAME = "output_video"
OUTPUT_HAND_PRESENCE_STREAM_NAME = "hand_presence"
OUTPUT_LANDMARKS_STREAM_NAME = "hand_landmarks"

#   private static final CameraHelper.CameraFacing CAMERA_FACING = CameraHelper.CameraFacing.FRONT;

FLIP_FRAMES_VERTICALLY = True

# What is eglManager
processor = FrameProcessor(BINARY_GRAPH_NAME, INPUT_VIDEO_STREAM_NAME, OUTPUT_VIDEO_STREAM_NAME)

processor.getVideoSurfaceOutput().setFlipY(FLIP_FRAMES_VERTICALLY)

# TODO: Add packet callbacks

