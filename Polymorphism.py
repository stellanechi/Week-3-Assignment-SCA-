class CrossRiver():
     def capital(self):
       print("Calabar")
 
     def language(self):
       print("Effic")
 
class Abia():
     def capital(self):
       print("Umuahia")
 
     def language(self):
       print("igbo")
 
obj_CRS = CrossRiver()
obj_ABI = Abia()
for state in (obj_CRS, obj_ABI):
state.capital()
state.language()
