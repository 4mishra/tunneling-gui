import subprocess

def save_ip():
    network_interface = open("netconfig", "w")
    content = ["IP Address \n", "Subnet Mask \n", "Gateway"]
    network_interface.writeLines(content)
    network_interface.close()

    subprocess.run(["mv", network_interface, "/etc/"])
    subprocess.run(["systemctl", "restart", "netctl"])

def do_change_password(new_password):
    subprocess.run(["scripts/do_change_password.sh", new_password])
