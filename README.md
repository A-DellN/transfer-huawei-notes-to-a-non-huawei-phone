
# transfer-huawei-notes-to-a-non-huawei-phone
transfer huawei notes to a non huawei phone without synchronizing the notes on huwawe cloud and without rooting your phone.


I've been searching a way to transfer my huawei notes from my old *p10 lite* huawei phone to my new android phone without puttingthe notes on huawei cloud (for privacy and security reasons) nor sharing them one by one on *google keep* and as it appeard to me there wasn't any other situable method explained online to transfer the notes so I decided to find one, in this repo you can find the method I used you can use it to and adabt it to import the notes wherever you want.

___



By following the steps in this repo you will be able to export your notes directry to **[QuilloNotes](https://github.com/msoultanidis/quillnote)**, or to any other note application by editing the python script code on this repo *(We are working on providing it also for **[Standard Notes](https://standardnotes.com/)** which has a windows and ios clients).*


- First of all you should make a huawei back up choosing the notes as one of the backedup items(or the only item).
- Then use this tool [kobackupdec](https://github.com/RealityNet/kobackupdec) to decrypt the encrypted huawei backup(remember to write the password used while the backup in the decryption process).
- Once decrypted the backup go to *output_folder/data/data* you should find a file with name **Memo.db** open it with [DB Browser for SQLite](https://sqlitebrowser.org/) or any other db viewer.
-In DB Browser for SQLite go to *Browse Data* and choose the table *comhuaweiproviderNotePadbackupnote_items_new_tb* or *comhuaweiproviderNotePadbackupnote_items_tb*.
-Now select and copy all the elements of **content** column and save them in .txt file (call it notes.txt).
-Ensure that all the notes begin with "Text|" and not "Bullet|" or other similar things, if not you can delete these lines (importatnt to work with the script made otherwise you can edit it to consider other note types)
-Select and copy all the elements of **created** column and save them in another .txt file (call it created.txt).
-Seleect and copy all the elements of **modified** column and save them in a .txt file (call it modified.txt).


At this point you should have 3 .txt files and you are ready to use the script that will convert your notes into a .json structure compatible with **[QuilloNote](https://github.com/msoultanidis/quillnote)**.


## Usage
<pre>
usage: jsonfyNotes.py "folder_path/notes.txt" folder_path/created.txt" "folder_path/modified.txt"

The arguments should be in order as shown.
</pre>

To import the .json file with your notes into QuilloNote put the output .json file into .zip file, send it to your phone and import it using the settings of QuilloNote app.


## Example
<pre>
python jsonfyNotes.py "folder_path/notes.txt" folder_path/created.txt" "folder_path/modified.txt"

Number of converted notes = 960
</pre>


