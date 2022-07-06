import wx
from SimplePlugin.simple_plugin_action import SimplePlugin


class SimplePluginApp(wx.App):
    def OnInit(self):
        frame = SimplePlugin()
        if frame.Show() == wx.ID_OK:
            print("Should generate bom")
        return True

def main():
    app = SimplePluginApp()
    app.MainLoop()

    print("Done")

if __name__ == "__main__":
    main()