import tkinter as tk
import time
from PIL import Image, ImageTk
from mongo_operations import find

HEIGHT = 1000
WIDTH = 1000
transcript_label_list = []
sentiment_label_list = []
emoji_label_list = []
old_record_count = 0

def refresh_label():
	global transcript_label_list
	global sentiment_label_list
	global emoji_label_list
	global old_record_count
	records=find()
	transcript = ''
	sentiment = ''
	emoji = ''
	if(len(records) > old_record_count):
		difference = len(records) - old_record_count
		for i in range(difference):
			add_label(records[old_record_count -1 + i])
		old_record_count = len(records)
	root.after(2000, refresh_label) # every 2 second...

def add_label(data):
	global transcript_label_list
	global sentiment_label_list
	global emoji_label_list
	global lower_frame

	row_num = transcript_label_list[-1].grid_info()['row']

	transcript = data['transcript']
	transcript_label_new=tk.Label(lower_frame, text=transcript, font=40, bg='#80c1ff')
	transcript_label_new.grid(row=row_num+1, column=0)
	transcript_label_list.append(transcript_label_new)

	sentiment = str(data['sentiment_polarity'])
	sentiment_label_new=tk.Label(lower_frame, text=sentiment, font=40, bg='#80c1ff')
	sentiment_label_new.grid(row=row_num+1, column=1)
	sentiment_label_list.append(sentiment_label_new)

	emoji = data['emoji']
	emoji_label_new=tk.Label(lower_frame, text=emoji, font=40, bg='#80c1ff')
	emoji_label_new.grid(row=row_num+1, column=2)
	emoji_label_list.append(emoji_label_new)

root=tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
	
background_image = tk.PhotoImage(file='landscape.png')
root.background_image = background_image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Start Transcription", font=40, command=lambda: refresh_label())
button.place(relx=0.05, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.75, anchor='n')

header_label_1=tk.Label(lower_frame, text='Transcript', font=60, fg='#E5704B', bg='#80c1ff')
header_label_1.grid(row=0, column=0)
header_label_2=tk.Label(lower_frame, text='Sentiment', font=60, fg='#E5704B', bg='#80c1ff')
header_label_2.grid(row=0, column=1, columnspan=2)

transcript_label=tk.Label(lower_frame, text='', font=40, bg='#80c1ff')
transcript_label.grid(row=1, column=0)
transcript_label_list.append(transcript_label)

sentiment_label=tk.Label(lower_frame, text='', font=40, bg='#80c1ff')
sentiment_label.grid(row=1, column=1)
sentiment_label_list.append(sentiment_label)

emoji_label=tk.Label(lower_frame, text='', font=40, bg='#80c1ff')
emoji_label.grid(row=1, column=2)
emoji_label_list.append(emoji_label)

lower_frame.grid_columnconfigure(0, weight=2)
lower_frame.grid_columnconfigure(1, weight=1)
lower_frame.grid_columnconfigure(2, weight=1)
root.mainloop()