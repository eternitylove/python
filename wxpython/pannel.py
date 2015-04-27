#!/usr/bin/env python

import wx
class exampleframe(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,size=(500,500))
		self.quote = wx.StaticText(self,label="your quota:",pos=(20,30))
		
		self.logger = wx.TextCtrl(self,pos=(300,20),size=(200,300),style=wx.TE_MULTILINE|wx.TE_READONLY)
		self.button = wx.Button(self,label="save",pos=(200,325))
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)

		self.lblname = wx.StaticText(self,label="your name:",pos=(20,60))
		self.editname = wx.TextCtrl(self,value="enter your name",pos=(150,60),size=(140,-1))
		self.Bind(wx.EVT_TEXT,self.EvtText,self.editname)
		self.Bind(wx.EVT_CHAR,self.EvtChar,self.editname)
		
		self.sampleList = [ 'friends','advertising','web serach','yellowpages']
		self.lblhear = wx.StaticText(self,label="how did you hear from us?",pos=(20,90))
		self.edithear=wx.ComboBox(self,pos=(150,90),size=(95,-1),choices=self.sampleList,style=wx.CB_DROPDOWN)
		self.Bind(wx.EVT_COMBOBOX,self.EvtComboBox,self.edithear)
		self.Bind(wx.EVT_TEXT,self.EvtText,self.edithear)
		
		self.insure = wx.CheckBox(self,label="do you want insured shipment?",pos=(20,180))
		self.Bind(wx.EVT_CHECKBOX,self.EvtCheckBox,self.insure)

		radioList=['blue','red','yellow','orange','green','purple','navy blue','black','gray']
		rb=wx.RadioBox(self,label="what color would you like?",pos=(20,210),choices=radioList,majorDimension=3,style=wx.RA_SPECIFY_COLS)

		self.Bind(wx.EVT_RADIOBOX,self.EvtRadioBox,rb)

	def EvtRadioBox(self,event):
		self.logger.AppendText("evtradiobox:%d\n"%event.GetInt())
	def EvtComboBox(self,event):
		self.logger.AppendText("evtcombobox:%s\n"%event.GetString())

	def OnClick(self,event):
		self.logger.AppendText("click on object with id:%d\n"%event.GetId())
	def EvtText(self,event):
		self.logger.AppendText("evtText:%s\n"%event.GetString())
	def EvtChar(self,event):
		self.logger.AppendText("evtchar:%d\n"%event.GetKeyCode())
		event.Skip()

	def EvtCheckBox(self,event):
		self.logger.AppendText("evtCheckBox:%d\n"%event.Checked())

app=wx.App(False)
frame=wx.Frame(None)
pannel=exampleframe(frame)
frame.Show()
app.MainLoop()
