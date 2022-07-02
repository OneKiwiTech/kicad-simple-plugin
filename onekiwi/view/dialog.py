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
## Class TestDialog
###########################################################################

class TestDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"TestDialog", pos = wx.DefaultPosition, size = wx.Size( 480,360 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonSend1 = wx.Button( self, wx.ID_ANY, u"Send1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonSend1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.buttonGet1 = wx.Button( self, wx.ID_ANY, u"Get1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonGet1, 1, wx.ALL, 5 )

		self.buttonSend2 = wx.Button( self, wx.ID_ANY, u"Send2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonSend2, 1, wx.ALL, 5 )

		self.buttonGet2 = wx.Button( self, wx.ID_ANY, u"Get2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.buttonGet2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.textStatus = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textStatus.Wrap( -1 )

		bSizer1.Add( self.textStatus, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Test1Panel
###########################################################################

class Test1PanelBase ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 390,260 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonSendMain1 = wx.Button( self, wx.ID_ANY, u"Send Main", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.buttonSendMain1, 1, wx.ALL, 5 )

		self.buttonGetMain1 = wx.Button( self, wx.ID_ANY, u"Get Main", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.buttonGetMain1, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonSendPanel1 = wx.Button( self, wx.ID_ANY, u"Send Panel2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonSendPanel1, 1, wx.ALL, 5 )

		self.buttonGetPanel1 = wx.Button( self, wx.ID_ANY, u"Get Panel2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonGetPanel1, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer7, 0, wx.ALL|wx.EXPAND, 5 )

		self.text1 = wx.StaticText( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text1.Wrap( -1 )

		bSizer3.Add( self.text1, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		

	def __del__( self ):
		pass


###########################################################################
## Class Test2Panel
###########################################################################

class Test2PanelBase ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 390,260 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonSendMain2 = wx.Button( self, wx.ID_ANY, u"Send Main", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.buttonSendMain2, 1, wx.ALL, 5 )

		self.buttonGetMain2 = wx.Button( self, wx.ID_ANY, u"Get Main", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.buttonGetMain2, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonSendPanel2 = wx.Button( self, wx.ID_ANY, u"Send Panel1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonSendPanel2, 1, wx.ALL, 5 )

		self.buttonGetPanel2 = wx.Button( self, wx.ID_ANY, u"Get Panel1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonGetPanel2, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer7, 0, wx.ALL|wx.EXPAND, 5 )

		self.text2 = wx.StaticText( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text2.Wrap( -1 )

		bSizer3.Add( self.text2, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

	def __del__( self ):
		pass
