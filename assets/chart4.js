d3.json(dataPath + "chart4.json", function (data) {
    var chart;

    nv.addGraph(function () {
        chart = nv.models.lineChart()
            .options({
                duration: 300,
                useInteractiveGuideline: true,
                showLegend: false
            });

        // chart sub-models (ie. xAxis, yAxis, etc) when accessed directly, return themselves, not the parent chart, so need to chain separately
        chart.xAxis
            .axisLabel("Ply")

        chart.yAxis
            .axisLabel('Evaluation')
            .tickFormat(function (d) {
                return d3.format(',.3f')(d);
            });

        d3.select('#chart4')
            .datum(data)
            .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });
});
