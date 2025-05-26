import os
import sys
import json
import torch

# for consistency between python2 and python3
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

import dreamplace.configure as configure
import Params
import PlaceDB

import time
import numpy as np
import logging


import Timer
import NonLinearPlace
import pdb
from dreamplace.ops.hpwl.hpwl import HPWL

def compute_raw_hpwl(placedb):
    import torch

    # Robust way to determine number of nets
    #if hasattr(placedb, 'flat_net2pin_start_map') and placedb.flat_net2pin_start_map is not None:
     #   num_nets = placedb.flat_net2pin_start_map.numel() - 1
    #elif hasattr(placedb, 'net2pin_map') and placedb.net2pin_map is not None:
     #   num_nets = len(placedb.net2pin_map)
    #elif hasattr(placedb, 'rawdb') and placedb.rawdb is not None and hasattr(placedb.rawdb, 'numNets'):
     #   num_nets = placedb.rawdb.numNets()
    #else:
     #   raise ValueError("Cannot determine number of nets for creating net_mask.")

    net_mask = torch.ones(placedb.net_weights, dtype=torch.bool, device='cpu')


    hpwl_op = HPWL(
        pin2net_map=placedb.pin2net_map,
        net_weights=placedb.net_weights,
        net_mask=net_mask,
        algorithm='atomic'
    )

    pos = placedb.init_pos.clone().detach().requires_grad_(False)
    raw_hpwl = hpwl_op(pos)
    return raw_hpwl.item()




if __name__ == "__main__":
    """
    @brief main function to invoke the entire placement flow.
    """
    logging.root.name = 'DREAMPlace'
    logging.basicConfig(level=logging.INFO,
                        format='[%(levelname)-7s] %(name)s - %(message)s',
                        stream=sys.stdout)
    params = Params.Params()
    params.printWelcome()
    if len(sys.argv) == 1 or '-h' in sys.argv[1:] or '--help' in sys.argv[1:]:
        params.printHelp()
        exit()
    elif len(sys.argv) != 2:
        logging.error("One input parameters in json format in required")
        params.printHelp()
        exit()

    # load parameters
    params.load(sys.argv[1])
    logging.info("parameters = %s" % (params))
    # control numpy multithreading
    os.environ["OMP_NUM_THREADS"] = "%d" % (params.num_threads)

    placedb = PlaceDB.PlaceDB()

    print("dir(placedb)")
    print("placedb.net_weights:", placedb.net_weights)
    #print("placedb.num_nets:", placedb.num_nets)
    print("pin2net_map:", placedb.pin2net_map)
    #print("placedb.num_nets:", placedb.net_mask)



    # Compute HPWL
    raw_hpwl = compute_raw_hpwl(placedb)
    print(f"[RESULT] Raw HPWL = {raw_hpwl}")


