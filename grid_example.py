__author__ = 'michal.broucek'

import Tkinter
root = Tkinter.Tk(  )
for r in range(3):
    for c in range(4):

        if (r == 1) and (c == 2):
            Tkinter.Label(root, text='R%s/C%s ... longer' % (r,c),
                borderwidth=1 ).grid(row=r,column=c)

        if not (r == 1 and c == 3):
            Tkinter.Label(root, text='R%s/C%s'%(r,c),
                borderwidth=1 ).grid(row=r,column=c)

root.mainloop()
