'use strict'

const mongoose = require('mongoose')
const Schema = mongoose.Schema

const UsuarioSchema = Schema({
	nombre: String,
	correo: String,
	clave: String,
	administrador: Boolean
})

module.exports = mongoose.model('Usuario', UsuarioSchema)


