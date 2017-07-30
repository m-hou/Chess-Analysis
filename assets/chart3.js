d3.json(dataPath + "data_chart3.json", function (data) {
    var chart;

    nv.addGraph(function () {
        chart = nv.models.boxPlotChart()
            .maxBoxWidth(75); // prevent boxes from being incredibly wide
        chart.tooltip.contentGenerator(function (d) {
            var series = d.series;
            console.log(series[0])
            if (series.length == 1) {
                var header =
                    "<thead>" +
                    "<tr>" +
                    "<td class='legend-color-guide'><div style='background-color: " + series[0].color + ";'></div></td>" +
                    "<td class='key'><strong>" + (series[0].key ? series[0].key.toFixed(2) : 0) + "</strong></td>" +
                    "</tr>" +
                    "</thead>";

                return "<table>" +
                    header +
                    "</table>";
            } else {
                var rows =
                    "<tr>" +
                    "<td class='key'>" + series[0].key + ": " + "</td>" +
                    "<td class='x-value'><strong>" + (series[0].value ? series[0].value.toFixed(2) : 0) + "<strong></td>" +
                    "</tr>" +
                    "<tr>" +
                    "<td class='key'>" + series[1].key + ": " + "</td>" +
                    "<td class='x-value'><strong>" + (series[1].value ? series[1].value.toFixed(2) : 0) + "<strong></td>" +
                    "</tr>" +
                    "<tr>" +
                    "<td class='key'>" + series[2].key + ": " + "</td>" +
                    "<td class='x-value'><strong>" + (series[2].value ? series[2].value.toFixed(2) : 0) + "<strong></td>" +
                    "</tr>";

                var header =
                    "<thead>" +
                    "<tr>" +
                    "<td class='legend-color-guide'><div style='background-color: " + series[0].color + ";'></div></td>" +
                    "<td class='key'>" + d.key + "</td>" +
                    "</tr>" +
                    "</thead>";

                return "<table>" +
                    header +
                    "<tbody>" +
                    rows +
                    "</tbody>" +
                    "</table>";
            }
        })

        chart.xAxis.axisLabel("Time Control")
        chart.yAxis.axisLabel('Evaluation Range in a Game')

        d3.select('#chart3')
            .datum(data)
            .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });
})