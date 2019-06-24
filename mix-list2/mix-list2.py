#/usr/bin/python3

proto=['ssh','http','https']
protoa=['ssh','http','https']
proto2=[22,80,443,53]
print (proto)
#print (proto[1])

proto.append('dns')
print (proto)

proto.extend(proto2)
print (proto)

#proto.extend(['dns'])
#print (proto)

proto.append(proto2)
print (proto)
