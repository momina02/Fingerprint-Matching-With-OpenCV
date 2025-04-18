# import os
# import cv2

# sample = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP")

# sample = cv2.resize(sample, None, fx=2.5, fy=2.5)

# # cv2.imshow("Sample", sample)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# best_score = 0
# filename = None
# image = None
# kp1, kp2, mp = None, None, None

# for file in [file for file in os.listdir("SOCOFing/Real")][:1000]:
#     fingerprint_image = cv2.imread(r"SOCOFing/Real/" + file)

#     sift = cv2.SIFT_create()
    
#     keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
#     keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)
    
#     matches = cv2.FlannBasedSegment({'algorithm':1, 'trees':10},
#                                     {}.knnMatch(descriptors_1, descriptors_2, k=2))
    
#     match_points = []
    
#     for p, q in matches:
#         if p.distance < 0.1 * q.distance:
#             match_points.append(p)
            
#     keypoints = 0
#     if len(keypoints_1) < len(keypoints_2):
#         keypoints = len(keypoints_1)
#     else:
#         keypoints = len(keypoints_2)
        
#     if len(match_points) / keypoints * 100 > best_score:
#         best_score = len(match_points) / keypoints * 100
#         filename = file
#         image = fingerprint_image
#         kp1, kp2, mp = keypoints_1, keypoints_2, match_points
        
        
# print("BEST MATCH: " + filename)
# print("SCORE: " + str(best_score))


# result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
# result = cv2.resize(result, fx=4, fy=4)

# cv2.imshow("Result : ", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import os
import cv2

# Load and resize the sample fingerprint
sample = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP", cv2.IMREAD_GRAYSCALE)
sample = cv2.resize(sample, None, fx=2.5, fy=2.5)

best_score = 0
filename = None
image = None
kp1, kp2, mp = None, None, None

# Create the SIFT object once (not inside the loop)
sift = cv2.SIFT_create()

# FLANN parameters
index_params = dict(algorithm=1, trees=10)  # FLANN_INDEX_KDTREE = 1
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Loop through real fingerprint images
for file in os.listdir("SOCOFing/Real")[:1000]:
    fingerprint_image = cv2.imread(f"SOCOFing/Real/{file}", cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded
    if fingerprint_image is None:
        print(f"Failed to load image: {file}")
        continue

    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    if descriptors_1 is None or descriptors_2 is None:
        continue  # Skip if descriptors can't be computed

    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []

    # Ratio test as per Lowe's paper
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            match_points.append(m)

    keypoints = min(len(keypoints_1), len(keypoints_2))

    if keypoints == 0:
        continue

    score = len(match_points) / keypoints * 100

    if score > best_score:
        best_score = score
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points

print("BEST MATCH: " + str(filename))
print("SCORE: " + str(best_score))

# Draw and show the matches
if image is not None:
    result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=4, fy=4)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No match found.")
