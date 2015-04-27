#!/usr/bin/env python

import wx
import os

class MainWindow(wx.Frame):
    """we simple devie a new class of Frame"""
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,300))
        self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu=wx.Menu()
        openmenu=wx.Menu()
        
        openfile = openmenu.Append(wx.ID_OPEN,"O&pen","open a file")

        menuAbout= filemenu.Append(wx.ID_ABOUT,"&about","informationa about this program")
        menuExit=filemenu.Append(wx.ID_EXIT,"E&xit","terminat the program")

        menuBar=wx.MenuBar()

        menuBar.Append(filemenu, "&File")
        menuBar.Append(openmenu, "&open")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)
        self.Bind(wx.EVT_MENU,self.OnOpen,openfile)
        filemenu.AppendSeparator()
        self.Show(True)

    def OnAbout(self,e):
        dlg=wx.MessageDialog(self,'a editor',"about sam")
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,e):
        self.Close(True)
    def OnOpen(self,e):
        """open a file"""
        self.dirname=' '
        dlg = wx.FileDialog(self,"choose a file",self.dirname,"","*.*",wx.OPEN)
        if dlg.ShowModal()==wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname,self.filename))
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app=wx.App(False)
frame=MainWindow(None,'small editor')
app.MainLoop()
