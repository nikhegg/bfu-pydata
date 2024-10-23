from argparse import ArgumentParser
from moviepy.editor import VideoFileClip

params = ArgumentParser()
params.add_argument("--input", required=True)
params.add_argument("--start", required=True)
params.add_argument("--end", required=True)
params.add_argument("--output", required=True)
args = params.parse_args()

with VideoFileClip(args.input) as file:
    file.subclip(args.start, args.end).write_videofile(args.output)