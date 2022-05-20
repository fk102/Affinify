import PySimpleGUI as sg
import os


def fcheck(target, path, shortname):

    if target == "" or target == "Select shorcut save location":
        return 0
    elif path == "" or path == "Select location of the program":
        return 1
    elif shortname == "" or shortname == "Enter Shortcut name":
        return 2


sg.theme("darkgray 12")
layout = [[sg.Text("Time to optimize your programs!")],
          [sg.Input("Select shorcut save location", key='-IN-', do_not_clear=False),
           sg.FolderBrowse("Browse")], [sg.Text('Select save location', key='err1', visible=False)],
          [sg.Input("Select location of the program", key="-out-", do_not_clear=False),
           sg.FileBrowse("Browse")], [sg.Text('Select program location', key='err2', visible=False)],
          [sg.Input("Enter Shortcut name", key="name", do_not_clear=False)],
          [sg.Text('Enter Shortcut name', key='err3', visible=False)],
          [sg.Button("Optimize")], [sg.Text('Optimized successfully', key='msg', visible=False)]]

window = sg.Window("Program", layout)
core_set = 'C:\windows\System32\cmd.exe /c start "" /Normal/Affinity 3F "'

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Optimize':
        target = values["-IN-"]
        path = values["-out-"]
        shortname = values["name"]
        name = '/'+shortname+'.bat'
        newtarget = target+name
        print(newtarget)
        flag = fcheck(target, path, shortname)
        if flag == 0:
            window['err1'].Update(visible=True)
        elif flag == 1:
            window['err2'].Update(visible=True)
        elif flag == 2:
            window['err3'].Update(visible=True)
        else:
            window['err1'].Update(visible=False)
            window['err2'].Update(visible=False)
            window['err3'].Update(visible=False)
            f = open(newtarget, 'x')
            f.write(core_set+path)
            f.close()
            window['msg'].Update(visible=True)
window.close()
