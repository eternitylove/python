#!/usr/bin/env python
#http://justcoding.iteye.com/category/91095

import wx

class StaticTextFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"Static text example",size=(400,300))
		panel=wx.Panel(self,-1)
		wx.StaticText(panel,-1,"this is an exampel of static text",(100,10))
		rev=wx.StaticText(panel,-1,"static wic reversed color",(100,30))
		rev.SetforegroundColour("white")
		rev.SetBackgroundColour("black")
		center = wx.StaticText(panel,-1,"align center",(100,50),(160,-1),wx.ALIGH_CENTER)

		center.SetforegroundColour("white")
		center.SetBackgroundColour("black")

		right = wx.StaticText(panel,-1,"align right",(100,70),(160,-1),wx.ALIGH_RIGHT) 
		right.SetforegroundColour("white")
		right.SetBackgroundColour("black")

		str = "you can also change the font"
		text = wx.StaticText(panel,-1,str,(20,100))
		font = wx.Font(18,wx.DECORATIVE,wx.ITALTC,wx.NORMAL)
		text.SetFont(font)
		
		wx.StaticText(panel,-1,"you text \n can be split\n" 
				"over mutilpe lines\n\n evev blandkone",(20,150))
		wx.StaticText(panel,-1,"you text \n can be split\n" 
				"over mutilpe lines\n\n evev blandkone",(220,150),style=wx.ALIGN_RIGHT)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame=StaticTextFrame()
	frame.Show()
	app.MainLoop()

