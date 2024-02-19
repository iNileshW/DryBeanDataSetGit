import mlflow
import numpy as np
import xgboost as xgb
from data import X_train, X_val, y_train, y_val
from sklearn.linear_model import Ridge, ElasticNet
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.model_selection import ParameterGrid
from params import ridge_param_grid, elasticnet_param_grid, xgb_param_grid, lightgbm_param_grid, randomforest_param_grid,decision_param_grid
from utils import eval_metrics
param_grid_list=[
    lightgbm_param_grid, 
    xgb_param_grid,
    elasticnet_param_grid,
    ridge_param_grid,
    randomforest_param_grid,
    decision_param_grid
    ]

model_name_list=[
    GradientBoostingClassifier,
    XGBRegressor,
    ElasticNet,
    Ridge,
    RandomForestClassifier,
    DecisionTreeClassifier]

# Loop through the hyperparameter combinations and log results in separate runs
for param_iterator,model_iterator in zip(param_grid_list,model_name_list):
    for params in ParameterGrid(param_iterator):
        mlflow.set_experiment("/mlops_project_dbds")
        with mlflow.start_run():
            if model_iterator=='GradientBoostingClassifier':
                lr = GradientBoostingClassifier(**params)
            elif model_iterator=='XGBRegressor':
                lr=XGBRegressor(**params)
            elif model_iterator=='ElasticNet':
                lr=ElasticNet(**params)
            elif model_iterator=='Ridge':
                lr = Ridge(**params)
            elif model_iterator=='RandomForestClassifier':
                lr = RandomForestClassifier(**params)
            else:
                lr = DecisionTreeClassifier(**params)    
            lr.fit(X_train, y_train)

            y_pred = lr.predict(X_val)

            metrics = eval_metrics(y_val, y_pred)

            # # Logging the inputs such as dataset
            # mlflow.log_input(
            #     mlflow.data.from_numpy(X_train.toarray()),
            #     context='Training dataset'
            # )

            # mlflow.log_input(
            #     mlflow.data.from_numpy(X_val.toarray()),
            #     context='Validation dataset'
            # )

            # Logging hyperparameters
            mlflow.log_params(params)

            # Logging metrics
            mlflow.log_metrics(metrics)

            # Log the trained model
            mlflow.sklearn.log_model(
                lr,
                param_iterator,
                input_example=X_train,
                code_paths=['train.py','data.py','params.py','utils.py']
            )