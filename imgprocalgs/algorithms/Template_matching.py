
import cv2
import numpy as np


def Template_matching(img, Img_Point, DesValue = 0.81, Debug_Enable = False):
    '''
    A function that looks for an image inside of another img.\n
    If the threshold is less than DesValue, the function would return None

    Output: The x,y,w,h of where the Img_Point is inside img OR a None if threshold not meeted. The function always returns something.
    
    @img the image that the algorthim should find Img_Point inside
    @Img_Point the image that should be found inside img
    @DesValue a value used to filter false positives
    @Debug_Enable show verbose printing and image processing
    '''
    if(Debug_Enable): cv2.imshow("TMStartImg", img)

    result = cv2.matchTemplate(Img_Point, img, cv2.TM_CCOEFF_NORMED)
    
    if(Debug_Enable): cv2.imshow('O_TM_Template', result)

    # We want the minimum squared difference
    (mn, maxVal, mnLoc, maxLoc) = cv2.minMaxLoc(result)

    print(maxLoc)

    conf = result.max()

    if(Debug_Enable):
        print("maxVal: ", maxVal)
        print("conf: ", conf)

    # senstivity check
    if(maxVal > DesValue):
        # Draw the rectangle:
        # Extract the coordinates of our best match
        x, y = maxLoc

        # Step 2: Get the size of the template. This is the same size as the match.
        h, w = Img_Point.shape[:2]
            
        if Debug_Enable:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            print("x1,y1: {},{}; x2,y2: {},{}".format(
                x, y, (x+w),  (y+h)))
            # Display the original image with the rectangle around the match.
            cv2.imshow('O_TM', img)
            cv2.waitKey(0)

        return x, y, w, h

    else:
        if Debug_Enable: print("Threshold not meeted")
        return None


img1 = cv2.imread('', cv2.IMREAD_COLOR)

img2 = cv2.imread('', cv2.IMREAD_COLOR)


cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)

print(Template_matching(img1,img2, 0.81, True))