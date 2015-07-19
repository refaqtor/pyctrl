import time
import numpy

from ctrl.algo import Proportional
import ctrl.client

HOST, PORT = "localhost", 9999

controller = ctrl.client.Controller(HOST, PORT)
with controller:

    print(controller.help())

    print(controller.help('s'))
    print(controller.help('S'))

    controller.set_echo(0)

    controller.reset_logger()

    controller.start()
    time.sleep(1)
    controller.set_reference1(100)
    time.sleep(1)
    controller.set_reference1(-50)
    time.sleep(1)
    controller.set_reference1(0)
    time.sleep(1)
    controller.stop()

    print(controller.get_log())

    controller.set_logger(2)

    controller.start()
    time.sleep(1)
    controller.set_reference1(100)
    time.sleep(1)
    controller.set_reference1(-100)
    time.sleep(1)
    controller.stop()

    print(controller.get_log())

    controller.set_controller1(Proportional(1, 1))
