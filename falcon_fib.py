import json, falcon
from fibonacci import fib_it

# Lista de diccionarios (contendra toda la informacion)
datos_completos = []

def busqueda_id(datos, id_busc):
	index = 0
	for dic in datos:
		
		id_rev = dic.get('id') 
		if id_rev == id_busc:
			return index
		index += 1
	return -1



class ObjRequstClass:

	count = 1

	# Funcion GET: recibe arg json vacio 
	# Devuelve la lista con todas los datos calculados
	def on_get(self, req, resp):

		resp.body = json.dumps(datos_completos)


	# Funcion POST: recibe json "numero"
	# asigna un id autoincremental y lo almacena en la lista datos_completos
	def on_post(self, req, resp):
		resp.status = falcon.HTTP_200

		dato_rec = json.loads(req.stream.read())

		# verifica que se haya ingresado dato en la casilla "numero"
		try: 
			nuevo_numero = dato_rec['numero']
		except:
			output = {
				'msg' : 'Debe ingresar un int en la entrada "numero" '
					}
			resp.body = json.dumps(output)

			print "Error no hay entrada id"
			return


		nuevo_fib = fib_it(nuevo_numero)

		print "Numero ingresado:", nuevo_numero , ", Fibonacci:", nuevo_fib
	
		# Creamos el nuevo diccionario con los datos recibidos y el id correspondiente
		dato_nuevo = {'id': ObjRequstClass.count, 'numero': nuevo_numero, 'fibonacci': nuevo_fib}

		output = {
			'msg' : 'Registrado numero {0} y su fibonacci {1} '.format(nuevo_numero, nuevo_fib)
				}
		resp.body = json.dumps(output)

		datos_completos.append(dato_nuevo)

		ObjRequstClass.count +=1


	# Funcion PUT: "No implementada"
	def on_put(self, req, resp):
		resp.status = falcon.HTTP_200

		output = {
			'msg' : 'Funcion PUT no implementada ' 
				}
		resp.body = json.dumps(output)



	# Funcion DELETE: borra el dato de la lista
	# Recibe solo el id de dato a eliminar de la lista
	def on_delete(self, req, resp):
		resp.status = falcon.HTTP_200

		dato_rec = json.loads(req.stream.read())

		# Busqueda del dato por su indice
		res = busqueda_id(datos_completos, int(dato_rec['id']))

		if res >= 0:
			# Mensaje de confirmacion
			output = {
				'msg' : 'borrando dato con id {0}'.format(datos_completos[res]['id'])
			}
			resp.body = json.dumps(output)
			datos_completos.pop(res)

		else:
			msg_error = {
			'msg' : 'id no encontrado'
			}
			resp.body = json.dumps(msg_error)




api = falcon.API()
api.add_route('/demo', ObjRequstClass())
