import cv2

image = cv2.imread("logo.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

dimensions = image.shape
total_number_of_elements = image.size
image_dtype = image.dtype


cv2.imshow("OpenCV logo", image)

# Show grayscale image:
cv2.imshow("OpenCV logo gray format", gray_image)
cv2.waitKey(0)

# To destroy all the windows we created call cv2.destroyAllWindows()
cv2.destroyAllWindows()