# coding: utf-8
# create by tongshiwei on 2019-8-14

from longling import as_out_io

from EduData.Task.KnowledgeTracing import tl2json, json2tl

TL_STR = """15
1,1,1,1,7,7,9,10,10,10,10,11,11,45,54
0,1,1,1,1,1,0,0,1,1,1,1,1,0,0
15
1,1,1,1,7,7,9,10,10,10,10,11,11,45,54
0,1,1,1,1,1,0,0,1,1,1,1,1,0,0
15
1,1,1,1,7,7,9,10,10,10,10,11,11,45,54
0,1,1,1,1,1,0,0,1,1,1,1,1,0,0
"""


def test_tl_json(tmpdir):
    tl_file = str(tmpdir / "demo.tl")
    json_file = str(tmpdir / "demo.json")

    with as_out_io(tl_file) as wf:
        print(TL_STR, file=wf, end='')

    tl2json(tl_file, json_file)
    json2tl(json_file, tl_file)

    with open(tl_file) as f:
        assert f.read() == TL_STR

    tl2json(tl_file, json_file, left_shift=True)
