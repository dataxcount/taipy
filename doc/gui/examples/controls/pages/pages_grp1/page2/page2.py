import os
from tempfile import NamedTemporaryFile

from taipy.gui import Markdown, download

# Remove the temporary file
def clean_up(state):
    print("Inside start")
    os.remove(state.temp_path)
    print("Inside end")

# Generate the digits, save them in a CSV temporary file, then trigger a download action
# for that file.
def download_pi(state):
    digits = 3.14
    with NamedTemporaryFile("r+t", suffix=".txt", delete=False) as temp_file:
        state.temp_path = temp_file.name
        temp_file.write(f"{digits}\n")
    download(state, content=temp_file.name, name="pi.txt", on_action="clean_up")

# Stores the path to the temporary file
temp_path = None

page2_md = Markdown(
"""
<|{None}|file_download|on_action=download_pi|label=Download Pi digits|>
"""
)
