
#Output --creates a new mp3 in same folder as mp3s selected by user.
#        Output file is from merge of user-selected mp3 files.
#         output file name based on name from first and last in selection.
#Input   -- Prompt user to select multiple mp3 files from a folder.
#Tested -- in python version python3.8
#For compatibility and backup purposes.
#Draft version-- Documentation, codes style and refactoring are works in progress.

#notes before uploading to GitHub
#     remove/refactor the line about sys variables  sys.path.insert since it links to an absolute path to my pip installation modules
#     remove the above line and this
#     OP was using a line that looked like sys.path.insert(0, '/Users/path-to/python3.8/site-packages')

import sys
 
import tkinter as tk
from tkinter import filedialog

import os

import time
import random


from pydub import AudioSegment

  

def open_file_dialog():
   
    # Ask the user to select multiple files
    file_paths = filedialog.askopenfilenames(
        title="Select files",
        filetypes=[("All Files", "*.*")]
    )

    # Initialize an empty AudioSegment
    combined_audio = AudioSegment.silent()
    outfilename = ""
    for index, file_path in enumerate(file_paths):
        # Load the MP3 files and append their audio to combined_audio
        audio = AudioSegment.from_mp3(file_path)
        combined_audio += audio
        if index == 0:
            outfilename = file_path + "-"
        elif index == len(file_paths) - 1:
            outfilename += os.path.basename(file_path)
 
    # Export the merged audio to a new MP3 file
    combined_audio.export(outfilename, format="mp3")

 

# Create the main application window
root = tk.Tk()
root.title("File Chooser Example")

# Create a button to trigger the file dialog
button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
