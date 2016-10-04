

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self,length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print ()
        
class Bassist(Musician):
    def __init__(self):
        super(Bassist,self).__init__(["Twang", "Thrumb", "Bling"])
        
class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["boom","bash","cymbal"])
    
    def Drummer_solo(self,length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print ()
    
    def count(self):
        print "One, two, three, four!"
    
    def spontaneously_combust(self):
        print "Boom! ......"
        
class Band(Musician):
    def __init__(self):
        self.members = {}
    
    def hire(self):
        new_member = raw_input("What is his/ her bandname?")
        type_musician = raw_input("Is he a drummer of a guitarist?").lower()
        
        if type_musician == "drummer":
            self.members[new_member] = Drummer()
        elif type_musician == "guitarist":
            self.members[new_member] = Guitarist()
            
    def fire(self, fired):
        del self.members[fired]
        
    def play_solos(self, length):
        
        Drummer().count()
        
        for musician in self.members.iteritems():
            musician.solo(length)
            
if __name__ == '__main__':
  The_Band = Band()
  The_Band.hire()
  The_Band.play_solos(3)
  The_Band.hire()
  The_Band.hire()
  The_Band.play_solos(4)
  The_Band.fire('guitarist')
  The_Band.play_solos(5)
