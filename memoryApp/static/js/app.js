document.addEventListener('DOMContentLoaded', ()=>{
    //Array of options
    const PanelArray = [
        {
            name:'im 1',
            img:'/static/images/im 1.png'
        },
        {
            name:'im 1',
            img:'/static/images/im 1.png'
        },
        {
            name:'im 2',
            img:'/static/images/im 2.png'
        },
        {
            name:'im 2',
            img:'/static/images/im 2.png'
        },
        {
            name:'im 3',
            img:'/static/images/im 3.png'
        },
        {
            name:'im 3',
            img:'/static/images/im 3.png'
        },
        {
            name:'im 4',
            img:'/static/images/im 4.png'
        },
        {
            name:'im 4',
            img:'/static/images/im 4.png'
        },
        {
            name:'im 5',
            img:'/static/images/im 5.png'
        },
        {
            name:'im 5',
            img:'/static/images/im 5.png'
        },
        {
            name:'im 6',
            img:'/static/images/im 6.png'
        },
        {
            name:'im 6',
            img:'/static/images/im 6.png'
        },
        {
            name:'im 7',
            img:'/static/images/im 7.png'
        },
        {
            name:'im 7',
            img:'/static/images/im 7.png'
        },
        {
            name:'im 8',
            img:'/static/images/im 8.png'
        },
        {
            name:'im 8',
            img:'/static/images/im 8.png'
        },
        {
            name:'im 9',
            img:'/static/images/im 9.png'
        },
        {
            name:'im 9',
            img:'/static/images/im 9.png'
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
            imgPanel.setAttribute('src', '/static/images/grey.png')
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
        if (panelOneId == panelTwoId){
            imgPanel[panelOneId].setAttribute('src','/static/images/'+ chosenPanels[0]+ ' red.png')
            setTimeout(() => {  imgPanel[panelOneId].setAttribute('src','/static/images/grey.png');
            }, 1000);
        }


        else if(chosenPanels[0] === chosenPanels[1]){
            alert('matching panels found')
            if(chosenPanels[0] === chosenPanels[1]) {
                imgPanel[panelOneId].setAttribute('src', '/static/images/'+ chosenPanels[0]+ ' green.png')
                imgPanel[panelTwoId].setAttribute('src', '/static/images/'+ chosenPanels[1]+ ' green.png')
            }
            completedPanels.push(chosenPanels)
        }
        else{
            imgPanel[panelOneId].setAttribute('src','/static/images/'+ chosenPanels[0]+ ' red.png')
            imgPanel[panelTwoId].setAttribute('src','/static/images/'+ chosenPanels[1]+ ' red.png')
            setTimeout(() => {  imgPanel[panelOneId].setAttribute('src','/static/images/grey.png');
                imgPanel[panelTwoId].setAttribute('src','/static/images/grey.png');
            }, 1000);

        }
        chosenPanels = []
        chosenPanelId = []
        displayResult.textContent = completedPanels.length.toString()
        if (completedPanels.length === PanelArray.length/2){
            displayResult.textContent='You have won'
        }
    }

    function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = 0;
            if(alert('time has run out')){}
            else window.location.reload();
            // timer = duration; // uncomment this line to reset timer automatically after reaching 0
        }
    }, 1000);
}

window.onload = function () {
    var time = 60 / 2, // your time in seconds here
        display = document.querySelector('#timer');
    startTimer(time, display);
};


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