const io = require('socket.io-client')

const socket = io()

var status = {
    right_speed: 0,
    left_speed: 0,
    x: 0,
    y: 0,
    rotate: 0
}

socket.on('motor:move', (msg) => {
    console.log(msg)
    status.right_speed = msg.right
    status.left_speed = msg.left
})

socket.on('motor:stop', (msg) => {
    console.log('stop')
    status.right_speed = 0
    status.left_speed = 0
})

socket.on('camera:face_detection', (msg) => {
    console.log('face_detection')
    socket.emit('camera:response', {faces: []})
})

socket.on('sensor:distant', (msg) => {
    console.log('distant')
    socket.emit('sensor:response', {right: 100 - status.x, left: 100})
})

setInterval(() => {
    status.x += Math.cos(status.rotate) * (status.right_speed / 10)
    status.y += Math.sin(status.rotate) * (status.left_speed / 10)
    var span = document.getElementById('text')
    span.innerHTML = JSON.stringify(status)
}, 1000)
