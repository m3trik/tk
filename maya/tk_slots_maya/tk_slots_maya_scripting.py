import maya.mel as mel
import pymel.core as pm

import os.path

from tk_slots_maya_init import Init





class Scripting(Init):
	def __init__(self, *args, **kwargs):
		super(Scripting, self).__init__(*args, **kwargs)



		tk_cmdScrollFieldReporter = pm.cmdScrollFieldReporter (
																height=35,
																backgroundColor=[0,0,0],
																highlightColor=[0,0,0],
																echoAllCommands=False,
																filterSourceType="")

		self.hotBox.ui.plainTextEdit.appendPlainText(tk_cmdScrollFieldReporter)
		

	def chk000(self): #toggle mel/python
		if self.hotBox.ui.chk000.isChecked():
			self.hotBox.ui.chk000.setText("python")
		else:
			self.hotBox.ui.chk000.setText("MEL")


	def b000(self): #toggle script output window
		state = pm.workspaceControl ("scriptEditorOutputWorkspace", query=1, visible=1)
		pm.workspaceControl ("scriptEditorOutputWorkspace", edit=1, visible=not state)

	def b001(self): #command line window
		mel.eval('tk_commandLineWindow;')

	def b002(self): #script editor
		mel.eval('ScriptEditor;')

	def b003(self): #new tab
		label = "MEL"
		if self.hotBox.ui.chk000.isChecked():
			label = ".py"
		# self.hotBox.ui.tabWidget.addTab(label)
		self.hotBox.ui.tabWidget.insertTab(0, label)

	def b004(self): #delete tab
		index = self.hotBox.ui.tabWidget.currentIndex()
		self.hotBox.ui.tabWidget.removeTab(index)

	def b005(self): #
		mel.eval('')

	def b006(self): #
		mel.eval('')

	def b007(self): #
		mel.eval('')

	def b008(self): #
		mel.eval("")

	def b009(self): #
		mel.eval('')



#module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------