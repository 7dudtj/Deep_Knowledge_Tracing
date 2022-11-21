# ====================================================
# CFG
# ====================================================
class CFG:
    use_cuda_if_available = True
    user_wandb = True

    # data
    basepath = "/opt/ml/input/data/"
    loader_verbose = True

    # dump
    output_dir = "./output/"
    pred_file = "submission.csv"

    # build
    embedding_dim = 32  # int
    num_layers = 2  # int
    alpha = None  # Optional[Union[float, Tensor]]
    build_kwargs = {}  # other arguments
    weight = "./weight/best_model.pt"

    # train
    n_epoch = 300
    learning_rate = 0.01
    weight_basepath = "./weight"

    
    wandb_kwargs = dict(project="DKT_LGCN", entity="ai-tech-4-recsys-12", name=f"EMB_DIM{embedding_dim},LR{learning_rate}")

logging_conf = {  # only used when 'user_wandb==False'
    "version": 1,
    "formatters": {
        "basic": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "basic",
            "stream": "ext://sys.stdout",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "basic",
            "filename": "run.log",
        },
    },
    "root": {"level": "INFO", "handlers": ["console", "file_handler"]},
}
