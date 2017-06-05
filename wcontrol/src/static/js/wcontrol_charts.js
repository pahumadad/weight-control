function get_measurement() {
    var e = document.getElementById("chart_measurement");
    var m_text = e.options[e.selectedIndex].text;
    var m_id = e.options[e.selectedIndex].id;
    return [m_text, m_id];
}
function get_data_set(data, limit, step) {
    if (data.length <= limit)
        return data;
    var aux = 0;
    var data_set = [];
    for (var i = data.length - 1; i >= 0; i--) {
        if ((aux >= (limit * (step - 1))) && (aux < (limit * step))){
            data_set.push(data[i]);
        }
        aux++;
    }
    if (data_set.length == limit)
        return data_set;
    for (var i = data_set.length - 1; i < limit; i++)
        data_set.push(data[i]);
    return data_set;
}
function left_right_state() {
    if (controls_len <= (limit * step))
        $('#chart_left').addClass('disabled');
    else
        $('#chart_left').removeClass('disabled');
    if ((step - 1) == 0)
        $('#chart_right').addClass('disabled');
    else
        $('#chart_right').removeClass('disabled');
}
function get_cant() {
    var e = document.getElementById("chart_cant");
    var cant_id = e.options[e.selectedIndex].id;
    return cant_id;
}
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
var limit = get_cant();
var step = 1;
var label;
var m_id;
var labels_set = [];
var data_set = [];
[label, m_id] = get_measurement();
labels_set = get_data_set(labels, limit, step);
data_set = get_data_set(data[m_id], limit, step);
var ctx = document.getElementById('chart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels_set,
        datasets: [{
            label: label,
            data: data_set,
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
left_right_state();
$('#chart_measurement').on("change", function(){
    [label, m_id] = get_measurement();
    labels_set = get_data_set(labels, limit, step);
    data_set = get_data_set(data[m_id], limit, step);
    chart.data.labels = labels_set;
    chart.data.datasets[0].data = data_set;
    chart.data.datasets[0].label = label;
    chart.update();
});
$('#chart_left').click(function(){
    if (controls_len <= (limit * step))
        return ;
    step++;
    left_right_state();
    labels_set = get_data_set(labels, limit, step);
    data_set = get_data_set(data[m_id], limit, step);
    chart.data.labels = labels_set;
    chart.data.datasets[0].data = data_set;
    chart.update();
});
$('#chart_right').click(function(){
    if (step == 1)
        return ;
    step--;
    left_right_state();
    labels_set = get_data_set(labels, limit, step);
    data_set = get_data_set(data[m_id], limit, step);
    chart.data.labels = labels_set;
    chart.data.datasets[0].data = data_set;
    chart.update();
});
$('#chart_cant').on("change", function(){
    limit = get_cant();
    if (controls_len <= limit)
        step = 1;
    left_right_state();
    labels_set = get_data_set(labels, limit, step);
    data_set = get_data_set(data[m_id], limit, step);
    chart.data.labels = labels_set;
    chart.data.datasets[0].data = data_set;
    chart.data.datasets[0].label = label;
    chart.update();
});
