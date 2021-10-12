from tkinter import *


def create_frame(master):
    print("create frame")

    frame = Frame(master)

    b = Button(frame, text="do something")
    b.pack(pady=10)

    clearall = Button(frame, text="reset", command=lambda: reset_frame(frame))
    clearall.pack(pady=10)

    return frame


def reset_frame(current_frame, new_frame):
    current_frame.destroy()
    # frame = create_frame(master)
    # frame.pack()
    conversion = create_frame(new_frame)
    conversion.pack()


master = Tk()

frame1 = create_frame(master)
frame1.pack()

# m2 = Tk()
# frame2 = create_frame(m2)
# frame2.pack()

mainloop()
