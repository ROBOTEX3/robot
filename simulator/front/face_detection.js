module.exports = (status, faces, ctx) => {
    const angle = status.rotate
    const v1 = {x: status.x, y: status.y}
    const v2 = {
        x: status.x + Math.cos(angle + Math.PI / 6) * 150,
        y: status.y + Math.sin(angle + Math.PI / 6) * 150
    }
    const v3 = {
        x: status.x + Math.cos(angle - Math.PI / 6) * 150,
        y: status.y + Math.sin(angle - Math.PI / 6) * 150
    }

    const positions = []
    for (face of faces) {
        const z1 = (v2.x - v1.x) * (face.y - v1.y) - (v2.y - v1.y) * (face.x - v1.x)
        const z2 = (v3.x - v2.x) * (face.y - v2.y) - (v3.x - v2.x) * (face.x - v2.x)
        const z3 = (v1.x - v3.x) * (face.y - v3.y) - (v1.y - v3.y) * (face.x - v3.x)
        if (z1 < 0 && z2 < 0 && z3 < 0) {
            const dir = Math.tan(face.y / face.x) - angle
            const distance = Math.sqrt(Math.pow(face.x - v1.x, 2) + Math.pow(face.y - v1.y, 2))
            positions.push({
                x: dir / (Math.PI / 6),
                y: 1 - distance / 40
            })
        }
    }
    drawSensorArea(v1, v2, v3, ctx)
    return positions
}

const drawSensorArea = (v1, v2, v3, ctx) => {
    ctx.beginPath()
    ctx.moveTo(300 + v1.x, 200 + v1.y)
    ctx.lineTo(300 + v2.x, 200 + v2.y)
    ctx.lineTo(300 + v3.x, 200 + v3.y)
    ctx.lineTo(300 + v1.x, 200 + v1.y)
    ctx.stroke()
}
