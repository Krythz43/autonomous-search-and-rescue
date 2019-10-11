import cv2 as cv


def get_scene():
    image = cv.imread("./images/earthscene2.jpg")
    cv.imshow("Original Image", image)

    return image


def preprocess(image):

    return image


def get_borders(image):
    edges = cv.Canny(image, 100, 200)
    cv.imshow("Image Edges", edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return edges


if __name__ == "__main__":

    image = get_scene()
    preprocessed_image = preprocess(image)
    bordered_image = get_borders(preprocessed_image)