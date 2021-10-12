"""Multi-frame tkinter conversion app"""

import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__()
        tk.Label(self, text="Start Page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Calculate Miles to Km",
                  command=lambda: master.switch_frame(PageOne)).pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Miles to Km").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        sign = tk.Label(text="=")
        sign.pack()
        # sign.grid(column=0, row=1, padx=(20, 0))
        user_input = tk.Entry(width=10)
        user_input.pack()
        first_unit = tk.Label(text="Miles")
        first_unit.pack()
        # user_input.grid(column=1, row=0)
        default_value = tk.Label(text="0")
        default_value.pack()
        # default_value.grid(column=1, row=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
