import tkinter as tk
from pynput.keyboard import Key, Controller
from threading import Thread
from time import sleep

source_text = "From a stunning first sentence to a perfect string of dialogue,"
source_text = source_text.lower()
source_text = source_text.split(" ")
# key_release = KeyTracker()
actual_word = []
wrong_word = []
key_id = [None] * 26
alphabet = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
low_alphabet = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
low_alphabet = low_alphabet.split(" ")

# print(alphabet[0])
order = 0
correct = 0
def key_release(event):
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
    print(text_input.get())
    print(correct)
    try:
        text_output.config(text=source_text[order + 1], )
        if (text_input.get() == source_text[order]):
            print(str(correct = correct + 1))
        else:
            actual_word.append(source_text[order + 1])
            wrong_word.append(text_input.get())
        
    except:
        print("end of the text\n\n")
        print("Correct word(s): " + str(correct))
        print("Speed: ")
        
        print("\n\nWrong word(s): " + str(len(source_text) - correct))
        print("What You Typed \t | \t Actual Word")
        
        for i in range(len(wrong_word)):
            print("{} \t | \t {}".format(wrong_word[i], actual_word[i]))
        
    order = order + 1
    text_input.delete(0, tk.END)
    # text_input.insert(0, '')

window = tk.Tk()
window.geometry('1000x400') 
window.title("Type Master | Developed by WanZ | v2023.0")

# text = source_text[0]

# print(text)

text_output = tk.Label(window, text=source_text[0], justify='center', font=(20))
text_output.place(x=470,y=0)
text_input = tk.Entry(window, width=60, justify='center')
text_input.place(x=295,y=50)
text_input.bind("<space>", next)


column1 = 10
column2 = 60
column3 = 190
for i in range(0, 26):
    if (i < 10):
        key_id[i] = tk.Label(window, text=alphabet[i], bg='gray',fg='white', padx=20, width=4,height=3)
        key_id[i].place(y=90, x=column1)
        text_input.bind("<{}>".format(low_alphabet[i]), key_press)
        # text_input.bind("<KeyRelease>", )
        column1 += 100
    elif (i > 9 and i < 19):
        key_id[i] = tk.Label(window, text=alphabet[i], bg='gray',fg='white', padx=20, width=4,height=3)
        key_id[i].place(y=190, x=column2)
        text_input.bind("<{}>".format(low_alphabet[i]), key_press)
        column2 += 100
    else:
         key_id[i] = tk.Label(window, text=alphabet[i], bg='gray',fg='white', padx=20, width=4,height=3)
         key_id[i].place(y=290, x=column3)
         text_input.bind("<{}>".format(low_alphabet[i]), key_press)
         column3 += 100
#     the_column += 1
    # if (i > 10 && i <= 19):
    #     tk.Label(window, text=i).grid(column=the_column +2, row=4)
text_input.bind("<KeyRelease>", key_release)
for j in range(len(low_alphabet)):
    print(low_alphabet[j])

window.mainloop()