import generateList
import draw


def main():

	

	t=1.13905122479
	a=1.96471333664
	fileName='test1'
	gDepth= 30
	minRadius = .001
	maxCount = 10000000

	parameters = [t,a,fileName,gDepth,minRadius,maxCount]

	# parameters = [1.13905122479, 1.96471333664, 'MyManifold', 30, 0.001, 10000000]

	generateList.main(parameters)

	draw.main(fileName)


if __name__ == '__main__':
	main()