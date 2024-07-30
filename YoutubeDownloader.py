import wx
import pytube

class main(wx.Frame):
	def __init__(self):
		super().__init__(None, title="YouTube downloader")
		panel = wx.Panel(self)
		wx.StaticText(panel, -1, "YouTube bideo link")
		self.url_text = wx.TextCtrl(panel)
		self.download_button = wx.Button(panel, label='&Download video')
		self.download_button.Bind(wx.EVT_BUTTON, self.OnDownload)
		self.Show()

	def OnDownload(self, event):
		url = self.url_text.GetValue()
		yt = pytube.YouTube(url)
		stream = yt.streams.first()
		stream.download()
		wx.MessageBox('Download complete!')
app=wx.App()
w=main()
w.Show()
app.MainLoop()