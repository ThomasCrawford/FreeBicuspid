import argparse


def gen_parser():
	parser = argparse.ArgumentParser(description="Draw an abridged horoball diagram")
	parser.add_argument('degrees', type=float,\
						help="Specify angle of rotation")
	parser.add_argument('a', type=float,\
						help="Specify shift value greater than 1.9")
	parser.add_argument('--fileName',default='MyManifold', type=str,\
						help="Name the txt and png files")
	parser.add_argument('--gDepth', type=int,default = 30,\
						help="maximum number of g or G letters")
	parser.add_argument('--minRadius',default=.001, type=float,\
						help="Specify the minimum radius for a ball to be shown")
	parser.add_argument('--maxCount',default=10000000, type=int,\
						help="Caps the number of horoballs to be drawn")

	return parser

def name_parser():
	parser = argparse.ArgumentParser(description="What manifold to draw")
	parser.add_argument('fileName', type=str,\
						help="fileName")
	return parser


def getargs():
	parser = gen_parser()
	args = vars(parser.parse_args())
	orderedArgs = [args['degrees'],args['a'],args['fileName'],\
		args['gDepth'],\
		args['minRadius'],args['maxCount']]
	return(orderedArgs)

def getname():
	parser = name_parser()
	args = vars(parser.parse_args())
	fileName = args['fileName']
	return(fileName)