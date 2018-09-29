import wx
from utils import load_image
from save_data import Data_save
from capture_data import Openfile
class TubeFrame(wx.Frame):
	def __init__(self, parent = None, id = -1, UpdateUI = None, UpdateSite = None, Number = None, BackSite = None):
		wx.Frame.__init__(self, parent, id, title = '样品管理系统', size = (400, 400), pos = (800, 250))

		self.UpdateUI = UpdateUI
		self.UpdateSite = UpdateSite
		self.Number = Number
		print(self.Number)
		self.BackSite = BackSite
		self.InitUI()

	def InitUI(self):
		panel = wx.Panel(self, -1, size = (500, 500), pos = (0, 0))

		self.name_text = wx.StaticText(panel, -1, label = '名称:', size = (50, 30))
		self.type_text = wx.StaticText(panel, -1, label = '类型:', size = (50, 30))
		self.source_text = wx.StaticText(panel, -1, label = '来源:', size = (50, 30))
		self.Intime_text = wx.StaticText(panel, -1, label = '收集时间:', size = (50, 30))
		self.Outtime_text = wx.StaticText(panel, -1, label = '取出时间:', size = (50, 30))
		
		self.name_show = wx.StaticText(panel, -1, label = '', size = (200, 30))
		self.type_show = wx.StaticText(panel, -1, label = '', size = (200, 30))
		self.source_show = wx.StaticText(panel, -1, label = '', size = (200, 30))
		self.Intime_show = wx.StaticText(panel, -1, label = '', size = (200, 30))
		self.Outtime_show =  wx.StaticText(panel, -1, label = '', size = (200, 30))

		self.name_write = wx.TextCtrl(panel, -1, value = '', size = (200, 30))
		self.type_write = wx.TextCtrl(panel, -1, value = '', size = (200, 30))
		self.source_write = wx.TextCtrl(panel, -1, value = '', size = (200, 30))
		self.Intime_write = wx.TextCtrl(panel, -1, value = '', size = (200, 30))
		self.Outtime_write = wx.TextCtrl(panel, -1, value = '', size = (200, 30))

		self.gbsizer = wx.GridBagSizer(hgap = 10, vgap = 10)
		self.gbsizer2 = wx.GridBagSizer(hgap = 10, vgap = 10)

		self.gbsizer.Add(self.name_text, pos = (0, 0), span = (1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.type_text, pos=(1, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.source_text, pos=(2, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.Intime_text, pos=(3, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.Outtime_text, pos=(4, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.name_show, pos=(0, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer.Add(self.type_show, pos=(1, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer.Add(self.source_show, pos=(2, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer.Add(self.Intime_show, pos=(3, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer.Add(self.Outtime_show, pos=(4, 1), span=(1, 1), flag = wx.EXPAND)


		self.gbsizer2.Add(self.name_text, pos = (0, 0), span = (1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer2.Add(self.type_text, pos=(1, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer2.Add(self.source_text, pos=(2, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer2.Add(self.Intime_text, pos=(3, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer2.Add(self.Outtime_text, pos=(4, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer2.Add(self.name_write, pos=(0, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer2.Add(self.type_write, pos=(1, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer2.Add(self.source_write, pos=(2, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer2.Add(self.Intime_write, pos=(3, 1), span=(1, 1), flag = wx.EXPAND)
		self.gbsizer2.Add(self.Outtime_write, pos=(4, 1), span=(1, 1), flag = wx.EXPAND)
		
		
		self.sbox = wx.StaticBox(panel, -1, label = u'样品资料')
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sbsizer = wx.StaticBoxSizer(self.sbox, wx.VERTICAL)
		self.sbsizer.Add(self.gbsizer, proportion = 0, flag = wx.EXPAND, border = 10)
		self.sbsizer2 = wx.StaticBoxSizer(self.sbox, wx.VERTICAL)
		self.sbsizer2.Add(self.gbsizer2, proportion = 0, flag = wx.EXPAND, border = 10)
		self.sizer.Add(self.sbsizer, 0, wx.EXPAND, 20)
		self.sizer.Add(self.sbsizer2, 0, wx.EXPAND, 20)

		Data_list = Openfile(self.Number)
		self.name_show.SetLabel(str(Data_list[0]))
		self.type_show.SetLabel(str(Data_list[1]))
		self.source_show.SetLabel(str(Data_list[2]))
		self.Intime_show.SetLabel(str(Data_list[3]))
		self.Outtime_show.SetLabel(str(Data_list[4]))

		self.is_Show = True
		self.sizer.Hide(self.sbsizer2)
		self.sizer.Show(self.sbsizer)
		self.sizer.Layout()

		self.Quit_button = wx.Button(panel, -1, 'Quit', size = (50, 50), pos = (0,300))
		self.Quit_button.SetBackgroundColour('red')
		self.Quit_button.SetForegroundColour('white')
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.Quit_button)

		self.Back_button = wx.Button(panel, -1, u'返回上级', size = (60, 50), pos = (50, 300))
		self.Bind(wx.EVT_BUTTON, self.IntoBack, self.Back_button)

		self.Back_Top = wx.Button(panel, -1, u'返回首页', size = (60, 50), pos = (110, 300))
		self.Bind(wx.EVT_BUTTON, self.BackTop, self.Back_Top)

		self.edit_button = wx.Button(panel, -1, u'编辑', size = (60, 50), pos = (170, 300))
		self.Bind(wx.EVT_BUTTON, self.Changebutton, self.edit_button)


	def OnExit(self, event):
		wx.Exit()

	def Changebutton(self, event):
		if self.edit_button.GetLabel() == u'编辑':
			self.edit_button.SetLabel(u'保存')
		else:
			name_data = self.name_write.GetValue()
			type_data = self.type_write.GetValue()
			source_data = self.source_write.GetValue()
			Intime_data = self.Intime_write.GetValue()
			Outtime_data = self.Outtime_write.GetValue()
			self.name_show.SetLabel(str(name_data))
			self.type_show.SetLabel(str(type_data))
			self.source_show.SetLabel(str(source_data))
			self.Intime_show.SetLabel(str(Intime_data))
			self.Outtime_show.SetLabel(str(Outtime_data))

			Data_save(name_data, type_data, source_data, Intime_data, Outtime_data, self.Number)
		if self.is_Show == True:
			self.sizer.Hide(self.sbsizer)
			self.is_Show = False
			self.sizer.Show(self.sbsizer2)
			self.sizer.Layout()
		else :
			self.sizer.Hide(self.sbsizer2)
			self.is_Show = True
			self.sizer.Show(self.sbsizer)
			self.sizer.Layout()

			
			self.edit_button.SetLabel(u'编辑')

	def BackTop(self,event):
		self.BackSite(2)
		self.UpdateUI(0)
	def IntoBack(self, event):
		self.BackSite(1)
		self.UpdateUI(5)