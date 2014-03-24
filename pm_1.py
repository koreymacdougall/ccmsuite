# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log()

# define the model
class MyModel(ACTR):
    goal=Buffer()


        
    def greeting(goal='action:greet'):
        #print "Hello"
        goal.clear()
        
# run the model
#B = ACTR()
#B.run()
model=MyModel()
#x = dir(model)
#print(model,"model1")

ccm.log_everything(model)
#y = dir(model)
#print(len(x),len(y))
#print(set(y)-set(x))
model.goal.set('action:greet')
model.run()


