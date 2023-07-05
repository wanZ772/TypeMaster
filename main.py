import tkinter as tk
from pynput.keyboard import Key, Controller
from threading import Thread
from time import sleep
from os import system

start_type = False

bad_char = [',', '?', "!", "(", ")", ".", "'"]

with open('source_text.txt', 'r') as data:
    source_text = data.read().replace('\n', ' ')
for i in bad_char:
    source_text = source_text.replace(i, "")
    
# source_text = source_text.replace("'", "")   
source_text = source_text.lower()
source_text = source_text.split(" ")


# key_release = KeyTracker()
actual_word = []
wrong_word = []
key_id = [None] * 26
# alphabet = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
low_alphabet = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
low_alphabet = low_alphabet.split(" ")

# print(alphabet[0])
order = 0
correct = 0

def timer():
    global start_type
    global order
    global correct
    start_type = True
    for i in reversed(range(30)):
        timer_alert.config(text="00:"+str(i))
        sleep(1)
    print("Correct word(s): " + str(correct))
    print("Wrong word(s): " + str((order + 1) - correct))
    print("Your speed: " + str(correct / .3) + " WPM")
    print("Accuracy: " + str((correct / (order+1)) * 100) + " %")
    start_type = False
    
    
    popup = tk.Toplevel(window)
    popup.geometry("250x100")
    popup.title("Score")
    
    tk.Label(popup, text= "Correct word(s): " + str(correct), font=('Mistral 10 italic')).place(x=0,y=0)
    tk.Label(popup, text= "Wrong word(s): " + str((order+1) - correct), font=('Mistral 10 italic')).place(x=0,y=20)
    tk.Label(popup, text= "Your speed: " + str(order / .3) + " WPM", font=('Mistral 10 italic')).place(x=0,y=40)
    tk.Label(popup, text= "Accuracy: " + str((correct / (order + 1)) * 100) + " %", font=('Mistral 10 italic')).place(x=0,y=60)
    # tk.Label(popup, text= "Correct word(s): " + str(correct), font=('Mistral 10 italic')).place(x=0,y=0)
    timer_alert.config(text="00:30")
    order = 0
    correct = 0
    text_input.delete(0, tk.END)
    text_output.config(text=source_text[0])
    
    

def load_text():
    global order
    
    order = 0
    global source_text
    system("notepad source_text.txt")
    
    with open('source_text.txt', 'r') as data:
        source_text = data.read().replace('\n', ' ')
    for i in bad_char:
        source_text = source_text.replace(i, "")
        
    # source_text = source_text.replace("'", "")   
    source_text = source_text.lower()
    source_text = source_text.split(" ")
    text_output.config(text=source_text[0])
def key_release(event):
    if (start_type == False):
        Thread(target=timer).start()
    try:
        key_id[low_alphabet.index(event.char)].config(bg='gray')
    except:
        pass
def key_press(event):
    # a.config(bg='green')
    key_id[low_alphabet.index(event.char)].config(bg='green')
    # if ()
    # key_id[low_alphabet.index(event.char)].config(bg='gray')
def next(event):
    
    global order
    global correct
    
    # if (source_text[order] == "  "):
    #     order += 1
    
    try:
        # next_text.config(text=source_text[order+1])
        if (text_input.get().strip(" ") == source_text[order]):
            correct += 1
        text_output.config(text=source_text[order + 1])
    except:
        pass
    text_input.delete(0, tk.END)
    order += 1
    
    # text_input.insert(0, '')

window = tk.Tk()
window.configure(background='black')
window.geometry('1000x400') 
window.title("Type Master | Developed by WanZ | v2023.0")

# text = source_text[0]

# print(text)

text_output = tk.Label(window, text=source_text[0], justify='center', font=('Calibry', 20), bg='black', fg='white')
# next_text = tk.Label(window, text=source_text[1], justify='center', font=('Calibry', 10), bg='black', fg='gray')
text_output.place(x=460,y=0)
# next_text.place(x=530, y=15)
timer_alert = tk.Label(window, text="00:30", justify='center', font=(10), fg='orange', bg='black')
timer_alert.place(x=0,y=0)
text_input = tk.Entry(window, width=60, justify='center')
text_input.place(x=295,y=50)
text_input.bind("<space>", next)
tk.Button(window, text="Load Text", command=load_text).place(x=940,y=0)

column1 = 10
column2 = 60
column3 = 190
for i in range(0, 26):
    if (i < 10):
        key_id[i] = tk.Label(window, text=low_alphabet[i].upper(), bg='gray',fg='white', padx=20, width=4,height=3)
        key_id[i].place(y=90, x=column1)
        text_input.bind("<{}>".format(low_alphabet[i]), key_press)
        # text_input.bind("<KeyRelease>", )
        column1 += 100
    elif (i > 9 and i < 19):
        key_id[i] = tk.Label(window, text=low_alphabet[i].upper(), bg='gray',fg='white', padx=20, width=4,height=3)
        key_id[i].place(y=190, x=column2)
        text_input.bind("<{}>".format(low_alphabet[i]), key_press)
        column2 += 100
    else:
         key_id[i] = tk.Label(window, text=low_alphabet[i].upper(), bg='gray',fg='white', padx=20, width=4,height=3)
         key_id[i].place(y=290, x=column3)
         text_input.bind("<{}>".format(low_alphabet[i]), key_press)
         column3 += 100
#     the_column += 1
    # if (i > 10 && i <= 19):
    #     tk.Label(window, text=i).grid(column=the_column +2, row=4)
text_input.bind("<KeyRelease>", key_release)

window.mainloop()