import PySimpleGUI as sg
import os

sg.theme("darkgray 12")
layout = [[sg.Text("Time to optimize your programs!")],
          [sg.Input("Select shorcut save location", key='-IN-', do_not_clear=False),
           sg.FolderBrowse("Browse")],
          [sg.Input("Select location of the program", key="-out-", do_not_clear=False),
           sg.FileBrowse("Browse")], [sg.Input("Enter Shortcut name", key="name", do_not_clear=False)],
          [sg.Button("Optimize")]]

window = sg.Window("Program", layout)
core_set = 'C:\windows\System32\cmd.exe /c start "" /Normal/Affinity 3F "'

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Optimize':
        target = values["-IN-"]
        path = values["-out-"]
        name = '/'+values["name"]+'.bat'
        newtarget = target+name
        print(newtarget)
        f = open(newtarget, 'x')
        f.write(core_set+path)
        f.close()
        window.close()
