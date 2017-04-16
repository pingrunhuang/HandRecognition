# /bin/python

import cv2
import numpy as np
# import tensorflow as tf


class Classifier():
    def __init__():
        pass

# TODO: use multithreading for training in the future

"""
@param image: object of cv2.Mat
@return:
    an array of keypoints
    an image with the keypoints on it
"""
def findKeypoints(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # create a sift object
    sift = cv2.xfeatures2d.SIFT_create()
    # get keypoints from gray image
    keypoints = sift.detect(gray, None)
    image = cv2.drawKeypoints(gray, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    return keypoints, image

"""
@param keypoints: the vector of keypoint
"""
def kmeans(keypoints):
    K = 4
    points = (x.pt for x in keypoints)
    # angles = (x.angle for x in keypoints)
    points = np.vstack(points)
    points = np.float32(points)
    # define criteria and apply kmeans()
    type = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
    max_iteration = 10
    epsilon = 1.0
    criteria = (type, max_iteration, epsilon)
    compactness,labels,centers=cv2.kmeans(points, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    feature_vector = []
    for i in range(K):
        print(centers[i])
        feature_vector.append((centers[i][0],centers[i][1]))

    return feature_vector

def SVM():
    # http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_svm/py_svm_basics/py_svm_basics.html#svm-understanding
    # http://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html
    return

def train():
    return
