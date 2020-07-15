import PySimpleGUI as sg
from models import Diary, Entry

# first load the diary and get the existing entries
diary = Diary()
diary.load()

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Diary entries:')],
            # add entries into multiline input
            [sg.Multiline(diary.build_entries(), disabled=True, size=(80, 20), key='_ENTRIES_')],
            [sg.Text('Type your diary entry:')],
            [sg.Multiline('', size=(80, 20), key='_NEW_ENTRY_')],
            [sg.OK(), sg.Cancel()] ]



# Create the Window
window = sg.Window('My Diary', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    
    # here is where we put the logic to 
    # save the new entry into the json file
    
    new_entry = values['_NEW_ENTRY_'] # entry[1] targets the 2nd multiline element

    if new_entry != '\n' :

        entry = Entry(new_entry)
        diary.add_entry(entry)
        # save
        diary.save()

        # update the gui to show the newwest entry as well
        window.Element('_ENTRIES_').Update(value=diary.build_entries())
        window.Element('_NEW_ENTRY_').Update(value='')
        
window.close()