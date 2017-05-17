'use strict'

const express = require('express')
const bodyParser = require('body-parser')

const app = express()

const UsuarioCtrl = require('./controlador/usuario')
const CuponCtrl = require('./controlador/cupon')


app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

//----------------------------------------------------------------------------


app.get('/usuario', UsuarioCtrl.getUsuarios)

app.get('/usuario/:usuarioId', UsuarioCtrl.getUsuario)

app.post('/usuario', UsuarioCtrl.postUsuario)

app.put('/usuario/:usuarioId',UsuarioCtrl.updateUsuario)

app.delete('/usuario/:usuarioId',UsuarioCtrl.deleteUsuario)

//----------------------------------------------------------------------------

//----------------------------------------------------------------------------


app.get('/cupon', CuponCtrl.getCupones)

app.get('/cupon/:cuponId', CuponCtrl.getCupon)

app.post('/cupon', CuponCtrl.postCupon)

app.put('/cupon/:cuponId',CuponCtrl.updateCupon)

app.delete('/cupon/:cuponId',CuponCtrl.deleteCupon)

//----------------------------------------------------------------------------


module.exports = app