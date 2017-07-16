d3.json("assets/data_chart3.json", function (data) {
    var chart;

    nv.addGraph(function () {
        chart = nv.models.boxPlotChart()
            .x(function (d) { return d.label })
            .y(function (d) { return d.value })
            .maxBoxWidth(75); // prevent boxes from being incredibly wide

        d3.select('#chart3')
            .datum(data)
            .call(chart);



        nv.utils.windowResize(chart.update);

        return chart;
    });
})