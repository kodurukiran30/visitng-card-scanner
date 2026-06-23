# Visiting Card scanner GUI

# imported tkinter library
from tkinter import *
import tkinter.messagebox as tmsg    

# Pillow library for importing images
from PIL import Image, ImageTk

# library for filedialog (For file selection)
from tkinter import filedialog

# Pytesseract module importing
import pytesseract        
import os.path

root = Tk()

# fixing geometry of GUI
root.geometry('800x500')        
root.maxsize(1000, 500)
root.minsize(600, 500)
root.title('Visiting card scanner')

# function for uploading file to GUI
def upload_file():        
    global filename
    global start, last
    filename = filedialog.askopenfilename(
        initialdir=os.path.expanduser('~/Desktop'), title = 'Select a card image',
        filetypes=(('jpeg files', '*.jpg'), ('png files', '*.png')))
    
    if filename == '':
        t.delete(1.0, END)
        t.insert(1.0, 'You have not provided any image to convert')
        tmsg.showwarning(
            title = 'Alert!', message = 'Please provide proper formatted image')
        return
    else:
        p_label_var.set('Image uploaded successfully')
        l.config(fg='#0CDD19')
    
    if filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.PNG') or filename.endswith('.png'):
        filename_rev = filename[::-1]
        last = filename.index('.')
        start = len(filename) - filename_rev.index('/') - 1

# function for conversion
def convert():        
    try:
        c_label_var.set('Output...')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string(filename)
        t.delete(1.0, END)
        t.insert(1.0, text)
        root1 = Toplevel()
        root1.title('Uploaded image')
        img1 = ImageTk.PhotoImage(Image.open(filename))
        Label(root1, image=img1).pack()
        root1.mainloop()
        
        # Save text to file
        f_name = filename[start+1:last]+'.txt'
        if not os.path.exists('Database'):
            os.makedirs('Database')
        f_name = os.path.join('Database', f_name)
        with open(f_name, 'w') as f:
            f.write(text)
    except Exception as e:
        t.delete(1.0, END)
        t.insert(1.0, 'You have not provided any image to convert')
        tmsg.showwarning(
            title='Alert!', message='Please provide proper formatted image')

# Menu bar and navigation tab creation
mainmenu = Menu(root)
mainmenu.config(font = ('Times', 29))

m1 = Menu(mainmenu, tearoff = 0)
m1.add_command(label = 'Scan/Upload Visiting or Business cards and get all the text of cards',
               font = ('Times', 13))
root.config(menu = mainmenu)
mainmenu.add_cascade(label = 'Aim', menu = m1)

m2 = Menu(mainmenu, tearoff = 0)
m2.add_command(label = '|| Electronics and Communication engineering student ||', 
               font = ('Times', 13))
m2.add_command(label = '|| Coding Enthusiast ||', font = ('Times', 13))
root.config(menu = mainmenu)
mainmenu.add_cascade(label = 'About us', menu = m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label = 'E-mail: kodurukiran30@gmail.com', 
               font = ('Times', 13))
m3.add_separator()
m3.add_command(label = 'Mobile: +91-7995564820', font=('Times', 13))
m3.add_separator()
m3.add_command(label = 'LinkedIn: https://www.linkedin.com/in/kirankumar-koduru-97aaab407?utm_source=share_via&utm_content=profile&utm_medium=member_android',
               font = ('Times', 13))
root.config(menu = mainmenu)
mainmenu.add_cascade(label = 'Contact us', menu = m3)

root.geometry('960x620')
root.configure(bg='#0f172a')
root.option_add('*Font', 'Segoe UI 10')
root.option_add('*Button.Font', 'Segoe UI 10 bold')
root.option_add('*Label.Font', 'Segoe UI 10')
root.option_add('*Entry.Font', 'Segoe UI 10')
root.option_add('*Text.Font', 'Segoe UI 10')
root.option_add('*Background', "#0fb0cd")
root.option_add('*Foreground', '#e5e7eb')
root.option_add('*Button.Background', '#0ea5e9')
root.option_add('*Button.Foreground', '#ffffff')
root.option_add('*Text.Background', '#111827')
root.option_add('*Text.Foreground', '#e5e7eb')
root.option_add('*Text.InsertBackground', '#0ea5e9')
root.option_add('*HighlightBackground', '#0ea5e9')

header = Frame(root, bg="#13A738", bd=0, pady=18, padx=18)
header.pack(fill='x', padx=16, pady=(16, 10))
Label(header, text='Visiting Card Scanner', bg="#15B8A7", fg='#f8fafc', font=('Segoe UI Semibold', 22)).pack(anchor='w')
Label(header, text='Scan business cards with a premium, modern interface.', bg='#111827', fg='#94a3b8', font=('Segoe UI', 10)).pack(anchor='w', pady=(6, 0))

main_frame = Frame(root, bg='#0f172a')
main_frame.pack(fill='both', expand=True, padx=16, pady=8)

left_panel = Frame(main_frame, bg='#111827', bd=0, relief='flat', padx=20, pady=18)
left_panel.pack(side='left', fill='both', expand=True, padx=(0, 8), pady=0)
right_panel = Frame(main_frame, bg='#111827', bd=0, relief='flat', padx=20, pady=18)
right_panel.pack(side='right', fill='both', expand=True, padx=(8, 0), pady=0)

section = Frame(left_panel, bg='#111827')
section.pack(fill='x', pady=(0, 14))
Label(section, text='Upload & Scan', bg='#111827', fg='#f8fafc', font=('Segoe UI Semibold', 16)).pack(anchor='w')
Label(section, text='Choose a card image and start OCR conversion.', bg='#111827', fg='#94a3b8').pack(anchor='w', pady=(6, 0))

file_frame = Frame(left_panel, bg='#111827')
file_frame.pack(fill='x', pady=(8, 18))
Button(file_frame, text='Upload Card', bg='#0ea5e9', fg='#ffffff', activebackground='#38bdf8', activeforeground='#ffffff', relief='flat', padx=16, pady=12, command=upload_file).pack(side='left')
Label(file_frame, text='Supported: PNG, JPG, JPEG', bg='#111827', fg='#cbd5e1').pack(side='left', padx=16)

p_label_var = StringVar()
p_label_var.set('Please upload an image to scan')
l = Label(left_panel, textvariable=p_label_var, bg='#111827', fg='#f97316', anchor='w')
l.pack(fill='x', pady=(0, 14))

Button(left_panel, text='Scan and Convert', bg='#0ea5e9', fg='#ffffff', activebackground='#38bdf8', activeforeground='#ffffff', relief='flat', padx=16, pady=14, command=convert).pack(fill='x')

preview_frame = Frame(left_panel, bg='#0f172a', bd=1, relief='solid')
preview_frame.pack(fill='both', expand=True, pady=(18, 0))
Label(preview_frame, text='Image preview will appear here after upload.', bg='#0f172a', fg='#94a3b8', wraplength=320, justify='center', padx=12, pady=20).pack(expand=True)

section = Frame(right_panel, bg='#111827')
section.pack(fill='x', pady=(0, 14))
Label(section, text='OCR Output', bg='#111827', fg='#f8fafc', font=('Segoe UI Semibold', 16)).pack(anchor='w')
Label(section, text='Your extracted text appears below.', bg='#111827', fg='#94a3b8').pack(anchor='w', pady=(6, 0))

text_frame = Frame(right_panel, bg='#111827')
text_frame.pack(fill='both', expand=True)
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side='right', fill='y')
t = Text(text_frame, height=18, bg='#0f172a', fg='#e5e7eb', insertbackground='#0ea5e9', bd=0, padx=14, pady=14, wrap='word', yscrollcommand=scrollbar.set)
scrollbar.config(command=t.yview)
t.pack(fill='both', expand=True)

t.insert(1.0, 'Text of converted card will be shown here...')

c_label_var = StringVar()
c_label_var.set('Ready for conversion')
c_label = Label(right_panel, textvariable=c_label_var, bg='#111827', fg='#94a3b8', anchor='w')
c_label.pack(fill='x', pady=(14, 0))

footer = Frame(root, bg='#111827', pady=10)
footer.pack(fill='x', padx=16, pady=(8, 16))
Label(footer, text='© 2026 — Developed by Kiran', bg='#111827', fg='#cbd5e1').pack(side='left')
Label(footer, text='Powered by Tesseract OCR', bg='#111827', fg='#94a3b8').pack(side='right')

root.mainloop()

