#To import random ip adresses
import random

#Func to generate random IP functions
def generate_random_ip():  
    return f"192.168.1.{random.randint(0,20)}"

#Defining the firewall rules of given ip address
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

#Logic of script, if the matched IP is used, it blocks access 
def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block", 
        "192.168.1.9": "block", 
        "192.168.1.13": "block", 
        "192.168.1.16": "block", 
        "192.168.1.19": "block" 
    }
#Simulated 12 different random IP adresses, tested them against the rules
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        #prints IP address, states whether it was blocked or not
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

#Ensuring main fucntion runs once script is exucuted
if __name__ == "__main__":
    main()

