import argparse
import json


def stastic(preds, results):
    corrects = {i: 0 for i in range(0, 9)}

    result_d = {}
    type_count = {}
    for res in results:
        result_d[res['question_id']] = res
        res_type = res['type']
        type_count[res_type] = type_count.get(res_type, 0)+1


    for pt in preds:
        pt_answer = pt['answer']
        pt_question_id = pt['question_id']
        pt_type = result_d[pt_question_id]['type']
        if pt_answer == result_d[pt_question_id]['answer']:
            corrects[pt_type] += 1

    return corrects, type_count

def output(corrects, type_count):

    all_type_corrects_count = sum(corrects.values())
    free_type_corrects_count = sum(list(corrects.values())[3:])

    accuracy = {}
    for type_id in corrects:
        accuracy[type_id] = corrects[type_id]/float(type_count[type_id])

    all_type_accuracy = all_type_corrects_count / float(sum(type_count.values()))

    free_type_accuracy = free_type_corrects_count / float(sum(list(type_count.values())[3:]))

    print('Motion: {:.04f}, Spat.Rel.: {:.04f}, Temp.Rel.: {:.04f}, Free: {:.04f}, All: {:.04f}'.format(accuracy[0], accuracy[1], accuracy[2], free_type_accuracy, all_type_accuracy))
    print('Yes/No: {:.04f}, Color: {:.04f}, Object: {:.04f}, Location: {:.04f}, Number: {:.04f}, Other: {:.04f}'.format(accuracy[3], accuracy[4], accuracy[5], accuracy[6], accuracy[7], accuracy[8]))

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pred_json', type=str, default='/data1/yuting/esa_test1/valpred.json',
                        help='path to the json file containing your prediction')
    parser.add_argument('--result_json', type=str, default='/data1/yuting/ActivityNetQA/val_a.json',
                        help='path to the json file containing the ground true')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    opt = parse_opt()
    preds = json.load(open(opt.pred_json, 'r'))
    results = json.load(open(opt.result_json, 'r'))
    corrects, type_count = stastic(preds, results)
    output(corrects, type_count)