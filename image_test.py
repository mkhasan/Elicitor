import numpy as np
import cv2

image = cv2.imread('example.png')
image_data = np.asarray(image)

def Test():
    for i in range(len(image_data)):
        for j in range(len(image_data[0])):
            #print(image_data[i][j])  # this row prints an array of RGB color for each pixel in the image
            if i>100 and i < 150:
                image.itemset((i,j,2),200)
 
def main():
    Test()
    #image.show()
    cv2.imwrite('test.png',image) 
if __name__ == '__main__':
    main()