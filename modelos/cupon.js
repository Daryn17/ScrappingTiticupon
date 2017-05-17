'use strict'

const mongoose = require('mongoose')
const Schema = mongoose.Schema

const CuponSchema = Schema({
    imagen: String,
    informacion: String,
    precio: String,
    ahorro: String,
    finaliza: String,
    tipo: String
})

module.exports = mongoose.model('Cupon', CuponSchema)