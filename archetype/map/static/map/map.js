var width = $("#mapcontainer").width(),
height = 500,
centered;

var svg = d3.select("#mapcontainer").append("svg")
    .attr("width", width)
    .attr("height", height);

var g = svg.append("g");

var projection;
var path;

var quantize = d3.scale.quantize()
    .domain([0, .15])
    .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

function getRandom(min, max) {
    return Math.random() * (max - min) + min;
}

d3.json("/static/nyc.json", function(json) {
      // create a first guess for the projection
    var center = d3.geo.centroid(json)
    var scale  = 150;
    var offset = [width/2, height/2];
    projection = d3.geo.mercator()
	.scale(scale)
	.center(center)
        .translate(offset);

      // create the path
    path = d3.geo.path().projection(projection);

      // using the path determine the bounds of the current map and use 
      // these to determine better values for the scale and translation
    var bounds  = path.bounds(json);
    var hscale  = scale*width  / (bounds[1][0] - bounds[0][0]);
    var vscale  = scale*height / (bounds[1][1] - bounds[0][1]);
    var scale   = (hscale < vscale) ? hscale : vscale;
    var offset  = [width - (bounds[0][0] + bounds[1][0])/2,
                   height - (bounds[0][1] + bounds[1][1])/2];

      // new projection
    projection = d3.geo.mercator().center(center)
        .scale(scale).translate(offset);
    path = path.projection(projection);

    g.selectAll("path").data(json.features)
	.enter()
	.append("path")
        .attr("d", path)
	.attr("class", function(d) { return "precinct " + quantize(getRandom(0,.15)); })
        .style("stroke-width", "1")
        .style("stroke", "black")
	.on("click", select);
});

function select(){
    
    var selection = d3.select(this);

    var x, y, k;

    if (selection) {
	if (centered) {
	    if (centered.attr("d")==selection.attr("d")) {
		centered = null;
	    } else {
		centered = selection;
	    }
	} else {
            centered = selection;
	}
    } else {
        centered = null;
    }
    
    if (centered){
	g.selectAll("path").style("fill", "");
	centered.style("fill", "red");
	$("#controlscontainer").fadeOut(1000).html("<div class='alert alert-info alert-dismissable'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>Instructions</strong> Drag some of the datasets from the explorer on the left onto the graph and creat a model for the possible causes of the selected crime.</div>").fadeIn(1000);
    } else {
	g.selectAll("path").style("fill", "");
    }

};