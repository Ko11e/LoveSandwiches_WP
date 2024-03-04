import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input form the user
    """
    print("Please enter sales from the last market.")
    print("Data should be six numbers, separated by commas")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here:")
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(value):
    """
    Inside the try, convert all string values into integers.
    Raises VAlueError if stings cannot be converted into int, 
    or if there aren't exacly 6 values.
    """
    try:
        if len(value) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(value)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    print(value)

get_sales_data()