from argparse import ArgumentParser
import cv2
from time import time

params = ArgumentParser()
params.add_argument("--path", required=True)
args = params.parse_args()

video = cv2.VideoCapture(args.path)
fps = video.get(cv2.CAP_PROP_FPS)
video_name = args.path.split('/')[-1]

frame_time = int(1000 / video.get(cv2.CAP_PROP_FPS))
last_frame_time = time()-  (frame_time/1000)
while video.isOpened():
    success, frame = video.read()
    current_frame = 1 / (time() - last_frame_time)
    last_frame_time = time()
    if not success:
        break

    cv2.putText(frame, video_name, (20, 20), 1, 1, (255,255,255))
    cv2.putText(frame, f"{fps:.1f}", (20, 46), 1, 1, (0,255,0))
    cv2.imshow(video_name, frame)
    cv2.waitKey(frame_time)

video.release()
cv2.destroyAllWindows()