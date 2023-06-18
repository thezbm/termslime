import colorful as cf
from PIL import Image
import argparse
import os
import random

# use true colors to display the image
cf.use_true_colors()

def display(imgPath: str, heightLimit: int, widthLimit: int, beginPadding: int, endPadding: int, leftPadding: int) -> None:
    """
    Display an image by printing half blocks with foreground and background colors to the terminal.

    Args:
        imgPath - the path to the image file
        heightLimit - maximum number of lines of blocks to display the image in the terminal
        widthLimit - maximum number of blocks per line to display the image in the terminal
        beginPadding - number of empty lines before the image
        endPadding - number of empty lines after the image
        leftPadding - number of empty spaces at the beginning of each line of the image
    """

    # open the image and convert it to 256 colors and get its width and height
    img = Image.open(imgPath).convert(mode="RGBA")
    imgWidth, imgHeight = img.size[0], img.size[1]

    # calculate the resize ratio
    resizeRatio = imgHeight / (heightLimit * 2) if imgHeight > heightLimit * 2 else 1
    resizeRatio = imgWidth / widthLimit if int(imgWidth / resizeRatio) > widthLimit else resizeRatio

    # compress the image to fit the width and height limits and make sure the compressed height is even
    imgResized = img.resize((int(imgWidth / resizeRatio), int(imgHeight / resizeRatio / 2) * 2), Image.Resampling.NEAREST)

    # print the begin padding
    print("\n" * beginPadding, end="")

    # for each two row numbers x and x+1 of pixels
    for x in range(0, imgResized.size[1], 2):

        # print the left padding
        print(" " * leftPadding, end="")

        # for each column number y of pixels
        for y in range(0, imgResized.size[0]):

            # initialize the palette
            p = {}

            # get the two pixels that will be displayed in the same block in the terminal
            pixelUpper = imgResized.getpixel((y, x))
            pixelLower = imgResized.getpixel((y, x + 1))

            # if the two pixels are transparent, print a space
            if pixelUpper[-1] == 0 and pixelLower[-1] == 0:
                print(" ", end="")

            # if only the upper pixel is transparent, print a lower half block with the lower pixel's color as the foreground color
            elif pixelUpper[-1] == 0:
                p["fore"] = tuple(pixelLower[:-1])
                with cf.with_palette(p) as c:
                    print(c.fore("▄"), end="")

            # if only the lower pixel is transparent, print a upper half block with the upper pixel's color as the foreground color
            elif pixelLower[-1] == 0:
                p["fore"] = tuple(pixelUpper[:-1])
                with cf.with_palette(p) as c:
                    print(c.fore("▀"), end="")

            # if either of the two pixels is transparent, print a lower half block with the corresponding pixel's color as the foreground and background colors
            else:
                p["fore"] = tuple(pixelLower[:-1])
                p["back"] = tuple(pixelUpper[:-1])
                with cf.with_palette(p) as c:
                    print(c.fore_on_back("▄"), end="")

        # start a new row
        print()

    # print the end padding
    print("\n" * endPadding, end="")

# the entry point of the cli
def main():

    # set up the argument parser
    parser = argparse.ArgumentParser(prog="termslime", description="Display an image in your terminal with true colors.")
    parser.add_argument("path", type=str, help="path to an image file or a directory containing image files")
    parser.add_argument("-hl", "--heightLimit", type=int, default=500, help="maximum number of lines of blocks to display the image in the terminal")
    parser.add_argument("-wl", "--widthLimit", type=int, default=1000, help="maximum number of blocks per line to display the image in the terminal")
    parser.add_argument("-bp", "--beginPadding", type=int, default=1, help="number of empty lines before the image")
    parser.add_argument("-ep", "--endPadding", type=int, default=0, help="number of empty lines after the image")
    parser.add_argument("-lp", "--leftPadding", type=int, default=1, help="number of empty spaces at the beginning of each line of the image")
    args = parser.parse_args()

    # get path from the arguments
    imgPath = args.path
    assert os.path.exists(imgPath), f"{imgPath} does not exist"

    # if imgPath is a path to a directory
    if os.path.isdir(imgPath):

        # randomly choose an image from the directory and make imgPath the path to that image
        imgList = [file for file in os.listdir(imgPath) if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("bmp")]
        assert len(imgList) > 0, f"{imgPath} does not contain any image files"
        imgPath = os.path.join(imgPath, random.choice(imgList))

    # call the display function and pass in the arguments
    display(imgPath, args.heightLimit, args.widthLimit, args.beginPadding, args.endPadding, args.leftPadding)

if __name__ == "__main__":
    main()