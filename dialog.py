# -*- coding: cp949 -*-
#!/usr/bin/python

# customdialog2.py


import wx


class MyDialog(wx.Dialog):
    # ���̾� �α� �ʱ�ȭ
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title)
        vbox = wx.BoxSizer(wx.VERTICAL)
        stline = wx.StaticText(self, 11, 'Discipline ist Macht.')
        vbox.Add(stline, 1, wx.ALIGN_CENTER|wx.TOP, 45)
        # ButtonSizer ����( NO, YES, HELP )
        sizer =  self.CreateButtonSizer(wx.NO|wx.YES|wx.HELP)
        vbox.Add(sizer, 0, wx.ALIGN_CENTER)
        self.SetSizer(vbox)
        # ��ư �̺�Ʈ ����
        self.Bind(wx.EVT_BUTTON, self.OnYes, id=wx.ID_YES)


    # YES ��ư �̺�Ʈ ó��
    def OnYes(self, event):
        self.Close()


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        panel = wx.Panel(self, -1)
        wx.Button(panel, 1, 'Show custom Dialog', (50,50))
        # 'Show Custom Dialog' ��ư �̺�Ʈ ����
        self.Bind(wx.EVT_BUTTON, self.OnShowCustomDialog, id=1)


    # �̺�Ʈ ó�� �Լ�
    def OnShowCustomDialog(self, event):
        # ���̾�α� ����
        dia = MyDialog(self, -1, '')
        # ���̾�α� ��޷� ����
        val = dia.ShowModal()
        # ���̾� �α� �ı��ϱ�
        dia.Destroy()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'customdialog2.py')
        frame.Show(True)
        frame.Centre()
        return True


app = MyApp(0)
app.MainLoop()

