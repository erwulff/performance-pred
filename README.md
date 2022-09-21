# Performance Predictors for MLPF hyperparameter optimization
> Predicting the performance of a Graph Neural Network for Particle-Flow reconstruction using (Quantum-)SVR

This project aims to asses the potential of using performance prediction techniques based on https://arxiv.org/abs/1705.10823 with the goal of optimizing the hyperparameters of [Machine Learning Particle Flow (MLPF)](https://github.com/jpata/particleflow) .

## Practical Info
* Use [code/QSVR_experiment.ipynb](/code/QSVR_experiment.ipynb) to run a QSVR on multiple train/test splits and/or analyze the results of these experiments. Saved results that can be analyzed without using quantum resources can be found in [results/good_qsvr/chain_str_10/](/results/good_qsvr/chain_str_10).
* Use [code/QSVR_combination.ipynb](/code/QSVR_combination.ipynb) to train and/or evaluate the combination technique that allows to use more training points on a QSVR. Saved results that can be analyzed without using quantum resources can be found in [results/good_qsvr/combination/](/results/good_qsvr/combination/).
* Use [code/saved_QSVR_true_vs_predicted_loss.ipynb](/code/saved_QSVR_true_vs_predicted_loss.ipynb) to load a saved pre-trained QSVR and plot its predicted loss vs true loss for all the reconstruction techniques. Some pre-trained QSVRs can be found in [results/good_qsvr/chain_str_10](/results/good_qsvr/chain_str_10).
* code/SVR_training.ipynb can be used to train and store a performance predictor to be used for downstream tasks as both [code/distributed_search.py](/code/distributed_search.py) and [code/optimize.py](/code/optimize.py) need to load pretrained scalers and regressors.
* [code/generate_data.py](/code/generate_data.py) can be used to generate a CSV file of learning curves for a given model. To use a model other than the default one edit [code/trial.py](/code/trial.py).
* The plots stored in [results/](/results/) can be generated with the notebook [code/plots.ipynb](/code/plots.ipynb).

## Configuration
* In order to run the scripts that use the QSVR class you need to have the `code/qa_summer` code repository which is not yet publicly available.
* Information on how to install and configure ocean (D-wave software) can be found [here](https://docs.ocean.dwavesys.com/en/stable/overview/install.html)

## Some plots

<p float="left">
  <img src="results/mlpf_SVR_vs_NuSVR.png" alt="Importance of learning curve and diffs" width="300"/>
   <img src="results/mlpf_train_size.png" alt="Importance of train size" width="300"/>
</p>

<p float="left" >
  <img src="results/mlpf_scalers_worst_case.png" alt="Downsampled curve and small training set" width="900"/>
</p>

<p float="left" >
  <img src="results/mlpf_loss_qsvr.png" alt="Some QSVR results" width="900"/>
</p>

## Licensing
"The code in this project is licensed under Apache License 2.0 license."
