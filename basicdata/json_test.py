import json

from flask import request

if __name__ == '__main__':
    req_data = request.form.get("reqData", type=str, default=None)
    # data = request.get_data()
    # data = json.loads(data)
    # trace_id = data['traceId']
    # req_data = data['reqData']
    # json_array = list_to_json(req_data)

    # 将请求json数据转成python数据
    json_array = json.loads(req_data, encoding='utf-8')

    result_dict = {}
    result_dict['traceId'] = "trace_id"
    result_dict['traceId1'] = "trace_id1"
    # 将python的字典数据转换成json
    ret = json.dumps(result_dict, ensure_ascii=False)