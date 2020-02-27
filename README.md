# MSCnnClassifier-Evualation

## 配置文件参数介绍
### default
  `output_dir`模型输出地址
  `image_source_dir`图片库地址
  `base_model_name`基础模型名称
  `class_name`分类类别名称
### train
  `use_base_model_weights`是否使用预训练权重
  `use_trained_model_weights`是否使用上次训练的权重
  `use_best_weights`是否使用最佳训练权重
  `output_weights_name`输出权重命名
  `epochs`epoch数
  `batch_size`批大小
  `initial_learning_rate`初始训练权重
  `image_dimension`输入图片维度
  `train_steps`训练步数
  `validation_steps`验证步数
  `patience_reduce_lr`学习率经过多少轮训练效果无提升后衰减
  `min_lr`最小学习率
  `positive_weights_multiply`正样本权重
  `dataset_csv_dir`数据集CSV文件存放地址
  `show_model_summary`是否打印输出模型概述
  `save_weights_only`是否仅保存权重
### test
  `batch_size`验证批大小
  `test_steps`测试步数
  `test_generator_random_state`测试随机数
  `use_best_weights`是否使用最佳权重

## 案例简介
1. 数据集划分放在data_split下，images目录下为案例数据集，针对40种车标分类
2. experiments目录存放个词模型输出结果。
3. models为模型文件夹，可自定义cnn模型
