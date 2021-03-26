Simple linear regression can be expressed in one simple equation.
![image](https://user-images.githubusercontent.com/57702598/112576720-db744700-8dc0-11eb-809b-95bb2d8355df.png)

Simple linear regression equation

The intercept is often known as beta zero (β0) and the coefficient as beta 1 (β1). The equation is equal to the equation for a straight line

![image](https://user-images.githubusercontent.com/57702598/112576748-e4fdaf00-8dc0-11eb-8532-dd25e8a386bf.png)


Ordinary least squares
Ordinary least squares is known to minimize the sum of squared residuals (SSR). There are two central parts to ordinary least squares in this special case: estimating the coefficients and estimating the intercept.

Estimating the coefficient
You can estimate the coefficient (the slope) by finding the covariance between x and y and dividing it by the variance of x. 

![image](https://user-images.githubusercontent.com/57702598/112576826-0fe80300-8dc1-11eb-8510-fa75efb4d1bc.png)

![image](https://user-images.githubusercontent.com/57702598/112576856-242c0000-8dc1-11eb-836a-19fb2b30fa6e.png)


Expanding formula

xi is one value of x at index i.

yi is one value of y at index i.

x̅ is pronounced as x bar and is the average of x.

y̅ is pronounced as y bar and is the average of y.

Estimating the intercept
The estimate of the intercept β0 should be easier to understand than the estimate of the coefficient β1.

![image](https://user-images.githubusercontent.com/57702598/112576872-2aba7780-8dc1-11eb-9479-53ecb168b7cf.png)


x̅ is pronounced as x bar and is the average of x.
y̅ is pronounced as y bar and is the average of y.
β1 is the coefficient that I estimated from earlier.
