from __future__ import print_function
from tk_slots_max_init import *

import os.path



class Rendering(Init):
	def __init__(self, *args, **kwargs):
		super(Rendering, self).__init__(*args, **kwargs)

		# #checkable comboBox not working
		# comboBox = self.CheckableComboBox(self.parentUi.cmb000)
		# for num in range(6):
		# 	comboBox.addItem("checkbox " + str(num))
		# comboBox.checkIndex(1)
		# comboBox.checkIndex(2)


	def pin(self, state=None):
		'''
		Context menu
		'''
		pin = self.parentUi.pin

		if state=='setMenu':
			pin.add(QComboBox_, setObjectName='cmb001', setToolTip='')

			return


	def cmb001(self, index=None):
		'''
		Editors
		'''
		cmb = self.parentUi.cmb001
		
		files = ['']
		contents = cmb.addItems_(files, ' ')

		if not index:
			index = cmb.currentIndex()
		if index!=0:
			if index==contents.index(''):
				pass
			cmb.setCurrentIndex(0)


	def cmb000(self):
		'''
		Render: camera
		'''
		cmb = self.parentUi.cmb000

		self.cams = [cam for cam in rt.cameras if 'Target' not in str(cam)]
		if self.cams:
			list_ = [str(cam.name) for cam in self.cams] #camera names
			cmb.addItems_(list_)


	def b000(self):
		'''
		Render Current Frame
		'''
		cmb = self.parentUi.cmb000
		index = cmb.currentIndex()

		try:
			rt.render (camera=self.cams[index]) #render with selected camera
		except:
			rt.render()


	def b001(self):
		'''
		Open Render Settings Window
		'''
		maxEval('unifiedRenderGlobalsWindow;')


	def b002(self):
		'''
		Redo Previous Render
		'''
		pass


	def b003(self):
		'''
		Editor: Render Setup
		'''
		maxEval('max render scene')


	def b004(self):
		'''
		Editor: Rendering Flags
		'''
		maxEval('renderFlagsWindow;')


	def b005(self):
		'''
		Apply Vray Attributes To Selected Objects
		'''
		selection = pm.ls(selection=1)
		currentID=1
		for obj in selection:
			# get renderable shape nodes relative to transform, iterate through and apply subdivision
			shapes = pm.listRelatives(obj,s=1,ni=1)
			if shapes:
				for shape in shapes:
					mel.eval ("vray addAttributesFromGroup "+shape+" vray_subdivision 1;")
					mel.eval ("vray addAttributesFromGroup "+shape+" vray_subquality 1;")
			# apply object ID to xform. i don't like giving individual shapes IDs.
			mel.eval ("vray addAttributesFromGroup "+obj+" vray_objectID 1;")
			pm.setAttr(obj+'.vrayObjectID',currentID)
			currentID+=1


	def b006(self):
		'''
		Load Vray Plugin
		'''
		vray = ['vrayformaya.mll','vrayformayapatch.mll']
		if pm.pluginInfo ('vrayformaya.mll', query=1, loaded=1):
			try:
				pm.unloadPlugin(vray)
			except:
				print("# Result: Force unloadPlugin:"+str(vray)+" #")
				pm.unloadPlugin(vray, force=1)
		else:
			pm.loadPlugin (vray)








#module name
print(os.path.splitext(os.path.basename(__file__))[0])
# -----------------------------------------------
# Notes
# -----------------------------------------------