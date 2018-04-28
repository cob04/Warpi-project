/* index.js */

function draw(data) {

  /*
    D3.js setup code
    */

    "use strict";

    var svg = dimple.newSvg("#chart", 1000, 600);
  /*
    Dimple.js Chart construction code
    */

    var myChart = new dimple.chart(svg, data);
    // var s = myChart.addTimeAxis("x", "time", "%H:%M:%S");
    // s.lineWeight = 4;
    
    var s = myChart.addCategoryAxis("x", "timestamp");
    s.lineWeight = 8; 
    s.addOrderRule("timestamp", false);
    myChart.addMeasureAxis("y", "speed");
    // myChart.addMeasureAxis("z", "staff-rating");
    // myChart.addSeries(null, dimple.plot.scatter);
    // myChart.addSeries(null, dimple.plot.line);
    myChart.addSeries(null, dimple.plot.bar);
    // myChart.addSeries(null, dimple.plot.area);
    // myChart.addSeries(null, dimple.plot.bubble);
    myChart.draw();
};