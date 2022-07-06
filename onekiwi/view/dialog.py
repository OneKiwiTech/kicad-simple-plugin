# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SimplePluginFrame
###########################################################################

class SimplePluginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Simple Plugin MVC", pos = wx.DefaultPosition, size = wx.Size( 320,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.button0 = wx.Button( self, wx.ID_ANY, u"Set text Panel1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.button0, 0, wx.ALL|wx.EXPAND, 5 )

		self.text0 = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text0.Wrap( -1 )

		bSizer2.Add( self.text0, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button0.Bind( wx.EVT_BUTTON, self.OnButton0Click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnButton0Click( self, event ):
		event.Skip()


###########################################################################
## Class SimplePluginPanel1
###########################################################################

class SimplePluginPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 320,240 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.button1 = wx.Button( self, wx.ID_ANY, u"Set text Panel2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.button1, 0, wx.ALL, 5 )

		self.text1 = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text1.Wrap( -1 )

		bSizer3.Add( self.text1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.button1.Bind( wx.EVT_BUTTON, self.OnButton1Click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnButton1Click( self, event ):
		event.Skip()


###########################################################################
## Class SimplePluginPanel2
###########################################################################

class SimplePluginPanel2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 320,240 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.button2 = wx.Button( self, wx.ID_ANY, u"Set text Frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.button2, 0, wx.ALL, 5 )

		self.text2 = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text2.Wrap( -1 )

		bSizer4.Add( self.text2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.button2.Bind( wx.EVT_BUTTON, self.OnButton2Click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnButton2Click( self, event ):
		event.Skip()


