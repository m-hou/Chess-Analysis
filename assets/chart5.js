d3.json("assets/data_chart5.json", function (data) {
    // create the chart
    var chart;

    nv.addGraph(function () {
        chart = nv.models.scatterChart()
            .showDistX(true)
            .showDistY(true)
            .useVoronoi(true)
            .color(d3.scale.category10().range())
            .pointRange([100,100])
            .duration(300);

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