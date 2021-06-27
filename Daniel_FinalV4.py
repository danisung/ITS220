import pandas as pd
import random
from tkinter import *
from tkinter import messagebox

def result():
    name = str(NFL.get())
    Output.insert(END, "Your Team: "+ name +" has been chosen: ")
    nflplayers_df = pd.read_excel("nflplayers.xlsx", engine='openpyxl')

    #QB
    if str(qb.get())== "1":
        posi = random.randrange(1,32)
        qb_1 = (nflplayers_df.loc[nflplayers_df['number'] == posi,['QB']])
        qb_a = str(qb_1.to_string(index=False, header=False))
        Output.insert(END, "\nQB is: " + qb_a + ".")
    if str(qb.get())== "2":
        posi = random.randrange(1, 32)
        posi2 = random.randrange(1, 32)
        qb_2 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['QB']])
        qb_3 = (nflplayers_df.loc[nflplayers_df['number'] == posi2, ['QB']])
        qb_b = str(qb_2.to_string(index=False, header=False))
        qb_c = str(qb_3.to_string(index=False, header=False))
        Output.insert(END,"\nQB are: "+qb_b+"\n and "+qb_c)

    #RB
    if str(rb.get())== "2":
        posi = random.randrange(1, 32)
        posi2 = random.randrange(1, 32)
        rb_2 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['RB']])
        rb_3 = (nflplayers_df.loc[nflplayers_df['number'] == posi2, ['RB']])
        rb_b = str(rb_2.to_string(index=False, header=False))
        rb_c = str(rb_3.to_string(index=False, header=False))
        Output.insert(END,"\nRB are: "+rb_b+"\n and "+rb_c)
    if str(rb.get())== "3":
        posi = random.randrange(1, 32)
        posi2 = random.randrange(1, 32)
        posi3 = random.randrange(1, 32)
        rb_1 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['RB']])
        rb_2 = (nflplayers_df.loc[nflplayers_df['number'] == posi2, ['RB']])
        rb_3 = (nflplayers_df.loc[nflplayers_df['number'] == posi3, ['RB']])
        rb_a = str(rb_1.to_string(index=False, header=False))
        rb_b = str(rb_2.to_string(index=False, header=False))
        rb_c = str(rb_3.to_string(index=False, header=False))
        Output.insert(END,"\nRB are: "+rb_a+"\n and "+rb_b+"\n and"+rb_c+".")

    #WR
    if str(wr.get())== "2":
        posi = random.randrange(1, 32)
        posi2 = random.randrange(1, 32)
        wr_2 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['WR']])
        wr_3 = (nflplayers_df.loc[nflplayers_df['number'] == posi2, ['WR']])
        wr_b = str(wr_2.to_string(index=False, header=False))
        wr_c = str(wr_3.to_string(index=False, header=False))
        Output.insert(END,"\nWR are: "+wr_b+"\n and "+wr_c)
    if str(wr.get())== "3":
        posi = random.randrange(1, 32)
        posi2 = random.randrange(1, 32)
        posi3 = random.randrange(1, 32)
        wr_1 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['WR']])
        wr_2 = (nflplayers_df.loc[nflplayers_df['number'] == posi2, ['WR']])
        wr_3 = (nflplayers_df.loc[nflplayers_df['number'] == posi3, ['WR']])
        wr_a = str(wr_1.to_string(index=False, header=False))
        wr_b = str(wr_2.to_string(index=False, header=False))
        wr_c = str(wr_3.to_string(index=False, header=False))
        Output.insert(END,"\nWR are: "+wr_a+"\n and "+wr_b+"\n and"+wr_c+".")

    #TE
    if str(te.get()) == "1":
        posi = random.randrange(1, 32)
        te_1 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['TE']])
        te_a = str(te_1.to_string(index=False, header=False))
        Output.insert(END, "\nTE is: " + te_a + ".")
    if str(te.get()) == "2":
        posi = random.randrange(1, 32)
        posi2 = random.randrange(1, 32)
        te_2 = (nflplayers_df.loc[nflplayers_df['number'] == posi, ['TE']])
        te_3 = (nflplayers_df.loc[nflplayers_df['number'] == posi2, ['TE']])
        te_b = str(te_2.to_string(index=False, header=False))
        te_c = str(te_3.to_string(index=False, header=False))
        Output.insert(END, "\nTE are: " + te_b + "\n and " + te_c)

def ExitApplication():
    MsgBox = messagebox.askquestion('Quit', 'Do you really want to quit?',icon='error')

    if MsgBox == 'yes':
        app.destroy()
    else:
       messagebox.showinfo('Back', 'Lets go back to the game.')

app = Tk()
app.title('Draft Kings Best Ball')
Label(app, text = "GIVE YOUR TEAM NAME",bg="navy blue", fg='silver').pack()
NFL = Entry(app)
NFL.pack()

#Position QB
Label(app, text = "QB?").pack()
qb = StringVar()
qb.set(None)
Radiobutton(app, variable = qb, text = "1", value = 1).pack()
Radiobutton(app, variable = qb, text = "2", value = 2).pack()

#Position RB
Label(app, text = "RB").pack()
rb = StringVar()
rb.set(None)
Radiobutton(app, variable = rb, text = "2", value = 2).pack()
Radiobutton(app, variable = rb, text = "3", value = 3).pack()

#Position WR
Label(app, text = "WR").pack()
wr = StringVar()
wr.set(None)
Radiobutton(app, variable = wr, text = "2", value = 2).pack()
Radiobutton(app, variable = wr, text = "3", value = 3).pack()

#PositionTE
Label(app, text = "TE").pack()
te = StringVar()
te.set(None)
Radiobutton(app, variable = te, text = "1", value = 1).pack()
Radiobutton(app, variable = te, text = "2", value = 2).pack()

Output = Text(app, height=10, width=50,bg="silver")
Output.pack()

Button(app, text = "Best Player Generator", command = result, bg='dark green', fg='silver').pack()
Button(app, text='Close App', command=ExitApplication, bg='dark red', fg='silver').pack()
app.mainloop()

