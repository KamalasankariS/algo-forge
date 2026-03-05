fetch("data/xp.json")

.then(res => res.json())

.then(data => {

let level = data.level
let xp = data.xp

let xpRequired = level * 100

let progress = xp / xpRequired

let angle = progress * 360

document.getElementById("ring").style.background =
`conic-gradient(#00ffe1 ${angle}deg,#333 ${angle}deg)`

document.getElementById("level").innerText =
"Level " + level

document.getElementById("xp").innerText =
xp + " / " + xpRequired

})