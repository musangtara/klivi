# $DEFINE >> vm machine
import pathlib
import os, sys
os.system("clear")
def get_sys():
	return sys

def extend(func):
	return func

REGISTERED_CODEGEN = {
    "compute-library": {
        "config_key": None,
        "pass_pipeline": "partition_for_arm_compute_lib"
    },
    "ethos-n77": {
        "config_key": "relay.ext.ethos-n.options",
        "pass_pipeline": "partition_for_ethosn"
    },
}
print(0x67)