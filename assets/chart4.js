d3.json("assets/data_chart4.json", function(data) {
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
            .axisLabel("Time (s)")
            .tickFormat(d3.format(',.1f'))
            .staggerLabels(true);

        chart.yAxis
            .axisLabel('Voltage (v)')
            .tickFormat(function (d) {
                if (d == null) {
                    return 'N/A';
                }
                return d3.format(',.2f')(d);
            });

        d3.select('#chart4')
            .datum(data)
            .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });
});
