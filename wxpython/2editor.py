#!/usr/bin/env python

import wx 
import os

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        self.dirname = ' '
        wx.Frame.__init__(self,parent,title=title,size=(200,500))
        self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN,"&open","open a file")
        menuAbout = filemenu.Append(wx.ID_ABOUT,"&about","open a file")
        menuExit = filemenu.Append(wx.ID_EXIT,"&exit","open a file")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&file")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.OnOpen,menuOpen)
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)
        self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)

        self.sizer2= wx.BoxSizer(wx.HORIZONTAL)
        self.buttons=[]
        for i in range(0,6):
            self.buttons.append(wx.Button(self,-1,"button &"+str(i)))
            self.sizer2.Add(self.buttons[i],1,wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,1,wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self," a editor \n in pyton","about editor",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,e):
        self.Close(True)

    def OnOpen(self,e):
        """ open a file"""
        dlg = wx.FileDialog(self,"choose a file",self.dirname,"","*.*",wx.OPEN)
        if dlg.ShowModal()==wx.ID_OK:
            self.filename= dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename),'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame= MainWindow(None,"sameple editor")
app.MainLoop()
