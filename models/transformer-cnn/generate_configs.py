# File: generate_configs.py

import os

# Define the cell line list from the provided string
cell_line_list = """KM12 MCF7 MDA-MB-231_ATCC HS_578T BT-549 T-47D SF-268 SF-295 SF-539 SNB-19 
SNB-75 U251 COLO_205 HCC-2998 HCT-116 HCT-15 HT29 SW-620 CCRF-CEM HL-60(TB) K-562 MOLT-4 RPMI-8226 
SR LOX_IMVI MALME-3M M14 SK-MEL-2 SK-MEL-28 SK-MEL-5 UACC-257 UACC-62 MDA-MB-435 MDA-N A549_ATCC 
EKVX HOP-62 HOP-92 NCI-H226 NCI-H23 NCI-H322M NCI-H460 NCI-H522 IGROV1 OVCAR-3 OVCAR-4 OVCAR-5 
OVCAR-8 SK-OV-3 NCI_ADR-RES PC-3 DU-145 786-0 A498 ACHN CAKI-1 RXF_393 SN12C TK-10 UO-31"""
cell_lines = cell_line_list.split()

# Define other parameters
folds = [1, 2, 3, 4, 5, 6, 7]  # Example seeds, add as needed
seeds = [1, 2, 3, 4, 5]  # Example seeds, add as needed
splitting_methods = ["UMAP", "scaffold", "random", "butina"]  # Example splitting methods, add as needed

# Base directories for the data, results, and generated configs
base_data_dir = "/rds/general/user/qg622/home/Y2/ScaffoldSplitsOverestimateVS/data/60_cell_lines/"
base_result_dir = "/rds/general/user/qg622/home/Y2/ScaffoldSplitsOverestimateVS/results/TRANSCNN/"
output_config_dir = "/rds/general/user/qg622/home/Y2/ScaffoldSplitsOverestimateVS/models/transformer-cnn/configs"


# base_data_dir = "/n/holylfs05/LABS/pfister_lab/Lab/coxfs01/pfister_lab2/Lab/tongding/transformer-cnn/data/60_cell_lines/"
# base_result_dir = "/n/holylfs05/LABS/pfister_lab/Lab/coxfs01/pfister_lab2/Lab/tongding/transformer-cnn/results/TRANSCNN/"
# output_config_dir = "/n/holylfs05/LABS/pfister_lab/Lab/coxfs01/pfister_lab2/Lab/tongding/transformer-cnn/configs"

# Ensure the output directory exists
os.makedirs(output_config_dir, exist_ok=True)

# Template for the configuration file
config_template = """[Task]
train_mode = True
model_file = model.tar
train_data_file = {train_data_file}
apply_data_file = {apply_data_file}
result_file = {result_file}
[Details]
retrain = False
canonize = True
gpu = 0
seed = {seed}
n_epochs = 5
batch_size = 32
fold = {fold}
split = {split}
"""

# Generate config files
for cell_line in cell_lines:
    for fold in folds:
        for split_method in splitting_methods:
            for seed in seeds:
                # Define file paths
                train_data_file = os.path.join(base_data_dir, f"{cell_line}.csv")
                apply_data_file = os.path.join(base_data_dir, f"{cell_line}.csv")
                result_file = os.path.join(base_result_dir, f"{cell_line}/fold_{fold}/seed_{seed}/split_{split_method}/test_predictions.csv")

                # Create the configuration content
                config_content = config_template.format(
                    train_data_file=train_data_file,
                    apply_data_file=apply_data_file,
                    result_file=result_file,
                    seed=seed,
                    fold=fold,
                    split=split_method.lower(),
                )

                # File name for the configuration
                config_filename = f"{cell_line}_split_{split_method.lower()}_fold_{fold}_seed_{seed}.cfg"
                config_filepath = os.path.join(output_config_dir, config_filename)

                # Write to the configuration file
                with open(config_filepath, "w") as config_file:
                    config_file.write(config_content)

                print(f"Generated config file: {config_filepath}")
