import random

lower_case ="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols ="!#$%^&*><?"


number ="0123456789"
use_for = lower_case + upper_case + symbols +number 

length_for_password =9
 
password ="".join(random.sample(use_for,length_for_password))
print("Your  Randomly Generated password is :" + password)