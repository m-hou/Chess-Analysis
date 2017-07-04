d3.json("assets/data_chart2.json", function(data) {
    nv.addGraph({
        generate: function() {
            var chart = nv.models.multiBarChart()
                .stacked(true)
                .useInteractiveGuideline(true);
            var svg = d3.select('#chart2').datum(data);
            svg.transition().duration(0).call(chart);

            nv.utils.windowResize(chart.update);
            return chart;
        }
    });
})