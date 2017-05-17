'use strict'

const Cupon = require('../modelos/cupon')


function getCupon(req, res){
	let cuponId = req.params.cuponId
	Cupon.findById(cuponId, (err, cupon) => {
		if (err) return res.status(500).send({message: `Error al realizar la petición ${err}`})

		if (!cupon) return res.status(404).send({message: 'El cupon no exixte'})

		res.status(200).send({cupon})
	})
}

function getCupones(req, res){

	Cupon.find({}, (err, cupones) => {
		if(err) return res.status(500).send({message:`Error al realizar la petición: ${err}`})
		if (!cupones) return res.status(404).send({message:'No existen cupones'})

		//res.send(200, {cupones})
		res.status(200).send({cupones})
	})
}

function updateCupon(req, res){
	let cuponId = req.params.cuponId
	let update = req.body

	Cupon.findByIdAndUpdate(cuponId, update ,(err, cuponUpdate) => {
		if (err) return res.status(500).send({message: `Error al actualizar el cupon ${err}`})

		res.status(200).send({cupon: cuponUpdate})
	})
}

function deleteCupon(req, res){
	let cuponId = req.params.cuponId

	Cupon.findById(cuponId, (err, cupon) => {
		if (err) return res.status(500).send({message: `Error al borrar el cupon ${err}`})

		cupon.remove(err => {
			if (err) return res.status(500).send({message: `Error al borrar el cupon ${err}`})
			res.status(200).send({message: 'El cupon ha sido eliminado'})
		})
	})
}

function postCupon (req, res){
	let cupon = new Cupon()
	console.log("Sii...........")
	console.log(req)
	/*cupon.imagen = req.query["imagen"]
	cupon.informacion = req.body.informacion
	cupon.precio = req.body.precio
	cupon.ahorro = req.body.ahorro
	cupon.finaliza = req.body.finaliza
	cupon.tipo = req.body.tipo

	cupon.save((err, cuponStored) =>{
		if(err) res.status(500).send({message: `Error al salvar en la base de datos: ${err}`})

		res.status(200).send({cupon: cuponStored})
	})*/
	res.status(200)
}

module.exports = {
	getCupon,
	getCupones,
	updateCupon,
	deleteCupon,
	postCupon
}