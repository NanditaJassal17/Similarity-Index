


from skimage.metrics import structural_similarity
import cv2
from sewar.full_ref import msssim


def orb_sim(img1, img2):
	orb = cv2.ORB_create()

	kp_a, desc_a = orb.detectAndCompute(img1, None)
	kp_b, desc_b = orb.detectAndCompute(img2, None)

	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	matches = bf.match(desc_a, desc_b)
	similar_regions = [i for i in matches if i.distance < 80]
	if len(matches) == 0:
		return 0
	print(len(similar_regions)/len(matches))


def structural_sim(img1, img2):
	sim, diff = structural_similarity(img1, img2, full=True )
	print('Structural Similarity is:' + str(sim) )



img1 = cv2.imread('C:\\Users\\NANDITA\\Desktop\\Oxo Solutions\\Similarity_Index\\1.jpg',0)
img2 = cv2.imread('C:\\Users\\NANDITA\\Desktop\\Oxo Solutions\\Similarity_Index\\2.jpg',0)
from skimage.transform import resize
img3 = resize(img2,(img1.shape[0],img1.shape[1]), anti_aliasing = True)


#orb_sim(img1,img3)
structural_sim(img1,img3)
#SI = msssim(img1,img3)
#print(SI)

