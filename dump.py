#!/usr/bin/python3

class Color:
    #change colors from here..
    GREEN = '\033[92m'
    WHITE='\033[37m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

class Compare():
    def off_color(self,off,bad_char,x):
        y=[]
        for i in range(len(x)):
            if i%8==0 and i!=0: #32 lines ,i!=0 drop first empty string
                y.append("\n")
            y.append(x[i])
        y=" ".join(map(str,y)).split("\n")
        for i in range(len(y)):
            if bad_char in y[i]:
                off_index=off.index(off[i])
                off_pop=off.pop(off_index)
                off.insert(off_index,Color.YELLOW+ off_pop+Color.RESET)
        return off

    def check(self,x,y,off):
        final=""
        bad=""
        bad_char=""
        for i in range(0,int("FF",16)+1):  
            if i==255: #255=FF #check for last line
                if bad_char !="":
                    off=self.off_color(off,bad_char,x)
            if i%8==0:
                if bad_char !="":
                    off=self.off_color(off,bad_char,x)
                if i!=0:
                    final+="\n"
                    bad+="\n"
            if x[i]==y[i]:
                final+=Color.GREEN+f" {y[i]} "+Color.RESET
                bad+=Color.WHITE+f" {x[i]} "+Color.RESET
                #bad_char=x[i]
            else:
                final+= Color.RED+f"[{y[i]}]"+Color.RESET
                bad+=Color.RED+f"[{x[i]}]"+Color.RESET
                bad_char=x[i] #bad_char found
        #For seperate use load as splitlines()or split("\n")
        for of,original, changed in zip(off,bad.splitlines(),final.splitlines()):
            print(of,original,changed)
        return final
    def file_read(self):
        x=[format(i, '02x').upper() for i in range(1,int("FF",16)+1)]+["00"]
        y,z=[],[]
        input_hex=''
        with open('dump.txt', encoding="utf8") as file:
            lines=file.readlines()
            for line in lines:
                input_hex += line.split("  ")[1]+'\n' #for print
                hex_value=line.split("  ")[1].split(" ")
                off_value=line.split("  ")[0]
                z.append(off_value)
                for value in hex_value:
                    y.append(value)
        return self.check(x,y,z)

if __name__ == "__main__":
    final=Compare()
    final.file_read()
