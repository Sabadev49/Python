import numpy as np
from sklearn.linear_model import LogisticRegression
X=np.array([[2],[4],[6],[8]]) #2 bo-di
y=np.array([0,0,1,1])
model=LogisticRegression() #creat model
model.fit(X,y) #teach to model
new_student=np.array([[5]])
prediction=model.predict(new_student) #do prediction
print("prediction for 5 h:",prediction)
if prediction[0] ==1:
    print("passed") 
else:
    print("failed")
#project 2
print("-" * 30)
import numpy as np
from sklearn.linear_model import LinearRegression
X=np.array([[50],[70],[90],[110]])
y=np.array([2,3,4,5])
model=LinearRegression()
model.fit(X,y)
home1=np.array([[80]])
prediction=model.predict(home1)
print("the price is:", prediction)
