const test = document.getElementById('test')


const wait1 = (ms) =>{ new Promise( resolve => setTimeout(resolve,ms))}

for (let i=0; i<10; i++) {
    task(i);
}

function task(i) {
    setTimeout(function() {
        test.innerHTML=i
    }, 2000 * i);
}

var max = `{{func[1]}}`
max=parseInt(max)
var data = `{{func[0]}}`


// We might need loops to pause on iterations
const wait = (ms) =>{ new Promise( resolve => setTimeout(resolve,ms))}
// lets store all the algos in a dict
const algo = {
    //Selection sort
    selectionSort: async (data)=>{
        var index = 0
        
        var finalMinIndex
        var finalMin
        var currMin
        var length = data.length
        var sorted = false
        data=JSON.parse(data)
        
        
        for(var iter=0; iter<data.length; iter++){
            
            finalMin=undefined
            currMin=undefined
            index++
            for(var i=index; i<length-1; i++){
                
                if(data[index]>data[i]){
                    console.log(data[i])
                    currMin=data[i]    
                    if(finalMin==undefined){
                        finalMin=currMin
                        finalMinIndex=i
                    }else if(currMin<finalMin){
                        finalMin=currMin
                        finalMinIndex=i
                        console.log(finalMin, ' final and index ' , finalMinIndex)
                    }

                }
                
            }
            if(finalMin!=undefined){
                console.log( data[finalMinIndex]," : ",data[index] )
                data[finalMinIndex]=data[iter]
                data[iter]=finalMin
            }
            console.log('run'+iter)
            setTimeout(() => {
                updateTable(data)
                
            }, 2000);
            
            await wait(2000)      
        }
        
    },
}
//EOF algo

const table = document.getElementById('table')
function updateTable(data){
    table.innerHTML=''
    for(var iter1=0; iter1<data.length; iter1++){
            table.innerHTML=table.innerHTML+`
            <div class="item" style="--item-height: ${data[iter1]/max*100}%">
                ${data[iter1]}
            </div>
            `
    }
}
algo.selectionSort(data)