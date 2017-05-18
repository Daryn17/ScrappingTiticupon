'use strict'

const mongoose = require('mongoose')
const Schema = mongoose.Schema

const CuponSchema = Schema({
    imagen: String,
    informacion: String,
    precioActual: String,
    ahorro: String,
    finaliza: String,
    tipo: String,
    precioOriginal: String,
    lugar: String,
    periodoDeUso: String,
    horario: String,
    comoLlegar: String,
    visitas: Number
})

module.exports = mongoose.model('Cupon', CuponSchema)