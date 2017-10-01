# Shipping Application bug fix
This code was done to help Mihai debug is shipment application in my absense, the purpose is to be able to create an API to receive json post data in the form:

{
"retailer":"RETAILER1",
"product_id":"ABCD",
"quantity":1,
"shipping":
{
"shipping_first_name":"123",
"shipping_last_name":"456",
"shipping_address_line1":"STREE",
"shipping_address_line2":"LINE2",
"shipping_zip_code":"ZIP",
"shipping_city":"CITY",
"shipping_state":"TX",
"shipping_country":"US",
"shipping_phone_number":"PHONE"
}
}


## SET UP
In order to set up the application,

1. Create a virtual environment and clone this code into the virtual environment:

`https://github.com/shemogumbe/shipping_api`

2. Cd into the shipping_api folder created and install requirements by running:
	`pip install -r requirements.txt'

3. Run the application:
`python manage.py runserver`
