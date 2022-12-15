import pandas as pd
import torch
from config import CFG, logging_conf

from lightgcn.datasets import prepare_dataset
from lightgcn.models import build, train
from lightgcn.utils import class2dict, get_logger

# wandb logger 설정하기
if CFG.user_wandb:
    import wandb

    wandb_name = "JS" + "_" + str(CFG.learning_rate) + "_" + str(CFG.embedding_dim)
    wandb.init(**CFG.wandb_kwargs, config=class2dict(CFG), name=wandb_name)


logger = get_logger(logging_conf)
use_cuda = torch.cuda.is_available() and CFG.use_cuda_if_available
device = torch.device("cuda" if use_cuda else "cpu")
print(device)


def main():
    logger.info("Task Started")

    logger.info("[1/1] Data Preparing - Start")
    train_data, test_data, valid_data,\
    user_problem_n_node, user_test_n_node, user_tag_n_node,\
    train_user_feature_engineering, train_item_feature_engineering,\
    test_user_feature_engineering, test_item_feature_engineering,\
    valid_user_feature_engineering, valid_item_feature_engineering = prepare_dataset(
        device,
        CFG.basepath,
        verbose=CFG.loader_verbose,
        logger=logger.getChild("data"),
        isTrain=True,
    )
    logger.info("[1/1] Data Preparing - Done")

    logger.info("[2/2] Model Building - Start")
    """
    model_type: 0 -> 모델 날 것 그대로
    model_type: 1 -> pretrained weight 사용
    model_type: 2 -> inference 시에 best 모델
    """
    model = build(
        user_problem_n_node,
        user_test_n_node, 
        user_tag_n_node,
        num_user_feature=len(train_user_feature_engineering.T),
        num_item_feature=len(train_item_feature_engineering.T),
        
        model_type=0,
        
        logger=logger.getChild("build"),
        **CFG.build_kwargs
    )
    model.to(device)

    if CFG.user_wandb:
        wandb.watch(model)

    logger.info("[2/2] Model Building - Done")

    user_problem_train_data, user_test_train_data, user_tag_train_data = train_data
    user_problem_valid_data, user_test_valid_data, user_tag_valid_data = valid_data
    
    user_problem_test_data, user_test_test_data, user_tag_test_data = test_data 
    
    logger.info("[3/3] Model Training - Start")
    train(
        model,
        
        train_user_feature_engineering,
        train_item_feature_engineering,
        
        valid_user_feature_engineering,
        valid_item_feature_engineering,
        
        test_user_feature_engineering,
        test_item_feature_engineering,
        
        user_problem_train_data,
        user_test_train_data,
        user_tag_train_data,
        
        user_problem_valid_data,
        user_test_valid_data,
        user_tag_valid_data,
        
        user_problem_test_data,
        user_test_test_data,
        user_tag_test_data,
        
        n_epoch=CFG.n_epoch,
        learning_rate=CFG.learning_rate,
        use_wandb=CFG.user_wandb,
        # weight=CFG.weight_basepath,
        logger=logger.getChild("train"),
        # model_type=0,
        model_type=1,
        

        
    )
    logger.info("[3/3] Model Training - Done")

    logger.info(f"user features: {CFG.user_features}")
    logger.info(f"item features: {CFG.item_features}")
    
    logger.info("Task Complete")


if __name__ == "__main__":
    main()