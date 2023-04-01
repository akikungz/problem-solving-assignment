const startProvinces = document.getElementById("start-province")
const endProvinces = document.getElementById("end-province")
const result = document.getElementById("result")

const appState = {
    start: false,
    end: false
}

startProvinces.onchange = ({ target }) => {
    if(target.value != "none"){
        appState.start = true
    } else {
        appState.start = false
    }
}

endProvinces.onchange = ({ target }) => {
    if (target.value != "none") {
        appState.end = true
    } else {
        appState.end = false
    }
}

document.getElementById("confirm").onclick = async () => {
    result.innerHTML = ""
    if(appState.start == appState.end && appState.start == true) {
        const shortestPath = await eel.getShortestPath(startProvinces.value, endProvinces.value)()

        const path = shortestPath[0]
        const distance = shortestPath[1]

        const p2p = document.createElement("p")
        p2p.innerText = `You will be travelling from ${startProvinces.value} to ${endProvinces.value}.`

        const path2path = document.createElement("p")
        path2path.innerText = `The shortest distance between ${startProvinces.value} and ${endProvinces.value} is ${distance} km.`

        const subpath = document.createElement("p")
        subpath.innerText = "The shortest path is "
        
        for(let i = 0; i < path.length; i++){
            subpath.innerText += path[i]
            if(i + 1 != path.length) subpath.innerText += " > "
        }

        result.append(p2p)
        result.append(path2path)
        result.append(subpath)

        console.log(shortestPath)
    } else {
        alert("Plese select start and end province")
    }
}

document.getElementById("reset").onclick = () => window.location.reload()