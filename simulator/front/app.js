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
    status.right_speed = msg.right - 30
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

const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
const draw = (status) => {
    ctx.setTransform(1, 0, 0, 1, 0, 0)
    ctx.clearRect(0, 0, 600, 400);
    ctx.strokeRect(400, 150, 20, 20)
    drawRobot(status)
}
const drawRobot = (status) => {
    ctx.setTransform(1, 0, 0, 1, 0, 0)
    ctx.translate(300 + status.x, 200 + status.y)
    ctx.rotate(status.rotate)
    ctx.strokeRect(-10, -5, 20, 10)
    ctx.setTransform(1, 0, 0, 1, 0, 0)
}

setInterval(() => {
    status.x += Math.cos(status.rotate) * (status.right_speed / 100)
    status.y += Math.sin(status.rotate) * (status.left_speed / 100)
    status.rotate += Math.PI * (status.right_speed - status.left_speed) / 100 / 180
    var span = document.getElementById('text')
    span.innerHTML = JSON.stringify(status)
    draw(status)
}, 100)
