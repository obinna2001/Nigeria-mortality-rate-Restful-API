import uuid
import hashlib


def generate_task_id():
    """Generating a unique id based on MAC address and current time using uuid1"""
    uuid_id = uuid.uuid1()
    
    # convert the generated uuid_id to string and encode it to bytes using utf-8
    string_uuid_id = str(uuid_id).encode('utf-8')
    
    # create a SHA-256 hash object based on the encoded uuid_id
    hash_id = hashlib.sha256(string_uuid_id[:-4])
    
    # create the hexadecimal representation of the hash_id
    task_id = hash_id.hexdigest()[:8]
    
    # return a unique task id of length 8
    return task_id

# def generate_userid(username: str) -> str:
#     """Generate a unique user id based on the user name or identity. User name must be unique
#         args: str
#             username: A unique username provided by the client/user
#         return:
#             used_id: A unique hexadecimal user id based on the username
#     """
#     encode_id = username.encode('utf-8')
    
#     # create a SHA-256 hash object based on encode_id
#     hash_id = hashlib.sha256(encode_id)
    
#     # create a unique hexadecimal user id
#     user_id = hash_id.hexdigest()
    
#     # return unique user_id
#     return user_id
    