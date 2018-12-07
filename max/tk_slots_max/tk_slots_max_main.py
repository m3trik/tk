import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path
from pydoc import locate

from tk_slots_max_init import Init




class Main(Init):
	def __init__(self, *args, **kwargs):
		super(Main, self).__init__(*args, **kwargs)



	def v000(self): #Extrude
		print "# Result: perform extrude #"
		locate('Polygons(self.hotBox).b006()')

	def v001(self): #Bridge
		print "# Result: bridge #"
		locate('Polygons(self.hotBox).b005()')

	def v002(self): #Multi-cut tool
		print "# Result: multi-cut #"
		locate('Polygons(self.hotBox).b012()')

	def v003(self): #Delete history
		print "# Result: delete history #"
		locate('Edit(self.hotBox).b016()')

	def v004(self): #Delete
		print "# Result: delete #"
		locate('Edit(self.hotBox).b032()')

	def v005(self): #
		pass

	def v006(self): #Toggle mode
		self.cycle('shortCutMode_01234')

	def v007(self): #Minimize main application
		mel.eval("minimizeApp;")
		self.hotBox.hbHide()



#module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------




# component mode:vertex
# 		pm.selectMode (component=True)
# 		pm.selectType (subdivMeshPoint=1, polymeshVertex=True)
# 		self.viewPortMessage("<hl>vertex</hl> mask.")

# component mode:edge
# 		pm.selectMode (component=True)
# 		pm.selectType (subdivMeshEdge=1, polymeshEdge=True)
# 		self.viewPortMessage("<hl>edge</hl> mask.")

# component mode:facet
# 		pm.selectMode (component=True)
# 		pm.selectType (subdivMeshFace=1, polymeshFace=True)
# 		self.viewPortMessage("<hl>facet</hl> mask.")

# object mode
# 		pm.selectMode (object=True)
# 		self.viewPortMessage("<hl>object</hl> mode.")

# component mode:uv
# 		pm.selectMode (component=True)
# 		pm.selectType (subdivMeshUV=True, polymeshUV=True)
# 		self.viewPortMessage("<hl>UV</hl> mask.")