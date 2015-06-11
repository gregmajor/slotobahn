var chartOptions = {
	responsive : true,

	// Boolean - Whether grid lines are shown across the chart
    scaleShowGridLines : true,

    // String - Colour of the grid lines
    scaleGridLineColor : "rgba(0,0,0,.05)",

    // Number - Width of the grid lines
    scaleGridLineWidth : 1,

    // Boolean - Whether to show horizontal lines (except X axis)
    scaleShowHorizontalLines: true,

    // Boolean - Whether to show vertical lines (except Y axis)
    scaleShowVerticalLines: true,

    // Boolean - Whether the line is curved between points
    bezierCurve : true,

    // Number - Tension of the bezier curve between points
    bezierCurveTension : 0.4,

    // Boolean - Whether to show a dot for each point
    pointDot : true,

    // Number - Radius of each point dot in pixels
    pointDotRadius : 4,

    // Number - Pixel width of point dot stroke
    pointDotStrokeWidth : 1,

    // Number - amount extra to add to the radius to cater for hit detection outside the drawn point
    pointHitDetectionRadius : 20,

    // Boolean - Whether to show a stroke for datasets
    datasetStroke : true,

    // Number - Pixel width of dataset stroke
    datasetStrokeWidth : 5,

    // Boolean - Whether to fill the dataset with a colour
    datasetFill : true,

    // String - A legend template
    legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].strokeColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
}

$(function() {
    $("#myTab a").click(function(e){
    	e.preventDefault();
    	$(this).tab('show');
    });
});

$(function() {
  $('button#blink').bind('click', function() {
    $.getJSON('/blinker/blink', { },
    function(data) {
      $("#result-alert").text(data.result);
      $("#result-alert").show();
      $("#result-alert").delay(3000).fadeOut(300);
    });
    return false;
  });
});

$(function() {
  $('button#consumer_start').bind('click', function() {
    $.getJSON('/consumer/start', { },
    function(data) {
      $("#result-alert").text(data.result);
      $("#result-alert").show();
      $("#result-alert").delay(3000).fadeOut(300);
    });
    return false;
  });
});

$(function() {
  $('button#consumer_stop').bind('click', function() {
    $.getJSON('/consumer/stop', { },
    function(data) {
      $("#result-alert").text(data.result);
      $("#result-alert").show();
      $("#result-alert").delay(3000).fadeOut(300);
    });
    return false;
  });
});

$(function() {
  $('button#display_write_message').bind('click', function() {
    $.getJSON('/display/write', {
      message: $('input[name="message"]').val(),
    }, function(data) {
      $("#result-alert").text(data.result);
      $("#result-alert").show();
      $("#result-alert").delay(3000).fadeOut(300);
    });
    return false;
  });
});

$(function() {
  $('button#motor_turn').bind('click', function() {
    $.getJSON('/motor/turn', {
      wait_time: $('input[name="wait_time"]').val(),
      duration: $('input[name="duration"]').val()
    }, function(data) {
      $("#result-alert").text(data.result);
      $("#result-alert").show();
      $("#result-alert").delay(3000).fadeOut(300);
    });
    return false;
  });
});