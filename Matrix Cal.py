import numpy as np


print("===========================================MATRIX CALCULATOR=============================================")   
def add(nos):
    if nos==2:
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 1 (use 2X2 or 3X3)\n")
        #Matrix 1
        while True:
            row=int(input("Enter Number of rows for matrix 1 : "))
            col=int(input("Enter number of columns for matrix 1 : "))
            if row and col not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break
        mat=[]
        for i in range(row):
            tem=[]
            for j in range(col):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat.append(tem)
        mat=np.array(mat)
       

        #matrix 2
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 2\n")   
        while True:
            row2=int(input("Enter Number of rows for matrix 2 : "))
            col2=int(input("Enter number of columns for matrix 2 : "))
            if row2 and col2 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat2=[]
        for i in range(row2):
            tem=[]
            for j in range(col2):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat2.append(tem)
        mat2=np.array(mat2)
        res=[]
        print("MATRIX 1 :")
        for i in mat:
            print(i)
        print("MATRIX 2 :")
        for i in mat2:
            print(i)
        
        res=np.add(mat,mat2)
        print("SUM OF TWO MATRICES : ")    
        for r in res:
            print(r)
            
    if nos==3:
        #Matrix 1
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 1\n")
        while True:
            row=int(input("Enter Number of rows for matrix 1 : "))
            col=int(input("Enter number of columns for matrix 1: "))
            if row and col not in [2,3]:
                print("INVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat=[]
        for i in range(row):
            tem=[]
            for j in range(col):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat.append(tem)
        mat=np.array(mat)
        

        #matrix 2
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 2\n")
        while True:
            row2=int(input("Enter Number of rows for matrix 2 : "))
            col2=int(input("Enter number of columns for matrix 2 : "))
            if row2 and col2 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat2=[]
        for i in range(row2):
            tem=[]
            for j in range(col2):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat2.append(tem)
        mat2=np.array(mat2)
        

        #Matrix 3
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 3\n")
        while True:
            row3=int(input("Enter Number of rows for matrix 3 : "))
            col3=int(input("Enter number of columns for matrix 3 : "))
            if row3 and col3 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat3=[]
        for i in range(row3):
            tem=[]
            for j in range(col3):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat3.append(tem)
        print("MATRIX 1 :")
        for i in mat:
            print(i)
        print("MATRIX 2 :")
        for i in mat2:
            print(i)    
        mat3=np.array(mat3)
        print("MATRIX 3 :")
        for i in mat3:
            print(i)
        res=[]    
        res=np.add(mat,mat2)
        res=np.add(res,mat3)
        print("SUM OF 3 MATRICES : ")
        for i in res:
            print(i)


def sub(nos):
    if nos==2:
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 1\n")
        #Matrix 1
        while True:
            row=int(input("Enter Number of rows for matrix 1 : "))
            col=int(input("Enter number of columns for matrix 1 : "))
            if row and col not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat=[]
        for i in range(row):
            tem=[]
            for j in range(col):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat.append(tem)
        mat=np.array(mat)
       

        #matrix 2
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 2\n")   
        while True:
            row2=int(input("Enter Number of rows for matrix 2 : "))
            col2=int(input("Enter number of columns for matrix 2 : "))
            if row2 and col2 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat2=[]
        for i in range(row2):
            tem=[]
            for j in range(col2):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat2.append(tem)
        mat2=np.array(mat2)
        res=[]
        print("MATRIX 1 :")
        for i in mat:
            print(i)
        print("MATRIX 2 :")
        for i in mat2:
            print(i)
        
        res=np.subtract(mat,mat2)
        print("DIFFERENCE OF TWO MATRICES : ")    
        for r in res:
            print(r)
            
    if nos==3:
        #Matrix 1
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 1\n")
        while True:
            row=int(input("Enter Number of rows for matrix 1 : "))
            col=int(input("Enter number of columns for matrix 1 : "))
            if row and col not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat=[]
        for i in range(row):
            tem=[]
            for j in range(col):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat.append(tem)
        mat=np.array(mat)
        

        #matrix 2
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 2\n")
        while True:
            row2=int(input("Enter Number of rows for matrix 2 : "))
            col2=int(input("Enter number of columns for matrix 2 : "))
            if row2 and col2 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat2=[]
        for i in range(row2):
            tem=[]
            for j in range(col2):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
                
                
            mat2.append(tem)
        mat2=np.array(mat2)
        

        #Matrix 3
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 3\n")
        while True:
            row3=int(input("Enter Number of rows for matrix 3 : "))
            col3=int(input("Enter number of columns for matrix 3 : "))
            if row3 and col3 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat3=[]
        for i in range(row3):
            tem=[]
            for j in range(col3):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat3.append(tem)
        print("MATRIX 1 :")
        for i in mat:
            print(i)
        print("MATRIX 2 :")
        for i in mat2:
            print(i)    
        mat3=np.array(mat3)
        print("MATRIX 3 :")
        for i in mat3:
            print(i)
        res=[]    
        res=np.subtract(mat,mat2)
        res=np.subtract(res,mat3)
        print("DIFFERENCE OF 3 MATRICES : ")
        for i in res:
            print(i)     
def mul(nos):
    if nos==2:
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 1\n")
        #Matrix 1
        while True:
            row=int(input("Enter Number of rows for matrix 1 : "))
            col=int(input("Enter number of columns for matrix 1 : "))
            if row and col not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat=[]
        for i in range(row):
            tem=[]
            for j in range(col):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat.append(tem)
        
       

        #matrix 2
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 2.\n")   
        while True:
            row2=int(input("Enter Number of rows for matrix 2 : "))
            col2=int(input("Enter number of columns for matrix 2 : "))
            if row2 and col2 not in [2,3]:
                print("INVALID INPUT USE 3X3 OR 2X2 Matrix form")
            else:
                break

        mat2=[]
        for i in range(row2):
            tem=[]
            for j in range(col2):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat2.append(tem)
        
        
        if (row and row2 and col and col2)==3:
            res=[[0,0,0],[0,0,0],[0,0,0]]
            
        if (row and row2 and col and col2)==2:
            res=[[0,0],[0,0]]
            
        
        for i in range(len(mat)):
            for j in range(len(mat2[0])):
                for k in range(len(mat)):
                    res[i][j]=res[i][j]+mat[i][k]*mat2[k][j]
        mat=np.array(mat)
        mat2=np.array(mat2)
        res=np.array(res)
        print("MATRIX 1 :")
        for i in mat:
            print(i)
        print("MATRIX 2 :")
        for i in mat2:
            print(i)
        print("MULTIPLICATION OF TWO MATRICES : ")    
        for r in res:
            print(r)
    if nos==3:
        #Matrix 1
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 1\n")
        while True:
            row=int(input("Enter Number of rows for matrix 1 : "))
            col=int(input("Enter number of columns for matrix 1 : "))
            if row and col not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat=[]
        for i in range(row):
            tem=[]
            for j in range(col):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat.append(tem)
        
        

        #matrix 2
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 2\n")
        while True:
            row2=int(input("Enter Number of rows for matrix 2 : "))
            col2=int(input("Enter number of columns for matrix 2 : "))
            if row2 and col2 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat2=[]
        for i in range(row2):
            tem=[]
            for j in range(col2):
                while True:
                    inp=input("Enter element : ")
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat2.append(tem)
        
        

        #Matrix 3
        print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX 3\n")
        while True:
            row3=int(input("Enter Number of rows for matrix 3 : "))
            col3=int(input("Enter number of columns for matrix 3 : "))
            if row3 and col3 not in [2,3]:
                print("\nINVALID INPUT USE 3X3 OR 2X2 Matrix form.\n")
            else:
                break

        mat3=[]
        for i in range(row3):
            tem=[]
            for j in range(col3):
                while True:
                    inp=input("Enter element : ")
                    
                    if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                        print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                    else:
                    
                        if int(inp)<0:
                            tem.append(int(inp))
                            break
                        tem.append(int(inp))
                        break
            mat3.append(tem)
            
        if (row and row2 and row3 and col and col2 and col3)==3:
            res=[[0,0,0],[0,0,0],[0,0,0]]
            res1=[[0,0,0],[0,0,0],[0,0,0]]
        if (row and row2 and row3 and col and col2 and col3)==2:
            res=[[0,0],[0,0]]
            res1=[[0,0],[0,0]]    
        for i in range(len(mat)):
            for j in range(len(mat2[0])):
                for k in range(len(mat)):
                    res[i][j]=res[i][j]+mat[i][k]*mat2[k][j]
   
        
        for i in range(len(res)):
            for j in range(len(mat3[0])):
                for k in range(len(res)):
                    res1[i][j]=res1[i][j]+res[i][k]*mat3[k][j]            
        mat=np.array(mat)
        mat2=np.array(mat2)
        print("MATRIX 1 :")
        for i in mat:
            print(i)
        print("MATRIX 2 :")
        for i in mat2:
            print(i)    
        mat3=np.array(mat3)
        print("MATRIX 3 :")
        for i in mat3:
            print(i)
        res1=np.array(res1)
        print("MULTIPLICATION OF 3 MATRICES : ")
        for i in res1:
            print(i)
def trans():
    print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX \n")
    row=int(input("Enter Number of rows for matrix : "))
    col=int(input("Enter number of columns for matrix : "))
        
    mat=[]
    for i in range(row):
        tem=[]
        for j in range(col):
            while True:
                inp=input("Enter element : ")
                if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                    print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                else:
                    
                    if int(inp)<0:
                        tem.append(int(inp))
                        break
                    tem.append(int(inp))
                    break
        mat.append(tem)

    
    print("GIVEN MATRIX : ")
    giv=np.array(mat)
    for i in giv:
        print(i)
    transpos=np.transpose(giv)
    print("TRANSPOSE OF THE GIVEN MATRIX : ")
    for i in transpos:
        print(i)
    return transpos    
def inv():
    print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX \n")
    while True:
            row=int(input("Enter Number of rows for matrix 1 (only square matrix): "))
            col=int(input("Enter number of columns for matrix 1 : "))
            if row!=col:
                print("\nINVALID INPUT, USE  SQUARE Matrix form.\n")
            else:
                break
        
    mat=[]
    for i in range(row):
        tem=[]
        for j in range(col):
            while True:
                inp=input("Enter element : ")
                if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                    print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                else:
                    
                    if int(inp)<0:
                        tem.append(int(inp))
                        break
                    tem.append(int(inp))
                    break
        mat.append(tem)
    print("GIVEN MATRIX : ")
    giv=np.array(mat)
    for i in giv:
        print(i)
    print("INVERSE OF THE GIVEN MATRIX : ")    
    invers=np.linalg.inv(giv)
    for i in invers:
        print(i)

def ortho():
    print("\nENTER THE NUMBER OF COLUMNS & ROWS FOR MATRIX \n")
    row=int(input("Enter Number of rows for matrix : "))
    col=int(input("Enter number of columns for matrix : "))
        
    mat=[]
    for i in range(row):
        tem=[]
        for j in range(col):
            while True:
                inp=input("Enter element : ")
                if inp in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
                    
                    print("\nINVALID INPUT, Only numbers are considered.\n")
                        
                else:
                    
                    if int(inp)<0:
                        tem.append(int(inp))
                        break
                    tem.append(int(inp))
                    break
        mat.append(tem)

    
    print("GIVEN MATRIX : ")
    giv=np.array(mat)
    transpos=np.transpose(giv)
    listcopy=list(transpos)
    for i in giv:
        print(i)
    if (row and col )==3:
            res=[[0,0,0],[0,0,0],[0,0,0]]
            
    if (row and col )==2:
            res=[[0,0],[0,0]]
            
        
    for i in range(len(mat)):
        for j in range(len(listcopy[0])):
            for k in range(len(mat)):
                res[i][j]=res[i][j]+mat[i][k]*listcopy[k][j]
    count=0
    
    if len(res)==2:
        for i in res:
            for j in [[1,0],[0,1]]:
                if i==j:
                    count=1
    elif len(res)==3:
        for i in res:
            for j in [[1,0,0],[0,1,0],[0,0,1]]:
                if i==j:
                    count=1

    if count:
        print("It is an ORTHOGONAL MATRIX")
    else:
        print("It is NOT AN ORTHOGONAL MATRIX")
                    
                
           
    
    
while True:
    choice=input("Enter your choice : \n1.ADD\n2.SUBTRACTION\n3.MULTIPLY\n4.TRANSPOSE\n5.INVERSE\n6.ORTHOGONAL\n7.EXIT\nEnter choice number : ")
    if choice in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-~`":
        print("\nINVALID INPUT, Please choose the numbers from the given option.\n")
    else:
        
        break
while True:
    if int(choice)==1:
        nos=int(input("\nADDITION\nENTER THE NUMBER OF MATRICES TO OPERATE ON (2 or 3): "))
        if nos not in [2,3]:
            print("INVALID INPUT ,The program only avails 2 or max 3 matrices to operate with.")
        else:
            add(nos)
            print("-----------------------------------------------------------------------------------------------------------")
            break
    if int(choice)==2:
        nos=int(input("\nSUBRACTION\nENTER THE NUMBER OF MATRICES TO OPERATE ON (2 or 3): "))
        if nos not in [2,3]:
            print("INVALID INPUT ,The program only avails 2 or max 3 matrices to operate with.")
        else:
            sub(nos)
            print("-----------------------------------------------------------------------------------------------------------")
            break
       
    if int(choice)==3:
        nos=int(input("\nMULTIPLY\nENTER THE NUMBER OF MATRICES TO OPERATE ON (2 or 3): "))
        if nos not in [2,3]:
            print("INVALID INPUT ,The program only avails 2 or max 3 matrices to operate with.")
        else:
            mul(nos)
            print("-----------------------------------------------------------------------------------------------------------")
            break
    if int(choice)==4:
        nos=int(input("\nTRANSPOSE\nENTER THE NUMBER OF MATRICES TO OPERATE ON (1 at a time): "))
        if nos not in [1]:
            print("INVALID INPUT ,The program finds transpose only for one matrix.")
        else:
            trans()
            print("-----------------------------------------------------------------------------------------------------------")
            break
    if int(choice)==5:
        nos=int(input("\nINVERSE\nENTER THE NUMBER OF MATRICES TO OPERATE ON (1 at a time): "))
        if nos not in [1]:
            print("INVALID INPUT ,The program finds transpose only for one matrix.")
        else:
            inv()
            print("-----------------------------------------------------------------------------------------------------------")
            break
    if int(choice)==6:
        nos=int(input("\nORTHOGONAL\nENTER THE NUMBER OF MATRICES TO OPERATE ON (1 at a time): "))
        if nos not in [1]:
            print("INVALID INPUT ,The program finds transpose only for one matrix.")
        else:
            ortho()
            print("-----------------------------------------------------------------------------------------------------------")
            break
        
    if int(choice)==7:
        print("-----------------------------------------------THANK YOU---------------------------------------------------")
        break
        
