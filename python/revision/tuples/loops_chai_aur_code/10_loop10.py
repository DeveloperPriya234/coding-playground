#expontial backoff
#empliment an exponential backoff strategy that doubles the wait time btw retries,starting
#from a seconnd,but stops after 5 retries..


import time
wait_time = 1
max_retries = 5
attempts = 0 

while attempts < max_retries:
    print("attempts",attempts,+1 , "- wait time",wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1