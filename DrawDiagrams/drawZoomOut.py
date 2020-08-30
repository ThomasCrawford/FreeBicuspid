import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections
import time
import parse
# import sys
# sys.path.append('/Generated')



# def addCircle(x,y,r):



def main(args):
	dpi = 400
	fileName, title = args
	start_time = time.time()
	data = []
	lines = open('Generated/{}.txt'.format(fileName),'r').readlines()
	t = float(lines[0].split(',')[0])
	a = float(lines[0].split(',')[1])
	for line in lines[1:]:
		entry = []
		for number in line.split(','):
			entry.append(float(number))
		data.append(entry)
	# print ("--- Read file at %s seconds ---" % (time.time() - start_time))

	patch1 = [plt.Circle((x,y),r) for x,y,r in data]
	patch2 = [plt.Circle((x+a,y),r) for x,y,r in data]
	patch3 = [plt.Circle((x+a/2,y + a*np.sqrt(3)/2),r) for x,y,r in data]
	patch4 = [plt.Circle((x-a/2,y + a*np.sqrt(3)/2),r) for x,y,r in data]
	patch5 = [plt.Circle((x+a/2,y - a*np.sqrt(3)/2),r) for x,y,r in data]
	patch6 = [plt.Circle((x-a/2,y - a*np.sqrt(3)/2),r) for x,y,r in data]
	patch7 = [plt.Circle((x+3*a/2,y + a*np.sqrt(3)/2),r) for x,y,r in data]
	patch8 = [plt.Circle((x+3*a/2,y - a*np.sqrt(3)/2),r) for x,y,r in data]
	patch9 = [plt.Circle((x+2*a,y),r) for x,y,r in data]
	patch10 = [plt.Circle((x-a,y),r) for x,y,r in data]
	patch11 = [plt.Circle((x+5*a/2,y + a*np.sqrt(3)/2),r) for x,y,r in data]
	patch12 = [plt.Circle((x+5*a/2,y - a*np.sqrt(3)/2),r) for x,y,r in data]

	patches =patch4+patch5+patch6+patch7 + patch8 + patch9 + patch10+patch11 + patch12

	# print ("--- Created patches at %s seconds ---" % (time.time() - start_time))
	
	coll1 = matplotlib.collections.PatchCollection(patch1,\
		facecolors=(230/256,159/256,0,.50), linewidth = .5)
	coll2 = matplotlib.collections.PatchCollection(patch2, \
		facecolors=(86/256,180/256,223/256,.50), linewidth = .5)
	coll3 = matplotlib.collections.PatchCollection(patch3, \
		facecolors=(0/256,158/256,115/256,.50), linewidth = .5)
		# edgecolor = (0/256,158/256,115/256,.8))
	coll4 = matplotlib.collections.PatchCollection(patches,\
		# facecolors=(100/256,100/256,100/256,.50), linewidth = .5)
		edgecolor=(100/256,100/256,100/256,.50), facecolors='none', linewidth = .2)

	# print ("--- Created collection at %s seconds ---" % (time.time() - start_time))
	
	fig, ax = plt.subplots()
	ax.add_collection(coll1)
	ax.add_collection(coll2)
	ax.add_collection(coll3)
	ax.add_collection(coll4)
	# print ("--- Added collection at %s seconds ---" % (time.time() - start_time))
	
	ax.axis([-1.6,4.8,-2.3,2.4])

	ax.margins(0.01)
	ax.set_aspect('equal', 'box')
	plt.title(title)
	plt.tight_layout()
	plt.savefig('Generated/{}.png'.format(fileName),dpi = dpi)
	plt.close(fig)

if __name__ == '__main__':
	args = parse.getname()
	main(args)