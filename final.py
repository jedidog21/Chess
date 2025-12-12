from tkinter import *

root = Tk()

gameover = False
selectedList = []
turn = "white"
selectedPieces = []
inPassing = []
turnCounter = 1
move50 = 0
repeat3 = []


class Pawn:
    def __init__(self,space,moved,color):
        self.space=space
        self.moved=moved
        self.color=color
        self.image = None
        self.hidden = False
        self.b = Button()
        self.justMoved = False
        self.pRook = Button(root, image="", command = lambda: self.promotedPiece.promoteTo("rook"))
        self.pKnight = Button(root, image="", command = lambda: self.promotedPiece.promoteTo("knight"))
        self.pBishop = Button(root, image="", command = lambda: self.promotedPiece.promoteTo("bishop"))
        self.pQueen = Button(root, image="", command = lambda: self.promotedPiece.promoteTo("queen"))
        global selectedList
        global selectedPieces
        global board

    def getImage(self, c):
        if self.color == "black":
            if c == 'white':
                self.image = PhotoImage(file = "assests/blackpawn_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/blackpawn_black.png")
                self.b.configure(image=self.image)
            return self.image
        elif self.color == "white":
            if c == 'white':
                self.image = PhotoImage(file = "assests/whitepawn_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/whitepawn_black.png")
                self.b.configure(image=self.image)
            return self.image
        
    def getSpace(self):
        return str(self.space)

    def getColor(self):
        return self.color
    
    def changeSpace(self, ns):
        self.space = ns
    def hideButton(self):
        self.b.place_forget()
        
        self.hidden = True

    def isHidden(self):
        return self.hidden

    def createButton(self):
        self.b = Button(root, image=self.getImage(board[(int(self.space[0:1]))][(int(self.space[1:2]))]["color"]), command=lambda: select(selectedList,self))
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)
    
    def selected(self):
        if self.color == "black":
            self.image = PhotoImage(file = "assests/blackpawn_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        elif self.color == "white":
            self.image = PhotoImage(file = "assests/whitepawn_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        return self.image

    def move(self):
        moveTo=[]
        try:
            if self.color == "white":
                
                if isinstance(board[(int(self.space[1:2])-1)][(int(self.space[0:1]))]["piece"], Empty):
                    moveTo.append(str((int(self.space[1:2])-1))+str(int(self.space[0:1])))
                    if isinstance(board[(int(self.space[1:2])-2)][(int(self.space[0:1]))]["piece"], Empty) and self.moved == False:
                        if self.moved == False:
                            moveTo.append((str(int(self.space[1:2])-2))+str(int(self.space[0:1])))
                if not isinstance(board[(int(self.space[1:2])-1)][(int(self.space[0:1])-1)]["piece"], Empty) or (isinstance(board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"], Pawn) and board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"].justMoved) and board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"].color != self.color:
                    moveTo.append(str((int(self.space[1:2])-1))+str(int(self.space[0:1])-1))
                if not isinstance(board[(int(self.space[1:2])-1)][(int(self.space[0:1])+1)]["piece"], Empty) or (isinstance(board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"], Pawn) and board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"].justMoved) and board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"].color != self.color:
                    moveTo.append(str((int(self.space[1:2])-1))+str(int(self.space[0:1])+1))
            elif self.color == "black":
                if isinstance(board[(int(self.space[1:2])+1)][(int(self.space[0:1]))]["piece"], Empty):
                    moveTo.append(str((int(self.space[1:2])+1))+str(int(self.space[0:1])))
                    if isinstance(board[(int(self.space[1:2])+2)][(int(self.space[0:1]))]["piece"], Empty) and self.moved == False:
                        if self.moved == False:
                            moveTo.append((str(int(self.space[1:2])+2))+str(int(self.space[0:1])))
                if not isinstance(board[(int(self.space[1:2])+1)][(int(self.space[0:1])-1)]["piece"], Empty) or (isinstance(board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"], Pawn) and board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"].justMoved) and board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"].color != self.color:
                    moveTo.append(str((int(self.space[1:2])+1))+str(int(self.space[0:1])-1))
                if not isinstance(board[(int(self.space[1:2])+1)][(int(self.space[0:1])+1)]["piece"], Empty) or (isinstance(board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"], Pawn) and board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"].justMoved) and board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"].color != self.color:
                    moveTo.append(str((int(self.space[1:2])+1))+str(int(self.space[0:1])+1))
        except IndexError:
            pass
        except AttributeError:
            pass
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
    
    def capture(self):
        try:
            if self.color == "white":
                return [(str((int(self.space[1:2])-1))+str(int(self.space[0:1])-1)),(str((int(self.space[1:2])-1))+str(int(self.space[0:1])+1))]
            elif self.color == "black":
                return [(str((int(self.space[1:2])+1))+str(int(self.space[0:1])-1)),(str((int(self.space[1:2])+1))+str(int(self.space[0:1])+1))]
        except IndexError:
            pass
        except AttributeError:
            pass
                    

    
    def promote(self,l):
        self.promotedPiece = l[0]
        if self.color == "white" and isinstance(self, Pawn):
            if l[0].space[1:2] == "1":
                self.pRook.place(x=(141*8)+70, y=340)
                self.pKnight.place(x=(141*8)+70, y=480)
                self.pBishop.place(x=(141*8)+70, y=620)
                self.pQueen.place(x=(141*8)+70, y=760)
                self.pRookImage = (PhotoImage(file = "assests/whiterook_white.png"))
                self.pRook.configure(image=self.pRookImage)
                self.pKnightImage = (PhotoImage(file = "assests/whiteknight_black.png"))
                self.pKnight.configure(image=self.pKnightImage)
                self.pBishopImage = (PhotoImage(file = "assests/whitebishop_white.png"))
                self.pBishop.configure(image=self.pBishopImage)
                self.pQueenImage = (PhotoImage(file = "assests/whitequeen_black.png"))
                self.pQueen.configure(image=self.pQueenImage)
        elif self.color == "black" and isinstance(self, Pawn):
            if l[0].space[1:2] == "6":
                self.pRook.place(x=(141*8)+70, y=340)
                self.pKnight.place(x=(141*8)+70, y=480)
                self.pBishop.place(x=(141*8)+70, y=620)
                self.pQueen.place(x=(141*8)+70, y=760)
                self.pRookImage = (PhotoImage(file = "assests/blackrook_white.png"))
                self.pRook.configure(image=self.pRookImage)
                self.pKnightImage = (PhotoImage(file = "assests/blackknight_black.png"))
                self.pKnight.configure(image=self.pKnightImage)
                self.pBishopImage = (PhotoImage(file = "assests/blackbishop_white.png"))
                self.pBishop.configure(image=self.pBishopImage)
                self.pQueenImage = (PhotoImage(file = "assests/blackqueen_black.png"))
                self.pQueen.configure(image=self.pQueenImage)
        

    def promoteTo(self, p):
        if p == "rook":
            board[int(self.space[1:2])][int(self.space[0:1])]["piece"] = Rook(self.space, True, self.color)
        elif p == "knight":
            board[int(self.space[1:2])][int(self.space[0:1])]["piece"] = Knight(self.space, self.color)
        elif p == "bishop":
            board[int(self.space[1:2])][int(self.space[0:1])]["piece"] = Bishop(self.space, self.color)
        elif p == "queen":
            board[int(self.space[1:2])][int(self.space[0:1])]["piece"] = Queen(self.space, self.color)
        board[int(self.space[1:2])][int(self.space[0:1])]["piece"].createButton()
        self.pRook.place_forget()
        self.pKnight.place_forget()
        self.pBishop.place_forget()
        self.pQueen.place_forget()
        self.b.place_forget()
        for i in range(8):
            for c in range(8):
                if isinstance(board[i][c]["piece"], King):
                    board[i][c]["piece"].inCheck()
            

class Rook:
    def __init__(self,space,moved,color):
        self.space=space
        self.moved=moved
        self.color=color
        self.image = None
        self.hidden = False
        self.b = Button()
        global selectedList
        global selectedPieces
        global board

    def getImage(self, c):
        if self.color == "black":
            if c == 'white':
                self.image = PhotoImage(file = "assests/blackrook_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/blackrook_black.png")
                self.b.configure(image=self.image)
            return self.image
        elif self.color == "white":
            if c == 'white':
                self.image = PhotoImage(file = "assests/whiterook_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/whiterook_black.png")
                self.b.configure(image=self.image)
            return self.image

    def getSpace(self):
        return self.space

    def getColor(self):
        return self.color
    
    def changeSpace(self, ns):
        self.space = ns

    def hideButton(self):
        self.b.place_forget()
        
        self.hidden = True

    def isHidden(self):
        return self.hidden

    def createButton(self):
        self.b = Button(root, image=self.getImage(board[(int(self.space[0:1]))][(int(self.space[1:2]))]["color"]), command=lambda: select(selectedList,self))
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)
        
    def selected(self):
        if self.color == "black":
            self.image = PhotoImage(file = "assests/blackrook_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        elif self.color == "white":
            self.image = PhotoImage(file = "assests/whiterook_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        return self.image
    
    def move(self):
        moveTo=[]
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty) and int(self.space[0:1])+i < 8):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty) and int(self.space[0:1])+i < 8:
                    if board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i]["piece"], Empty) and int(self.space[0:1])-i >= 0):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i]["piece"], Empty) and int(self.space[0:1])-i >= 0:
                    if board[int(self.space[1:2])][int(self.space[0:1])-i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])+i < 8):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])+i < 8:
                    if board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])-i >= 0):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])-i >= 0:
                    if board[int(self.space[1:2])-i][int(self.space[0:1])]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
    
    def capture(self):
        moveTo=[]
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty) or isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i  in range(8):
            try:
                if isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i-1]["piece"], Empty) or isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i-1]["piece"], King):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i-1))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i-1]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i-1))
                    break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                    if i != 0:
                        break
            except IndexError:
                break
        for i  in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])-i-1)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])-i-1][int(self.space[0:1])]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])-i-1)+str(int(self.space[0:1])))
                    break
            except IndexError:
                break
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
            
class Knight:
    def __init__(self,space,color):
        self.space=space
        self.color=color
        self.image = None
        self.hidden = False
        self.b = Button()
        global selectedList
        global selectedPieces
        global board

    def getImage(self, c):
        if self.color == "black":
            if c == 'white':
                self.image = PhotoImage(file = "assests/blackknight_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/blackknight_black.png")
                self.b.configure(image=self.image)
            return self.image
        elif self.color == "white":
            if c == 'white':
                self.image = PhotoImage(file = "assests/whiteknight_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/whiteknight_black.png")
                self.b.configure(image=self.image)
            return self.image

    def getSpace(self):
        return self.space
    
    def getColor(self):
        return self.color
    
    def changeSpace(self, ns):
        self.space = ns

    def hideButton(self):
        self.b.place_forget()
        
        self.hidden = True

    def isHidden(self):
        return self.hidden
    
    def createButton(self):
        self.b = Button(root, image=self.getImage(board[(int(self.space[0:1]))][(int(self.space[1:2]))]["color"]), command=lambda: select(selectedList,self))
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)
        
    def selected(self):
        if self.color == "black":
            self.image = PhotoImage(file = "assests/blackknight_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        elif self.color == "white":
            self.image = PhotoImage(file = "assests/whiteknight_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        return self.image

    def move(self):
        moveTo = []
        try:
            if isinstance(board[int(self.space[1:2])+2][int(self.space[0:1])+1]["piece"], Empty) or board[int(self.space[1:2])+2][int(self.space[0:1])+1]["piece"].color != self.color and not (int(self.space[1:2])+2 >= 8 or int(self.space[0:1])+1 >= 8):
                moveTo.append(str(int(self.space[1:2])+2)+str(int(self.space[0:1])+1))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])+1][int(self.space[0:1])+2]["piece"], Empty) or board[int(self.space[1:2])+1][int(self.space[0:1])+2]["piece"].color != self.color and not (int(self.space[1:2])+1 >= 8 or int(self.space[0:1])+2 >= 8):
                moveTo.append(str(int(self.space[1:2])+1)+str(int(self.space[0:1])+2))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])-2][int(self.space[0:1])-1]["piece"], Empty) or board[int(self.space[1:2])-2][int(self.space[0:1])-1]["piece"].color != self.color and not (int(self.space[1:2])-2 < 0 or int(self.space[0:1])-1 < 0):
                moveTo.append(str(int(self.space[1:2])-2)+str(int(self.space[0:1])-1))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])-1][int(self.space[0:1])-2]["piece"], Empty) or board[int(self.space[1:2])-1][int(self.space[0:1])-2]["piece"].color != self.color and not (int(self.space[1:2])-1 < 0 or int(self.space[0:1])-2 < 0):
                moveTo.append(str(int(self.space[1:2])-1)+str(int(self.space[0:1])-2))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])+2][int(self.space[0:1])-1]["piece"], Empty) or board[int(self.space[1:2])+2][int(self.space[0:1])-1]["piece"].color != self.color and not (int(self.space[1:2])+2 >= 8 or int(self.space[0:1])-1 < 0):
                moveTo.append(str(int(self.space[1:2])+2)+str(int(self.space[0:1])-1))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])+1][int(self.space[0:1])-2]["piece"], Empty) or board[int(self.space[1:2])+1][int(self.space[0:1])-2]["piece"].color != self.color and not (int(self.space[1:2])+1 >= 8 or int(self.space[0:1])-2 < 0):
                moveTo.append(str(int(self.space[1:2])+1)+str(int(self.space[0:1])-2))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])-2][int(self.space[0:1])+1]["piece"], Empty) or board[int(self.space[1:2])-2][int(self.space[0:1])+1]["piece"].color != self.color and not (int(self.space[1:2])-2 < 0 or int(self.space[0:1])+1 >= 8):
                moveTo.append(str(int(self.space[1:2])-2)+str(int(self.space[0:1])+1))
        except IndexError:
            pass
        try:
            if isinstance(board[int(self.space[1:2])-1][int(self.space[0:1])+2]["piece"], Empty) or board[int(self.space[1:2])-1][int(self.space[0:1])+2]["piece"].color != self.color and not (int(self.space[1:2])-1 < 0 or int(self.space[0:1])+2 >= 8):
                moveTo.append(str(int(self.space[1:2])-1)+str(int(self.space[0:1])+2))
        except IndexError:
            pass

        return moveTo
            
class Bishop:
    def __init__(self,space,color):
        self.space=space
        self.color=color
        self.image = None
        self.hidden = False
        self.b = Button()
        global selectedList
        global selectedPieces
        global board
    
    def getImage(self, c):
        if self.color == "black":
            if c == 'white':
                self.image = PhotoImage(file = "assests/blackbishop_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/blackbishop_black.png")
                self.b.configure(image=self.image)
            return self.image
        elif self.color == "white":
            if c == 'white':
                self.image = PhotoImage(file = "assests/whitebishop_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/whitebishop_black.png")
                self.b.configure(image=self.image)
            return self.image
        
    def getSpace(self):
        return self.space
    
    def getColor(self):
        return self.color

    def changeSpace(self, ns):
        self.space = ns

    def hideButton(self):
        self.b.place_forget()
        
        self.hidden = True

    def isHidden(self):
        return self.hidden
    
    def createButton(self):
        self.b = Button(root, image=self.getImage(board[(int(self.space[0:1]))][(int(self.space[1:2]))]["color"]), command=lambda: select(selectedList,self))
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)

    def selected(self):
        if self.color == "black":
            self.image = PhotoImage(file = "assests/blackbishop_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        elif self.color == "white":
            self.image = PhotoImage(file = "assests/whitebishop_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        return self.image
    
    def move(self):
        moveTo=[]
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[0:1])+i < 8 and int(self.space[1:2])+i < 8)):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[0:1])+i < 8 and int(self.space[1:2])+i < 8):
                    if board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[0:1])-i >= 0 and int(self.space[1:2])+i < 8)):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[0:1])-i >= 0 and int(self.space[1:2])+i < 8):
                    if board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int(self.space[0:1])+i < 8)):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int(self.space[0:1])+i < 8):
                    if board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int (self.space[0:1])-i >= 0)):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int (self.space[0:1])-i >= 0):
                    if board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
    
    def capture(self):
        moveTo=[]
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty) or isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty) or isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
            
class Queen:
    def __init__(self,space,color):
        self.space=space
        self.color=color
        self.image = None
        self.hidden = False
        self.b = Button()
        global selectedList
        global selectedPieces
        global board
    
    def getImage(self, c):
        if self.color == "black":
            if c == 'white':
                self.image = PhotoImage(file = "assests/blackqueen_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/blackqueen_black.png")
                self.b.configure(image=self.image)
            return self.image
        elif self.color == "white":
            if c == 'white':
                self.image = PhotoImage(file = "assests/whitequeen_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/whitequeen_black.png")
                self.b.configure(image=self.image)
            return self.image
        
    def getSpace(self):
        return self.space

    def getColor(self):
        return self.color
    
    def changeSpace(self, ns):
        self.space = ns
    
    def hideButton(self):
        self.b.place_forget()
        
        self.hidden = True

    def isHidden(self):
        return self.hidden

    def createButton(self):
        self.b = Button(root, image=self.getImage(board[(int(self.space[0:1]))][(int(self.space[1:2]))]["color"]), command=lambda: select(selectedList,self))
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)

    def selected(self):
        if self.color == "black":
            self.image = PhotoImage(file = "assests/blackqueen_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        elif self.color == "white":
            self.image = PhotoImage(file = "assests/whitequeen_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        return self.image
    
    def move(self):
        moveTo=[]
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty) and int(self.space[0:1])+i < 8):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty) and int(self.space[0:1])+i < 8:
                    if board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i]["piece"], Empty) and int(self.space[0:1])-i >= 0):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i]["piece"], Empty) and int(self.space[0:1])-i >= 0:
                    if board[int(self.space[1:2])][int(self.space[0:1])-i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])+i < 8):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])+i < 8:
                    if board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])-i >= 0):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])]["piece"], Empty) and int(self.space[1:2])-i >= 0:
                    if board[int(self.space[1:2])-i][int(self.space[0:1])]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass


        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[0:1])+i < 8 and int(self.space[1:2])+i < 8)):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[0:1])+i < 8 and int(self.space[1:2])+i < 8):
                    if board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[0:1])-i >= 0 and int(self.space[1:2])+i < 8)):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[0:1])-i >= 0 and int(self.space[1:2])+i < 8):
                    if board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int(self.space[0:1])+i < 8)):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int(self.space[0:1])+i < 8):
                    if board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        for i  in range(8):
            try:
                if (isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int (self.space[0:1])-i >= 0)):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty) and (int(self.space[1:2])-i >= 0 and int (self.space[0:1])-i >= 0):
                    if board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"].color == self.color and i != 0:
                        break
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
            except AttributeError:
                pass
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
    
    def capture(self):
        moveTo=[]
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty) or isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])+i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i  in range(8):
            try:
                if isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i-1]["piece"], Empty) or isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i-1]["piece"], King):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i-1))
                elif not isinstance(board[int(self.space[1:2])][int(self.space[0:1])-i-1]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-i-1))
                    break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])))
                    if i != 0:
                        break
            except IndexError:
                break
        for i  in range(8):
            try:
                if isinstance(board[int(self.space[1:2])-i-1][int(self.space[0:1])]["piece"], Empty) or isinstance(board[int(self.space[1:2])-i-1][int(self.space[0:1])]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])-i-1)+str(int(self.space[0:1])))
                elif not isinstance(board[int(self.space[1:2])-i-1][int(self.space[0:1])]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])-i-1)+str(int(self.space[0:1])))
                    break
            except IndexError:
                break


        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])+i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty) or isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])+i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])+i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty) or isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])+i][int(self.space[0:1])-i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])+i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
        for i in range(8):
            try:
                if isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty) or isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], King):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                elif not isinstance(board[int(self.space[1:2])-i][int(self.space[0:1])-i]["piece"], Empty):
                    moveTo.append(str(int(self.space[1:2])-i)+str(int(self.space[0:1])-i))
                    if i != 0:
                        break
            except IndexError:
                break
        while self.space[1:2]+self.space[0:1] in moveTo:
            moveTo.remove(self.space[1:2]+self.space[0:1])
        return moveTo
        
            
class King:
    def __init__(self,space,moved,color):
        self.space=space
        self.moved=moved
        self.color=color
        self.image = None
        self.hidden = False
        self.b = Button()
        self.checkSquare = []
        self.kingCheck = False
        global selectedList
        global selectedPieces
        global castle
        global board
    
    def getImage(self, c):
        if self.color == "black":
            if c == 'white':
                self.image = PhotoImage(file = "assests/blackking_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/blackking_black.png")
                self.b.configure(image=self.image)
        elif self.color == "white":
            if c == 'white':
                self.image = PhotoImage(file = "assests/whiteking_white.png")
                self.b.configure(image=self.image)
            elif c == 'black':
                self.image = PhotoImage(file = "assests/whiteking_black.png")
                self.b.configure(image=self.image)
            return self.image
        
    def getSpace(self):
        return self.space
    
    def getColor(self):
        return self.color
    
    def changeSpace(self, ns):
        self.space = ns

    def hideButton(self):
        self.b.place_forget()
        
        self.hidden = True

    def isHidden(self):
        return self.hidden

    def createButton(self):
        self.b = Button(root, image=self.getImage(board[(int(self.space[0:1]))][(int(self.space[1:2]))]["color"]), command=lambda: select(selectedList,self))
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)
        self.b.configure(image=self.image)

    def selected(self):
        self.check()
        if self.color == "black":
            self.image = PhotoImage(file = "assests/blackking_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        elif self.color == "white":
            self.image = PhotoImage(file = "assests/whiteking_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
        return self.image
    
    def move(self):
        global castle
        moveTo = []
        self.i = ""
        self.noMove = 0
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2])+1)+str(int(self.space[0:1])+1) in self.i) or int(self.space[1:2])+1 > 7 or int(self.space[0:1])+1 > 7 or (not isinstance(board[(int(self.space[1:2])+1)][(int(self.space[0:1])+1)]["piece"], Empty) and board[(int(self.space[1:2])+1)][(int(self.space[0:1])+1)]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2])+1)+str(int(self.space[0:1])+1))
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2])-1)+str(int(self.space[0:1])+1) in self.i) or int(self.space[1:2])-1 < 0 or int(self.space[0:1])+1 > 7 or (not isinstance(board[(int(self.space[1:2])-1)][(int(self.space[0:1])+1)]["piece"], Empty) and board[(int(self.space[1:2])-1)][(int(self.space[0:1])+1)]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2])-1)+str(int(self.space[0:1])+1))
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2])+1)+str(int(self.space[0:1])-1) in self.i) or int(self.space[1:2])+1 > 7 or int(self.space[0:1])-1 < 0 or (not isinstance(board[(int(self.space[1:2])+1)][(int(self.space[0:1])-1)]["piece"], Empty) and board[(int(self.space[1:2])+1)][(int(self.space[0:1])-1)]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2])+1)+str(int(self.space[0:1])-1))
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2])+1)+str(int(self.space[0:1])) in self.i) or int(self.space[1:2])+1 > 7 or (not isinstance(board[(int(self.space[1:2])+1)][(int(self.space[0:1]))]["piece"], Empty) and board[(int(self.space[1:2])+1)][(int(self.space[0:1]))]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2])+1)+str(int(self.space[0:1])))
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2]))+str(int(self.space[0:1])+1) in self.i) or int(self.space[0:1])+1 > 7 or (not isinstance(board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"], Empty) and board[(int(self.space[1:2]))][(int(self.space[0:1])+1)]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+1))
            try:
                if (self.color == "white" and self.space[1:2] == "0") or (self.color == "black" and self.space[1:2] == "7") or (str(int(self.space[1:2]))+str(int(self.space[0:1])+2) in self.i):
                    if (isinstance(board[int(self.space[1:2])][int(self.space[0:1])+2]["piece"], Empty) and isinstance(board[int(self.space[1:2])][int(self.space[0:1])+3]["piece"], Rook)):
                        if board[int(self.space[1:2])][int(self.space[0:1])+3]["piece"].moved == False and self.moved == False:
                            moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])+2))
            except IndexError:
                pass
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2])-1)+str(int(self.space[0:1])) in self.i) or int(self.space[1:2])-1 < 0 or (not isinstance(board[(int(self.space[1:2])-1)][(int(self.space[0:1]))]["piece"], Empty) and board[(int(self.space[1:2])-1)][(int(self.space[0:1]))]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2])-1)+str(int(self.space[0:1])))
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2]))+str(int(self.space[0:1])-1) in self.i) or int(self.space[0:1])-1 < 0 or (not isinstance(board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"], Empty) and board[(int(self.space[1:2]))][(int(self.space[0:1])-1)]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-1))
            try:
                if (self.color == "white" and self.space[1:2] == "0") or (self.color == "black" and self.space[1:2] == "7") or (str(int(self.space[1:2]))+str(int(self.space[0:1])-2) in self.i):
                    if (isinstance(board[int(self.space[1:2])][int(self.space[0:1])-2]["piece"], Empty) and isinstance(board[int(self.space[1:2])][int(self.space[0:1])-3]["piece"], Empty) and isinstance(board[int(self.space[1:2])][int(self.space[0:1])-4]["piece"], Rook)):
                        if board[int(self.space[1:2])][int(self.space[0:1])+3]["piece"].moved == False and self.moved == False:
                            moveTo.append(str(int(self.space[1:2]))+str(int(self.space[0:1])-2))
            except IndexError:
                pass
        for self.i in self.checkSquare:
            if (str(int(self.space[1:2])-1)+str(int(self.space[0:1])-1) in self.i) or int(self.space[1:2])-1 < 0 or int(self.space[0:1])-1 < 0 or (not isinstance(board[(int(self.space[1:2])-1)][(int(self.space[0:1])-1)]["piece"], Empty) and board[(int(self.space[1:2])-1)][(int(self.space[0:1])-1)]["piece"].color == self.color):
                self.noMove += 1
                break
        else:
            moveTo.append(str(int(self.space[1:2])-1)+str(int(self.space[0:1])-1))
        #Add for to not castle through check
        
        
        return moveTo
    def inCheck(self):
        noSquare = self.check()
        for i in noSquare:
            if self.space[1:2]+self.space[0:1] in i:
                if self.color == "black":
                    self.image = PhotoImage(file = "assests/blackking_check.png")
                    self.b.configure(image=self.image)
                    self.kingCheck = True
                    break
                elif self.color == "white":
                    self.image = PhotoImage(file = "assests/whiteking_check.png")
                    self.b.configure(image=self.image)
                    self.kingCheck = True
                    break
            else:
                self.getImage(self.space)
                self.kingCheck = False

    def check(self):
        self.checkSquare = []
        for i in range(8):
            for c in range(8):
                if not isinstance(board[i][c]["piece"], Empty) and not board[i][c]["piece"].color == self.color:
                    try:
                        self.checkSquare.append(board[i][c]["piece"].capture())
                        if board[i][c]["piece"].space in self.checkSquare[-1]:
                            self.checkSquare[-1].remove(board[i][c]["piece"].space)

                    except AttributeError:
                        self.checkSquare.append(board[i][c]["piece"].move())
                        if board[i][c]["piece"].space in self.checkSquare[-1]:
                            self.checkSquare[-1].remove(board[i][c]["piece"].space)
        return self.checkSquare
            
        
class Empty:
    def __init__(self,space):
        self.space = space
        self.b = Button()
        self.selectedSquare = False
        global allMoves
        global selectedList
        global turn
        global selectedPieces
        global board
        global move50
        global repeat3

    def getImage(self,c):
        if c == "black":
            self.image = PhotoImage(file = "assests/blacksquare.png")
            self.b.configure(image=self.image)
            self.selectedSquare = False
        elif c == "white":
            self.image = PhotoImage(file = "assests/whitesquare.png")
            self.b.configure(image=self.image)
            self.selectedSquare = False
        return self.image

    def getSpace(self):
        return self.space
    
    def changeSpace(self, ns):
        self.space = ns

    def getColor(self):
        return board[int(self.space[0:1])][int(self.space[1:2])]["color"]

    def createButton(self):
        self.b = Button(root, image=self.getImage(board[int(self.space[0:1])][int(self.space[1:2])]["color"]),command = lambda: self.move())
        self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)

    def selected(self, c):
        if c == "black":
            self.image = PhotoImage(file = "assests/blacksquare_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
            self.selectedSquare = True
        elif c == "white":
            self.image = PhotoImage(file = "assests/whitesquare_select.png")
            self.b.configure(image=self.image)
            selectedList.append(self)
            self.selectedSquare = True
        return self.image
    
    def move(self):
        global board
        global selectedPieces
        global inPassing
        global turnCounter
        global moveCounter
        global move50
        global repeat3
        global allMoves
        newBoard = board
        if self.selectedSquare:
            
            global turn
            tempSpace = self.space
            temp = selectedList[0].getSpace()
            selectedList[0].changeSpace(tempSpace)
            self.changeSpace(temp)
            try:
                selectedList[0].promote(selectedList)
            except AttributeError:
                pass
            tempSquare = newBoard[int(tempSpace[1:2])][int(tempSpace[0:1])]["piece"]
            newBoard[int(tempSpace[1:2])][int(tempSpace[0:1])]["piece"] = newBoard[int(temp[1:2])][int(temp[0:1])]["piece"]
            newBoard[int(temp[1:2])][int(temp[0:1])]["piece"] = tempSquare
            selectedList[0].b.place(x=int(selectedList[0].getSpace()[0:1])*140,y=int(selectedList[0].getSpace()[1:2])*140)
            self.b.place(x=((int(self.space[0:1])))*140,y=((int(self.space[1:2])))*140)
            selectedList[0].changeSpace(tempSpace)
            if isinstance(selectedList[0], Pawn):
                move50 = 0
            self.changeSpace(temp)
            if len(inPassing) >= 2:
                inPassing[0].justMoved = False
                inPassing.remove(inPassing[0])
            board = newBoard
            temp = selectedList[0].getSpace()
            try:
                if (selectedList[0].color == "white" and selectedList[0].space[1:2] == "0") or (selectedList[0].color == "black" and selectedList[0].space[1:2] == "7"):
                    if isinstance(selectedList[0], King) and isinstance(board[int(temp[1:2])][int(temp[0:1])+1]["piece"], Rook):
                        tempSquare = board[int(temp[1:2])][int(temp[0:1])-1]["piece"]
                        board[int(temp[1:2])][int(temp[0:1])-1]["piece"] = board[int(temp[1:2])][int(temp[0:1])+1]["piece"]
                        board[int(temp[1:2])][int(temp[0:1])+1]["piece"] = tempSquare
                        board[int(temp[1:2])][int(temp[0:1])-1]["piece"].b.place(x=(int(temp[0:1])-1)*140,y=int(selectedList[0].getSpace()[1:2])*140)
                        board[int(temp[1:2])][int(temp[0:1])+1]["piece"].b.place(x=((int(temp[0:1]))+1)*140,y=((int(self.space[1:2])))*140)
                        board[int(temp[1:2])][int(temp[0:1])-1]["piece"].changeSpace(str(int(temp[0:1])-1)+str(int(temp[1:2])))
                        board[int(temp[1:2])][int(temp[0:1])+1]["piece"].changeSpace(str(int(temp[0:1])+1)+str(int(temp[1:2])))
                    elif isinstance(selectedList[0], King) and isinstance(board[int(temp[1:2])][int(temp[0:1])-2]["piece"], Rook):
                        tempSquare = board[int(temp[1:2])][int(temp[0:1])+1]["piece"]
                        board[int(temp[1:2])][int(temp[0:1])+1]["piece"] = board[int(temp[1:2])][int(temp[0:1])-2]["piece"]
                        board[int(temp[1:2])][int(temp[0:1])-2]["piece"] = tempSquare
                        board[int(temp[1:2])][int(temp[0:1])+1]["piece"].b.place(x=(int(temp[0:1])+1)*140,y=int(selectedList[0].getSpace()[1:2])*140)
                        board[int(temp[1:2])][int(temp[0:1])-2]["piece"].b.place(x=((int(temp[0:1]))-2)*140,y=((int(self.space[1:2])))*140)
                        board[int(temp[1:2])][int(temp[0:1])+1]["piece"].changeSpace(str(int(temp[0:1])+1)+str(int(temp[1:2])))
                        board[int(temp[1:2])][int(temp[0:1])-2]["piece"].changeSpace(str(int(temp[0:1])-2)+str(int(temp[1:2])))
            except IndexError:
                pass


            temp = selectedList[0].getSpace()
            try:
                if selectedList[0].color == "white" and isinstance(board[int(temp[1:2])][int(temp[0:1])]["piece"], Pawn) and isinstance(board[int(temp[1:2])+1][int(temp[0:1])]["piece"], Pawn):                    
                    takenPiece = board[int(temp[1:2])+1][int(temp[0:1])]["piece"]
                    board[int(temp[1:2])+1][int(temp[0:1])]["piece"] = Empty(str(int(temp[0:1]))+str(int(temp[1:2])+1))
                    board[int(temp[1:2])+1][int(temp[0:1])]["piece"].createButton()
                    takenPiece.b.place_forget()
                elif selectedList[0].color == "black" and isinstance(board[int(temp[1:2])][int(temp[0:1])]["piece"], Pawn) and isinstance(board[int(temp[1:2])-1][int(temp[0:1])]["piece"], Pawn):
                    takenPiece = board[int(temp[1:2])-1][int(temp[0:1])]["piece"]
                    board[int(temp[1:2])-1][int(temp[0:1])]["piece"] = Empty(str(int(temp[0:1]))+str(int(temp[1:2])-1))
                    board[int(temp[1:2])-1][int(temp[0:1])]["piece"].createButton()
                    takenPiece.b.place_forget()
            except IndexError:
                pass

            while len(selectedList) > 0:
                selectedList[0].getImage(board[int(selectedList[0].getSpace()[1:2])][int(selectedList[0].getSpace()[0:1])]["color"])
                if isinstance(selectedList[0], Empty):
                    self.selectedSquare = False
                try:
                    if inPassing[0].color == turn:
                        inPassing[0].justMoved = False
                except AttributeError:
                    pass
                except IndexError:
                    pass
                selectedList.remove(selectedList[0])
                try:
                    if selectedList[0].moved == False and not isinstance(selectedList[0], Pawn):
                        selectedList[0].moved = True
                    elif isinstance(selectedList[0], Pawn):                        
                        if selectedList[0].moved == False and selectedList[0].justMoved == False:
                            selectedList[0].moved = True
                            selectedList[0].justMoved = True
                            inPassing.append(selectedList[0])
                        elif selectedList[0].move == True or selectedList[0].justMoved == True:
                            selectedList[0].moved = True
                            selectedList[0].justMoved = False
                except AttributeError:
                    pass
                except IndexError:
                    pass
                
            if turn == "white":
                turn = "black"
                move50 += .5

            elif turn == "black":
                turn = "white"
                turnCounter += 1
                move50 += .5
            if move50 >= 49:
                draw("50 move rule")

            for i in range(8):
                for c in range(8):
                    if isinstance(board[i][c]["piece"], King):
                        board[i][c]["piece"].inCheck()      
            moveCounter.config(text = f"It is {turn}'s turn\nTurn: {turnCounter}")
            countPieces()      

        else:
            while len(selectedList) > 0:
                selectedList[0].getImage(board[int(selectedList[0].getSpace()[1:2])][int(selectedList[0].getSpace()[0:1])]["color"])
                if isinstance(selectedList[0], Empty):
                    self.selectedSquare = False
                selectedList.remove(selectedList[0])
            for i in range(8):
                for c in range(8):
                    if isinstance(board[i][c]["piece"], King):
                        board[i][c]["piece"].inCheck()
            
        selectedPieces = []
                

def select(l,s):
    if not gameover:
        l.append(s)
        global selectedPieces
        global turn
        global board
        for i in range(8):
            for c in range(8):
                if isinstance(board[i][c]["piece"], King):
                    board[i][c]["piece"].inCheck()
        if l[-1] in selectedPieces:
            take(l)
        else:
            while len(l) > 1:
                l[0].getImage(board[int(l[0].getSpace()[1:2])][int(l[0].getSpace()[0:1])]["color"])
                l.remove(l[0])
            selectedPieces = []
            if (turn == "white" and l[0].color == "white") or (turn == "black" and l[0].color == "black"):
                l = [l[0]]
                l[0].selected()
                m = l[0].move()
                for i in range(len(m)):
                    try:
                        if not l[0].isHidden():
                            if isinstance(board[int(m[i][0:1])][int(m[i][1:2])]["piece"], Empty):
                                board[int(m[i][0:1])][int(m[i][1:2])]["piece"].selected(board[int(m[i][0:1])][int(m[i][1:2])]["color"])
                            elif not isinstance(board[int(m[i][0:1])][int(m[i][1:2])]["piece"], Empty):
                                if not board[int(m[i][0:1])][int(m[i][1:2])]["piece"].getColor() == l[0].getColor():
                                    board[int(m[i][0:1])][int(m[i][1:2])]["piece"].selected()
                                    selectedPieces.append(board[int(m[i][0:1])][int(m[i][1:2])]["piece"])

                    except IndexError:
                        pass
                    except ValueError:
                        pass
        

def take(l):
    global selectedPieces
    global turn
    global moveCounter
    global turnCounter
    global move50
    global repeat3
    global allMoves

    takeSquare = l[-1]
    takingSquare = l[0]
    if len(selectedPieces) >= 1:
        try:
            takingSquare.promote(selectedList)
        except AttributeError:
            pass
        tempSpace = takingSquare.space
        temp = takeSquare.getSpace()
        takenPiece = board[int(temp[1:2])][int(temp[0:1])]["piece"]
        board[int(temp[1:2])][int(temp[0:1])]["piece"] = takingSquare
        board[int(tempSpace[1:2])][int(tempSpace[0:1])]["piece"] = Empty(tempSpace[1:2]+tempSpace[0:1])
        board[int(tempSpace[1:2])][int(tempSpace[0:1])]["piece"].createButton()
        board[int(temp[1:2])][int(temp[0:1])]["piece"].changeSpace(temp)
        board[int(tempSpace[1:2])][int(tempSpace[0:1])]["piece"].changeSpace(tempSpace)
        board[int(temp[1:2])][int(temp[0:1])]["piece"].b.place(x=int(temp[0:1])*140,y=int(temp[1:2])*140)
        board[int(tempSpace[1:2])][int(tempSpace[0:1])]["piece"].b.place(x=int(tempSpace[0:1])*140,y=int(tempSpace[1:2])*140)
        board[int(temp[1:2])][int(temp[0:1])]["piece"].moved = True
        board[int(temp[1:2])][int(temp[0:1])]["piece"].justMoved = False
        takenPiece.b.place_forget()
        move50 = 0
        i = 0
        if turn == "white":
            turn = "black"
        elif turn == "black":
            turn = "white"
            turnCounter += 1
                    
        moveCounter.config(text = f"It is {turn}'s turn\nTurn: {turnCounter}")
        countPieces()
        while len(selectedPieces) >= 1:
            selectedPieces = []
        while len(l) > 1:
            l[0].getImage(board[int(l[0].getSpace()[1:2])][int(l[0].getSpace()[0:1])]["color"])
            l.remove(l[0])
        try:
            takingSquare.moved = True
        except AttributeError:
            pass

def countPieces():
    for i in range(8):
        for c in range(8):
            if isinstance(board[i][c]["piece"], King):
                board[i][c]["piece"].inCheck()
    repeat3 = {}
    pieceLeft = []
    i = 0
    for r in range(8):
        for c in range(8):
            if not isinstance(board[r][c]["piece"], Empty):
                repeat3.update({str(type(board[r][c]["piece"]))+str(i):[board[r][c]["piece"].color, int(board[r][c]["piece"].space)]})
                pieceLeft.append(type(board[r][c]["piece"]))
                i += 1
    if allMoves.count(repeat3) >= 2:
        draw("repitition")
        return
    else:
        allMoves.append(repeat3)

    countPawn = pieceLeft.count(cPawn)
    countRook = pieceLeft.count(cRook)
    countKnight = pieceLeft.count(cKnight)
    countBishop = pieceLeft.count(cBishop)
    countQueen = pieceLeft.count(cQueen)
    countKing = pieceLeft.count(cKing)
    print(cKing,countKing, pieceLeft)
    if countKing >= 2:
        if countPawn <= 0:
            if countRook <= 0 and countQueen <= 0:
                if (countBishop == 1 and countKnight == 0) or (countBishop == 0 and countKnight == 1) or (countBishop == 0 and countKnight == 0):
                    draw("Insufficient material")
                    return
    else:
        for i in range(8):
            for c in range(8):
                if isinstance(board[i][c]["piece"], King):
                    if board[i][c]["piece"].color == "black":
                        checkmate("black")
                        return
                    else:
                        checkmate("white")
                        return
                    
    for i in range(8):
        for c in range(8):
            if isinstance(board[i][c]["piece"], King):
                if board[i][c]["piece"].kingCheck == False and board[i][c]["piece"].noMove >= 8:
                    for h in repeat3.values():
                        if h[0] == board[i][c]["piece"].color:
                            print(len(board[int(h[1]%10)][int(h[1]//10)]["piece"].move()))
                            if len(board[int(h[1]%10)][int(h[1]//10)]["piece"].move()) > 0:
                                break
                    else:
                        draw("Stalemate")

def draw(drawType):
    global gameover
    global moveCounter
    print(drawType)
    moveCounter.config(text = f"Draw by\n{drawType}")
    gameover = True

def checkmate(winner):
    global gameover
    global moveCounter
    print(winner + " wins")
    moveCounter.config(text = f"{winner.title()}\nwins by checkmate")
    gameover = True


root.title("Chess Board")
root.maxsize(1500, 140*8+1)
root.minsize(1500, 140*8)
canvas = Canvas(root, width=1500,height=140*8,bg="#2E2E2E")
moveCounter = Label(root, bg = "#2E2E2E", bd = 0, font = ("Arial", 24), fg = "white", text = f"It is {turn}'s turn\nTurn: {turnCounter}", anchor = "center")
moveCounter.place(x=(141*8)+70,y=1)
board = [[{"color":"white","piece":Rook("00",False,"black")},{"color":"black","piece":Knight("10","black")},{"color":"white","piece":Bishop("20","black")},{"color":"black","piece":Queen("30","black")},{"color":"white","piece":King("40",False,"black")},{"color":"black","piece":Bishop("50","black")},{"color":"white","piece":Knight("60","black")},{"color":"black","piece":Rook("70",False,"black")}],
        [{"color":"black","piece":Pawn("01",False,"black")},{"color":"white","piece":Pawn("11",False,"black")},{"color":"black","piece":Pawn("21",False,"black")},{"color":"white","piece":Pawn("31",False,"black")},{"color":"black","piece":Pawn("41",False,"black")},{"color":"white","piece":Pawn("51",False,"black")},{"color":"black","piece":Pawn("61",False,"black")},{"color":"white","piece":Pawn("71",False,"black")}],
        [{"color":"white","piece":Empty("02")},{"color":"black","piece":Empty("12")},{"color":"white","piece":Empty("22")},{"color":"black","piece":Empty("32")},{"color":"white","piece":Empty("42")},{"color":"black","piece":Empty("52")},{"color":"white","piece":Empty("62")},{"color":"black","piece":Empty("72")}],
        [{"color":"black","piece":Empty("03")},{"color":"white","piece":Empty("13")},{"color":"black","piece":Empty("23")},{"color":"white","piece":Empty("33")},{"color":"black","piece":Empty("43")},{"color":"white","piece":Empty("53")},{"color":"black","piece":Empty("63")},{"color":"white","piece":Empty("73")}],
        [{"color":"white","piece":Empty("04")},{"color":"black","piece":Empty("14")},{"color":"white","piece":Empty("24")},{"color":"black","piece":Empty("34")},{"color":"white","piece":Empty("44")},{"color":"black","piece":Empty("54")},{"color":"white","piece":Empty("64")},{"color":"black","piece":Empty("74")}],
        [{"color":"black","piece":Empty("05")},{"color":"white","piece":Empty("15")},{"color":"black","piece":Empty("25")},{"color":"white","piece":Empty("35")},{"color":"black","piece":Empty("45")},{"color":"white","piece":Empty("55")},{"color":"black","piece":Empty("65")},{"color":"white","piece":Empty("75")}],
        [{"color":"white","piece":Pawn("06",False,"white")},{"color":"black","piece":Pawn("16",False,"white")},{"color":"white","piece":Pawn("26",False,"white")},{"color":"black","piece":Pawn("36",False,"white")},{"color":"white","piece":Pawn("46",False,"white")},{"color":"black","piece":Pawn("56",False,"white")},{"color":"white","piece":Pawn("66",False,"white")},{"color":"black","piece":Pawn("76",False,"white")}],
        [{"color":"black","piece":Rook("07",False,"white")},{"color":"white","piece":Knight("17","white")},{"color":"black","piece":Bishop("27","white")},{"color":"white","piece":Queen("37","white")},{"color":"black","piece":King("47",False,"white")},{"color":"white","piece":Bishop("57","white")},{"color":"black","piece":Knight("67","white")},{"color":"white","piece":Rook("77",False,"white")}]]
canvas.pack()
for r in range(8):
    for c in range(8):
        board[r][c]["piece"].createButton()
allMoves = [board]

cPawn = type(board[1][0]["piece"])
cRook = type(board[0][0]["piece"])
cKnight = type(board[0][1]["piece"])
cBishop = type(board[0][2]["piece"])
cQueen = type(board[0][3]["piece"])
cKing = type(board[0][4]["piece"])


root.mainloop()