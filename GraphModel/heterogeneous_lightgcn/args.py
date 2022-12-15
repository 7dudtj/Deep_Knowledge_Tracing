import argparse
import time
from typing import Optional, Union
from torch import Tensor

def parse_args():
    timestr = time.strftime("%m.%d-%H:%M:%S")
    parser = argparse.ArgumentParser()
    
    ### 옵션 ###
    parser.add_argument(
        "--run_wandb", default=False, type=bool, help="option for running wandb"
    )
    wandb_kwargs = dict(project="DKT_LGCN", entity="ai-tech-4-recsys-12")
    
    parser.add_argument(
        "--basepath",
        default="../../data",
        type=str,
        help="data directory",
    )
    parser.add_argument(
        "--loader_verbose",
        default=True,
        type=bool,
        help="verbose on/off",
    )
    parser.add_argument(
        "--timestr",
        default=timestr,
        type=str,
        help="timestr"
    )
    parser.add_argument(
        "--output_dir",
        default="./output/",
        type=str,
        help="output_dir"
    )
    parser.add_argument(
        "--pred_file",
        default="submission_{}.csv".format(timestr),
        type=str,
        help="pred_file"
    )    
    parser.add_argument(
        "--embedding_dim",
        default=64,
        type=int,
        help="embedding_dim"
    )    
    parser.add_argument(
        "--feature_num_layers",
        default=[3, 3, 3],
        nargs='+',
        type=int,
    )   
    parser.add_argument(
        "--alpha",
        default=None,
        type=Optional[Union[float, Tensor]],
        help="alpha"
    )    
    parser.add_argument(
        "--build_kwargs",
        default={},
        type=dict,
        help="build_kwargs"
    )
    parser.add_argument(
        "--n_epoch",
        default=1000,
        type=int,
    )
    parser.add_argument(
        "--learning_rate",
        default=0.001,
        type=float,
    )    
    parser.add_argument(
        "--weight_basepath",
        default="./weight",
        type=str,
    )
    parser.add_argument(
        "--patience",
        default=20,
        type=int,
    )
    parser.add_argument(
        "--edge_dropout",
        default=0,
        type=int,
    )
    parser.add_argument(
        "--edge_dropout_rate",
        default=0.1,
        type=float,
    )
    parser.add_argument(
        "--feature_aggregation_method",
        default=0,
        type=float,
    )
    parser.add_argument(
        "--use_custom",
        default=1,
        type=float,
    )
    args = parser.parse_args()
    
    return args, wandb_kwargs