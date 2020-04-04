from tk_slots_max_init import *


import os.path



class Convert(Init):
	def __init__(self, *args, **kwargs):
		super(Convert, self).__init__(*args, **kwargs)

		self.ui = self.sb.getUi('convert')



	def cmb000(self, index=None):
		'''
		Editors
		'''
		cmb = self.ui.cmb000

		files = ['']
		contents = cmb.addItems_(files, ' ')

		if not index:
			index = cmb.currentIndex()
		if index!=0:
			if index==contents.index(''):
				pass
			cmb.setCurrentIndex(0)


	def cmb001(self, index=None):
		'''
		Convert To
		'''
		cmb = self.ui.cmb001

		list_ = ['NURBS to Polygons', 'NURBS to Subdiv', 'Polygons to Subdiv', 'Smooth Mesh Preview to Polygons', 'Polygon Edges to Curve', 'Type to Curves', 'Subdiv to Polygons', 'Subdiv to NURBS', 'NURBS Curve to Bezier', 'Bezier Curve to NURBS', 'Paint Effects to NURBS', 'Paint Effects to Curves', 'Texture to Geometry', 'Displacement to Polygons', 'Displacement to Polygons with History', 'Fluid to Polygons', 'nParticle to Polygons', 'Instance to Object', 'Geometry to Bounding Box', 'Convert XGen Primitives to Polygons'] 

		contents = cmb.addItems_(list_, 'Convert To')

		if not index:
			index = cmb.currentIndex()
		if index!=0:
			if index==contents.index('NURBS to Polygons'): #index 1
				mel.eval('performnurbsToPoly 0;')
			elif index==contents.index('NURBS to Subdiv'): #index 2
				mel.eval('performSubdivCreate 0;')
			elif index==contents.index('Polygons to Subdiv'): #index 3
				mel.eval('performSubdivCreate 0;')
			elif index==contents.index('Smooth Mesh Preview to Polygons'): #index 4
				mel.eval('performSmoothMeshPreviewToPolygon;')
			elif index==contents.index('Polygon Edges to Curve'): #index 5
				mel.eval('polyToCurve -form 2 -degree 3 -conformToSmoothMeshPreview 1;')
			elif index==contents.index('Type to Curves'): #index 6
				mel.eval('convertTypeCapsToCurves;')
			elif index==contents.index('Subdiv to Polygons'): #index 7
				mel.eval('performSubdivTessellate  false;')
			elif index==contents.index('Subdiv to NURBS'): #index 8
				mel.eval('performSubdToNurbs 0;')
			elif index==contents.index('NURBS Curve to Bezier'): #index 9
				mel.eval('nurbsCurveToBezier;')
			elif index==contents.index('Bezier Curve to NURBS'): #index 10
				mel.eval('bezierCurveToNurbs;')
			elif index==contents.index('Paint Effects to NURBS'): #index 11
				mel.eval('performPaintEffectsToNurbs  false;')
			elif index==contents.index('Paint Effects to Curves'): #index 12
				mel.eval('performPaintEffectsToCurve  false;')
			elif index==contents.index('Texture to Geometry'): #index 13
				mel.eval('performTextureToGeom 0;')
			elif index==contents.index('Displacement to Polygons'): #index 14
				mel.eval('displacementToPoly;')
			elif index==contents.index('Displacement to Polygons with History'): #index 15
				mel.eval('setupAnimatedDisplacement;')
			elif index==contents.index('Fluid to Polygons'): #index 16
				mel.eval('fluidToPoly;')
			elif index==contents.index('nParticle to Polygons'): #index 17
				mel.eval('particleToPoly;')
			elif index==contents.index('Instance to Object'): #index 18
				mel.eval('convertInstanceToObject;')
			elif index==contents.index('Geometry to Bounding Box'): #index 19
				mel.eval('performGeomToBBox 0;')
			elif index==contents.index('Convert XGen Primitives to Polygons'): #index 20
				import xgenm.xmaya.xgmConvertPrimToPolygon as cpp
				cpp.convertPrimToPolygon(False)

			cmb.setCurrentIndex(0)


	def b000(self):
		'''
		Polygon Edges to Curve
		'''
		self.cmb001(index=5)


	def b001(self):
		'''
		Instance to Object
		'''
		self.cmb001(index=18)


	def b002(self):
		'''
		NURBS to Polygons
		'''
		self.cmb001(index=1)


	def b003(self):
		'''
		Smooth Mesh Preview to Polygons
		'''
		self.cmb001(index=4)


	def b004(self):
		'''
		
		'''
		pass


	def b005(self):
		'''
		
		'''
		pass


	def b006(self):
		'''
		
		'''
		pass


	def b007(self):
		'''
		
		'''
		pass


	def b008(self):
		'''
		
		'''
		pass


	def b009(self):
		'''
		
		'''
		pass







#module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------