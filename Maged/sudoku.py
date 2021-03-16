from random import sample
from tkinter import *

sudoku=Tk()
sudoku.title('Sudoku')

#General Functions
def draw_grid(root):
	global Field
	grid_frame=Frame(root)
	grid_frame.grid(row=0,column=0)
	Field=[[Entry(grid_frame,width=5) for j in range(9)] for i in range(9)]
	for i in range(9):
		if i<3:
			row=i
		elif i<6:
			row=i+1
		else:
			row=i+2
		for j in range(9):
			if j<3:
				column=j
			elif j<6:
				column=j+1
			else:
				column=j+2
			Field[i][j].grid(row=row,column=column,ipady=5)
	border_canvas1=Canvas(grid_frame,width=320,height=1,bg='black')
	border_canvas1.grid(row=3,column=0,columnspan=11)
	border_canvas2=Canvas(grid_frame,width=320,height=1,bg='black')
	border_canvas2.grid(row=7,column=0,columnspan=11)
	border_canvas3=Canvas(grid_frame,width=1,height=300,bg='black')
	border_canvas3.grid(row=0,column=3,rowspan=11)
	border_canvas4=Canvas(grid_frame,width=1,height=300,bg='black')
	border_canvas4.grid(row=0,column=7,rowspan=11)

def user_solving():
	global puzzle
	global Field
	solving_frame.pack()
	draw_grid(solving_frame)
	for i in range(9):
		for j in range(9):
			if puzzle[i][j]!=0:
				Field[i][j].insert(0,puzzle[i][j])
				Field[i][j]['state']='disabled'

def generator():
	base  = 3
	side  = base*base
	def pattern(r,c): return (base*(r%base)+r//base+c)%side
	def shuffle(s): return sample(s,len(s)) 
	rBase = range(base) 
	rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
	cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
	nums  = shuffle(range(1,base*base+1))
	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
	squares = side*side
	empties = squares * 3//4
	for p in sample(range(squares),empties):
	    board[p//side][p%side] = 0
	return board

def solver(bo):
	find = find_empty(bo)
	if not find:
		return True
	else:
		row, col = find
	for i in range(1,10):
		if valid(bo, i, (row, col)):
			bo[row][col] = i
			if solver(bo):
				return True
			bo[row][col] = 0
	return False

#The functions used in the solver
def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False   
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

#The opening frame button functions
def generate():
	global puzzle
	opening.pack_forget()
	puzzle=generator()
	user_solving()

def make():
	opening.pack_forget()
	make_frame0.pack()

#The "make my own sudoku" button functions
def make_in_app():
	make_frame0.pack_forget()
	make_frame1.pack()
	draw_grid(make_frame1)

def submit_puzzle():
	global puzzle
	puzzle=[[ int(Field[i][j].get()) if Field[i][j].get()!='' else 0 for j in range(9)] for i in range(9)]
	make_frame1.pack_forget()
	user_solving()

def importing_frame():
	make_frame0.pack_forget()
	make_frame2.pack()

def import_puzzle():
	global puzzle
	make_frame2.pack_forget()
	file=F4_1.get()
	input_board=open(file,'r')
	input_list=[x.strip().split(',') for x in input_board]
	puzzle=[[0 for j in range(9)] for i in range(9)]
	for i in input_list:
		puzzle[int(i[0])][int(i[1])]=int(i[2])
	user_solving()

#The (user_solving) button functions
def check_solution():
	global Field
	global puzzle
	text1='Congratulations!!!\nYou solved the sudoku puzzle successfully!'
	text2='Your solution doesn\'t match ours.\nEither you made a mistake or you obtained a different solution!!'
	solver(puzzle)
	user_solution=[[ int(Field[i][j].get()) if Field[i][j].get()!='' else 0 for j in range(9)] for i in range(9)]
	if puzzle==user_solution:
		L5_1['text']=text1
	else:
		L5_1['text']=text2
	L5_1.grid(row=5,column=0)

def show_solution():
	global Field
	global puzzle
	solver(puzzle)
	for i in range(9):
		for j in range(9):
			Field[i][j].delete(0,'end')
			Field[i][j].insert(0,puzzle[i][j])

def new_game():
	L5_1.grid_forget()
	solving_frame.pack_forget()
	opening.pack()

def export_game():
	game=[[ int(Field[i][j].get()) if Field[i][j].get()!='' else 0 for j in range(9)] for i in range(9)]
	file=open('game.txt','w')
	for i in range(9):
		for j in range(9):
			file.write(f'{i},{j},{game[i][j]}\n')
	file.close()

#The opening frame
opening=Frame(sudoku,padx=20,pady=20)
opening.pack()
L1_1=Label(opening,text='I want to:')
L1_1.grid(row=0,column=0)
b1_1=Button(opening,text='let the app generate a sudoku',command=generate)
b1_1.grid(row=1,column=0,pady=10)
b1_2=Button(opening,text='make my own sudoku',command=make)
b1_2.grid(row=2,column=0,pady=10)

#The "make my own sudoku" frames
make_frame0=Frame(sudoku,padx=20,pady=20)
L2_1=Label(make_frame0,text='I want to:')
L2_1.grid(row=0,column=0)
b2_1=Button(make_frame0,text='make the sudoku in the app',command=make_in_app)
b2_1.grid(row=1,column=0,pady=10)
b2_2=Button(make_frame0,text='import the sudoku from a text file',command=importing_frame)
b2_2.grid(row=2,column=0,pady=10)

make_frame1=Frame(sudoku,padx=10,pady=10)
b3_1=Button(make_frame1,text='Submit Puzzle',command=submit_puzzle)
b3_1.grid(row=1,column=0)

make_frame2=Frame(sudoku,padx=20,pady=20)
L4_1=Label(make_frame2,text='Code your game in a text file where each line contains the x-coordinate of a clue, its y-coordinate and its value all seperated by commas.\nThe x and y coordinates start from 0 not 1.\nEnter the file name in the field as (path/file_name.txt)')
L4_1.grid(row=0,column=0)
F4_1=Entry(make_frame2)
F4_1.grid(row=1,column=0)
b4_1=Button(make_frame2,text='Import',command=import_puzzle)
b4_1.grid(row=2,column=0)

#The frame where the user solves a puzzle
solving_frame=Frame(sudoku,padx=10,pady=10)
b5_1=Button(solving_frame,text='Check My Solution',command=check_solution)
b5_1.grid(row=1,column=0)
b5_2=Button(solving_frame,text='Show Solution',command=show_solution)
b5_2.grid(row=2,column=0)
b5_3=Button(solving_frame,text='New Game',command=new_game)
b5_3.grid(row=3,column=0)
b5_4=Button(solving_frame,text='Export game to a text File',command=export_game)
b5_4.grid(row=4,column=0)
L5_1=Label(solving_frame)

sudoku.mainloop()
