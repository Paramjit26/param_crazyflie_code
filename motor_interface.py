import time
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
import cflib.crtp

uri = 'radio://0/80/2M/E7E7E7E704'

def send_motor_power(cf, m1, m2, m3, m4):
    cf.param.set_value('motorPowerSet.m1', str(m1))
    cf.param.set_value('motorPowerSet.m2', str(m2))
    cf.param.set_value('motorPowerSet.m3', str(m3))
    cf.param.set_value('motorPowerSet.m4', str(m4))

if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        print("Connected to Crazyflie!")

        #  Enable direct motor power control
        scf.cf.param.set_value('motorPowerSet.enable', '1')
        time.sleep(0.1)  # Give it a moment to apply

        print(" Starting motors at power = 20000")
        start_time = time.time()
        duration = 10  # seconds

        while time.time() - start_time < duration:
            # send_motor_power(scf.cf, 20000, 20000, 20000, 20000)
            send_motor_power(scf.cf, 10000, 00000, 00000, 00000)
            time.sleep(0.1)  # Send every 100ms

        print("Stopping motors")
        send_motor_power(scf.cf, 0, 0, 0, 0)
        scf.cf.param.set_value('motorPowerSet.enable', '0')
        time.sleep(0.5)  #  Give time for the packet to be sent before disconnect
        print(" Done")
