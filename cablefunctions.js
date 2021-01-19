const functions = {
    shuffle (array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
    },

    formatTime(seconds){
        //minutes
        var minutes = Math.floor(seconds/60);
        //seconds
        var partInSeconds = seconds%60;
        //adds left zeros to seconds
        partInSeconds = partInSeconds.toString().padStart(2,'0');
        //returns formatted time
        return `${minutes}:${partInSeconds}`;
    },

    lineBreak (strng){
        if (strng.length <30 ){
            return strng
        }else{
            for (i=0; i<strng.length;i++){
                if(i>15 && strng.charAt(i)===" "){
                    strng = strng.slice(0, i) + "\n" + lineBreak(strng.slice(i, strng.length));

                    return strng;

                }

            }
        }
    }
}
module.exports = functions;