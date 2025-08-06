import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

# Change this URI to match your Crazyflie
uri = 'radio://0/80/2M/E7E7E7E704'

def print_all_params(cf):
    """
    Print all parameters grouped by their parameter group.
    Handles both 'group.name' and standalone parameters.
    """
    all_params = cf.param.toc.toc  # Dictionary of parameters
    group_dict = {}

    for key in all_params:
        if '.' in key:
            group, name = key.split('.', 1)
        else:
            group = key
            name = '(no subparam)'

        if group not in group_dict:
            group_dict[group] = []
        group_dict[group].append(name)

    for group in sorted(group_dict):
        print(f"\n📁 Parameter Group: {group}")
        for name in sorted(group_dict[group]):
            print(f"   └── {group}.{name}")

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    # Connect to the Crazyflie and print the parameter list
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        print("✅ Connected to Crazyflie!")
        print_all_params(scf.cf)
