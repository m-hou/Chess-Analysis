var chart;

d3.json("assets/rnbqkbnr_pppppppp_8_8_8_8_PPPPPPPP_RNBQKBNR w KQkq -.json", function (data) {
    // create the chart
    nv.addGraph(function () {
        chart = nv.models.scatterChart()
            .showDistX(true)
            .showDistY(true)
            .useVoronoi(true)
            .color(d3.scale.category10().range())
            .pointRange([100, 100])
            .duration(300);
        chart.tooltip.contentGenerator(function (e) {
            var series = e.series[0];
            if (series.value === null) return;
            var rows =
                "<tr>" +
                "<td class='key'>" + 'Win Rate: ' + "</td>" +
                "<td class='x-value'>" + (series.value ? (series.value * 100).toFixed(2) + "%" : 0) + "</td>" +
                "</tr>" +
                "<tr>" +
                "<td class='key'>" + 'Play Rate: ' + "</td>" +
                "<td class='x-value'>" + (e.value ? (e.value * 100).toFixed(2) + "%" : 0) + "</td>" +
                "</tr>";

            var header =
                "<thead>" +
                "<tr>" +
                "<td class='legend-color-guide'><div style='background-color: " + series.color + ";'></div></td>" +
                "<td class='key'><strong>" + e.point.move + "</strong></td>" +
                "</tr>" +
                "</thead>";

            return "<table>" +
                header +
                "<tbody>" +
                rows +
                "</tbody>" +
                "</table>";
        });
        chart.xAxis
            .axisLabel('Play Rate (%)')
            .tickFormat(d3.format(',.02%'));
        chart.yAxis
            .axisLabel('Win Rate (%)')
            .tickFormat(d3.format(',.02%'));

        d3.select('#chart5')
            .datum(data)
            .call(chart);

        nv.utils.windowResize(chart.update);

        chart.dispatch.on('stateChange', function (e) { ('New State:', JSON.stringify(e)); });
        return chart;
    });
});

function updateData(url) {
    d3.json(url, function (jsondata) {
        d3.select('#chart5')
            .datum(jsondata)
            .transition().duration(500)
            .call(chart);
    });
}

var board,
    game = new Chess();

var removeGreySquares = function () {
    $('#board .square-55d63').css('background', '');
};

var greySquare = function (square) {
    var squareEl = $('#board .square-' + square);

    var background = '#a9a9a9';
    if (squareEl.hasClass('black-3c85d') === true) {
        background = '#696969';
    }

    squareEl.css('background', background);
};

var onDragStart = function (source, piece) {
    // do not pick up pieces if the game is over
    // or if it's not that side's turn
    if (game.game_over() === true ||
        (game.turn() === 'w' && piece.search(/^b/) !== -1) ||
        (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
        return false;
    }
};

var onDrop = function (source, target) {
    removeGreySquares();

    // see if the move is legal
    var move = game.move({
        from: source,
        to: target,
        promotion: 'q' // NOTE: always promote to a queen for example simplicity
    });

    // illegal move
    if (move === null) return 'snapback';
};

var onMouseoverSquare = function (square, piece) {
    // get list of possible moves for this square
    var moves = game.moves({
        square: square,
        verbose: true
    });

    // exit if there are no moves available for this square
    if (moves.length === 0) return;

    // highlight the square they moused over
    greySquare(square);

    // highlight the possible squares for this piece
    for (var i = 0; i < moves.length; i++) {
        greySquare(moves[i].to);
    }
};

var onMouseoutSquare = function (square, piece) {
    removeGreySquares();
};

var onSnapEnd = function () {
    board.position(game.fen());
};

var onChange = function (oldPos, newPos) {
    var boardStateFen = game.fen(newPos).split(" ").slice(0, -2).join(" ");
    var fenReplaceSlash = boardStateFen.replace(new RegExp("/", 'g'), "_");
    var dataFile = "assets/" + fenReplaceSlash + ".json"
    updateData(dataFile)
};

var resetGame = function () {
    game = new Chess();
    board.start();
}

var cfg = {
    draggable: true,
    position: 'start',
    onDragStart: onDragStart,
    onDrop: onDrop,
    onMouseoutSquare: onMouseoutSquare,
    onMouseoverSquare: onMouseoverSquare,
    onSnapEnd: onSnapEnd,
    onChange: onChange
};

board = ChessBoard('board', cfg);
$(window).resize(board.resize);
$('#resetBtn').on('click', resetGame);
