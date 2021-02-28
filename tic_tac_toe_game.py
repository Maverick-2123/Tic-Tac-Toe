from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("290x380")
root.config(background = "grey")

win_cond = True

turn = 0

list1 = {1:"-",2:"-",3:"-",}
list2 = {1:"-",2:"-",3:"-",}
list3 = {1:"-",2:"-",3:"-",}

def play(tile):
    global list1
    global turn
    if turn%2 == 0:
        tile.config(text = "X", state = DISABLED, background = "red")
        if tile == sq_1_1:
            list1[1] = "X"
            win()
        elif tile == sq_1_2:
            list1[2] = "X"
        elif tile == sq_1_3:
            list1[3] = "X"

        elif tile == sq_2_1:
            list2[1] = "X"
        elif tile == sq_2_2:
            list2[2] = "X"
        elif tile == sq_2_3:
            list2[3] = "X"

        elif tile == sq_3_1:
            list3[1] = "X"
        elif tile == sq_3_2:
            list3[2] = "X"
        elif tile == sq_3_3:
            list3[3] = "X"


    else:
        tile.config(text = "O", state = DISABLED, background = "yellow")
        if tile == sq_1_1:
            list1[1] = "O"
        elif tile == sq_1_2:
            list1[2] = "O"
        elif tile == sq_1_3:
            list1[3] = "O"
            
        elif tile == sq_2_1:
            list2[1] = "O"
        elif tile == sq_2_2:
            list2[2] = "O"
        elif tile == sq_2_3:
            list2[3] = "O"

        elif tile == sq_3_1:
            list3[1] = "O"
        elif tile == sq_3_2:
            list3[2] = "O"
        elif tile == sq_3_3:
            list3[3] = "O"

            

        
    turn += 1
    win()
    

def win():
    
    if list1[1] == list2[1] == list3[1] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()
        
    elif list1[1] == list2[1] == list3[1] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()
        
    elif list1[2] == list2[2] == list3[2] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()

    elif list1[2] == list2[2] == list3[2] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()
        

    elif list1[3] == list2[3] == list3[3] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()


    elif list1[3] == list2[3] == list3[3] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()
        

    elif list1[1] == list1[2] == list1[3] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()


    elif list1[1] == list2[2] == list3[3] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()


    elif list2[1] == list2[2] == list2[3] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()


    elif list2[1] == list2[2] == list2[3] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()


    elif list3[1] == list3[2] == list3[3] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()


    elif list3[1] == list3[2] == list3[3] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()


    elif list1[1] == list2[2] == list3[3] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()

    elif list1[1] == list2[2] == list3[3] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()


    elif list1[3] == list2[2] == list3[1] == "X":
        messagebox.showinfo(title = "Win", message = "Player 1 Won!")
        root.destroy()


    elif list1[3] == list2[2] == list3[1] == "O":
        messagebox.showinfo(title = "Win", message = "Player 2 Won!")
        root.destroy()
    elif turn == 9:
        draw()

def draw():
    if len(list1) == len(list2) == len(list3) == 3:
        messagebox.showinfo(title = "Draw", message = "Match Drawn!")
        root.destroy()
        
        
        
    
sq_1_1 = Button(root, text = "-", command = lambda:play(sq_1_1))
sq_1_1.config(padx = 40, pady = 50)
sq_1_1.grid(row = 0, column = 0)

sq_1_2 = Button(root, text = "-", command = lambda:play(sq_1_2))
sq_1_2.config(padx = 40, pady = 50)
sq_1_2.grid(row = 0, column = 1)

sq_1_3 = Button(root, text = "-", command = lambda:play(sq_1_3))
sq_1_3.config(padx = 40, pady = 50)
sq_1_3.grid(row = 0, column = 2)

sq_2_1 = Button(root, text = "-", command = lambda:play(sq_2_1))
sq_2_1.config(padx = 40, pady = 50)
sq_2_1.grid(row = 1, column = 0)

sq_2_2 = Button(root, text = "-", command = lambda:play(sq_2_2))
sq_2_2.config(padx = 40, pady = 50)
sq_2_2.grid(row = 1, column = 1)

sq_2_3 = Button(root, text = "-", command = lambda:play(sq_2_3))
sq_2_3.config(padx = 40, pady = 50)
sq_2_3.grid(row = 1, column = 2)

sq_3_1 = Button(root, text = "-", command = lambda:play(sq_3_1))
sq_3_1.config(padx = 40, pady = 50)
sq_3_1.grid(row = 2, column = 0)

sq_3_2 = Button(root, text = "-", command = lambda:play(sq_3_2))
sq_3_2.config(padx = 40, pady = 50)
sq_3_2.grid(row = 2, column = 1)

sq_3_3 = Button(root, text = "-", command = lambda:play(sq_3_3))
sq_3_3.config(padx = 40, pady = 50)
sq_3_3.grid(row = 2, column = 2)



root.mainloop()
