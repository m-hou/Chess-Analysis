d3.json("data.json", function(data) {
    var colors = d3.scale.category20();
    var chart;

    nv.addGraph(function() {
        chart = nv.models.stackedAreaWithFocusChart()
            .useInteractiveGuideline(true)
            .x(function(d) { return d[0] })
            .y(function(d) { return d[1] })
            .controlLabels({stacked: "Stacked"})
            .duration(300);
        chart.brushExtent([1000, 2800]);
        chart.xAxis.axisLabel("Elo");
        chart.yAxis.axisLabel("Frequency");
        d3.select('#chart1')
            .datum(data)
            .transition().duration(1000)
            .call(chart)
            .each('start', function() {
                setTimeout(function() {
                    d3.selectAll('#chart1 *').each(function() {
                        if(this.__transition__)
                            this.__transition__.duration = 1;
                    })
                }, 0)
            });

        nv.utils.windowResize(chart.update);
        return chart;
    });
});
