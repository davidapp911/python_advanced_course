# Task Instructions
https://www.demoblaze.com/ - demo site to test


__Automate testcases (install pytest and selenium; install ChromeDriver and Chrome browser)__\
__Suite Precondition: User is registered__
1.   
- step 1: click login button\
-- expected result: login and password fields are presented\
- step 2: set up login and password and click login button\
-- expected result: Log out button is presented;  Welcome {username} message is presented

2. __test precondition: User is logged in__\
- step 1: Click on Monitors category\
- step 2: Click on the product with the highest price on the page\
-- expected result: product's page with {product_name} and {product_price} is open\
- step 3: Click on Add to cart button\
- step 4: Click on Cart button\
-- expected result: product is successfully added to cart; {product_name} and {product_price} are presented

*(Optional)
Add a listener that makes screenshots after executing every keyword with the tag 'screenshot'.*

Useful links:\
[Robot Framework documentation](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)\
[Selenium Library documentation](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)