d3.json(dataPath + "chart2.json", function (data) {
    var chart;

    nv.addGraph({
        generate: function () {
            var chart = nv.models.multiBarChart()
                .margin({ bottom: 150 })
                .stacked(true)
                .useInteractiveGuideline(true)
                .showControls(false)
                .rotateLabels(-60)
                .reduceXTicks(false)
            chart.interactiveLayer.tooltip.valueFormatter(function(d) {
                return (d * 100).toFixed(2) + "%"
            })
            chart.xAxis
                .tickFormat(function (d) {
                    var maxLength = 20;
                    return d.length > 20 ?
                        d.substring(0, 17) + "..." :
                        d;
                })

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