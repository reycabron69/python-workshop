print('Stone : s','Paper : p','Scissor : c')

a=b=0
chance=0
while a==b or chance<3:
             p1=input('player 1 :')
             p2=input('player 2 :')
             chance+=1
             if p1==p2:
                          continue
             elif p1=='s' and p2=='p':
                          b+=1               
             elif p1=='p' and p2=='s':
                          a+=1                          
             elif p1=='p' and p2=='c':
                          b+=1                        
             elif p1=='c' and p2=='p':
                          a+=1                         
             elif p1=='c' and p2=='s':
                          b+=1                          
             elif p1=='s' and p2=='c':
                          a+=1                         

print('Winner : ','player2' if b>a else 'player1')
