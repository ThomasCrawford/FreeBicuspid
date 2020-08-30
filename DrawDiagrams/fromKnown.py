#For now parameters like gDepth and minRadius are hard coded in main()
import generateListSingle
import draw
import time
import multiprocessing as mp

#generate .txt, then .png
def gen(parameters):
	this_time = time.time()
	params,start_time = parameters
	generateListSingle.main(params)
	print('Generated \t {} in \t {} seconds, at \t {} seconds'\
		.format(params[2],time.time()-this_time, time.time()-start_time))
	draw.main([params[2],params[0]])
	print('Drew  \t \t {} in \t {} seconds, at \t {} seconds'\
		.format(params[2],time.time()-this_time, time.time()-start_time))

def getCandidates (data,targets):
	out = []
	for t in targets:
		out.append(min(range(len(data)), key=lambda i: abs(data[i][2]-t)))
	return (out)


def main():

	gDepth= 200
	minRadius = .0002
	minRadius = .0005 #4 hours for 600 frames dDepth 150
	maxCount = 500000
	path = 'Early/'

	start_time = time.time()
	allData = []
	lines = open('fullKnown.txt','r').readlines()
	for line in lines:
		entry = []
		for number in line.split(','):
			entry.append(float(number))
		allData.append(entry)


	anglesWanted = [i/200 for i in range(200)]


	data = []
	for i in (getCandidates(allData,anglesWanted)):
		data.append(allData[i])

	newData = []
	index = 0
	for m in data:
		x = [[m[2],m[3],path+str(index),gDepth,minRadius,maxCount],start_time]
		newData.append(x)
		index = index +1


	pool = mp.Pool(mp.cpu_count())
	pool.map(gen, newData)
	pool.close()




	# for m in data:
	# 	params = [m[2],m[3],index,gDepth,minRadius,maxCount]

	# 	generateListSingle.main(params)
	# 	print('Generated Manifold {} at {} seconds'.format(index,time.time()-start_time))
	# 	draw.main([index,m[2]])
	# 	print('Drew Manifold {} at {} seconds'.format(index,time.time()-start_time))
	# 	index = index +1
	quit()



if __name__ == '__main__':
	main()