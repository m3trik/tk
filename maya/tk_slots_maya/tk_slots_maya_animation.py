import maya.mel as mel
import pymel.core as pm

import os.path

from tk_slots_maya_init import Init





class Animation(Init):
	def __init__(self, *args, **kwargs):
		super(Animation, self).__init__(*args, **kwargs)




	def chk000(self):
		'''
		Pin Open A Separate Instance Of The Ui In A New Window

		'''
		if self.hotBox.ui.chk000.isChecked():
			self.hotBox.pin()
		else:
			self.hotBox.pin.hide()

	def b000(self):
		'''
		

		'''
		mel.eval('')

	def b001(self):
		'''
		

		'''
		mel.eval('')

	def b002(self):
		'''
		

		'''
		mel.eval('')

	def b003(self):
		'''
		

		'''
		mel.eval('')

	def b004(self):
		'''
		

		'''
		mel.eval('')

	def b005(self):
		'''
		

		'''
		mel.eval('')

	def b006(self):
		'''
		

		'''
		mel.eval('')

	def b007(self):
		'''
		

		'''
		mel.eval('')

	def b008(self):
		'''
		

		'''
		mel.eval("")

	def b009(self):
		'''
		

		'''
		mel.eval('')



#module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------