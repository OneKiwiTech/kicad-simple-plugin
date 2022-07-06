import logging
from ..model.model import Model
from ..view.view import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = SimplePluginView()
        self.panel1 = SimplePluginView1(self.view.notebook)
        self.panel2 = SimplePluginView2(self.view.notebook)
        self.view.notebook.AddPage(self.panel1, "Panel1")
        self.view.notebook.AddPage(self.panel2, "Panel2")

        # Connect Events
        self.view.button0.Bind(wx.EVT_BUTTON, self.OnButton0Click)
        self.panel1.button1.Bind(wx.EVT_BUTTON, self.OnButton1Click)
        self.panel2.button2.Bind(wx.EVT_BUTTON, self.OnButton2Click)

    def Show(self):
        self.view.Show()
    
    # Event handlers
    def OnButton0Click(self, event):
        self.panel1.SetTextStatus(self.model.status0)
        logging.debug('button0 pressed')

    def OnButton1Click(self, event):
        self.panel2.SetTextStatus(self.model.status1)
        logging.debug('button1 pressed')

    def OnButton2Click(self, event):
        self.view.SetTextStatus(self.model.status2)
        logging.debug('button2 pressed')