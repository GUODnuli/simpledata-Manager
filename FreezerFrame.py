import wx
from utils import load_image

class TopFrame(wx.Frame):			#顶部窗口
	def __init__(self, parent = None, id = -1, UpdateUI = None):
		wx.Frame.__init__(self, parent, id, title = '样品管理系统',  size = (400, 500), pos = (800, 250))

		self.UpdateUI = UpdateUI
		self.InitUI()

	def InitUI(self):				#顶部窗口样式
		panel = wx.Panel(self)

		logo_freezer = wx.Image(load_image('refrigerator.png'),wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		txt_freezer = '单击进入冰箱'
		even = ['name','type','source','Input time','out time']
		#通过位图按钮实现冰箱样式的按钮
		self.button_freezer = wx.BitmapButton(panel, id = -1, bitmap = logo_freezer, size = (logo_freezer.GetWidth() + 10, logo_freezer.GetHeight() + 10))		
		
		self.Bind(wx.EVT_BUTTON, self.Intofreezer, self.button_freezer)

		#退出主循环的按钮
		self.Quit_button = wx.Button(panel, -1, 'Quit', size = (50, 50), pos = (0, logo_freezer.GetHeight() + 60))		
		self.Quit_button.SetBackgroundColour('red')
		self.Quit_button.SetForegroundColour('white')
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.Quit_button)

	def Intofreezer(self, event):  		#更新UI的函数
		self.UpdateUI(1)

	def OnExit(self, event):		#退出主循环的函数
		wx.Exit()