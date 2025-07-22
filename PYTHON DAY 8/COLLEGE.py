class college:
   col="NITTE"
   def student(self,name,mark):
      self.name= name
      self.mark=mark
   def passfall (self):
      if (self.mark>40):
         print("clear")
      else:
        print("FAIL")
   def modify(self,grace):
      self.mark=self.mark+grace
   def display(self):
      print("Name",self.name)
      print("College",self.col)
      print("Mark",self.mark)
      print("Status",self.passfall())
s1=college()
s2=college()
s1.student("NIKKI",45)
s2 .student("adi.",75)  
s1.passfall()
s2.passfall()
s2.modify(29)
s2.passfall()
s1.display()
s2.display()

print(college.col)
               

      