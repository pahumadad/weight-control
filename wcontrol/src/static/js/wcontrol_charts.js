var dates = $('#div_dates').data('name');
var controls = $('#div_controls').data('name');
var controls_len = Object.keys(controls).length;
var controls_num = Object.keys(controls[0]).length;
var labels = [];
for (var i = 0; i < controls_len; i++) {
    labels.push(dates[i]);
}
var data = [];
for (var i = 0; i < controls_num; i++) {
    data[i] = [];
    for (var j = 0; j < controls_len; j++) {
        data[i].push(controls[j][i]);
    }
}
var e = document.getElementById("chart_measurement");
var label = e.options[e.selectedIndex].text;
var ctx = document.getElementById('chart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: label,
            data: data[0],
            backgroundColor: "rgba(151,187,205,0.4)",
            borderColor: "rgba(151,187,205,1)",
            lineTension: 0
        }]
    },
    options: {
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    displayFormats: {
          	        'millisecond': 'MMM DD',
                        'second': 'MMM DD',
                        'minute': 'MMM DD',
                        'hour': 'MMM DD',
                        'day': 'MMM DD',
                        'week': 'MMM DD',
                        'month': 'MMM DD',
                        'quarter': 'MMM DD',
                        'year': 'MMM DD'
                    }
                }
            }]
        }
    }
});
$('#chart_measurement').on("change", function(){
    var m_id = e.options[e.selectedIndex].id;
    label = e.options[e.selectedIndex].text;
    chart.data.datasets[0].data = data[m_id];
    chart.data.datasets[0].label = label;
    chart.update();
});
