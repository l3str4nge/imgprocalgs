import cv2

def GetContours(img):
    '''
    One of the core functions of this whole algorithm.
    returns Contours.
    '''
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue, saturation, value = cv2.split(hsv)

    retval, thresholded = cv2.threshold(
        saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    medianFiltered = cv2.medianBlur(thresholded, 5)

    cnts, hierarchy = cv2.findContours(
        medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    return cnts