#!/usr/bin/env python3
import wx
import wx.grid

from .dialog import *

class DialogMain(TestDialogBase):
    def __init__(self, parent):
        TestDialogBase.__init__(self, parent)
        self.SetTitle('Component Placement')
    
    def SetText(self, status):
        self.textStatus.LabelText = status

class Test1Panel(Test1PanelBase):
    def __init__(self, parent):
        Test1PanelBase.__init__(self, parent)
    
    def SetText1(self, status):
        self.text1.LabelText = status

class Test2Panel(Test2PanelBase):
    def __init__(self, parent):
        Test2PanelBase.__init__(self, parent)
    
    def SetText2(self, status):
        self.text2.LabelText = status

