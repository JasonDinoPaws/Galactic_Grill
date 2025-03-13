csvpath = "".join(x+"/" for x in __file__.split("/")[:-1])+"Menu.csv"
class Menu:
    def __init__(self):
        self.items = []
        self.itempos = ["price","name","type","description"]

        with open(csvpath,"r") as csv:
            for x in csv.readlines()[1:]:
                s = x.strip().split(",")
                self.AddItem(float(s[0]),s[1],s[2],s[3])
        pass

    def SaveMenu(self):
        with open(csvpath,"w") as csv:
            for p,i,t,d in self.items:
                line = f"{p},{i},{t},\"{d}\"\n"
                csv.write(line)

    def GetItemPos(self,name:str):
        for x in range(len(self.items)):
            if self.items[x][1] == name:
                return x
        return -1


    def AddItem(self,price:float,name:str,type:str,description:str):
        if self.GetItemPos(name) == -1:
            self.items.append([int(price),name,type,description])
            print(f"added {name}")
        else:
            print(f"Can't add {name}, already in system")

    def RemoveItem(self,name:str):
        pos = self.GetItemPos(name)
        if pos != -1:
            self.items.pop(pos)
            print(f"removed {name}")
        else:
            print(f"{name} not in menu")
    
    def EditItem(self,name:str,props:dict):
        pos = self.GetItemPos(name)
        if pos != -1:
            for p in props.keys():
                if p in self.itempos:
                    self.items[pos][self.itempos.index(p)] = props[p]
    
            print(f"Edited {name}")
        else:
            print(f"{name} not in menu")
    
    def GetMenu(self):
        return self.items


    def __str__(self):
        for p,i,t,d in self.items:
            print(f"{i}:")
            print(f" Price: ${p}")
            print(f" Type: {t}")
            print(f" Description: {d}")
            print()
        return ""