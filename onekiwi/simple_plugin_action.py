import logging
import pcbnew
import os
from .simple_plugin_gui import SimplePluginDialog

class SimplePlugin(SimplePluginDialog):

    def __init__(self):
        super(SimplePlugin, self).__init__(None)
    
    def OnDialogShow(self, event):
        file_name = pcbnew.GetBoard().GetFileName()
        base = os.path.basename(file_name)
        self.text.LabelText = base
        logging.debug('dialog show')

    def OnDialogClose(self, event):
        logging.debug('dialog close')
        self.Destroy()
        #self.EndModal(0)
        
    def OnButtonPress(self, event):
        logging.debug('button pressed')
        txt = self.edit.GetValue()
        if txt == '':
            self.text.LabelText = 'Please input text'
        else:
            self.text.LabelText = txt
            self.edit.SetValue('')

    