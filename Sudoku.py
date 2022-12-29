import printing


def definition_mat_local(x,y):
    c_left = [0,1,2]
    c_center=[3,4,5]
    c_right=[6,7,8]
    l_up=[0,1,2]
    l_center=[3,4,5]
    l_down=[6,7,8]
    c=[c_left,c_center,c_right]
    l=[l_up,l_center,l_down]
    mtrx_loc=[]
    i=0
    while i<3:
        j=0
        while j<3:
            if c[i][j]==x:
                mtrx_loc.append(c[i])
            j+=1
        i+=1
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if l[i][j] == y:
                mtrx_loc.append(l[i])
            j += 1
        i += 1
    return mtrx_loc


def proba_list(mtrx,x,y,mtrx_lc,fst):
    if fst == True:
        prim_list=[1,2,3,4,5,6,7,8,9]
    else:
        prim_list = mtrx[x][y]
    for i in range(9):
        try:
            prim_list.remove(mtrx[x][i])
        except ValueError:
            pass
    for i in range(9):
        try:
            prim_list.remove(mtrx[i][y])
        except ValueError:
            pass
    for i in mtrx_lc[0]:
        for j in mtrx_lc[1]:
            try:
                prim_list.remove(mtrx[i][j])
            except ValueError:
                pass
    if len(prim_list) == 1:
        mtrx[x][y] = prim_list[0]
    else:
        mtrx[x][y] = prim_list


found = False
while not found :
    try:
        game_file = input("Enter the path or the name of the puzzle file : ")
        f = open(game_file, "r")
        found = True
    except FileNotFoundError:
        print("File not found, please try again or create the file")
        found = False
the_tab = []
ch = f.readline()
while ch != "":
    a = []
    for i in range(len(ch)-1):
        a.append(int(ch[i]))
    the_tab.append(a)
    ch = f.readline()
f.close()
fst = True
for i in range(9):
    for j in range(9):
        if the_tab[i][j] == 0:
            tab_local = definition_mat_local(i,j)
            proba_list(the_tab,i,j, tab_local,fst)
fst = False
comp = 1
while comp != 0:
    comp = 0
    for i in range(9):
        for j in range(9):
            if type(the_tab[i][j]) == list:
                tab_local = definition_mat_local(i, j)
                proba_list(the_tab, i, j, tab_local,fst)
                comp += 1
printing.screen(the_tab)
