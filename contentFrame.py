import wx
from utils import load_image

class ContentFrame(wx.Frame):
	def __init__(self, parent = None, id = -1, UpdateUI = None, UpdateSite = None, Number = None):
		wx.Frame.__init__(self, parent, id, title = '样品管理系统', size = (400, 1000), pos = (500, 100))
		
		self.UpdateUI = UpdateUI
		self.UpdateSite = UpdateSite
		self.Number = Number
		self.InitUI()

	def InitUI(self):
		panel = wx.Panel(self)

		text1 = '1'
		text2 = '2'
		text3 = '3'
		text4 = '4'
		txt_select = '选择层数'

		self.text_select = wx.StaticText(panel, -1, label = txt_select, size = (200, 50), pos = (175, 0))
		
		self.first_button = wx.Button(panel, -1, label = text1, size = (400, 200), pos = (0,50))
		self.second_button = wx.Button(panel, -1, label = text2, size = (400, 200), pos = (0,250))
		self.third_button = wx.Button(panel, -1, label = text3, size = (400, 200), pos = (0,450))
		self.fourth_button = wx.Button(panel, -1, label = text4, size = (400, 200), pos = (0,650))

		self.Quit_button = wx.Button(panel, -1, 'Quit', size = (50, 50), pos = (0,850))
		self.Quit_button.SetBackgroundColour('red')
		self.Quit_button.SetForegroundColour('white')
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.Quit_button)

		self.Back_button = wx.Button(panel, -1, '返回上级', size = (60, 50), pos = (50,850))
		self.Bind(wx.EVT_BUTTON, self.IntoBack, self.Back_button)

		self.Bind(wx.EVT_BUTTON, self.Intodrawer, self.first_button)
		self.Bind(wx.EVT_BUTTON, self.Intodrawer, self.second_button)
		self.Bind(wx.EVT_BUTTON, self.Intodrawer, self.third_button)
		self.Bind(wx.EVT_BUTTON, self.Intodrawer, self.fourth_button)

	def Intodrawer(self, event):
		ID2 = event.GetEventObject().GetLabel()
		for x in list(range(1,5)):
			if str(x) == ID2:
				self.UpdateSite(self.Number, x)
		self.UpdateUI(2)

	def IntoBack(self, event):
		self.UpdateUI(0)

	def OnExit(self, event):
		wx.Exit()