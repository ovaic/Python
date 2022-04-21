# Python

Download the CSV file. (EXCEL Dataset file "train2.csv" for YouTube video links.)

Filter the LABEL (e.g. slapping) for which you want to Download all videos.

For filtering:

select all headings (Row #1 Colomn A-H) -> Click on Data Tab -> Click on Filter from Sort & Filter box -> Drop Down Arrows will be shown on each heading in Row #1 -> Click on LABEL Drop Down Arrow -> Write your Label Name (e.g. slapping) in Search -> Press Enter

COPY-PASTE all data for that Label in another EXCEL file and ADD its full PATH in the code (line #9 df = pd.read_csv(r'PATH\excel.csv') 

Run this command: !python requirements.txt ... to install libraries.

If any ERROR occur, intall each library one by one: 
!pip install pytube==12.0.0
!pip install moviepy==1.0.3
!pip install pandas==1.2.4 

Now goto: C:\Users\{user name}\anaconda3\Lib\site-packages\pytube\cipher.py

In funtion: get_throttling_function_name
Chane function_patterns to the following:

r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'

And you also have to change line 288 to this:

nfunc=re.escape(function_match.group(1))),

RUN your Jupyter Notebook TERMINAL in the folder where you want to Download the videos.

Make another folder named "clipped" and "not clipped" in it to store clipped videos. (REQUIRED)*

Now just RUN it.
