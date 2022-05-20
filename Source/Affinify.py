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
          [sg.Input("Select shorcut save location", key='IN', do_not_clear=False),
           sg.FolderBrowse("Browse")],
          [sg.Input("Select location of the program", key="out", do_not_clear=False),
           sg.FileBrowse("Browse")],
          [sg.Input("Enter Shortcut name", key="name", do_not_clear=False)],
          [sg.Slider(range=(0, 15), default_value=5, size=(
              30, 15), key='slid', orientation='horizontal', font=("Helvetica", 10))],
          [sg.Button("Optimize")], [sg.Text('Optimized successfully', key='msg', visible=False)]]

window = sg.Window("Program", layout)
core_count = ['1', '3', '7', 'F', '1F', '3F', '7F', 'FF',
              '1FF', '3FF', '7FF', 'FFF', '1FFF', '3FFF', '7FFF', 'FFFF']


while True:
    event, values = window.read()
    core_set = 'C:\windows\System32\cmd.exe /c start "" /Normal/Affinity '
    if event == sg.WIN_CLOSED:
        break
    if event == 'Optimize':
        target = values["IN"]
        path = values["out"]
        shortname = values["name"]
        slider = int(values['slid'])

        name = '/'+shortname+'.bat'
        newtarget = target+name
        print(newtarget)
        flag = fcheck(target, path, shortname)
        if flag == 0:
            sg.popup('Make sure all the fields are filled')
        else:
            core_set = core_set+core_count[slider]+' "'
            f = open(newtarget, 'x')
            f.write(core_set+path)
            f.close()
            window['msg'].Update(visible=True)
window.close()
