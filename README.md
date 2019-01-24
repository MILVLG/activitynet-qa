# Activitynet-QA
The ActivityNet-QA dataset contains 58,000 human-annotated QA pairs on 5,800 videos derived from the popular ActivityNet dataset. The dataset provides a benckmark for testing the performance of VideoQA models on long-term spatio-temporal reasoning. 

## Dataset
The [dataset](dataset) folder contains the `json` files for the questions and answers. We do not maintain the raw video files, and video files can be obtained from the official website: [ActivityNet 200 (v1.3)](http://activity-net.org/download.html)

## Evaluation
We provide a simple script and a exmaple prediction json file under the [eval](eval) folder to calculate the accuracy per type.  

`
python eval/eval.py --pred_file /eval/pred_val_examples.json --gt_file /dataset/val_a.json
`

## Licence

The code and the dataset are distributed under MIT LICENSE. They are only allowed for non-commercial use.

## Citation

If the project are helpful for your research, please cite

```
@inproceedings{yu2019activityqa,
    author    = {Yu, Zhou and Xu, Dejing and Yu, Jun and Yu, Ting and Zhao, Zhou and Zhuang, Yueting and Tao, Dacheng},
    title     = {ActivityNet-QA: A Dataset for Understanding Complex Web Videos via Question Answering},
    booktitle = {AAAI},
    year      = {2019}
}
```










