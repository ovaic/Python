# Python

Download the ZIP file and extract it in your Project folder.

Make New Folders for your Label e.g. sleeping, slapping.

Make two sub folders with name "clipped" and "not clipped" in the New Folders. (REQUIRED)*

Copy the python "Video-Downloader-Clipper.ipynb" file in New Folders.

Filter the LABEL (e.g. slapping) for which you want to Download all videos from the CSV file. (EXCEL Dataset file "train2.csv" for YouTube video links.)

For filtering:

select all headings (Row #1 Colomn A-H) -> Click on Data Tab -> Click on Filter from Sort & Filter box -> Drop Down Arrows will be shown on each heading in Row #1 -> Click on LABEL Drop Down Arrow -> Write your Label Name (e.g. slapping) in Search -> Press Enter

COPY-PASTE all data for that Label in another EXCEL file and ADD its full PATH in the code (line #9 df = pd.read_csv(r'PATH\excel.csv') 

Run the "Video-Downloader-Clipper.ipynb" file from Jupyter Notebook.

Run these commandscto install libraries:

!pip install pytube==12.0.0
!pip install moviepy==1.0.3
!pip install pandas==1.2.4 

Now goto: C:\Users\{user name}\anaconda3\Lib\site-packages\pytube\cipher.py

Incase you cant find it use this code to the get the address of site-packages:

from distutils.sysconfig import get_python_lib
print(get_python_lib())

In funtion: get_throttling_function_name
Change function_patterns to the following:

r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'

And you also have to change line 288 to this:

nfunc=re.escape(function_match.group(1))),

Now just RUN it.

