from ..model.model import Model
from ..view.view import *

class Controller:
    def __init__(self, parent):
        self.model = Model()
        self.view = DialogMain(parent)
        self.panel1 = Test1Panel(self.view.notebook)
        self.panel2 = Test2Panel(self.view.notebook)
        self.view.notebook.AddPage(self.panel1, "Panel1")
        self.view.notebook.AddPage(self.panel2, "Panel2")

        self.DialogtoPanel1(self.model.status1.get())
        self.model.status1.addCallback(self.DialogtoPanel1)

        self.DialogtoPanel2(self.model.status2.get())
        self.model.status2.addCallback(self.DialogtoPanel2)

        self.view.buttonSend1.Bind( wx.EVT_BUTTON, self.OnSend1Click )
        self.view.buttonGet1.Bind( wx.EVT_BUTTON, self.OnGet1Click )
        self.view.buttonSend2.Bind( wx.EVT_BUTTON, self.OnSend2Click )
        self.view.buttonGet2.Bind( wx.EVT_BUTTON, self.OnGet2Click )

        self.panel1.buttonSendMain1.Bind( wx.EVT_BUTTON, self.OnSendMain1Click )
        self.panel1.buttonGetMain1.Bind( wx.EVT_BUTTON, self.OnGetMain1Click )
        self.panel1.buttonSendPanel1.Bind( wx.EVT_BUTTON, self.OnSendPanel1Click )
        self.panel1.buttonGetPanel1.Bind( wx.EVT_BUTTON, self.OnGetPanel1Click )

        self.panel2.buttonSendMain2.Bind( wx.EVT_BUTTON, self.OnSendMain2Click )
        self.panel2.buttonGetMain2.Bind( wx.EVT_BUTTON, self.OnGetMain2Click )
        self.panel2.buttonSendPanel2.Bind( wx.EVT_BUTTON, self.OnSendPanel2Click )
        self.panel2.buttonGetPanel2.Bind( wx.EVT_BUTTON, self.OnGetPanel2Click )

        
    def Show(self):
        self.view.ShowModal()

    # DialogMain Events
    def OnSend1Click(self, event):
        self.model.set_status1('from Dialog to Panel1')

    def OnGet1Click(self, event):
        self.view.textStatus.LabelText = 'OnGet1 x'

    def OnSend2Click(self, event):
        self.model.set_status2('from Dialog to Panel2')

    def OnGet2Click(self, event):
        self.view.textStatus.LabelText = 'OnGet2 v'

    # Test1Panel Events
    def OnSendMain1Click( self, event ):
        self.panel1.text1.LabelText = 'OnSendMain1'

    def OnGetMain1Click( self, event ):
        self.panel1.text1.LabelText = 'OnGetMain1'

    def OnSendPanel1Click( self, event ):
        self.panel1.text1.LabelText = 'OnSendPanel1'

    def OnGetPanel1Click( self, event ):
        self.panel1.text1.LabelText = 'OnGetPanel1'

    # Test2Panel Events
    def OnSendMain2Click( self, event ):
        self.panel2.text2.LabelText = 'OnSendMain2'

    def OnGetMain2Click( self, event ):
        self.panel2.text2.LabelText = 'OnGetMain2'

    def OnSendPanel2Click( self, event ):
        self.panel2.text2.LabelText = 'OnSendPanel2'

    def OnGetPanel2Click( self, event ):
        self.panel2.text2.LabelText = 'OnGetPanel2'
    
    def DialogtoPanel1(self, status):
        self.panel1.SetText1(status)
    
    def DialogtoPanel2(self, status):
        self.panel2.SetText2(status)