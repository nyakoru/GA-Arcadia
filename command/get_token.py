from command.arcadia_functions import arcadia, time
from command.tools.ArcaneUtils import fetch_json, misc, Wrapper
from command.accesskey import tokenUrl, keyheaders, payload
from command.tools.logrecord import logger
import sys

TOKEN_TERM = "access_token"
EXPIRY_TERM = "expiration_timestamp"

@Wrapper.log_function_call
def get_token(tokenUrl:str=tokenUrl, keyheaders:dict=keyheaders, payload:dict=payload) -> tuple[str, int, int]:
    """
    Function returns Access Token String, and Time of Expiry Integer\n
    No Input is required unless there is a change
    """
    token_data = arcadia(url=tokenUrl, headers=keyheaders).posting(payload=payload).json()
    if token_data == False:
        print('Unable to get key')
        sys.exit()
    else: print('Token Response received')
    data_header = True
    if data_header: token_data = token_data["data"]
    access_token = token_data.get(TOKEN_TERM)
    timeStampNow = time.timeStamp()
    hourglass = token_data.get("expires")
    expiryTime = int(timeStampNow + hourglass/1000)
    token_data[EXPIRY_TERM] = expiryTime
    savingfile = fetch_json(file_name='api_access_token').dump([token_data])
    if not savingfile:
        logger.error('CMD-GTK-TOKEN')
        sys.exit()
    print("Refresh token: ", token_data.get("refresh_token"))
    print("Expires at ", time.readableTimeStamp(timestamp = expiryTime))

    return access_token, int(expiryTime)

@Wrapper.log_function_call
def token_details():
    """
    Function returns Access Token String, and Time of Expiry Integer\n
    No Input is required unless there is a change
    """
    file_name='api_access_token.json'
    if misc.path_check(file_name):
        API_data:list = fetch_json(file_name=file_name).read()
        API_token = API_data[0].get(TOKEN_TERM)
        TimeOfExpiry = int(API_data[0].get(EXPIRY_TERM))
        isitExpired = time.timeStampExpiryChecker(expiryTime=TimeOfExpiry)
        if isitExpired == True: 
            API_token, TimeOfExpiry = get_token()
            logger.info(f'time has expired: {isitExpired}')
        else: 
            logger.info(f'time has not expired: {isitExpired}')
    else:
        API_token, TimeOfExpiry = get_token()
        logger.info(f'time has expired')
    return API_token