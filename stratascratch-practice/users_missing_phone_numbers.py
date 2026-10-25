import pandas as pd 
no_phone_numbers_df = fintech_app_users[fintech_app_users['phone_number'].isnull()]
no_phone_numbers_df[['user_id', 'user_name']]