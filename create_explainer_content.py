import tkinter
import time
from tkinter import Label, Frame, Entry, Button, Text, OptionMenu, StringVar, filedialog, IntVar, Checkbutton

magic_wizard = tkinter.Tk()
magic_wizard.title("Magic Room Wizard")
magic_wizard.geometry('500x500')
index = 0
factual_index = 1
global factual_button_one
data_collector = {}
rowindex = 4
title_frame = Frame(magic_wizard)

title_Label = Label(title_frame, text="Title of your topic", pady=50)
title_text = Entry(title_frame)
global filename

title_frame.pack()
title_Label.pack(side='left')
title_text.pack(side='right')

bottom_frame = Frame(magic_wizard)
factual_frame = Frame(magic_wizard)
apply_frame = Frame(magic_wizard)
apply_activity_frame = Frame(apply_frame)
apply_activity_steps_frame = Frame(apply_activity_frame)
create_frame = Frame(magic_wizard)

global factual_term_text, factual_term_desc_text, factual_term_text2, factual_term_desc_text2, factual_term_text1, factual_term_desc_text1


def add_factual():
    global factual_term_text, factual_term_desc_text

    factual_term_label = Label(factual_frame, text="Definition or New Term", pady=20)
    factual_term_text = Entry(factual_frame)
    factual_term_desc_label = Label(factual_frame, text="Description")
    factual_term_desc_text = Text(factual_frame, width=30, height=5)
    factual_term_label.grid(row=0, column=0)
    factual_term_text.grid(row=0, column=1)
    factual_term_desc_label.grid(row=1, column=0)
    factual_term_desc_text.grid(row=1, column=1)


def add_factual_one():
    global factual_index, factual_button, factual_button_one, factual_term_text1, factual_term_desc_text1
    factual_index += 1
    factual_term_label = Label(factual_frame, text="Definition or New Term", pady=10)
    factual_term_text1 = Entry(factual_frame)
    factual_term_desc_label = Label(factual_frame, text="Description")
    factual_term_desc_text1 = Text(factual_frame, width=30, height=5)
    factual_term_label.grid(row=2, column=0)
    factual_term_text1.grid(row=2, column=1)
    factual_term_desc_label.grid(row=3, column=0)
    factual_term_desc_text1.grid(row=3, column=1)
    print(factual_index)
    factual_button.grid_remove()
    factual_button_one = Button(factual_frame, text='Add One More', command=add_factual_two)
    factual_button_one.grid(row=5, column=2)


add_factual()

factual_button = Button(factual_frame, text='Add One More', command=add_factual_one)
factual_button.grid(row=3, column=3)


def add_factual_two():
    global factual_index, factual_button_one, rowindex, factual_term_text2, factual_term_desc_text2
    factual_index += 1
    factual_button_one.grid_remove()
    factual_term_label = Label(factual_frame, text="Definition or New Term", pady=10)
    factual_term_text2 = Entry(factual_frame)
    factual_term_desc_label = Label(factual_frame, text="Description")
    factual_term_desc_text2 = Text(factual_frame, width=30, height=5)
    rowindex += 1
    print(rowindex)
    factual_term_label.grid(row=rowindex, column=0)
    factual_term_text2.grid(row=rowindex, column=1)
    rowindex += 1
    factual_term_desc_label.grid(row=rowindex, column=0)
    factual_term_desc_text2.grid(row=rowindex, column=1)
    # factual_button_one.grid(row=rowindex, column=2)


def add_apply_frame():
    apply_term_label = Label(apply_frame, text="How would you want to show the application?", pady=10)
    selected = StringVar(magic_wizard)
    selected.set('No Selection')
    apply_dropdown = OptionMenu(apply_frame, selected, 'No Selection', 'Activity', 'Video', command=show_steps)
    apply_term_label.grid(row=0, column=0)
    apply_dropdown.grid(row=0, column=1)
    print(selected.get())


def show_steps(selected_string):
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
        for widget in apply_activity_frame.winfo_children():
            if widget != apply_activity_steps_frame:
                widget.destroy()
        if apply_activity_steps_frame is not None and len(apply_activity_steps_frame.children) > 1:
            for widget_steps in apply_activity_steps_frame.winfo_children():
                widget_steps.destroy()
        video_link_label = Label(apply_activity_frame, text="Video Link", pady=10)
        video_link_button = Button(apply_activity_frame, text='Add Video',
                                   command=lambda: add_video(apply_frame))

        video_link_label.grid(row=1, column=0)
        video_link_button.grid(row=1, column=1)


def add_video(apply_frame):
    filename_vid = filedialog.askopenfilename(title='open')
    print(filename_vid)
    if (filename_vid != ''):
        vid_label = Label(apply_frame, text=filename_vid, pady=10)
        vid_label.grid(row=1, column=2)


def show_individual_steps(selected_number):
    # for widget in apply_activity_steps_frame.winfo_children():
    #    widget.destroy()
    data_collector['Application_Steps_Number'] = selected_number
    number_of_steps = int(selected_number)

    i = 0
    for i in range(number_of_steps):
        step_label = Label(apply_activity_steps_frame, text="Step Description", pady=10)
        step_text = Entry(apply_activity_steps_frame)
        step_image_button = Button(apply_activity_steps_frame, text='Add Image',
                                   command=lambda row=i: add_image(apply_frame, row))

        step_label.grid(row=i, column=0)
        step_text.grid(row=i, column=1)
        step_image_button.grid(row=i, column=3)
        i += 1


def add_image(apply_frame, i):
    filename = filedialog.askopenfilename(title='open')
    print(filename)
    if (filename != ''):
        step_label = Label(apply_frame, text=filename, pady=10)
        step_label.grid(row=i + 1, column=4)


def add_create_frame():
    create_test_label = Label(create_frame, text='Provide the Answer Key in this format(1-a, 2-b, 3-c,4-d, 5-e)')
    create_test_entry = Entry(create_frame, width=20)
    record_audio_video_label = Label(create_frame, text='Do you want to record an audio or video response?')
    var_video_audio = IntVar()
    record_audio_video_checkbox = Checkbutton(create_frame, text="yes/no", var=var_video_audio)
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
        title_frame.pack_forget()
        factual_frame.pack(side='top')
    if index == 2:
        data_collector["Factual_Term1"] = factual_term_text.get()
        data_collector["Factual_Term1_Description"] = factual_term_desc_text.get('1.0', 'end')

        data_collector['Factual_Term2'] = factual_term_text1.get()
        data_collector['Factual_Term2_Description'] = factual_term_desc_text1.get('1.0', 'end')


        data_collector["Factual_Term3"] = factual_term_text2.get()
        data_collector["Factual_Term3_Description3"] = factual_term_desc_text2.get('1.0', 'end')

        factual_frame.pack_forget()
        apply_frame.pack(side='top')
        apply_activity_frame.grid(row=1, column=0, columnspan=2)
        apply_activity_steps_frame.grid(row=1, column=0, columnspan=2)
    if index == 3:
        apply_frame.pack_forget()
        create_frame.pack()
        next_button.config(text='Submit')
    if index == 4:
        save_data()
        magic_wizard.destroy()
    print(data_collector)


def save_data():
    pass


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
