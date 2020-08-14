import random

citizen_one= """
    ,.__             
  ..///////r         
  /,. _  _\        
 q|==(o)-(o)       
  | "     >     
   \   '__|      
    |  __/            
  __|\  /|__       
 /  __ W     \.      
/  /   []  \  \,     

"""

citizen_two="""
    ,,.. __    
  (@######@)
 .(#########)    
  (o)(o)(#@#)    
   <  "" (##@@)  
  \ ,    (##@@)  
   \    .(#3@3@) 
  @@@|   |@#@###) 
   OOOOOO.####@)
  V      \   \@@

"""

bandit="""

        __
   /\/ V  \/ \\     
  |   // __/_\\`    /\\
  \/\_/V \/\/,_`   ||
   {≤≥= ≤≥ '}P/>   ||
   |=------ =|<    ||
   \       _/ \>   ||
    \_____/'       ;x;
   _ _|_  _\_____  v_v
  / / \_' '_/  | \,||
 / /           \   ||
 | |  -"  `    |- ||

"""

beggar="""
      ~*
~ _______  ~*
 /=.     =\'
/___=_____\.     
/\/ (.~)(~)/ ~      
W C;... .>    
 \\;;.;__|   ~*
~* \''''/ ~       
 __/____\__    ~ 
/ =        \

"""

def EncounterBeggar():

  print("You encountered a beggar.\nThe beggar asks for food.")
  print(beggar)
        
def EncounterBandit(trigger):

  if trigger==5:
    print("You encountered a bandit.\nPrepare to defend yourself!")
    print(bandit)

  if trigger==6:
    print("You encountered a bandit.\nPrepare to defend yourself!")
    print(bandit)

