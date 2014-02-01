import Tkinter
import random

master = Tkinter.Tk()
window = Tkinter.Canvas(master, width=400, height=400)
window.pack()

color_list = ['#ff3100', '#21313e', '#8f9e99', '#0189e1', '#e1e000']

linelen = 20

for count in range(0,500):
    origin_x = random.randint(0, 400)
    origin_y = random.randint(0, 400)

    destination_x = random.randint(0, 400)
    destination_y = random.randint(0, 400)

    window.create_line(origin_x, origin_y, destination_x, destination_y, width=3, fill=random.choice(color_list))

master.mainloop()
