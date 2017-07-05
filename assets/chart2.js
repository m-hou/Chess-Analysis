d3.json("assets/data_chart2.json", function(data) {
    nv.addGraph({
        generate: function() {
            var chart = nv.models.multiBarChart()
                .stacked(true)
                .useInteractiveGuideline(true)
                .showControls(false);
            chart.color(["#EEEEEE", "#777777", "#000000"])
            chart.yAxis
                .axisLabel("Outcome (%)")
                .tickFormat(d3.format(',.0%'));
            var svg = d3.select('#chart2').datum(data);
            svg.transition().duration(0).call(chart);

            nv.utils.windowResize(chart.update);
            return chart;
        }
    });
})