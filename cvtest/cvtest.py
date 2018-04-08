import cv2
import os

img_root = "./pics/"

def videoFromPics(img_path):
    output_file = "output.mp4"
    images = [str(image) for image in os.listdir(img_root)]

    image_path = os.path.join(img_root, images[0])
    frame = cv2.imread(image_path)
    height, width, channels = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 1, (width, height))

    for image in images:
        frame = cv2.imread(img_root + image)
        out.write(frame)

    out.release()
    print("Converted")

if __name__ == "__main__":
    videoFromPics(img_root)
