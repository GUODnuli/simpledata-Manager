import wx
from utils import load_image
from capture_data import Openfile

class TubeFrame(wx.Frame):
	def __init__(self, parent = None, id = -1, UpdateUI = None, UpdateSite = None, Number = None, BackSite = None):
		wx.Frame.__init__(self, parent, id, title = '样品管理系统', size = (1000, 800), pos = (500, 100))

		self.UpdateUI = UpdateUI
		self.UpdateSite = UpdateSite
		self.Number = Number
		self.Now_Number = Number
		self.BackSite = BackSite
		self.InitUI()


	def InitUI(self):
		self.panel = wx.Panel(self, -1, size = (1000, 800), pos = (0, 0))

		self.panel2 = wx.Panel(self, -1, size = (300, 300), pos = (630, 0))
		self.name_text = wx.StaticText(self.panel2, -1, label = '名称:')
		self.name_show = wx.StaticText(self.panel2, -1, label = '', size = (200, 30))
		
		self.type_text = wx.StaticText(self.panel2, -1, label = '类型:')
		self.type_show = wx.StaticText(self.panel2, -1, label = '', size = (200, 30))

		self.source_text = wx.StaticText(self.panel2, -1, label = '来源:')
		self.source_show = wx.StaticText(self.panel2, -1, label = '', size = (200, 30))

		self.Intime_text = wx.StaticText(self.panel2, -1, label = '收集时间:')
		self.Intime_show = wx.StaticText(self.panel2, -1, label = '', size = (200, 30))

		self.Outtime_text = wx.StaticText(self.panel2, -1, label = '取出时间:')
		self.Outtime_show =  wx.StaticText(self.panel2, -1, label = '', size = (200, 30))

		self.gbsizer = wx.GridBagSizer(hgap = 10, vgap = 10)

		self.gbsizer.Add(self.name_text, pos = (0, 0), span = (1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.name_show, pos=(0, 1), span=(1, 1), flag = wx.EXPAND)
		
		self.gbsizer.Add(self.type_text, pos=(1, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.type_show, pos=(1, 1), span=(1, 1), flag = wx.EXPAND)

		self.gbsizer.Add(self.source_text, pos=(2, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.source_show, pos=(2, 1), span=(1, 1), flag = wx.EXPAND)

		self.gbsizer.Add(self.Intime_text, pos=(3, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.Intime_show, pos=(3, 1), span=(1, 1), flag = wx.EXPAND)

		self.gbsizer.Add(self.Outtime_text, pos=(4, 0), span=(1, 1), flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
		self.gbsizer.Add(self.Outtime_show, pos=(4, 1), span=(1, 1), flag = wx.EXPAND)

		sbox = wx.StaticBox(self.panel2, 1, label = u'样品资料')
		self.sbsizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)
		self.sbsizer.Add(self.gbsizer, proportion = 0, flag = wx.EXPAND, border = 10)
		
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.sbsizer, 0, wx.EXPAND, 20)
		self.isShown = False
		self.sizer.Hide(self.sbsizer)

		self.button1  = wx.Button(self.panel, 1, label = '1',  size = (50, 50), pos = (0,0))
		self.button2  = wx.Button(self.panel, 2, label = '2',  size = (50, 50), pos = (70,0))
		self.button3  = wx.Button(self.panel, 3, label = '3',  size = (50, 50), pos = (140,0))
		self.button4  = wx.Button(self.panel, 4, label = '4',  size = (50, 50), pos = (210,0))
		self.button5  = wx.Button(self.panel, 5, label = '5',  size = (50, 50), pos = (280,0))
		self.button6  = wx.Button(self.panel, 6, label = '6',  size = (50, 50), pos = (350,0))
		self.button7  = wx.Button(self.panel, 7, label = '7',  size = (50, 50), pos = (420,0))
		self.button8  = wx.Button(self.panel, 8, label = '8',  size = (50, 50), pos = (490,0))
		self.button9  = wx.Button(self.panel, 9, label = '9',  size = (50, 50), pos = (560,0))
		self.button10 = wx.Button(self.panel, 10, label = '10', size = (50, 50), pos = (0,70))
		self.button11 = wx.Button(self.panel, 11, label = '11', size = (50, 50), pos = (70,70))
		self.button12 = wx.Button(self.panel, 12, label = '12', size = (50, 50), pos = (140,70))
		self.button13 = wx.Button(self.panel, 13, label = '13', size = (50, 50), pos = (210,70))
		self.button14 = wx.Button(self.panel, 14, label = '14', size = (50, 50), pos = (280,70))
		self.button15 = wx.Button(self.panel, 15, label = '15', size = (50, 50), pos = (350,70))
		self.button16 = wx.Button(self.panel, 16, label = '16', size = (50, 50), pos = (420,70))
		self.button17 = wx.Button(self.panel, 17, label = '17', size = (50, 50), pos = (490,70))
		self.button18 = wx.Button(self.panel, 18, label = '18', size = (50, 50), pos = (560,70))
		self.button19 = wx.Button(self.panel, 19, label = '19', size = (50, 50), pos = (0,140))
		self.button20 = wx.Button(self.panel, 20, label = '20', size = (50, 50), pos = (70,140))
		self.button21 = wx.Button(self.panel, 21, label = '21', size = (50, 50), pos = (140,140))
		self.button22 = wx.Button(self.panel, 22, label = '22', size = (50, 50), pos = (210,140))
		self.button23 = wx.Button(self.panel, 23, label = '23', size = (50, 50), pos = (280,140))
		self.button24 = wx.Button(self.panel, 24, label = '24', size = (50, 50), pos = (350,140))
		self.button25 = wx.Button(self.panel, 25, label = '25', size = (50, 50), pos = (420,140))
		self.button26 = wx.Button(self.panel, 26, label = '26', size = (50, 50), pos = (490,140))
		self.button27 = wx.Button(self.panel, 27, label = '27', size = (50, 50), pos = (560,140))
		self.button28 = wx.Button(self.panel, 28, label = '28', size = (50, 50), pos = (0,210))
		self.button29 = wx.Button(self.panel, 29, label = '29', size = (50, 50), pos = (70,210))
		self.button30 = wx.Button(self.panel, 30, label = '30', size = (50, 50), pos = (140,210))
		self.button31 = wx.Button(self.panel, 31, label = '31', size = (50, 50), pos = (210,210))
		self.button32 = wx.Button(self.panel, 32, label = '32', size = (50, 50), pos = (280,210))
		self.button33 = wx.Button(self.panel, 33, label = '33', size = (50, 50), pos = (350,210))
		self.button34 = wx.Button(self.panel, 34, label = '34', size = (50, 50), pos = (420,210))
		self.button35 = wx.Button(self.panel, 35, label = '35', size = (50, 50), pos = (490,210))
		self.button36 = wx.Button(self.panel, 36, label = '36', size = (50, 50), pos = (560,210))
		self.button37 = wx.Button(self.panel, 37, label = '37', size = (50, 50), pos = (0,280))
		self.button38 = wx.Button(self.panel, 38, label = '38', size = (50, 50), pos = (70,280))
		self.button39 = wx.Button(self.panel, 39, label = '39', size = (50, 50), pos = (140,280))
		self.button40 = wx.Button(self.panel, 40, label = '40', size = (50, 50), pos = (210,280))
		self.button41 = wx.Button(self.panel, 41, label = '41', size = (50, 50), pos = (280,280))
		self.button42 = wx.Button(self.panel, 42, label = '42', size = (50, 50), pos = (350,280))
		self.button43 = wx.Button(self.panel, 43, label = '43', size = (50, 50), pos = (420,280))
		self.button44 = wx.Button(self.panel, 44, label = '44', size = (50, 50), pos = (490,280))
		self.button45 = wx.Button(self.panel, 45, label = '45', size = (50, 50), pos = (560,280))
		self.button46 = wx.Button(self.panel, 46, label = '46', size = (50, 50), pos = (0,350))
		self.button47 = wx.Button(self.panel, 47, label = '47', size = (50, 50), pos = (70,350))
		self.button48 = wx.Button(self.panel, 48, label = '48', size = (50, 50), pos = (140,350))
		self.button49 = wx.Button(self.panel, 49, label = '49', size = (50, 50), pos = (210,350))
		self.button50 = wx.Button(self.panel, 50, label = '50', size = (50, 50), pos = (280,350))
		self.button51 = wx.Button(self.panel, 51, label = '51', size = (50, 50), pos = (350,350))
		self.button52 = wx.Button(self.panel, 52, label = '52', size = (50, 50), pos = (420,350))
		self.button53 = wx.Button(self.panel, 53, label = '53', size = (50, 50), pos = (490,350))
		self.button54 = wx.Button(self.panel, 54, label = '54', size = (50, 50), pos = (560,350))
		self.button55 = wx.Button(self.panel, 55, label = '55', size = (50, 50), pos = (0,420))
		self.button56 = wx.Button(self.panel, 56, label = '56', size = (50, 50), pos = (70,420))
		self.button57 = wx.Button(self.panel, 57, label = '57', size = (50, 50), pos = (140,420))
		self.button58 = wx.Button(self.panel, 58, label = '58', size = (50, 50), pos = (210,420))
		self.button59 = wx.Button(self.panel, 59, label = '59', size = (50, 50), pos = (280,420))
		self.button60 = wx.Button(self.panel, 60, label = '60', size = (50, 50), pos = (350,420))
		self.button61 = wx.Button(self.panel, 61, label = '61', size = (50, 50), pos = (420,420))
		self.button62 = wx.Button(self.panel, 62, label = '62', size = (50, 50), pos = (490,420))
		self.button63 = wx.Button(self.panel, 63, label = '63', size = (50, 50), pos = (560,420))
		self.button64 = wx.Button(self.panel, 64, label = '64', size = (50, 50), pos = (0,490))
		self.button65 = wx.Button(self.panel, 65, label = '65', size = (50, 50), pos = (70,490))
		self.button66 = wx.Button(self.panel, 66, label = '66', size = (50, 50), pos = (140,490))
		self.button67 = wx.Button(self.panel, 67, label = '67', size = (50, 50), pos = (210,490))
		self.button68 = wx.Button(self.panel, 68, label = '68', size = (50, 50), pos = (280,490))
		self.button69 = wx.Button(self.panel, 69, label = '69', size = (50, 50), pos = (350,490))
		self.button70 = wx.Button(self.panel, 70, label = '70', size = (50, 50), pos = (420,490))
		self.button71 = wx.Button(self.panel, 71, label = '71', size = (50, 50), pos = (490,490))
		self.button72 = wx.Button(self.panel, 72, label = '72', size = (50, 50), pos = (560,490))
		self.button73 = wx.Button(self.panel, 73, label = '73', size = (50, 50), pos = (0,560))
		self.button74 = wx.Button(self.panel, 74, label = '74', size = (50, 50), pos = (70,560))
		self.button75 = wx.Button(self.panel, 75, label = '75', size = (50, 50), pos = (140,560))
		self.button76 = wx.Button(self.panel, 76, label = '76', size = (50, 50), pos = (210,560))
		self.button77 = wx.Button(self.panel, 77, label = '77', size = (50, 50), pos = (280,560))
		self.button78 = wx.Button(self.panel, 78, label = '78', size = (50, 50), pos = (350,560))
		self.button79 = wx.Button(self.panel, 79, label = '79', size = (50, 50), pos = (420,560))
		self.button80 = wx.Button(self.panel, 80, label = '80', size = (50, 50), pos = (490,560))
		self.button81 = wx.Button(self.panel, 81, label = '81', size = (50, 50), pos = (560,560))

		self.Quit_button = wx.Button(self.panel, -1, 'Quit', size = (50, 50), pos = (0,610))
		self.Quit_button.SetBackgroundColour('red')
		self.Quit_button.SetForegroundColour('white')
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.Quit_button)

		self.BackTop_button = wx.Button(self.panel, -1, '返回首页', size = (60, 50), pos = (110, 610))
		self.Bind(wx.EVT_BUTTON, self.BackTop, self.BackTop_button)

		self.Back_button = wx.Button(self.panel, -1, '返回上级', size = (60, 50), pos = (50, 610))
		self.Bind(wx.EVT_BUTTON, self.IntoBack, self.Back_button)

		self.button1.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button1.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button1.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button2.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button2.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button2.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button3.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button3.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button3.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button4.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button4.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button4.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button5.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button5.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button5.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button6.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button6.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button6.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button7.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button7.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button7.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button8.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button8.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button8.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button9.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button9.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button9.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button10.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button10.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button10.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button11.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button11.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button11.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button12.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button12.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button12.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button13.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button13.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button13.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button14.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button14.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button14.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button15.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button15.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button15.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button16.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button16.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button16.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button17.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button17.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button17.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button18.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button18.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button18.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button19.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button19.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button19.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button20.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button20.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button20.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button21.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button21.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button21.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button22.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button22.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button22.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button23.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button23.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button23.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button24.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button24.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button24.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button25.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button25.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button25.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button26.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button26.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button26.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button27.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button27.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button27.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button28.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button28.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button28.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button29.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button29.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button29.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button30.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button30.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button30.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button31.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button31.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button31.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button32.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button32.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button32.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button33.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button33.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button33.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button34.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button34.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button34.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button35.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button35.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button35.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button36.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button36.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button36.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button37.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button37.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button37.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button38.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button38.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button38.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button39.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button39.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button39.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button40.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button40.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button40.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button41.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button41.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button41.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button42.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button42.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button42.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button43.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button43.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button43.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button44.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button44.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button44.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button45.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button45.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button45.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button46.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button46.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button46.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button47.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button47.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button47.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button48.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button48.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button48.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button49.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button49.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button49.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button50.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button50.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button50.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button51.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button51.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button51.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button52.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button52.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button52.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button53.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button53.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button53.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button54.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button54.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button54.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button55.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button55.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button55.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button56.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button56.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button56.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button57.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button57.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button57.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button58.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button58.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button58.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button59.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button59.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button59.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button60.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button60.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button60.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button61.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button61.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button61.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button62.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button62.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button62.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button63.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button63.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button63.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button64.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button64.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button64.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button65.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button65.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button65.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button66.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button66.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button66.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button67.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button67.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button67.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button68.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button68.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button68.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button69.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button69.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button69.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button70.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button70.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button70.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button71.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button71.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button71.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button72.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button72.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button72.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button73.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button73.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button73.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button74.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button74.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button74.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button75.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button75.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button75.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button76.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button76.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button76.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button77.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button77.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button77.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button78.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button78.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button78.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button79.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button79.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button79.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

		self.button80.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button80.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button80.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)
		
		self.button81.Bind(wx.EVT_BUTTON, self.Intoimformation)
		self.button81.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterbutton)
		self.button81.Bind(wx.EVT_LEAVE_WINDOW, self.OutLeavebutton)

	def OnEnterbutton(self, event):
		ID = event.GetEventObject().GetLabel()
		for x in list(range(1,82)):
			if str(x) == ID:
				self.Now_Number = self.Now_Number * x

		Data_list = Openfile(self.Now_Number)

		self.name_show.SetLabel(str(Data_list[0]))
		self.type_show.SetLabel(str(Data_list[1]))
		self.source_show.SetLabel(str(Data_list[2]))
		self.Intime_show.SetLabel(str(Data_list[3]))
		self.Outtime_show.SetLabel(str(Data_list[4]))

		self.sizer.Show(self.sbsizer)
		self.isShown = True
		self.sizer.Layout()

	def OutLeavebutton(self, event):
		self.Now_Number = self.Number
		self.sizer.Hide(self.sbsizer)
		self.isShown = False

	def backSite(self, event):
		self.BackSite(1)

	def backTopSite(self, event):
		self.BackSite(2)

	def Intoimformation(self, event):
		ID2 = event.GetEventObject().GetLabel()
		for x in list(range(1,82)):
			if str(x) == ID2:
				self.UpdateSite(self.Number, x)
		self.UpdateUI(6)

	def IntoBack(self, event):
		self.BackSite(1)
		self.UpdateUI(4)

	def BackTop(self,event):
		self.BackSite(2)
		self.UpdateUI(0)

	def OnExit(self, event):
		wx.Exit()
	