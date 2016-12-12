const express = require('express')
const app = express()
const http = require('http').createServer(app);
const io = require('socket.io')(http);

var response = null

http.listen(3000, () => {
    console.log('simulation server is listening on port 3000')
})

io.on('connection', (socket) => {
    console.log('connected')
    socket.on('camera:response', (msg) => {
        console.log(msg)
        cameraResponse.send(JSON.stringify(msg))
    })
    socket.on('sensor:response', (msg) => {
        console.log(msg)
        sensorResponse.send(JSON.stringify(msg))
    })
    socket.on('voice:response', (msg) => {
        console.log(msg)
        voiceResponse.send(msg)
    })
})

app.use(express.static('public'));

app.post('/motor/move', (req, res, next) => {
    console.log('motor/move ' + JSON.stringify(req.query))
    io.emit('motor:move', req.query)
    res.send('')
})

app.post('/motor/stop', (req, res, next) => {
    console.log('motor/stop')
    io.emit('motor:stop', {})
    res.send('')
})

var cameraResponse = null
app.post('/camera/face_detection', (req, res, next) => {
    console.log('camera/face_detection')
    io.emit('camera:face_detection', {})
    cameraResponse = res
})

var sensorResponse = null
app.post('/sensor/distant', (req, res, next) => {
    console.log('sensor/distant')
    io.emit('sensor:distant', {})
    sensorResponse = res
})

var voiceResponse = null
app.post('/voice', (req, res, next) => {
    console.log('voice')
    io.emit('voice', {})
    voiceResponse = res
})
