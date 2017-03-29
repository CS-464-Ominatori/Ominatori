#! /bin/bash
DATA_FOLDER_PATH = . # TODO: Change the path according to your folder location

find $DATA_FOLDER_PATH -type d -name "*.*" -exec rm -rf "{}" \; # Only deletes directories that contain at least one dot character. 
