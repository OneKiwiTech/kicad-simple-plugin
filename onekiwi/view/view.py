#!/usr/bin/env python3
import wx
import wx.grid

from .dialog import *

class DialogMain(TestDialogBase):
    def __init__(self, parent):
        TestDialogBase.__init__(self, parent)
        self.SetTitle('Component Placement')
    
    def SetMoney(self, money):
        self.textStatus.LabelText = str(money)

class Test1Panel(Test1PanelBase):
    def __init__(self, parent):
        Test1PanelBase.__init__(self, parent)

class Test2Panel(Test2PanelBase):
    def __init__(self, parent):
        Test2PanelBase.__init__(self, parent)

