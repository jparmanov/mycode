#!/usr/bin/python3

import yaml

def main():
    yammyfile=open('/home/student/mycode/yamlintor/myYAML.yml','r')

    pyyammy=yaml.load(yammyfile)

    print(pyyammy)

main()
