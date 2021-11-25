# transfer huawei notes to any other phone including android or iPhone ones
transfer huawei notes to a non huawei phone without synchronizing the notes on huwawe cloud and without rooting your phone.


I've been searching a way to transfer my huawei notes from my old *p10 lite* huawei phone to my new android phone without puttingthe notes on huawei cloud (for privacy and security reasons) nor sharing them one by one on *google keep* and as it appeard to me there wasn't any other situable method explained online to transfer the notes so I decided to find one, in this repo you can find the method I used you can use it to and adabt it to import the notes wherever you want.

___



By following the steps in this repo you will be able to export your notes directry to **[QuilloNotes](https://github.com/msoultanidis/quillnote)**, to **[Standard Notes](https://standardnotes.com/)** (this last has Windows and ios clients) or to any other note application by editing the python script code on this repo ~~(We are working on providing it also for **[Standard Notes](https://standardnotes.com/))**.~~ ✅


- First of all you should make a huawei back up choosing the notes as one of the backedup items(or the only item).
- Then use this tool [kobackupdec](https://github.com/RealityNet/kobackupdec) to decrypt the encrypted huawei backup(remember to write the password used while the backup in the decryption process).
- Once decrypted the backup go to *output_folder/data/data* you should find a file with name **Memo.db** open it with [DB Browser for SQLite](https://sqlitebrowser.org/) or any other db viewer.
-In DB Browser for SQLite go to *Browse Data* and choose the table *comhuaweiproviderNotePadbackupnote_items_new_tb* or *comhuaweiproviderNotePadbackupnote_items_tb*.
-Now select and copy all the elements of **content** column and save them in .txt file (call it notes.txt).
-Ensure that all the notes begin with "Text|" and not "Bullet|" or other similar things, if not you can delete these lines (important to work with the script made otherwise you can edit it to consider other note types)
-Select and copy all the elements of **created** column and save them in another .txt file (call it created.txt).
-Seleect and copy all the elements of **modified** column and save them in a .txt file (call it modified.txt).


At this point you should have 3 .txt files and you are ready to use the script that will convert your notes into a .json file compatible with **[QuilloNote](https://github.com/msoultanidis/quillnote)** or with **[Standard Notes](https://standardnotes.com/)**

**If you are outside Italy remember to change the time zone in the code according to your local time zone before use** 

## Usage
<pre>
usage:python jsonfyNotes.py [quillo][standard] "PATH/notes.txt" "PATH/created.txt" "PATH/modified.txt"

The arguments should be ordered as shown.
</pre>

_try **python3** and **python** one of the two should work depending on your operation system_

_Replace PATH with the path to the folder where the file is_

**Export to Quillo Notes** 
To import the .json file with your notes into QuilloNote put the output .json file into .zip file, send it to your phone and import it using the settings of QuilloNote app(since the app requires the file to be compressed inside .zip file).

**Export to Standard Notes**
Rename the .json output file to end with .txt _(example: backup.json --> backup.txt)_ to import the .txt file you will just need the .txt file as it is and import it directly from the settings of the app.

## Example
To Quillo Notes
<pre>
python jsonfyNotes.py quillo "PATH/notes.txt" "PATH/created.txt" "PATH/modified.txt"

>Number of converted notes = 960
</pre>

To Standard Notes
<pre>
python jsonfyNotes.py standard "PATH/notes.txt" "PATH/created.txt" "PATH/modified.txt"

>Number of converted notes = 960
</pre>
