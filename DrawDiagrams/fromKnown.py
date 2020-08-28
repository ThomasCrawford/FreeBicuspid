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


def main():

	gDepth= 100
	minRadius = .0008
	maxCount = 10000000

	start_time = time.time()
	data = []
	lines = open('known.txt','r').readlines()
	for line in lines:
		entry = []
		for number in line.split(','):
			entry.append(float(number))
		data.append(entry)

	index = 0

	data = data[:100]
	data.sort(key=lambda x: x[2])

	newData = []
	index = 0
	for m in data:
		x = [[m[2],m[3],index,gDepth,minRadius,maxCount],start_time]
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