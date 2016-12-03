module.exports = (status, obstacles, ctx) => {
    const a = Math.tan(status.rotate)
    const robotX = status.x
    const robotY = status.y
    const angle = Math.atan(1/2)
    const sensorPos = [
        {
            x: robotX + Math.sqrt(125) * Math.cos(status.rotate - angle),
            y: robotY + Math.sqrt(125) * Math.sin(status.rotate - angle)
        },
        {
            x: robotX + Math.sqrt(125) * Math.cos(status.rotate + angle),
            y: robotY + Math.sqrt(125) * Math.sin(status.rotate + angle)
        }
    ]
    const distances = []
    for (sensor of sensorPos) {
        const b = sensor.y - sensor.x * a
        var min = 1000
        for (obstacle of obstacles) {
            const w = obstacle.w
            const h = obstacle.h
            var x = obstacle.x
            for (pos of [{x: x + w/ 2, y: (x + w / 2) * a + b}, {x: x - w / 2, y: (x - w / 2) * a + b}]) {
                if (pos.y >= obstacle.y - h / 2 && pos.y <= obstacle.y + h / 2) {
                    const xPow = Math.pow(sensor.x - pos.x, 2)
                    const yPow = Math.pow(sensor.y - pos.y, 2)
                    const distance = Math.sqrt(xPow + yPow)
                    if (distance < min) {
                        min = distance
                    }
                }
            }
            var y = obstacle.y
            for (pos of [{x: (y - b + h / 2) / a, y: y + h / 2}, {x: (y - b - h / 2) / a, y: y - h / 2}]) {
                if (pos.x >= obstacle.x - w / 2 && pos.x <= obstacle.x + w / 2) {
                    const xPow = Math.pow(sensor.x - pos.x, 2)
                    const yPow = Math.pow(sensor.y - pos.y, 2)
                    const distance = Math.sqrt(xPow + yPow)
                    if (distance < min) {
                        min = distance
                    }
                }
            }
        }
        drawSensor(ctx, sensor.x, sensor.y, status.rotate, min)
        distances.push(min)
    }
    return distances
}

const drawSensor = (ctx, x, y, angle, length) => {
    ctx.beginPath()
    ctx.moveTo(300 + x, 200 + y)
    ctx.lineTo(300 + x + Math.cos(angle) * length, 200 + y + Math.sin(angle) * length)
    ctx.stroke()
}
