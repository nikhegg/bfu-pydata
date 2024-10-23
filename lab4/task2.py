from argparse import ArgumentParser
from moviepy.editor import VideoFileClip
from PIL import Image
import os

params = ArgumentParser()
params.add_argument("--input", required=True)
params.add_argument("--start", required=True)
params.add_argument("--end", required=True)
params.add_argument("--output", required=True)
params.add_argument("--step", default=10, type=int)
args = params.parse_args()

os.makedirs(args.output, exist_ok=True)    
with VideoFileClip(args.input) as file:
    clip = file.subclip(args.start, args.end)
    i = 0
    resize = min(250 / file.size[0], 1)
    size = (int(file.size[0] * resize), int(file.size[1] * resize))    
    for timestamp in range(0, int(clip.duration), args.step):
        frame = clip.get_frame(timestamp)
        img = Image.fromarray(frame)
        img = img.resize(size)
        img.save(os.path.join(args.output, f"{i}.png"))
        i += 1
        