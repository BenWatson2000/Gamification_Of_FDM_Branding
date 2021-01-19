const functions = {
    Pipe (){
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
},
        initializeGrid: function (size) {
            if (size % 2 == false) {
                console.log("Cannot create grid with even number of rows/columns");
                return;
            }
        },
            getThisPipe: function (x, y) {
                if (typeof this.pipes[x] !== "undefined" && typeof this.pipes[x][y] !== "undefined") {
                    return this.pipes[x][y];
                }
            },
            getAllPipes: function () {
                var pipes = [];
                for (x in this.pipes) {
                    for (y in this.pipes[x]) {
                        pipes.push(this.getThisPipe(x, y));
                    }
                }

                return pipes;
            },

}
