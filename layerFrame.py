import wx
from utils import load_image

class LayerFrame(wx.Frame):
	def __init__(self, parent = None, id = -1, UpdateUI = None, UpdateSite = None, Number = None, BackSite = None):
		wx.Frame.__init__(self, parent, id, title = '样品管理系统', size = (320, 600), pos = (500, 100))

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
		text4 = '4'
		text5 = '5'

		self.first_button = wx.Button(panel, -1, label = text1, size = (300, 100), pos = (0, 0))
		self.second_button = wx.Button(panel, -1, label = text2, size = (300, 100), pos = (0, 100))
		self.third_button = wx.Button(panel, -1, label = text3, size = (300, 100), pos = (0, 200))
		self.fourth_button = wx.Button(panel, -1, label = text4, size = (300, 100), pos = (0, 300))
		self.fifth_button = wx.Button(panel, -1, label = text5, size = (300, 100), pos = (0, 400))

		self.Quit_button = wx.Button(panel, -1, 'Quit', size = (50, 50), pos = (0, 500))
		self.Quit_button.SetBackgroundColour('red')
		self.Quit_button.SetForegroundColour('white')
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.Quit_button)

		self.Back_button = wx.Button(panel, -1, '返回上级', size = (60, 50), pos = (50, 500))

		self.Bind(wx.EVT_BUTTON, self.IntoBack, self.Back_button)

		self.Bind(wx.EVT_BUTTON, self.Intobox, self.first_button)
		self.Bind(wx.EVT_BUTTON, self.Intobox, self.second_button)
		self.Bind(wx.EVT_BUTTON, self.Intobox, self.third_button)
		self.Bind(wx.EVT_BUTTON, self.Intobox, self.fourth_button)
		self.Bind(wx.EVT_BUTTON, self.Intobox, self.fifth_button)

	def Intobox(self, event):
		ID2 = event.GetEventObject().GetLabel()
		for x in list(range(1,6)):
			if str(x) == ID2:
				self.UpdateSite(self.Number, x)
		self.UpdateUI(4)

	def IntoBack(self, event):
		self.BackSite(1)
		self.UpdateUI(2)

	def OnExit(self, event):
		wx.Exit()