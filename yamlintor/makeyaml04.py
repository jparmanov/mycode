#!/usr/bin/python3

import yaml

def main():
    yammyfile=open('/home/student/mycode/yamlintor/myYAML.yml','r')

    pyyammy=yaml.load(yammyfile,Loader=yaml.FullLoader)

    yammyfile.close()

    print (pyyammy)

    pyyammy[0]['apps'].append('minecraft')

    print (pyyammy)


    yammyfile2=open('/home/student/mycode/yamlintor/myYAML.yml.updated','w')

    yaml.dump(pyyammy,yammyfile2)

    yammyfile2.close()

main()
