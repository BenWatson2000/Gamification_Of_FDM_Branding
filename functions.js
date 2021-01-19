const functions = {
        returnIntTime(timeString){
        let mins = timeString.slice(0,2)
        let secs = timeString.slice(3,5)
        let totalMins = parseInt(mins)
        let totalSecs = parseInt(secs)

        let timeBeforeChange = (totalMins * 60) + totalSecs

        return 120 - timeBeforeChange
    }

};

module.exports = functions;