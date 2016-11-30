const io = require('socket.io-client')
const obstacles = require('./obstacles')
const sensor = require('./sensor')

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
    const distance = sensor(status, obstacles)
    socket.emit('sensor:response', {right: distance, left: distance})
})

const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
const draw = (status) => {
    ctx.setTransform(1, 0, 0, 1, 0, 0)
    ctx.clearRect(0, 0, 600, 400);
    drawRobot(status)
    drawObstacles(status, obstacles)
}
const drawRobot = (status) => {
    ctx.setTransform(1, 0, 0, 1, 0, 0)
    ctx.translate(300 + status.x, 200 + status.y)
    ctx.rotate(status.rotate)
    ctx.strokeRect(-10, -5, 20, 10)
    ctx.setTransform(1, 0, 0, 1, 0, 0)
}
const drawObstacles = (status, obstacles) => {
    ctx.setTransform(1, 0, 0, 1, 0, 0)
    ctx.translate(300, 200)
    for (obstacle of obstacles) {
        const w = obstacle.w
        const h = obstacle.h
        ctx.strokeRect(obstacle.x - w / 2, obstacle.y - h / 2, w, h)
    }
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
