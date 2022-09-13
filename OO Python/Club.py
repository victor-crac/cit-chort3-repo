class Club:
    def __init__(self , name ,yearOfEstd,color,stadium):
            self.name=name
            self.year=yearOfEstd
            self.color=color
            self.stadium=stadium

    def __determineClub__():

        #    self.stadium=stadium
        print('OT\n')
        print('FE')
        x =input('What is the Stadium of your Club?: ')

        if x =='OT':
            print('Your club is Man U')
        else: 
        
            print('Mediocre Club')
        
    def __repr__(self):
        return f'Person("{self.stadium}","{self.year}",{self.name}, {self.color})'

 
print('######OFFICIAL CLUB DETAILS######')  

man_U = Club('Man U' , 1987 , 'Red' ,'OT')
print(man_U.name)
print(man_U.year)
print(man_U.stadium)
print(man_U.color)

print('######Printing Object attributes with the __repr__ function')
print(man_U)

# Club.determineClub
 
Club.__determineClub__()

         


    


        