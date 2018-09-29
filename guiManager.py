import wx
import FreezerFrame
import contentFrame
import drawerFrame
import layerFrame
import boxFrame
import tubeFrame
import information

class GuiManager():
	def __init__(self, UpdateUI):
		self.UpdateUI = UpdateUI
		self.frameDict = {}#装载已经创建的Frame对象
		self.flag = 1
		self.Number = [1,1,]

	def GetFrame(self, type):
		frame = self.frameDict.get(type)

		if frame is None:
			frame = self.CreateFrame(type)
			self.frameDict[type] = frame
		return frame

	def UpdateSite(self, number, site):
		self.number = number * site
		self.flag += 1
		self.Number.append(self.number)
		print(self.Number)
		print(self.flag)

	def BackSite(self, ps):
		if ps == 1:
			self.Number.pop()
			self.flag -= 1
		else :
			while self.flag >=3:
				self.Number.pop()
				self.flag -=1


	def CreateFrame(self, type):
		if type == 0:
			return FreezerFrame.TopFrame(parent = None, id = type, UpdateUI = self.UpdateUI)
		elif type == 1:
			return contentFrame.ContentFrame(parent = None, id = type, UpdateUI = self.UpdateUI, UpdateSite = self.UpdateSite,  Number = self.Number[self.flag])
		elif type == 2:
			return drawerFrame.DrawerFrame(parent = None, id = type, UpdateUI = self.UpdateUI, UpdateSite = self.UpdateSite,  Number = self.Number[self.flag], BackSite = self.BackSite)
		elif type == 3:
			return layerFrame.LayerFrame(parent = None, id = type, UpdateUI = self.UpdateUI, UpdateSite = self.UpdateSite,  Number = self.Number[self.flag], BackSite = self.BackSite)
		elif type == 4:
			return boxFrame.BoxFrame(parent = None, id = type, UpdateUI = self.UpdateUI, UpdateSite = self.UpdateSite,  Number = self.Number[self.flag], BackSite = self.BackSite)
		elif type == 5:
			return tubeFrame.TubeFrame(parent = None, id = type, UpdateUI = self.UpdateUI, UpdateSite = self.UpdateSite,  Number = self.Number[self.flag], BackSite = self.BackSite)
		elif type == 6:
			return information.TubeFrame(parent = None, id = type, UpdateUI = self.UpdateUI, UpdateSite = self.UpdateSite,  Number = self.Number[self.flag], BackSite = self.BackSite)