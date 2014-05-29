#~/.gnome2/nautilus-scripts
IFS_BAK=$IFS
IFS="
"
#give a check here to see if the files coming are .mp4........videoformat files only otherwise exit.....
for line in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
     
       
        full_path="/home/"$USER"/Desktop/"rs_subtitle_downloader.py
        lang="pt"
        #notify-send $full_path $lang
        python $full_path $line $lang
done

IFS=$IFS_BAK

