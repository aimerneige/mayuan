#!/usr/local/bin/env python3
# -*- encoding: utf-8 -*-

import json
from os import system


def readfile(file_name, encoding):
    f = open(file_name, 'r', encoding=encoding)
    text = f.read()
    json_obj = json.loads(text)
    return json_obj['data']


def question(problem):
    system("clear")
    print(problem['question'])
    print()
    for option in problem['options']:
        print(option['mark'], option['data'])
    print()
    user_answer = input("请输入你的答案:\t")
    print()
    print("正确答案:\t %s" % problem['answer'])
    print("你的答案:\t %s" % user_answer)
    print()
    exit_or_not = input("回车继续，q 退出程序")
    return exit_or_not == 'q' or exit_or_not == 'Q'


def main():
    data = readfile('../data.json', 'utf-8')
    for problem in data:
        if question(problem):
            exit()


if __name__ == "__main__":
    main()

