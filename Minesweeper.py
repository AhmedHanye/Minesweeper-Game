from tkinter import *  # this is for the GUI
# this if for the messagebox that will show up when you win
from tkinter import messagebox
from random import choice  # this is for choosing a random number


# Create the main window
root = Tk()  # this is the main window
root.title("Minesweeper Game")  # this is the title of the window
root.geometry("1200x600")  # this is the size of the window
root.config(bg="white")  # this is the background color of the window
root.iconbitmap("favicon.ico")  # this is the icon of the window


# Menu bar functions
def toggle_fullscreen():  # this function is for the full screen
    # this is the attribute of the full screen
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


def new_game():  # this function is for the new game
    # this if for reseting the cells
    for cell in Cells:
        cell.destroy()
    create_cells()
    # this is for reseting the sidebar
    global left_cells
    left_cells = 22
    update_number_lost(left_cells)
    global chance  # this is for reseting the chance
    global win  # this is for reseting the win
    chance = 3
    win = 0
    chance_var.set(f"You have {chance} chances")


def show_help():  # this function is for the help
    help_window = Toplevel(root)
    help_window.title("Help")
    help_text = """
    This is winwows minesweeper game.\n\n
    The goal of the game is to find all the cells with 1.\n\n
    If you click on a cell with 0, you will lose a chance.\n\n 
    If you lose all your chances, you will lose the game.\n\n 
    If you find all the cells with 1, you will win the game.\n\n
    You can find the number of the cells with 1 in the sidebar.\n\n 
    You can find the number of your chances in the sidebar.\n\n
    You can find the new game button in the menu bar.\n\n
    You can find the full screen button in the menu bar.\n\n
    You can find the help button in the menu bar.\n\n 
    You can find the exit button in the menu bar.\n\n Good luck!
    """
    help_label = Label(help_window, text=help_text, padx=20, pady=20)
    help_label.pack()


# Menu bar
menu_bar = Menu(root)  # this is for making the menu bar
# this is for adding the new game button
menu_bar.add_command(label="New Game", command=new_game)
# this is for adding the full screen button
menu_bar.add_command(label="Full Screen", command=toggle_fullscreen)
# this is for adding the help button
menu_bar.add_command(label="Help", command=show_help)
# this is for adding the exit button
menu_bar.add_command(label="Exit", command=root.quit)
# this is for adding the menu bar to the main window
root.config(menu=menu_bar)


# Sidebar
sidebar_frame = Frame(root, bg="gray", width=200)
sidebar_frame.pack(side=LEFT, fill=Y)


# Sidebar content
left_cells = 81


def update_number_win(left_cells):
    number_label.config(text=f"Left Cells: {left_cells}")
    smiley_label.config(text="😎")


chance = 3


def update_number_lost(left_cells):
    number_label.config(text=f"Left Cells: {left_cells}")
    smiley_label.config(text="😊")

    chance_var.set(f"You have {chance} chances")


number_label = Label(sidebar_frame, text="Left Cells: 81",
                     bg="gray", fg="white", font=("Arial", 16))
number_label.pack(pady=20)

smiley_label = Label(sidebar_frame, text="😊", bg="gray",
                     fg="orange", font=("Arial", 60))
smiley_label.pack(pady=10)

chance_var = StringVar()
chance_var.set(f"You have {chance} chances")
number_chances = Label(
    sidebar_frame, textvariable=chance_var, bg="gray", fg="white", font=("Arial", 16))
number_chances.pack(pady=30)


# Game over function
def toggle_cell(event):
    global chance  # this is for being able to change the chance variable
    global win  # this is for being able to change the win variable

    cell = event.widget
    if cell["bg"] == "white":  # if you click on the cell with white background
        if cell["text"] == "0":  # if you click on the cell with 0
            cell.config(fg="red",bg="red")
            if chance == 1:
                messagebox.showinfo("Game Over", "You lost the game!")
                new_game()
            else:  # if you have more than 1 chance
                chance -= 1
                chance_var.set(f"You have {chance} chances!")
        elif cell["text"] == "1":  # if you click on the cell with 1
            cell.config(fg="black",bg="black")
            global left_cells
            left_cells -= 1
            update_number_win(left_cells)
            win += 1
    if win == 22:  # if you win the game
        messagebox.showinfo("Winner", "You won the game!")
        new_game()


# Create cells frame
# this is the frame that contains the cells
cells_frame = Frame(root, bg="white")
# this is the position of the frame
cells_frame.pack(side=LEFT, fill=BOTH, expand=True)

Cells = []  # this is the list that contains the cells
A = [0] * 3 + [1] * 22  # this is the list that contains the numbers of the cells


def create_cells():  # this function is for creating the cells
    B = A.copy()  # this is for copying the list A
    global Cells  # this is for being able to change the Cells variable
    for row in range(5):
        for column in range(5):
            # this is for choosing a random number from the list B
            O = choice(B)
            cell = Label(cells_frame, text=str(O), borderwidth=1, relief="solid", font=(
                "Arial", 16), width=2, height=1, bg="white")
            # this is for removing the number that we chose from the list B
            B.remove(O)
            Cells.append(cell)  # this is for adding the cell to the list Cells
            # this is for the position of the cells
            cell.grid(row=row, column=column, sticky="nsew")
            # this is for adapting the size of the cells
            cells_frame.grid_columnconfigure(column, weight=1)
            # this is for adapting the size of the cells
            cells_frame.grid_rowconfigure(row, weight=1)
            # this is for binding the left click to the toggle_cell function
            cell.bind("<Button-1>", toggle_cell)
            # this is for binding the right click to the toggle_cell function
            cell.bind("<Button-3>", toggle_cell)
            # this is for making the text invisible
            cell.config(fg="white", bg="white")


create_cells()  # this is for calling the create_cells() function
new_game()  # you call the function so that you don't get an error when you run the program for the first time


# Exit from the game
root.mainloop()
