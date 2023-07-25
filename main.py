from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App
from kivymd.app import MDApp


Builder.load_file("cal.kv")


class calculator(Widget) :
    string1 = ""
    string2 = ""
    equal = []
    equal2 = ""
    def view(self,id) :
        if id in '+/-*' : 
            if len(self.string1) > 0 and self.string1[-1] not in '+/-*' : 
                self.string1 +=id
                self.ids.calculations.text = self.string1
        else :
            self.string1 +=id
            self.ids.calculations.text = self.string1
    def clear(self) :
        self.ids.calculations.text = ""
        self.string1,self.string2 = "",""
    def delete(self):
        if self.string1 != "" :
            self.string1 = self.string1[:-1]
            self.ids.calculations.text  = self.string1
    def delete2(self):
        if self.string2 != "" :
            self.string2 = self.string2[:-1]
        if self.equal != [] :
            self.equal = self.equal[:-1]
            self.string2 = str(self.equal[-1])
            self.equal = self.equal[:-1]
    def add_nums(self,id) :
        if id in '+/-*' : 
            if len(self.string2) > 0 and self.string2[-1] not in '+/-*' :
                self.string2 +=id
                self.ids.calculations.text = self.string2
        elif id == '.' and len(self.string2) >0 and self.string2[-1] not in '+/-*' :
            self.string2 +=id
            self.ids.calculations.text = self.string2
        elif id == "." and len(self.string2) == 0 :
            self.string2 +=id
            self.ids.calculations.text = self.string2
        else :
            self.string2 +=id
            self.ids.calculations.text = self.string2
    def calculate(self,s) :
        if s == '+':
            self.add_nums(s)
            self.a = self.string2[:-1]
            if '%' in self.a and len(self.a) >1:
                self.a=self.a.replace('%',"")
                self.a = float(self.a)/100 if '.' in self.a else int(self.a)/100
            else :
                if self.a != "" :
                    self.a = float(self.a) if '.' in self.a else int(self.a)

            if self.a != "" :
                self.equal.append(self.a)
                self.equal.append('+')

            self.string2 = ""
        elif s == '-':
            self.add_nums(s)
            self.a = self.string2[:-1]
            if '%' in self.a and len(self.a) >1:
                self.a = self.a.replace('%',"")
                self.a = float(self.a)/100 if '.' in self.a else int(self.a)/100
            else :
                if self.a != "" :
                    self.a = float(self.a) if '.' in self.a else int(self.a)

            if self.a != "" :
                self.equal.append(self.a)
                self.equal.append('-')
            self.string2 = ""
        elif s == '/':
            self.add_nums(s)
            self.a = self.string2[:-1]
            if '%' in self.a and len(self.a) >1:
                self.a=self.a.replace('%',"")
                self.a = float(self.a)/100 if '.' in self.a else int(self.a)/100
            else :
                if self.a != "" :
                    self.a = float(self.a) if '.' in self.a else int(self.a)

            if self.a != "" :
                self.equal.append(self.a)
                self.equal.append('/')
            self.string2 = ""
        elif s == '*':
            self.add_nums(s)
            self.a = self.string2[:-1]
            if '%' in self.a and len(self.a) >1:
                self.a=self.a.replace('%',"")
                self.a = float(self.a)/100 if '.' in self.a else int(self.a)/100
            else :
                if self.a != "" :
                    self.a = float(self.a) if '.' in self.a else int(self.a)
            
            if self.a != "" :
                self.equal.append(self.a)
                self.equal.append('*')
            self.string2 = ""
    def eq (self) :
        print(self.string2)
        if self.string2 != "" :
            if '%' in self.string2 :
                self.string2=self.string2.replace('%',"")
                self.string2 = float(self.string2)/100 if '.' in self.string2 else int(self.string2)/100
            else :
                self.string2 = float(self.string2) if '.' in self.string2 else int(self.string2)
            self.equal.append(self.string2)
        print(self.equal)
        if len(self.equal) >0 and str(self.equal[-1]) in '+/-*' :
            self.equal.clear()
            self.ids.calculations.text = "Invalid Syntax"
            self.string1,self.string2 = "",""
        else :
            self.string2=""
            print(self.equal)
            while len(self.equal) > 1:
                print(self.equal)
                if "*" in self.equal :
                    self.num = self.equal.index("*") 
                    self.ans = self.equal[self.num-1]*self.equal[self.num+1]
                    self.equal2 = self.equal[self.num+2:]
                    self.equal = self.equal[:self.num-1]    
                    self.equal.append(self.ans)
                    self.equal = self.equal+self.equal2
                elif "/" in self.equal :
                    try :
                        self.num = self.equal.index("/") 
                        self.ans = self.equal[self.num-1]/self.equal[self.num+1]
                        self.equal2 = self.equal[self.num+2:]
                        self.equal = self.equal[:self.num-1]    
                        self.equal.append(self.ans)
                        self.equal = self.equal+self.equal2
                    except ZeroDivisionError as ZD:
                        self.equal.clear()
                        self.equal.append(ZD)
                elif "-" in self.equal :
                    self.num = self.equal.index("-") 
                    self.ans = self.equal[self.num-1]-self.equal[self.num+1]
                    self.equal2 = self.equal[self.num+2:]
                    self.equal = self.equal[:self.num-1]    
                    self.equal.append(self.ans)
                    self.equal = self.equal+self.equal2
                elif "+" in self.equal :
                    self.num = self.equal.index("+") 
                    self.ans = self.equal[self.num-1]+self.equal[self.num+1]
                    self.equal2 = self.equal[self.num+2:]
                    self.equal = self.equal[:self.num-1]    
                    self.equal.append(self.ans)
                    self.equal = self.equal+self.equal2
            else : pass
            self.clear()
            if len(self.equal) == 0 : self.ids.calculations.text = str(self.equal2)
            else :
                self.ids.calculations.text = str(self.equal[0])
                self.equal2=str(self.equal[0])
                self.equal.clear()
        
class calapp(App):
    def build(self):
        self.icon = "logo.jpg"
        return calculator()

calapp().run()