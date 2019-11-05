# extracts each video frames into its own folder
import cv2
import os
import sys

def extract_frames(videos_path):

    videos_list = os.listdir(videos_path)

    for video in videos_list:
        video_name = video[:-4] # remove the extension and '.'
        video_folder = os.path.join(videos_path, video_name)
        try:
            os.mkdir(video_folder)
        except Exception as e: # if the folder is already created skip
            pass

        vidcap = cv2.VideoCapture(os.path.join(videos_path, video))
        success, image = vidcap.read()
        count = 0
        print(f'Read first frame from {video_name}: {count}, {success}')

        while success:
            cv2.imwrite(f'{video_folder}/{video_name}F{count}.jpeg', image)
            success, image = vidcap.read()
            print(f'Read frame from {video_name}: {count}, {success}')
            count += 1

def main():
    if len(sys.argv) == 2:
        extract_frames(sys.argv[1])
    else:
        print("Use: python extract_frames.py [vidoes path]")
        print("Example: python extract_frames.py videos/")

if __name__ == '__main__':
    main()
