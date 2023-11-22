function dijkstra(graphq,startProduct){
    console.log(graphq)
    let n = graphq.length;
    console.log("n",n)
    let minDistances = new Array(n).fill(Infinity);
    let visited = new Array(n).fill(false);
    console.log(minDistances)
    console.log(visited)

    minDistances[startProduct]=0;
    console.log("minDistances",minDistances)

    for( let i=0;i<n;i++){
        let minIndex = -1;
        for(let j=0;j<n;j++){
            console.log("for j: "+ j + " the minIndex: "+ minIndex)
            if(!visited[j] && (minIndex===-1 || minDistances[j]<minDistances[minIndex])){
                console.log("minIndex changed from "+ minIndex + " to "+ j)
                minIndex = j;
            }
        }

        if( minDistances[minIndex]===Infinity){
            console.log("minDistances[minIndex] is : "+ minDistances[minIndex]+ " for minIndex: "+ minIndex)
            break;
        }

        visited[minIndex]=true;
        console.log("Updated visited: "+ visited)
        console.log(" previous minDistance: "+minDistances)
        for (let j=0; j<n; j++){
            if (graphq[minIndex][j]!== 0){
                console.log("minIndex: "+ minIndex + " J is : "+ j)
                let potentialDist = minDistances[minIndex]+ graphq[minIndex][j]
                if(potentialDist <minDistances[j]){
                    minDistances[j]=potentialDist
                }
                console.log("updated minDistance[j]: "+ minDistances[j])
                console.log(" updated minDistance: "+minDistances)
            }
        }
    }
    return minDistances

}


function clicEvent(){

    let graph1 = [
        [0,2,0,1,0],
        [2,0,3,0,0],
        [0,3,0,4,0],
        [1,0,4,0,5],
        [0,0,0,5,0]
    ]

    console.log(dijkstra(graph1,0));
}