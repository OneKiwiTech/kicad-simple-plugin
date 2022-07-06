from .dialog import *

class SimplePluginView (SimplePluginFrame):
    def __init__(self):
        super(SimplePluginView, self).__init__(None)
    
    def SetTextStatus(self, value):
        self.text0.LabelText = value

class SimplePluginView1 (SimplePluginPanel1):
    def __init__( self, parent):
        SimplePluginPanel1.__init__(self, parent)

    def SetTextStatus(self, value):
        self.text1.LabelText = value

class SimplePluginView2 (SimplePluginPanel2):
    def __init__( self, parent):
        SimplePluginPanel2.__init__(self, parent)
    
    def SetTextStatus(self, value):
        self.text2.LabelText = value