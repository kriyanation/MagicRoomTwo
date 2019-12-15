import tkinter
import time
from tkinter import Label, Frame, Entry, Button, Text, OptionMenu, StringVar, filedialog, IntVar, Checkbutton
import sqlite3
import datetime

magic_wizard = tkinter.Tk()
magic_wizard.title("Magic Room Wizard")
magic_wizard.geometry('500x500')
index = 0
factual_index = 1
global factual_button_one
data_collector = {}
rowindex = 4
title_frame = Frame(magic_wizard)

data_collector['Date'] = ''
data_collector['Lesson_Type'] = 'Science'
data_collector['Lesson_Template'] = 'Hogwarts'
data_collector['Lesson_Title'] = ''
data_collector['Title_Image'] = ''
data_collector['Title_Video'] = ''
data_collector['Title_Running_Notes'] = ''
data_collector['Factual_Term1'] = ''
data_collector['Factual_Term1_Description'] = ''
data_collector['Factual_Term2'] = ''
data_collector['Factual_Term2_Description'] = ''
data_collector['Factual_Term3'] = ''
data_collector['Factual_Term3_Description'] = ''
data_collector['Factual_Image1'] = ''
data_collector['Factual_Image2'] = ''
data_collector['Factual_Image3'] = ''
data_collector['Application_Mode'] = ''
data_collector['Application_Steps_Number'] = 0
data_collector['Application_Step_Description1'] = ''
data_collector['Application_Step_Description2'] = ''
data_collector['Application_Step_Description3'] = ''
data_collector['Application_Step_Description4'] = ''
data_collector['Application_Step_Description5'] = ''
data_collector['Application_Step_Description6'] = ''
data_collector['Application_Step_Description7'] = ''
data_collector['Application_Step_Description8'] = ''
data_collector['Application_Step_Widget1'] = ''
data_collector['Application_Step_Widget2'] = ''
data_collector['Application_Step_Widget3'] = ''
data_collector['Application_Step_Widget4'] = ''
data_collector['Application_Step_Widget5'] = ''
data_collector['Application_Step_Widget6'] = ''
data_collector['Application_Step_Widget7'] = ''
data_collector['Application_Step_Widget8'] = ''
data_collector['Answer_Key'] = ''
data_collector['Video_Audio_Assessment_Flag'] = 0
data_collector['Application_Video_Link'] = ''
data_collector['Application_Video_Running_Notes'] = ''


def add_title_video():
    filename_vid_title = filedialog.askopenfilename(title='open')
    print(filename_vid_title)
    if (filename_vid_title != ''):
        vid_title_label = Label(title_frame, text=filename_vid_title, pady=10)
        vid_title_label.grid(row=2,column=2)
        data_collector['Title_Image'] = filename_vid_title
def add_title_image():
    filename_vid_title = filedialog.askopenfilename(title='open')
    print(filename_vid_title)
    if (filename_vid_title != ''):
        img_title_label = Label(title_frame, text=filename_vid_title, pady=10)
        img_title_label.grid(row=1,column=2)
        data_collector['Title_Video'] = filename_vid_title

title_label = Label(title_frame, text="Title of your topic", pady=2)
title_text = Entry(title_frame)
title_image_label = Label(title_frame, text="Image Related to Title", pady=2)
title_image_button = Button(title_frame, text="Add Image", pady=2,command=add_title_image)
title_image_video_label = Label(title_frame, text="Video Related to Title", pady=2)
title_video_button = Button(title_frame, text="Add Video", pady=2,command=add_title_video)
title_running_notes_label = Label(title_frame, text="Running Notes", pady=2)
title_running_notes = Text(title_frame, width=30, height=5,pady=2)
title_frame.pack()
title_label.grid(row=0, column=0)
title_text.grid(row=0, column=1)
title_image_label.grid(row=1,column=0)
title_image_button.grid(row=1,column=1)
title_image_video_label.grid(row=2,column=0)
title_video_button.grid(row=2,column=1)
title_running_notes_label.grid(row=3,column=0)
title_running_notes.grid(row=3,column=1)






global filename



bottom_frame = Frame(magic_wizard)
factual_frame = Frame(magic_wizard)
apply_frame = Frame(magic_wizard)
apply_activity_frame = Frame(apply_frame)
apply_activity_steps_frame = Frame(apply_activity_frame)
create_frame = Frame(magic_wizard)

factual_term_text1 = Entry(factual_frame)
factual_term_desc_text1 = Text(factual_frame, width=30, height=5)
factual_term_text2 = Entry(factual_frame)
factual_term_desc_text2 = Text(factual_frame, width=30, height=5)

def  add_factual_image(id):
    filename_img_title = filedialog.askopenfilename(title='open')
    print(filename_img_title)
    print("ID="+str(id))
    if (filename_img_title != ''):
        img_title_label = Label(factual_frame, text=filename_img_title, pady=10)
        if id == 0:
            img_title_label.grid(row=2, column=1)
            data_collector['Factual_Image1'] = filename_img_title
        elif id == 1:
            img_title_label.grid(row=5, column=1)
            data_collector['Factual_Image2'] = filename_img_title
        elif id == 2:
            img_title_label.grid(row=7, column=1)
            data_collector['Factual_Image3'] = filename_img_title


def add_factual():
    global factual_term_text, factual_term_desc_text

    factual_term_label = Label(factual_frame, text="Definition or New Term", pady=20)
    factual_term_text = Entry(factual_frame)
    factual_term_desc_label = Label(factual_frame, text="Description")
    factual_term_desc_text = Text(factual_frame, width=30, height=5)
    factual_term_image_button = Button(factual_frame, text='Add Image', command=lambda id=0: add_factual_image(id))
    factual_term_label.grid(row=0, column=0)
    factual_term_text.grid(row=0, column=1)
    factual_term_desc_label.grid(row=1, column=0)
    factual_term_desc_text.grid(row=1, column=1)
    factual_term_image_button.grid(row=2,column=0)


def add_factual_one():
    global factual_index, factual_button, factual_button_one, factual_term_text1, factual_term_desc_text1
    factual_index += 1
    factual_term_label = Label(factual_frame, text="Definition or New Term", pady=10)

    factual_term_desc_label = Label(factual_frame, text="Description")
    factual_term_image_button = Button(factual_frame, text='Add Image', command=lambda id=1: add_factual_image(id))

    factual_term_label.grid(row=3, column=0)
    factual_term_text1.grid(row=3, column=1)
    factual_term_desc_label.grid(row=4, column=0)
    factual_term_desc_text1.grid(row=4, column=1)
    print(factual_index)
    factual_button.grid_remove()
    factual_button_one = Button(factual_frame, text='Add One More', command=add_factual_two)
    factual_button_one.grid(row=5, column=2)
    factual_term_image_button.grid(row=5,column=0)


add_factual()

factual_button = Button(factual_frame, text='Add One More', command=add_factual_one)
factual_button.grid(row=3, column=3)


def add_factual_two():
    global factual_index, factual_button_one, rowindex, factual_term_text2, factual_term_desc_text2
    factual_index += 1
    factual_button_one.grid_remove()
    factual_term_label = Label(factual_frame, text="Definition or New Term", pady=10)

    factual_term_desc_label = Label(factual_frame, text="Description")
    factual_term_image_button = Button(factual_frame, text='Add Image', command=lambda id=2: add_factual_image(id))

    rowindex += 2
    print(rowindex)
    factual_term_label.grid(row=rowindex, column=0)
    factual_term_text2.grid(row=rowindex, column=1)
    rowindex += 1
    factual_term_desc_label.grid(row=rowindex, column=0)
    factual_term_desc_text2.grid(row=rowindex, column=1)
    rowindex += 1
    factual_term_image_button.grid(row=rowindex,column=0)
    # factual_button_one.grid(row=rowindex, column=2)


def add_apply_frame():
    apply_term_label = Label(apply_frame, text="How would you want to show the application?", pady=10)
    selected = StringVar(magic_wizard)
    selected.set('No Selection')
    apply_dropdown = OptionMenu(apply_frame, selected, 'No Selection', 'Activity', 'Video', command=show_steps)
    apply_term_label.grid(row=0, column=0)
    apply_dropdown.grid(row=0, column=1)
    print(selected.get())


global video_link_running_notes

def show_steps(selected_string):
    global video_link_running_notes
    if selected_string == 'Activity':
        data_collector['Application_Mode'] = selected_string
        for widget in apply_activity_frame.winfo_children():
            if widget != apply_activity_steps_frame:
                widget.destroy()

        apply_steps_label = Label(apply_activity_frame, text="Number of Steps?", pady=10)
        selected_steps = StringVar(magic_wizard)
        apply_steps_dropdown = OptionMenu(apply_activity_frame, selected_steps, '0', '1', '2', '3', '4', '5', '6', '7',
                                          '8',
                                          command=show_individual_steps)

        print(selected_string)

        selected_steps.set('0')
        apply_steps_label.grid(row=0, column=0)
        apply_steps_dropdown.grid(row=0, column=1)

    if selected_string == 'Video':
        data_collector['Application_Mode'] = selected_string
        for widget in apply_activity_frame.winfo_children():
            if widget != apply_activity_steps_frame:
                widget.destroy()
        if apply_activity_steps_frame is not None and len(apply_activity_steps_frame.children) > 1:
            for widget_steps in apply_activity_steps_frame.winfo_children():
                widget_steps.destroy()
        video_link_label = Label(apply_activity_frame, text="Video Link", pady=10)
        video_link_button = Button(apply_activity_frame, text='Add Video',
                                   command=lambda: add_video(apply_frame))
        video_link_notes_label = Label(apply_activity_frame, text="Running Notes", pady=10)
        video_link_running_notes = Text(apply_activity_frame, width=30, height=5)
        video_link_label.grid(row=1, column=0)
        video_link_button.grid(row=1, column=1)
        video_link_notes_label.grid(row=2, column=0)
        video_link_running_notes.grid(row=2, column=1)


def add_video(apply_frame):
    filename_vid = filedialog.askopenfilename(title='open')
    print(filename_vid)
    if (filename_vid != ''):
        vid_label = Label(apply_frame, text=filename_vid, pady=10)
        vid_label.grid(row=1, column=2)
        data_collector['Application_Video_Link'] = filename_vid


def show_individual_steps(selected_number):
    # for widget in apply_activity_steps_frame.winfo_children():
    #    widget.destroy()
    data_collector['Application_Steps_Number'] = int(selected_number)
    number_of_steps = int(selected_number)

    i = 0
    step_text1 = Entry(apply_activity_steps_frame)
    step_text2 = Entry(apply_activity_steps_frame)
    step_text3 = Entry(apply_activity_steps_frame)
    step_text4 = Entry(apply_activity_steps_frame)
    step_text5 = Entry(apply_activity_steps_frame)
    step_text6 = Entry(apply_activity_steps_frame)
    step_text7 = Entry(apply_activity_steps_frame)
    step_text8 = Entry(apply_activity_steps_frame)
    step_image_button1 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button2 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button3 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button4 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button5 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button6 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button7 = Button(apply_activity_steps_frame, text='Add Image')
    step_image_button8 = Button(apply_activity_steps_frame, text='Add Image')
    i = 1
    for i in range(number_of_steps):
        step_label = Label(apply_activity_steps_frame, text="Step Description", pady=10)
        if i == 0:
            index1 = i
            step_text1.bind("<FocusOut>",lambda event, index = i: add_step(event,index1))
            step_image_button1.config(command=lambda row=i: add_image(apply_frame, index1))
            step_label.grid(row=i, column=0)
            step_text1.grid(row=i, column=1)
            step_image_button1.grid(row=i, column=3)

        if i == 1:
            index2 = i
            step_text2.bind("<FocusOut>",lambda event, index = i: add_step(event,index2))
            step_image_button2.config(command=lambda row=i: add_image(apply_frame, index2))
            step_label.grid(row=i, column=0)
            step_text2.grid(row=i, column=1)
            step_image_button2.grid(row=i, column=3)
        if i == 2:
            index3 = i
            step_text3.bind("<FocusOut>",lambda event, index = i: add_step(event,index3))
            step_image_button3.config(command=lambda row=i: add_image(apply_frame, index3))
            step_label.grid(row=i, column=0)
            step_text3.grid(row=i, column=1)
            step_image_button3.grid(row=i, column=3)
        if i == 3:
            index4 = i
            step_text4.bind("<FocusOut>",lambda event, index = i: add_step(event,index4))
            step_image_button4.config(command=lambda row=i: add_image(apply_frame, index4))
            step_label.grid(row=i, column=0)
            step_text4.grid(row=i, column=1)
            step_image_button4.grid(row=i, column=3)
        if i == 4:
            index5 = i
            step_text5.bind("<FocusOut>",lambda event, index = i: add_step(event,index5))
            step_image_button5.config(command=lambda row=i: add_image(apply_frame, index5))
            step_label.grid(row=i, column=0)
            step_text5.grid(row=i, column=1)
            step_image_button5.grid(row=i, column=3)
        if i == 5:
            index6 = i
            step_text6.bind("<FocusOut>",lambda event, index = i: add_step(event,index6))
            step_image_button6.config(command=lambda row=i: add_image(apply_frame, index6))
            step_label.grid(row=i, column=0)
            step_text6.grid(row=i, column=1)
            step_image_button6.grid(row=i, column=3)
        if i == 6:
            index7 = i
            step_text7.bind("<FocusOut>",lambda event, index = i: add_step(event,index7))
            step_image_button7.config(command=lambda row=i: add_image(apply_frame, index7))
            step_label.grid(row=i, column=0)
            step_text1.grid(row=i, column=1)
            step_image_button7.grid(row=i, column=3)
        if i == 7:
            index8 = i
            step_text8.bind("<FocusOut>", lambda event, index=i: add_step(event, index8))
            step_image_button8.config(command=lambda row=i: add_image(apply_frame, index8))
            step_label.grid(row=i, column=0)
            step_text1.grid(row=i, column=1)
            step_image_button8.grid(row=i, column=3)
        i += 1


def add_step(event, index):
    print("Index:"+str(index)+" Widget:"+event.widget.get())

    data_collector["Application_Step_Description"+str(index+1)] = event.widget.get()


def add_image(apply_frame, i):
    filename = filedialog.askopenfilename(title='open')
    print(filename)
    if (filename != ''):
        data_collector["Application_Steps_Widget_"+str(i+1)] = filename
        step_label = Label(apply_frame, text=filename, pady=10)
        step_label.grid(row=i + 1, column=4)

var_video_audio = IntVar()
record_audio_video_checkbox = Checkbutton(create_frame, text="yes/no", var=var_video_audio)
create_test_entry = Entry(create_frame, width=20)
def add_create_frame():
    create_test_label = Label(create_frame, text='Provide the Answer Key in this format(1-a, 2-b, 3-c,4-d, 5-e)')

    record_audio_video_label = Label(create_frame, text='Do you want to record an audio or video response?')


    create_test_label.grid(row=0, column=0)
    create_test_entry.grid(row=0, column=1)
    record_audio_video_label.grid(row=1, column=0)
    record_audio_video_checkbox.grid(row=1, column=1)


add_apply_frame()
add_create_frame()


def next_page():

    global index
    index += 1
    if index == 1:
        data_collector['Lesson_Title'] = title_text.get()
        data_collector["Application_Mode"] = ''
        title_frame.pack_forget()
        factual_frame.pack(side='top')
    if index == 2:
        data_collector["Factual_Term1"] = factual_term_text.get()
        data_collector["Factual_Term1_Description"] = factual_term_desc_text.get('1.0', 'end')

        if factual_term_text1 is not None:
            data_collector['Factual_Term2'] = factual_term_text1.get()
        if factual_term_desc_text1 != None:
            data_collector['Factual_Term2_Description'] = factual_term_desc_text1.get('1.0', 'end')

        if factual_term_text2 != None:
            data_collector["Factual_Term3"] = factual_term_text2.get()
        if factual_term_desc_text2 != None:
            data_collector["Factual_Term3_Description"] = factual_term_desc_text2.get('1.0', 'end')

        factual_frame.pack_forget()
        apply_frame.pack(side='top')
        apply_activity_frame.grid(row=1, column=0, columnspan=2)
        apply_activity_steps_frame.grid(row=1, column=0, columnspan=2)
    if index == 3:
        if data_collector['Application_Mode'] =='Video':
            data_collector['Application_Video_Link_Notes'] = video_link_running_notes.get('1.0', 'end')
        apply_frame.pack_forget()
        create_frame.pack()
        next_button.config(text='Submit')
    if index == 4:
        data_collector["Answer_Key"] = create_test_entry.get()
        data_collector["Video_Audio_Assessment_Flag"] = 0
        '''var_video_audio.get()'''
        save_data()
        magic_wizard.destroy()
    print(data_collector)


def save_data():





    connection = sqlite3.connect("/home/ram/MagicRoom.db")
    cur = connection.cursor()
    sql = ('Insert into Magic_Science_Lessons (Lesson_Type, Lesson_Template, Lesson_Title,Title_Image,Title_Video,Title_Running_Notes,Factual_Term1,Factual_Term1_Description,Factual_Term2,Factual_Term2_Description,Factual_Term3,Factual_Term3_Description'
           ', Application_Mode,Application_Steps_Number,Application_Step_Description_1,Application_Step_Description_2,Application_Step_Description_3,Application_Step_Description_4,Application_Step_Description_5, Application_Step_Description_6, Application_Step_Description_7, Application_Step_Description_8, Application_Steps_Widget_1'
           ', Application_Steps_Widget_2, Application_Steps_Widget_3, Application_Steps_Widget_4, Application_Steps_Widget_5, Application_Steps_Widget_6, Application_Steps_Widget_7,Application_Steps_Widget_8,Answer_Key,Video_Audio_Assessment_Flag, Date, Factual_Image1, Factual_Image2, Factual_Image3'
           ', Application_Video_Link , Application_Video_Running_Notes) values( :Lesson_Type, :Lesson_Template, :Lesson_Title, :Title_Image, :Title_Video, :Title_Running_Notes, :Factual_Term1'
           ', :Factual_Term1_Description, :Factual_Term2, :Factual_Term2_Description, :Factual_Term3, :Factual_Term3_Description '
           ', :Application_Mode, :Application_Steps_Number, :Application_Step_Description1'
           ', :Application_Step_Description2, :Application_Step_Description3, :Application_Step_Description4, :Application_Step_Description5'
           ', :Application_Step_Description6, :Application_Step_Description7, :Application_Step_Description8, :Application_Step_Widget1'
           ', :Application_Step_Widget2, :Application_Step_Widget3, :Application_Step_Widget4, :Application_Step_Widget5, :Application_Step_Widget6'
           ', :Application_Step_Widget7, :Application_Step_Widget8, :Answer_Key, :Video_Audio_Assessment_Flag, :Date,:Factual_Image1, :Factual_Image2, :Factual_Image3'
           ', :Application_Video_Link, :Application_Video_Running_Notes)')





    cur.execute(sql, data_collector)
    connection.commit()




def previous_page():
    global index
    next_button.config(text='Next')
    if index == 1:
        index = 0
        factual_frame.pack_forget()
        title_frame.pack(side='top')
    if index == 2:
        index = 1
        apply_frame.pack_forget()
        factual_frame.pack(side='top')
    if index == 3:
        index = 2
        create_frame.pack_forget()
        apply_frame.pack(side='top')


next_button = Button(bottom_frame, text='Next', command=next_page)
back_button = Button(bottom_frame, text="Back", command=previous_page)

bottom_frame.pack(side='bottom')
next_button.pack(side='right')
back_button.pack(side='left')

magic_wizard.mainloop()
