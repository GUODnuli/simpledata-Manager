import wx
from utils import load_image

class DrawerFrame(wx.Frame):
	def __init__(self, parent = None, id = -1, UpdateUI = None, UpdateSite = None, Number = None, BackSite = None):
		wx.Frame.__init__(self, parent, id, title = '样品管理系统', size = (700, 600), pos = (500, 100))

		self.UpdateUI = UpdateUI
		self.UpdateSite = UpdateSite
		self.Number = Number
		self.BackSite = BackSite
		self.InitUI()

	def InitUI(self):
		panel = wx.Panel(self)

		text1 = '1'
		text2 = '2'
		text3 = '3'

		self.first_button = wx.Button(panel, -1, label = text1, size = (200, 400), pos = (0,0))
		self.second_button = wx.Button(panel, -1, label = text2, size = (200, 400), pos = (200,0))
		self.third_button = wx.Button(panel, -1, label = text3, size = (200, 400), pos = (400,0))

		self.Quit_button = wx.Button(panel, -1, 'Quit', size = (50, 50), pos = (0,400))
		self.Quit_button.SetBackgroundColour('red')
		self.Quit_button.SetForegroundColour('white')
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.Quit_button)

		self.Back_button = wx.Button(panel, -1, '返回上级', size = (60, 50), pos = (50, 400))
		self.Bind(wx.EVT_BUTTON, self.IntoBack, self.Back_button)

		self.Bind(wx.EVT_BUTTON, self.Intolayer, self.first_button)
		self.Bind(wx.EVT_BUTTON, self.Intolayer, self.second_button)
		self.Bind(wx.EVT_BUTTON, self.Intolayer, self.third_button)

	def Intolayer(self, event):
		ID2 = event.GetEventObject().GetLabel()
		for x in list(range(1,4)):
			if str(x) == ID2:
				self.UpdateSite(self.Number, x)
		self.UpdateUI(3)

	def IntoBack(self, event):
		self.BackSite(1)
		self.UpdateUI(1)

	def OnExit(self, event):
		wx.Exit()