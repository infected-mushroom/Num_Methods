from tkinter import *
import solver

fields = 'S(t)', 'z(t)', 'p(w)', 'x_0', 'y_0', 'T', 'Beta', 'Start Beta', 'Final Beta'

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def solve(entries, automatic=False):
    parameters = {}
    for entry in entries:
	if entry[0] == 'S(t)' or entry[0] == 'p(w)' or entry[0] == 'z(t)':
	    parameters[entry[0]] = entry[1].get()
	else:
            try:
                parameters[entry[0]] = float(entry[1].get())
            except ValueError:
                if entry[0] == 'Beta' and automatic:
                    continue
                if (entry[0] == 'Start beta' or entry[0] == 'Final Beta') \
                        and not automatic:
                    continue
                return
    solver.solve(**parameters)



if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b0 = Button(root, text="Solve", command=(lambda e=ents: solve(e)))
   b0.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
