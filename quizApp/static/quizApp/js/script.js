const nextButton = document.getElementById('next-btn')
const finishedButton = document.getElementById('finished-btn')
const redirectButton = document.getElementById('redirect-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')
const responseElement = document.getElementById('result-response')

let count = 0

let shuffledQuestions, currentQuestionIndex

let softwareTest, businessIntel, techOperations, tempST, tempBI, tempTO

nextButton.addEventListener('click', () => {
    currentQuestionIndex++
    count = 0

    Array.from(answerButtonsElement.children).forEach(button => {
        if (button.classList.contains("selected")) {
            if (button.dataset.ST) {
                softwareTest = softwareTest + 5
            }
            if (button.dataset.BI) {
                businessIntel = businessIntel + 5
            }
            if (button.dataset.TO) {
                techOperations = techOperations + 5
            }
        }
    })

    console.log("Current Score: Software Testing-",softwareTest
        ," Business Intelligence-",businessIntel, "Technical Operations-",techOperations)
    setNextQuestion()
})


function startGame() {
    shuffledQuestions = questions.sort(() => Math.random() - .5)
    currentQuestionIndex = 0
    softwareTest = 0
    businessIntel = 0
    techOperations = 0
    setNextQuestion()
    questionContainerElement.classList.remove('hide')
}

function setNextQuestion() {
    resetState()
    showQuestion(shuffledQuestions[currentQuestionIndex])
}

function showQuestion(question) {
    questionElement.innerText = question.question
    question.answers.forEach(answer => {
        const button = document.createElement('button')
        button.innerText = answer.text
        button.classList.add('btn')
        if (answer.ST) {
            button.dataset.ST = answer.ST
        }
        if (answer.BI) {
            button.dataset.BI = answer.BI
        }
        if (answer.TO) {
            button.dataset.TO = answer.TO
        }
        button.addEventListener('click', selectAnswer)
        answerButtonsElement.appendChild(button)
    })
}

function resetState() {
    nextButton.classList.add('hide')
    while (answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild)
    }
}

function endState() {
    resetState()
    questionElement.classList.add("hide")
    finishedButton.classList.add("hide")
    let labels1 = ['Software Testing', 'Technical Operations',"Business Intelligence"];
    let colors1 = ['#49A9EA', '#36CAAB','#008000'];
    let pieChart = document.getElementById("myChart").getContext('2d');

    let chart1 = new Chart(pieChart, {
        type: 'pie',
        data: {
            labels: labels1,
            datasets: [ {
                data: [softwareTest,techOperations,businessIntel],
                backgroundColor: colors1
            }]
        },
        options: {
            title: {
                text: "Results",
                display: true,
                fontSize: 20
            },
            responsive: false,
            maintainAspectRatio: false,
            showScale: false,
        }
    })
    redirectButton.classList.remove("hide")

    let arrayOfOutcomes = []
    let highScore = Math.max(softwareTest,techOperations,businessIntel)
    if (softwareTest === highScore){
        arrayOfOutcomes.push("Software Testing")
    }
    if (techOperations === highScore){
        arrayOfOutcomes.push("Technical Operations")
    }
    if (businessIntel === highScore){
        arrayOfOutcomes.push("Business Intelligence")
    }
    let textOutput = 'From this test we can suggest to you that you would be good at'
    let count = 0
    arrayOfOutcomes.forEach(outcome => {
        if (count !== 0){
            textOutput = textOutput + " and " + outcome
        } else {
            textOutput = textOutput + " " + outcome
        }
        count ++
    })
    textOutput = textOutput + "."

    responseElement.innerText = textOutput
    responseElement.classList.remove("hide")
}

function selectAnswer(e) {

    let question = shuffledQuestions[currentQuestionIndex]
    let numOfSelections = question.selections

    const selectedButton = e.target

    if (selectedButton.classList.contains("selected")){
        selectedButton.classList.remove("selected")
        count--
        if (count === 0){
            nextButton.classList.add("hide")
        }
    } else if (count !== question.selections) {

        selectedButton.classList.add('selected')

        count = 0

        Array.from(answerButtonsElement.children).forEach(button => {
            if (button.classList.contains("selected")) {
                count++
            }
        })
        console.log(count)

        if (shuffledQuestions.length > currentQuestionIndex + 1) {
            nextButton.classList.remove('hide')
        } else {
            finishedButton.classList.remove("hide")

            finishedButton.addEventListener("click", endState)
            // startButton.innerText = 'Restart'
            // startButton.classList.remove('hide')
        }
    }
}

const questions = [
    {
        question: 'Choose up to 3 skills you can identify yourself with the most: ',
        answers: [
            {text: 'Strategic Thinking',ST:true,BI:true,TO:false},
            {text: 'Objectivity',ST:true,BI:false,TO:false},
            {text: 'Ability to work under pressure',ST:false,BI:false,TO:true},
            {text: 'Creativity',ST:true,BI:false,TO:false},
            {text: 'Customer service skills',ST:false,BI:false,TO:true},
            {text: 'Team-player',ST:false,BI:true,TO:false},
            {text: 'Quality-driven',ST:false,BI:true,TO:false},
            {text: 'Attention to detail',ST:true,BI:true,TO:false},
            {text: 'Innovative thinking',ST:true,BI:false,TO:true},
            {text: 'Ability to work in dynamic environment',ST:false,BI:false,TO:true},
            {text: 'Strong communicator',ST:true,BI:true,TO:true},
            {text: 'Quick-wit and situational orientation skills',ST:false,BI:false,TO:true},
        ],
        selections: 3
    },
    {
        question: 'Choose up to 3 sentences that describe you best: ',
        answers: [
            {text: 'I would like a career which combines technology and development with business and management.',
                ST:false,BI:false,TO:true},
            {text: 'I am looking for a career in technology which will see me involved in each stage of software development.',
                ST:true,BI:false,TO:true},
            {text: 'I think it is of great importance that businesses understand and learn to use the data they collect, and I could help them do it.',
                ST:false,BI:true,TO:false},
            {text: 'I want to have access to the newest, cutting-edge technologies in my line of your work.',
                ST:true,BI:false,TO:false},
            {text: 'I would like to learn more about how modern technology supports today’s businesses.',
                ST:false,BI:true,TO:true},
            {text: 'I want to work closely with clients, for example by offering them technical support and making sure all their platforms are online and working.',
                ST:false,BI:false,TO:true},
            {text: 'I would like to use data to help my company strategically plan future steps.',
                ST:false,BI:true,TO:false},
            {text: 'I am more interested in the technical than the business side of things',
                ST:true,BI:false,TO:false},
        ],
        selections: 3
    },
    {
        question: 'Which of these sound the most interesting to you? (choose up to 3):',
        answers: [
            {text: 'Automation Testing',
                ST:true,BI:false,TO:false},
            {text: 'Cloud Engineering',
                ST:false,BI:false,TO:true},
            {text: 'Data Analysis ',
                ST:false,BI:true,TO:false},
            {text: 'Site Reliability',
                ST:false,BI:false,TO:true},
            {text: 'Operational Acceptance Testing ',
                ST:true,BI:false,TO:false},
            {text: 'Database Management',
                ST:false,BI:true,TO:false},
            {text: 'Security Testing',
                ST:true,BI:false,TO:false},
            {text: 'Information Security ',
                ST:false,BI:false,TO:true},
            {text: 'Platform Engineering',
                ST:false,BI:false,TO:true},
            {text: 'Predictive Analysis',
                ST:false,BI:true,TO:false},
        ],
        selections: 3
    },
    {
        question: 'Which of these are you most confident in doing?:',
        answers: [
            {text: 'Working in a small group of people.',
                ST:true,BI:false,TO:false},
            {text: 'Working with a large number of customers.',
                ST:false,BI:false,TO:true},
            {text: 'Working with businesses and public speaking.',
                ST:false,BI:true,TO:false},
        ],
        selections: 1
    },
    {
        question: 'How do you make decisions?:',
        answers: [
            {text: 'I take my time dissecting the problem and then use context to make an informed decision.',
                ST:false,BI:false,TO:true},
            {text: 'I look at the time I have to solve this problem and depending on how long that is, I will make my decision as quickly as I can.',
                ST:true,BI:false,TO:false},
            {text: 'I will speak to other professionals to help solve this problem and use their expertise to make an informed decision.',
                ST:false,BI:true,TO:false},
        ],
        selections: 1
    },
]

startGame();