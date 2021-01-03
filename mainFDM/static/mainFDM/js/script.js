$(document).ready(function(){

    $("#upload-scores").submit(function(event){
        event.preventDefault(); //prevent default form submission action

        //delete the error div on next submission so that they don't pile up
        $(".alert-danger").remove();

        console.log("start form submission"); //sanity check

        //get the csrf token form django and pass it to ajax
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        //get the username given by user:
        let uname = $("#upload-user").val();
        console.log(uname);

        //prepare the form data
        let formData = {
            'player_username' : uname,
            'csrfmiddlewaretoken': csrftoken,
        };

        //process the form
        $.post("", formData)
            .done(function( data ){
                if (data['result'] === 'Submitted'){
                    console.log("submitted");
                    $("#success").addClass("alert alert-success").empty().append(data.message);
                    $("#upload-scores").addClass("d-none");
                    $("#leaderboard").removeClass("d-none");
                    //get the leaderboard from the view
                    const leaderboard = data['leaderboard'];
                    //for each score in the leaderboard, add the username and score to the leaderboard
                    leaderboard.forEach(item =>
                        //$("#leaderboard-list").append('<li>' + item.player_username + '  -->  '+ item.score + '</li>')
                        $('#leaderboard').append('<div class="row gx-0 align-items-center board-row">' +
                            ' <div class="col col-6 text-start"> ' +
                                '<div class="board-username">' + item.player_username + '</div></div>' +
                            '<div class="col col-6 text-end">' +
                                '<div class="board-score">' + item.score + '</div> </div> </div>')
                    );
                }
                else{
                    console.log("form errors");
                    $("#form-title-div").append('<div class="alert alert-danger">' + data.message + '</div>');

                }

            })
            .fail(function(){
                console.log("server error");
                //Server failed to respond - Show an error message
                $("#form-title-div").append('<div class="alert alert-danger">Could not reach server, please try again later.</div>');
        });
    });
});