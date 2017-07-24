d3.json("assets/data_chart5.json", function (data) {
    // create the chart
    var chart;

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