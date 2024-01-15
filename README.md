# About
This repo is a small python "clay pigeon shooting" simulation project. 
It was created as part of an interdisciplinary project involving mathematics, physics, business management, english and computer science.

## A closer look at the formulas
To begin, I define the motion formulas for my two projectiles.
![]()
### Target
* Abscissa : ![](https://quicklatex.com/cache3/db/ql_79cc0190c80c85d025438d2f0c8e2bdb_l3.png)
* Ordinate : ![](https://quicklatex.com/cache3/e6/ql_420784d27b796828235baf2db3c26ee6_l3.png)
### Shot
* Abscissa : ![](https://quicklatex.com/cache3/32/ql_0906b50f3522d4f2a6d2f73fe0c53232_l3.png)
* Ordinate : ![](https://quicklatex.com/cache3/d8/ql_20753dea61f6853f2feef1f3585502d8_l3.png)

### Time to cross in abscissa
To find out whether my shot crosses the target that was thrown, I start by calculating how long it will take for my two projectiles to cross each other on the abscissa after the simulation has started.

![](https://quicklatex.com/cache3/31/ql_3220dd8ef019c4881e1463f98ae25c31_l3.png)

If the time result is negative, then my projectiles would probably have crossed each other in the "virtual past", so the simulation can already know that the shooter missed his target.

### Time to cross in ordinate
If the projectiles cross each other positively on the x-axis, then we can calculate how long it will take them to cross each other on the y-axis. The special thing here is that the target's motion function is quadratic. This means that my projectiles can cross each other 0, 1 or 2 times on this axis. That's why I start by calculating the discriminant.

![](https://quicklatex.com/cache3/ed/ql_5ddb43b4168eaf7ff27bd47d2e2517ed_l3.png)

If the discriminant is negative, then my two projectiles never cross in order, and the shooter has missed his target. On the other hand, if the discriminant is equal to 0, then I can use the following formula.

![image](https://quicklatex.com/cache3/26/ql_bc1740b999e8d0b7df5bc3f69e2dbc26_l3.png)

And if the discriminant is positive, I calculate the following two variants of the formula.

![image](https://quicklatex.com/cache3/26/ql_bc1740b999e8d0b7df5bc3f69e2dbc26_l3.png)
![image](https://quicklatex.com/cache3/1d/ql_c528857ea26ddb0257177887a6ffb61d_l3.png)

In the end, I compare the "Time to cross in abscissa" and the result of the above formulas, depending on the case. If my times are equal to a user-defined number of decimal places, then the shooter has successfully hit the target. In any other case, the shooter has failed.

## Cheat sheet
* Delay : 2 
* Distance : 0 
* Height : 177
* Angle : 30
* Precision : 1

or

* Delay : 1
* Distance : 9
* Height : 1000
* Angle : 60
* Precision : 2
