import wx

from gui.widget import ft
from lib.info import version


class AboutPanel(wx.Panel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.title_text = wx.StaticText(self, label="CloudStatus")
        self.title_text.SetFont(ft(48))
        self.version_label = wx.StaticText(self, label=f"Version {version}")
        self.version_label.SetFont(ft(24))

        main_sizer.Add(self.title_text, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)
        main_sizer.Add(self.version_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        
        main_sizer.AddStretchSpacer()
        main_sizer.AddStretchSpacer()
        
        self.SetSizer(main_sizer)
