document.addEventListener('DOMContentLoaded', ()=>{
    //Array of options
    const PanelArray = [
        {
            name:'im 1',
            img:'images/im 1.png'
        },
        {
            name:'im 1',
            img:'images/im 1.png'
        },
        {
            name:'im 2',
            img:'images/im 2.png'
        },
        {
            name:'im 2',
            img:'images/im 2.png'
        },
        {
            name:'im 3',
            img:'images/im 3.png'
        },
        {
            name:'im 3',
            img:'images/im 3.png'
        },
        {
            name:'im 4',
            img:'images/im 4.png'
        },
        {
            name:'im 4',
            img:'images/im 4.png'
        },
        {
            name:'im 5',
            img:'images/im 5.png'
        },
        {
            name:'im 5',
            img:'images/im 5.png'
        },
        {
            name:'im 6',
            img:'images/im 6.png'
        },
        {
            name:'im 6',
            img:'images/im 6.png'
        },
        {
            name:'im 7',
            img:'images/im 7.png'
        },
        {
            name:'im 7',
            img:'images/im 7.png'
        },
        {
            name:'im 8',
            img:'images/im 8.png'
        },
        {
            name:'im 8',
            img:'images/im 8.png'
        },
        {
            name:'im 9',
            img:'images/im 9.png'
        },
        {
            name:'im 9',
            img:'images/im 9.png'
        }
    ]

    PanelArray.sort(()=>0.5 - Math.random())
    const grid = document.querySelector('.grid')
    const displayResult = document.querySelector('#result')
    //create array for chosen panels
    var chosenPanels=[]
    var chosenPanelId = []
    var completedPanels = []
    //creating main game panel

    function createGamePanel(){
        for (let i = 0; i< PanelArray.length; i++){
            var imgPanel = document.createElement('img')
            imgPanel.setAttribute('src', 'images/grey.png')
            imgPanel.setAttribute('data-id', i)
            imgPanel.addEventListener('click',flipPanel)
            grid.appendChild(imgPanel)
        }
    }

    //check for matching panels
    function checkMatchingPanel() {
        var imgPanel = document.querySelectorAll('img')
        const panelOneId = chosenPanelId[0]
        const panelTwoId = chosenPanelId[1]
        if(chosenPanels[0] === chosenPanels[1]){
            alert('matching panels found')
            if(chosenPanels[0] === chosenPanels[1]) {
                imgPanel[panelOneId].setAttribute('src', 'images/'+ chosenPanels[0]+ ' green.png')
                imgPanel[panelTwoId].setAttribute('src', 'images/'+ chosenPanels[1]+ ' green.png')
            }
            completedPanels.push(chosenPanels)
        }
        else{
            imgPanel[panelOneId].setAttribute('src','images/'+ chosenPanels[0]+ ' red.png')
            imgPanel[panelTwoId].setAttribute('src','images/'+ chosenPanels[1]+ ' red.png')
            setTimeout(() => {  imgPanel[panelOneId].setAttribute('src','images/grey.png');
                imgPanel[panelTwoId].setAttribute('src','images/grey.png');
            }, 1000);

        }
        chosenPanels = []
        chosenPanelId = []
        displayResult.textContent = completedPanels.length.toString()
        if (completedPanels.length === PanelArray.length/2){
            displayResult.textContent='You have won'
        }
    }

    //flip panel function
    function flipPanel(){
        var panelId = this.getAttribute('data-id')
        chosenPanels.push(PanelArray[panelId].name)
        chosenPanelId.push(panelId)
        this.setAttribute('src',PanelArray[panelId].img)
        if (chosenPanels.length ===2){
            setTimeout(checkMatchingPanel, 600)
        }
    }

    createGamePanel()

})