import PySimpleGUI as sg
import os


def fcheck(target, path, shortname):

    if target == "" or target == "Select shorcut save location":
        return 0
    elif path == "" or path == "Select location of the program":
        return 0
    elif shortname == "" or shortname == "Enter Shortcut name":
        return 0
    else:
        return 1


sg.theme("darkgray 12")
layout = [[sg.Text("Time to optimize your programs!")],
          [sg.Input("Select shorcut save location", key='-IN-', do_not_clear=False),
           sg.FolderBrowse("Browse")],
          [sg.Input("Select location of the program", key="-out-", do_not_clear=False),
           sg.FileBrowse("Browse")],
          [sg.Input("Enter Shortcut name", key="name", do_not_clear=False)],
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
            sg.popup('Make sure all the fields are filled')
        else:
            f = open(newtarget, 'x')
            f.write(core_set+path)
            f.close()
            window['msg'].Update(visible=True)
window.close()
