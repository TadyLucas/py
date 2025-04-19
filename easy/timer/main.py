import time
import customtkinter as ctk


def main():
    app = ctk.CTk()
    app.title("Timer")
    app.geometry("600x400") # w x h
    ctk.set_appearance_mode("dark")
    TIME = ctk.StringVar()


    h1 = ctk.CTkLabel(app, text="Timer", font=("Helvetica", 30), pady=30)
    h1.pack()

    enterTime = ctk.CTkEntry(app, placeholder_text="Enter time in seconds", textvariable=TIME)
    enterTime.pack()

    timer = ctk.CTkLabel(app, text="00:00", font=("Helvetica", 20))
    
    btn = ctk.CTkButton(app, text="Start Timer", command=lambda: [start_timer(int(TIME.get()), timer), enterTime.pack_forget()])
    btn.pack()

    app.mainloop()

def start_timer(seconds, timer):
    countdown(seconds, timer)

def countdown(seconds, timer):
    if seconds >= 0:
        timer.pack()
        mins, secs = divmod(seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"

        timer.configure(text=time_str)

        timer.after(1000, countdown, seconds-1, timer)
    else:
        timer.configure(text="Time's up!")



if __name__ == "__main__":
    main() 