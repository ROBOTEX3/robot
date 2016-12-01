module.exports = (status, obstacles) => {
    const a = Math.tan(status.rotate)
    const b = status.y - status.x * a
    const robotX = status.x
    const robotY = status.y
    const angle = Math.atan(1/2)
    const sensorPos = [
        {
            x: robotX + Math.sqrt(125) / Math.cos(status.rotate - angle),
            y: robotY + Math.sqrt(125) / Math.sin(status.rotate - angle)
        },
        {
            x: robotX + Math.sqrt(125) / Math.cos(status.rotate + angle),
            y: robotY + Math.sqrt(125) / Math.sin(status.rotate + angle)
        }
    ]
    const distances = []
    for (sensor of sensorPos) {
        var min = 1000
        for (obstacle of obstacles) {
            const w = obstacle.w
            const h = obstacle.h
            var x = obstacle.x
            for (y of [(x + w / 2) * a + b, (x - w / 2) * a + b]) {
                if (y >= obstacle.y - h / 2 && y <= obstacle.y + h / 2) {
                    const xPow = Math.pow(sensor.x - x, 2)
                    const yPow = Math.pow(sensor.y - y, 2)
                    const distance = Math.sqrt(xPow + yPow)
                    if (distance < min) {
                        min = distance
                    }
                }
            }
            var y = obstacle.y
            for (x of [(y - b + h / 2) / a, (x - b - w / 2) / a]) {
                if (x >= obstacle.x - w / 2 && x <= obstacle.x + w / 2) {
                    const xPow = Math.pow(sensor.x - x, 2)
                    const yPow = Math.pow(sensor.y - y, 2)
                    const distance = Math.sqrt(xPow + yPow)
                    if (distance < min) {
                        min = distance
                    }
                }
            }
        }
        distances.push(min)
    }
    return distances
}
