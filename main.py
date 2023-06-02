# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import time

from pymeasure.instruments.wenworthlabs.s200 import S200

log = logging.getLogger(__name__)


# log.addHandler(logging.NullHandler())

def getting_chuck_position_info_test(probe_table):
    print(probe_table.x_position)
    print(probe_table.y_position)
    print(probe_table.z_position)
    print(probe_table.x_index)
    print(probe_table.y_index)
    print(probe_table.theta_position)
    print(probe_table.z_overtravel)
    print(probe_table.z_finelift)
    print(probe_table.z_grosslift)


def moving_test(probe_table):
    """
    :type probe_table:S200
    """
    probe_table.chuck_lift = False
    probe_table.move_to_probing_zone_centre_position()
    probe_table.x_index = 2000
    probe_table.y_index = 2000
    # probe_table.indexing_mode = True
    for i in range(0, 10):
        probe_table.chuck_lift = False
        probe_table.next_die = "R"
        probe_table.chuck_lift = True

    probe_table.chuck_lift = False


def lamp_test(probe_table):
    """
    :type probe_table:S200
    """
    probe_table.chuck_lift = False
    probe_table.move_to_probing_zone_centre_position()
    for i in range(0, 10):
        probe_table.lamp_on = True
        probe_table.lamp_on = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s200 = S200("GPIB0::28::INSTR",
                query_delay=0.5,
                write_delay=0.5)
    getting_chuck_position_info_test(s200)
    # moving_test(s200)
    # lamp_test(s200)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
