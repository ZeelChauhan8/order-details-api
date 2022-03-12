Order-detais api 

Details : We have created model for order details page in model.py. in which i have created order,order_details,item,delayed_order model 

Step to install django project :

1. Download the project 

2. "pip install -r requirements.txt" by using this whichever i have used packages it will get install packages in your     system

3. Run project by command "python manage.py runserver"
    - Check List of order details , Here is only one end-point for all operation (CRUD) :
        - http://localhost:8000/orders/v1/
    - Get List of delayed order details then go to : 
        - http://localhost:8000/orders/v1/delayed/get/
    
4. For scheduling task go to the project and write "python/python3 schedule.py" then command fire every 1 minutes

                                                 ***
    

