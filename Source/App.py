import PySimpleGUI as sg
import os

sg.theme("darkgray 12")
layout = [[sg.Text("Time to optimize your programs!")],
          [sg.Input("Select shorcut save location", key='-IN-'),
           sg.FolderBrowse("Browse")],
          [sg.Input("Select location of the program", key="-out-"),
           sg.FileBrowse("Browse")], [sg.Input("Enter Shortcut name", key="name")]
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
        print(target)
        print(path)
window.close()
