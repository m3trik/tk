import MaxPlus; maxEval = MaxPlus.Core.EvalMAXScript
from pymxs import runtime as rt

import os.path

from tk_slots_max_init import Init






class Selection(Init):
	def __init__(self, *args, **kwargs):
		super(Selection, self).__init__(*args, **kwargs)

		self.ui = self.sb.getUi('selection')
		self.submenu = self.sb.getUi('selection_submenu')


		#set checked button states
		#chk004 ignore backfacing (camera based selection)
		# sel = rt.Filters.GetModOrObj()
		# state = sel.ignoreBackfacing
		# self.ui.chk004.setChecked(state)

		# #selection style: set initial checked state
		# ctx = pm.currentCtx() #flags (ctx, c=True) get the context's class.
		# if ctx == 'lassoContext':
		# 	self.cmb004(index=1)
		# 	self.submenu.chk006.setChecked(True)
		# elif ctx == 'paintContext':
		# 	self.cmb004(index=2)
		# 	self.submenu.chk007.setChecked(True)
		# else: #selectContext
		# 	self.cmb004(index=0)
		# 	self.submenu.chk005.setChecked(True)


	def t000(self):
		'''
		Select The Selection Set Itself (Not Members Of)
		'''
		name = str(self.ui.t000.text())+"Set"
		pm.select (name, noExpand=1) #noExpand=select set itself


	def t001(self):
		'''
		Select By Name
		'''
		searchStr = str(self.ui.t001.text()) #asterisk denotes startswith*, *endswith, *contains* 
		if searchStr:
			selection = rt.select(searchStr)


	def s002(self):
		'''
		Select Island: tolerance x
		'''
		if self.ui.chk003.isChecked():
			text = self.ui.s002.value()
			self.ui.s004.setValue(text)
			self.ui.s005.setValue(text)


	def s004(self):
		'''
		Select Island: tolerance y
		'''
		if self.ui.chk003.isChecked():
			text = self.ui.s004.value()
			self.ui.s002.setValue(text)
			self.ui.s005.setValue(text)


	def s005(self):
		'''
		Select Island: tolerance z
		'''
		if self.ui.chk003.isChecked():
			text = self.ui.s005.value()
			self.ui.s002.setValue(text)
			self.ui.s004.setValue(text)


	def chk000(self):
		'''
		Select Nth: uncheck other checkboxes
		'''
		self.setWidgets(self.ui, setChecked_False='chk001-2')


	def chk001(self):
		'''
		Select Nth: uncheck other checkboxes
		'''
		self.setWidgets(self.ui, setChecked_False='chk000,chk002')


	def chk002(self):
		'''
		Select Nth: uncheck other checkboxes
		'''
		self.setWidgets(self.ui, setChecked_False='chk000-1')


	def chk004(self):
		'''
		Ignore Backfacing (Camera Based Selection)
		'''
		for obj in rt.selection:
			if self.ui.chk004.isChecked():
				sel.ignoreBackfacing = True
				# self.viewPortMessage("Camera-based selection <hl>On</hl>.")
			else:
				sel.ignoreBackfacing = False
				# self.viewPortMessage("Camera-based selection <hl>Off</hl>.")


	def chk005(self):
		'''
		Select Style: Marquee
		'''
		self.setSelectionStyle('selectContext')
		self.setWidgets(self.ui, setChecked='chk005', setChecked_False='chk006-7')
		self.ui.cmb004.setCurrentIndex(0)


	def chk006(self):
		'''
		Select Style: Lasso
		'''
		self.setSelectionStyle('lassoContext')
		self.setWidgets(self.ui, setChecked='chk006', setChecked_False='chk005,chk007')
		self.ui.cmb004.setCurrentIndex(1)


	def chk007(self):
		'''
		Select Style: Paint
		'''
		self.setSelectionStyle('paintContext')
		self.setWidgets(self.ui, setChecked='chk007', setChecked_False='chk005-6')
		self.ui.cmb004.setCurrentIndex(2)


	def setSelectionStyle(self, ctx):
		'''
		Set the selection style context.
		args:
			ctx (str) = Selection style context. Possible values include: 'marquee', 'lasso', 'drag'.
		'''
		if pm.contextInfo(ctx, exists=True):
			pm.deleteUI(ctx)

		if ctx=='selectContext':
			ctx = pm.selectContext(ctx)
		elif ctx=='lassoContext':
			ctx = pm.lassoContext(ctx)
		elif ctx=='paintContext':
			ctx = pm.artSelectCtx(ctx)

		pm.setToolTo(ctx)
		self.viewPortMessage('Select Style: <hl>'+ctx+'</hl>')


	def cmb000(self, index=None):
		'''
		List Selection Sets
		'''
		cmb = self.ui.cmb000

		selectionSets = [set for set in rt.selectionSets]
		contents = self.comboBox(cmb, [set.name for set in selectionSets], "Sets")

		if not index:
			index = cmb.currentIndex()
		if index!=0:
			rt.select(contents[index])
			cmb.setCurrentIndex(0)


	def cmb001(self, index=None):
		'''
		Editors
		'''
		cmb = self.ui.cmb001

		files = ['']
		contents = self.comboBox(cmb, files, ' ')

		if not index:
			index = cmb.currentIndex()
		if index!=0:
			if index==contents.index(''):
				pass
			cmb.setCurrentIndex(0)


	def cmb002(self, index=None):
		'''
		Select All Of Type
		'''
		cmb = self.ui.cmb002
	
		list_ = ['Geometry', 'Shapes', 'Lights', 'Cameras', 'Helpers', 'Space Warps', 'Particle Systems', 'Bone Objects']
		contents = self.comboBox(cmb, list_, 'Select by Type:')

		if not index:
			index = cmb.currentIndex()
		if index!=0:
			if index==contents.index('Geometry'): #Select all Geometry
				rt.select(rt.geometry)
			if index==contents.index('Shapes'): #Select all Geometry
				rt.select(rt.shapes)
			if index==contents.index('Lights'): #Select all Geometry
				rt.select(rt.lights)
			if index==contents.index('Cameras'): #Select all Geometry
				rt.select(rt.cameras)
			if index==contents.index('Helpers'): #Select all Geometry
				rt.select(rt.helpers)
			if index==contents.index('Space Warps'): #Select all Geometry
				rt.select(rt.spacewarps)
			if index==contents.index('Particle Systems'): #Select all Geometry
				rt.select(rt.particelsystems)
			if index==contents.index('Bone Objects'): #Select all Geometry
				rt.select(rt.boneobjects)

			cmb.setCurrentIndex(0)


	def cmb003(self, index=None):
		'''
		Convert To
		'''
		cmb = self.ui.cmb003

		list_ = ['Vertex', 'Edge', 'Border', 'Face', 'Element']
		contents = self.comboBox(cmb, list_, 'Convert To')
		
		if not index:
			index = cmb.currentIndex()
		if index!=0:
			for obj in rt.selection:
				for i in list_:
					if index==contents.index(i):
						obj.convertSelection('CurrentLevel', i) #Convert current selection to index of string i
						# rt.setSelectionLevel(obj, i) #Change component mode to i
						rt.subObjectLevel = contents.index(i)
			cmb.setCurrentIndex(0)


	def cmb004(self, index=None):
		'''
		Select Style: Set Context
		'''
		cmb = self.ui.cmb004

		list_ = ['Marquee', 'Lasso', 'Paint'] 

		contents = self.comboBox (cmb, list_)

		if not index:
			index = cmb.currentIndex()

		if index==contents.index('Marquee'): #
			self.chk005()
		if index==contents.index('Lasso'): #
			self.chk006()
		if index==contents.index('Paint'): #
			self.chk007()


	def b000(self):
		'''
		Create Selection Set
		'''
		name = str(self.ui.t000.text())+"Set"

		sel = rt.selection

		if sel:
			if name=='set#Set': #generate a generic name based on obj.name
				num = self.cycle(list(range(99)), 'selectionSetNum')
				name=sel[0].name+'Set'+str(num)
				rt.selectionSets[name]
			else:
				rt.selectionSets[name] #if set exists, overwrite set; else create set
		else:
			print '# Warning: No valid objects selected. #'


	def b001(self):
		'''
		'''


	def b002(self):
		'''
		
		'''
		pass


	def b003(self):
		'''
		
		'''
		pass


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
		Select Similar
		'''
		tolerance = str(self.ui.s000.value()) #string value because mel.eval is sending a command string
		mel.eval("doSelectSimilar 1 {\""+ tolerance +"\"}")


	def b007(self):
		'''
		Select Island: Select Polygon Face Island
		'''
		rangeX = float(self.ui.s002.value())
		rangeY = float(self.ui.s004.value())
		rangeZ = float(self.ui.s005.value())

		curmod = rt.Modpanel.getcurrentObject()
		curmod.selectAngle=rangeX
		curmod.selectByAngle= not curmod.selectByAngle

		# $.selectAngle=rangeX
		# $.selectByAngle = on
		# sel = $.selectedfaces as bitarray #maintains current single selection. need to reselect with angle contraint active to make work.
		# $.selectByAngle = off
		# print sel
		# setFaceSelection sel #{}


	def b008(self):
		'''
		Select Nth
		'''
		step = self.ui.s003.value()


		if self.ui.chk000.isChecked(): #Select Ring
			rt.macros.run('PolyTools', 'Ring')

		elif self.ui.chk001.isChecked(): #Select contigious
			if rt.subObjectLevel==2: #Edge
				maxEval('''
				curmod = Modpanel.getcurrentObject()
				if ( Ribbon_Modeling.IsEditablePoly() ) then
				(
					curmod.SelectEdgeRing();
				)
				else
				(
					curmod.ButtonOp #SelectEdgeRing;
				)
				''')
			elif rt.subObjectLevel==4: #Face
				pass
		
		elif self.ui.chk002.isChecked(): #Shortest Edge Path
			self.shortestEdgePath()
			# maxEval('SelectShortestEdgePathTool;')

		else: #Select Loop
			rt.macros.run('PolyTools', 'Loop')
			
			# if rt.subObjectLevel==2: #Edge
			# 	mel.eval("selectEveryNEdge;")
			# elif rt.subObjectLevel==4: #Face
			# 	self.selectFaceLoop(tolerance=50)


	def b009(self):
		'''

		'''
		pass


	def b10(self):
		'''
		
		'''
		pass


	def b011(self):
		'''
		
		'''
		pass


	def b012(self):
		'''
		
		'''
		pass


	def b013(self):
		'''
		Lasso Select
		'''
		mel.eval("LassoTool;")


	def b014(self):
		'''
		Grow Selection
		'''
		# expand functionalitly to grow according to selection type
		#grow line #PolytoolsSelect.Pattern7 1
		#grow loop #PolytoolsSelect.GrowLoop()
		#grow ring #PolytoolsSelect.GrowRing()
		for obj in rt.selection:
			obj.EditablePoly.GrowSelection()


	def b015(self):
		'''
		Shrink Selection
		'''
		for obj in rt.selection:
			obj.EditablePoly.ShrinkSelection()


	def b016(self):
		'''
		
		'''
		pass


	def b017(self):
		'''
		
		'''
		pass


	def b018(self):
		'''
		
		'''
		pass


	def b019(self):
		'''
		
		'''
		pass


	def b020(self):
		'''

		'''
		pass





		




#module name
print os.path.splitext(os.path.basename(__file__))[0]
# -----------------------------------------------
# Notes
# -----------------------------------------------