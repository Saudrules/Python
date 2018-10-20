class Udacian:
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status 
    
    def print_udacian(self):
        #print(self.name+" is enrolled in "+self.enrollment+" and lives is "+self.city+" studying a "+self.nanodegree+" status is "+self.status+" .")
        return self.name+" is enrolled in "+self.enrollment[0]+self.enrollment[1]+self.enrollment[2]+" and lives is "+self.city+" studying a "+self.nanodegree+" status is "+self.status+" ."

udacian = Udacian("Saud","Riyadh",("Sat","PM","Lujain"),"FSND","Ontrack")
   
print(udacian.print_udacian())