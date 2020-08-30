import os, sys, glob, time
import multiprocessing as mp
from cmath import *
import numpy as np
import parse


class Manifold:

	def __init__(self,t,a):
		self.a = a
		self.t = t
		self.hexagons()

	def g(self,z):
		return self.a+ np.e**(1.j*np.pi*self.t/180.)/z

	def G(self,z):
		return np.e**(1.j*np.pi*self.t/180.)/(z-self.a)

	def m(self,z):
		return z + self.a/2.*(1-1.j*sqrt(3))

	def M(self,z):
		return z - self.a/2.*(1-1.j*sqrt(3))

	def n(self,z):
		return z + self.a/2.*(3+1.j*sqrt(3))

	def N(self,z):
		return z - self.a/2.*(3+1.j*sqrt(3))

	def hexagons(self):
		self.hexagong=[['g',self.a],['Mg',self.M(self.a)],['MG',self.M(0)],['MNg',self.M(self.N(self.a))],['Ng',self.N(self.a)],['mG',self.m(0)]]
		self.hexagonG=[['G',0],['Mg',self.M(self.a)],['nG',self.n(0)],['mnG',self.m(self.n(0))],['mg',self.m(self.a)],['mG',self.m(0)]]

	def evaluate(self,z,word):
		for letter in word[::-1]:
			z=eval('self.{letter}({z})'.format(letter=letter,z=z))
			# z=eval(letter + '(' + str(z) + ')')
		return z

def nextStep(mani,info,minRadius):
	[z,r,w] = info
	out = []
	if w[-1] == 'G':
		for suffix, preZ in mani.hexagonG:
			newZ = mani.evaluate(preZ,w)
			newR = abs(z-newZ)**2/(4*r)
			newW =   w+ suffix
			if newR > minRadius:
				out.append([newZ,newR,newW])
	elif w[-1] == 'g':
		for suffix, preZ in mani.hexagong:
			newZ = mani.evaluate(preZ,w)
			newR = abs(z-newZ)**2/(4*r)
			newW =   w+ suffix
			if newR > minRadius:
				out.append([newZ,newR,newW])
	return out

#format: [[z1,r1],[z2,r2],...]
def publish(toBePublished, fileName):
	file = open('Generated/{}.txt'.format(fileName),'a')
	for ball in toBePublished:
	    file.write(str(ball[0].real) +','+str(ball[0].imag)+','+str(ball[1])+'\n')
	file.close()

def main(args):
	start_time = time.time()
	t,a,fileName,gDepth,minRadius,maxCount = args
	manifold = Manifold(t,a)
	horoCounter = 0
	stage = [[0.,0.5,'G']] 


	f = open('Generated/{}.txt'.format(fileName),'w')
	f.write('{t},{a}\n'.format(t=t,a=a))
	f.close()

	for i in range(gDepth):
		newStage = []
		#to optimize for multi-core processors
		if len(stage)>200 and horoCounter < maxCount:
			pool = mp.Pool(mp.cpu_count())
			zipped = zip([manifold]*len(stage),stage,[minRadius]*len(stage))
			results = pool.starmap(nextStep, zipped)
			for x in results:
				for y in x:
					newStage.append(y)
			pool.close()
			print ('\t\t level %s: %s new horoballs, in %s seconds total ---' %(i +1, len(newStage), time.time() - start_time)) 
		elif len(stage)>0 and horoCounter < maxCount:
			for ball in stage:
				x = nextStep(manifold,ball,minRadius)
				for y in x:
					newStage.append(y)
			print ('\t\t level %s: %s new horoballs, in %s seconds total ---' %(i +1, len(newStage), time.time() - start_time)) 
		publish(stage,fileName)
		horoCounter = horoCounter + len(stage)
		stage = newStage
		
	print('\t Number of Horoballs:' + str(horoCounter))
	publish(stage,fileName)
	print ("\t --- %s seconds ---" % (time.time() - start_time))



if __name__ == '__main__':
	arguments = parse.getargs()
	main(arguments)