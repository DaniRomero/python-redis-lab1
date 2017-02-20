import redis

r = redis.StrictRedis(host='localhost', port=6379, db=1)
archivo = open("entrada.in", "r")

#######################
### REQUERIMIENTO 1 ###
#######################
line = archivo.readline()
for line in archivo:
	line = line.split()
	clave = line[0]
	valor = line[1]
	r.set(clave,valor)


# print 'a) Se han insertado exitosamente {} '.format(cant_reg)


#######################
### REQUERIMIENTO 2 ###
#######################
cant_start = r.get('start')
cant_help = r.get('help')
cant_turns = r.get('turns')
cant_twenty = r.get('twenty')
cant_uncle = r.get('uncle')
cant_undone = r.get('undone')
cant_place = r.get('place')
cant_pity = r.get('pity')
cant_into = r.get('into')
cant_end = r.get('end')

# print 'b) La frecuencia de las palabras solicitadas es '
print '\tstart {}'.format(cant_start)
print '\thelp {}'.format(cant_help)
print '\tturns {}'.format(cant_turns)
print '\ttwenty {}'.format(cant_twenty)
print '\tuncle {}'.format(cant_uncle)
print '\tundone {}'.format(cant_undone)
print '\tplace {}'.format(cant_place)
print '\tpity {}'.format(cant_pity)
print '\tinto {}'.format(cant_into)
print '\tend {}'.format(cant_end)


#######################
### REQUERIMIENTO 3 ###
#######################

tam_db = r.dbsize()
archivo.seek(0)
line = archivo.readline()
for line in archivo:
	line = line.split()
	clave = line[0]
	valor = line[1]
	r.zadd('sorted_list',valor,clave)
	
minmax = r.zrange('sorted_list', tam_db-11, tam_db)


# print 'c) Las 10 palabras con la frecuencia mas alta son '

for j in range(len(minmax)-1,-1,-1):
	print '\t{} {}'.format(minmax[j], r.get(minmax[j]))