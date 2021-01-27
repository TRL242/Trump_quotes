from tkinter import *
import requests


def get_quote():
    response = requests.get('https://api.tronalddump.io/random/quote')
    response.raise_for_status()
    data = response.json()
    quote = data["value"]
    #print(data)
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Trump Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click the Trump for a quote.", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

trump_img = PhotoImage(file="trump_img.png")
trump_button = Button(image=trump_img, highlightthickness=0, command=get_quote)
trump_button.grid(row=1, column=0)



window.mainloop()