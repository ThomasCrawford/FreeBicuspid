import argparse


def draw_parser():
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

	return parser


def getargs():
	parser = draw_parser()
	args = vars(parser.parse_args())
	orderedArgs = [args['degrees'],args['a'],args['fileName'],\
		args['gDepth'],\
		args['minRadius']]
	return(orderedArgs)