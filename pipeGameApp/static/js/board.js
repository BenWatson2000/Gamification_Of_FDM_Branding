var Pipe = function(){
    this.x = 0;
    this.y = 0;

    this.active = 0;

    // Up, Right, Down, Left
    this.connections = Array.apply(null, new Array(4)).map(Number.prototype.valueOf,0);

    this.isActive = function() {
        return this.active === 1;
    };

    this.setActive = function(active) {
        this.active = (active ? 1 : 0);
    };

    /**
     * Get the neighbouring pipe in the given direction
     *
     * @param {grid.direction} direction
     */
    this.getNeighbouringPipe = function(direction) {
        var dx = 0;
        var dy = 0;

        if (direction == grid.direction.RIGHT) {
            dx = 1;
        } else if(direction == grid.direction.LEFT) {
            dx = -1;
        }

        if (direction == grid.direction.UP) {
            dy = 1;
        } else if(direction == grid.direction.DOWN) {
            dy = -1;
        }

        return grid.getThisPipe(this.x + dx, this.y + dy);
    };

    this.hasConnection = function(direction) {
        return this.connections[direction] === 1;
    };

    this.rotate = function() {
        this.connections.splice(0, 0, this.connections.splice((this.connections.length-1), 1)[0]);
    }
};

/**
  * the grid
  */
var grid = {

    size: 0,

    pipes: [],

    direction: {
        DOWN: 2,
        LEFT: 3,
        RIGHT: 1,
        UP: 0
    },

    reverse_direction: {
        2: 0,
        3: 1,
        1: 3,
        0: 2
    },

    /**
      * Grid initialization
      */
    initializeGrid: function(size) {
        if (size % 2 == false) {
            console.log("Cannot create grid with even number of rows/columns");
            return;
        }

        this.initializeAllPipes(size);
        this.buildPipesConnection();
        this.randomisePipes();
        this.checkPipesConnection();
        this.drawGrid();
    },

    /**
      * Get the pipe on the grid on the given X and Y
      *
      * @param {Number} x
      * @param {Number} y
      */
    getThisPipe: function(x, y) {
        if (typeof this.pipes[x] !== "undefined" && typeof this.pipes[x][y] !== "undefined") {
            return this.pipes[x][y];
        }
    },

    /**
      * Get all pipes in the grid
      */
    getAllPipes: function() {
        var pipes = [];
        for (x in this.pipes) {
            for(y in this.pipes[x]) {
                pipes.push(this.getThisPipe(x, y));
            }
        }

        return pipes;
    },

    /**
      * Initialize all pipes in the grid
      *
      * @param {Number} size
      */
    initializeAllPipes: function(size) {
        this.size = size;
        this.pipes = [];
        for (x = 1; x <= size; x++) {
            this.pipes[x] = [];
            for (y = 1; y <= size; y++) {
                pipe = new Pipe();
                pipe.x = x;
                pipe.y = y;

                this.pipes[x][y] = pipe;
            }
        }
    },

    /**
      * Build the connections for all pipes
      */
    buildPipesConnection: function() {
        // Define variables
        var all_pipes = this.size * this.size;
        var pipes_with_connection = [];

        // Add a random first pipe
        var x = Math.ceil(this.size / 2);
        var y = Math.ceil(this.size / 2);

        pipe = this.getThisPipe(x, y);
        pipe.active = 1;

        pipes_with_connection.push(pipe);

        while (pipes_with_connection.length < all_pipes) {
            // Get a pipe in the set
            var pipe = pipes_with_connection[Math.floor(Math.random() * pipes_with_connection.length)];

            // Create a random direction
            var direction = Math.floor(Math.random() * 4);

            var neighbor = pipe.getNeighbouringPipe(direction);
            var reverse_direction = this.reverse_direction[direction];

            if (typeof neighbor != "undefined" && neighbor.connections.indexOf(1) == -1) {
                pipe.connections[direction] = 1;
                neighbor.connections[reverse_direction] = 1;

                pipes_with_connection.push(neighbor);
            }
        }
    },

    /**
      * Scramble all pipes by rotating them a random amount of times
      */
    randomisePipes: function() {
        for (x = 1; x < this.pipes.length; x++) {
            for (y = 1; y < this.pipes.length; y++) {
                var pipe = this.getThisPipe(x, y);
                var random = Math.floor(Math.random() * 4);

                for (i = 0; i < random; i++) {
                    pipe.rotate();
                }
            }
        }
    },

    /**
      * Deactivate all pipes
      */
    deactivateAllPipes: function() {
        for (x = 1; x < this.pipes.length; x++) {
            for (y = 1; y < this.pipes.length; y++) {
                this.getThisPipe(x, y).setActive(false);
            }
        }
    },

    /**
      * Check all pipes to see if they are connected to an active pipe
      */
    checkPipesConnection: function() {
        pipes_with_connection = [];
        pipes_to_check = [];

        // Disable all pipes
        this.deactivateAllPipes();

        // Get the center pipe, set is to active, an add it to the set to be checked
        var center_pipe = this.getThisPipe(Math.ceil(this.size/2), Math.ceil(1));
        center_pipe.setActive(true);

        pipes_with_connection.push(center_pipe);
        pipes_to_check.push(center_pipe);

        // While there are still pipes left to be checked
        while (pipes_to_check.length > 0) {
            var pipe = pipes_to_check.pop();
            var x = pipe.x;
            var y = pipe.y

            // Check if this pipe has a connection up
            if (pipe.hasConnection(grid.direction.UP)) {
                var pipe_above = this.getThisPipe(x-1, y);
                if (typeof pipe_above !== "undefined" && pipe_above.hasConnection(grid.direction.DOWN) && !pipe_above.isActive()) {
                    pipe_above.setActive(true);

                    pipes_with_connection.push(pipe_above);
                    pipes_to_check.push(pipe_above);
                }
            }

            // Check if this pipe has a connection down
            if(pipe.hasConnection(grid.direction.DOWN)) {
                var pipe_below = this.getThisPipe(x+1, y);
                if (typeof pipe_below !== "undefined" && pipe_below.hasConnection(grid.direction.UP) && !pipe_below.isActive()) {
                    pipe_below.setActive(true);

                    pipes_with_connection.push(pipe_below);
                    pipes_to_check.push(pipe_below);
                }
            }

            // Check if this pipe has a connection right
            if (pipe.hasConnection(grid.direction.RIGHT)) {
                var pipe_next = this.getThisPipe(x, y+1);
                if (typeof pipe_next !== "undefined" && pipe_next.hasConnection(grid.direction.LEFT) && !pipe_next.isActive()) {
                    pipe_next.setActive(true);

                    pipes_with_connection.push(pipe_next);
                    pipes_to_check.push(pipe_next);
                }
            }

            // Check if the pipe has a connection left
            if (pipe.hasConnection(grid.direction.LEFT)) {
                var pipe_previous = this.getThisPipe(x, y-1);
                if (typeof pipe_previous !== "undefined" && pipe_previous.hasConnection(grid.direction.RIGHT) && !pipe_previous.isActive()) {
                    pipe_previous.setActive(true);

                    pipes_with_connection.push(pipe_previous);
                    pipes_to_check.push(pipe_previous);
                }
            }
        }
        function getRandomInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1) + min);
        }
        var top = this.getThisPipe(Math.ceil(1), Math.ceil(this.size));
        var mid = this.getThisPipe(Math.ceil(this.size/2), Math.ceil(this.size));
        var bot = this.getThisPipe(Math.ceil(this.size), Math.ceil(this.size));
        losingOptions=[];
        var computerResponse = getRandomInt(1, 3);
        sessionStorage.setItem("computerResponse", computerResponse.toString());
        if (computerResponse==1){
            var winningOption = top;
            losingOptions= [mid,bot];
        }
        else if (computerResponse==2){
            var winningOption = mid;
            losingOptions= [top,bot];
        }
        else if (computerResponse==3){
            var winningOption = bot;
            losingOptions = [top,mid];

        }




        // Check if the user has won
        if (pipes_with_connection.includes(top)) {

            setTimeout(alert("won game"),200)
        }

        //check loss
        else if (pipes_with_connection.includes(bot)) {

             setTimeout(alert("wrong answer"),200)
        }
        else if (pipes_with_connection.includes(mid)) {

             setTimeout(alert("wrong answer"),200)
        }

    },

    drawGrid: function() {
        var grid_div = document.getElementById("grid");
        grid_div.innerHTML = '';

        for (x in this.pipes) {
            var row = this.pipes[x];

            var row_div = document.createElement('div');
            row_div.className = "row";

            for (y in row) {
                var pipe = row[y];
                var pipe_div = document.createElement('div');

                pipe_div.className = "pipe";

                pipe_div.setAttribute('data-x', x);
                pipe_div.setAttribute('data-y', y);

                pipe_div.setAttribute('onClick', 'rotatePipe(this)');

                if (pipe.connections[0] === 1) {
                    pipe_div.className += " u";
                }

                if (pipe.connections[1] === 1) {
                    pipe_div.className += " r";
                }

                if (pipe.connections[2] === 1) {
                    pipe_div.className += " d";
                }

                if (pipe.connections[3] === 1) {
                    pipe_div.className += " l";
                }

                if (pipe.active == 1) {
                    pipe_div.className += " a";
                }

                row_div.appendChild(pipe_div);
            }

            grid_div.appendChild(row_div);
        }
    }
};
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
    var time = 180 , // your time in seconds here
        display = document.querySelector('#timer');
    startTimer(time, display);
};

// Called when clicking a pipe
function rotatePipe(element) {
    var x = element.dataset.x;
    var y = element.dataset.y;

    grid.getThisPipe(x,y).rotate();
    grid.checkPipesConnection();
    grid.drawGrid();
}

grid.initializeGrid(7);