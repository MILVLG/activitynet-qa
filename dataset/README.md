# Dataset

## Splits
train: 32,000 QA pairs on 3,200 videos

val: 18,000 QA pairs on 1,800 videos

test: 8,000 QA pairs on 800 videos

## Question Format
All the questions are stored in the `*_q.json` files. Each entry in the json file is of the following format.

```
{
  "video_name": str, 
  "question": str, 
  "question_id": str
}
```
The `video_name` field corresponds to the orginal video id in the ActivityNet dataset, the url for this video is `https://www.youtube.com/watch?v=<video_name>`. The `question_id` field refer to the unique id for the question in the dataset. The `question` field contains the questions in English.


## Answer Format
All the answers are stored in the `*_a.json` files. Each entry in the file is of the following format. 

```
{
  "answer": str, 
  "type": int, 
  "question_id": str
}
```

The `answer` field contains the answer with respect to the question with `question_id`
The `type` file contains the question or answer types for this question: 

Question types: [0].Motion  [1].Spatial Relationship  [2].Temporal Relationship  [3-8].Free

Answer types: [3].Yes/No  [4].Color  [5].Object  [6].Location  [7].Number  [8].Other


