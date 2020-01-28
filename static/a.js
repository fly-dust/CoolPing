var chart = null; // 定义全局变量
$(document).ready(function () {
    chart = Highcharts.chart('container', {
        chart: {
            type: 'spline',
            events: {
                load: requestData // 图表加载完毕后执行的回调函数
            }
        },
        title: {
            text: 'CoolPing监测 v0.2'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 50 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Time in ms',
                margin: 80
            }
        },
        series: [{
            name: 'Baidu.com',
            data: [],
        }]
    });

});

/**
 * Ajax 请求数据接口，并通过 Highcharts 提供的函数进行动态更新
 * 接口调用完毕后间隔 10 s 继续调用本函数，以达到实时请求数据，实时更新的效果
 */
function requestData() {
    $.get({
        url: '/get/',
        'success': function (point) {
　　　　　// console.log(point); // point为请求接口返回的数据 Array [ 1551065494000, 82 ]
            var series = chart.series[0],
                shift = series.data.length > 50; // 当数据点数量超过 50 个，则指定删除第一个点

            // 新增点操作
            //具体的参数详见：https://api.hcharts.cn/highcharts#Series.addPoint
            chart.series[0].addPoint(point, true, shift);

            // 十秒后继续调用本函数
            setTimeout(requestData, 10000);
        },
        cache: false
    });
}