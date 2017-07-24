d3.json("assets/data_chart5.json", function (data) {
    // create the chart
    var chart;

    nv.addGraph(function () {
        chart = nv.models.scatterChart()
            .showDistX(true)
            .showDistY(true)
            .useVoronoi(true)
            .color(d3.scale.category10().range())
            .duration(300);

        chart.xAxis.tickFormat(d3.format('.02f'));
        chart.yAxis.tickFormat(d3.format('.02f'));

        d3.select('#chart5')
            .datum(data)
            .call(chart);

        nv.utils.windowResize(chart.update);

        chart.dispatch.on('stateChange', function (e) { ('New State:', JSON.stringify(e)); });
        return chart;
    });
});