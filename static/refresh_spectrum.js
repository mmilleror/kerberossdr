var url = ""; //url to load image from
var refreshInterval = 1000; //in ms
var drawDate = true; //draw date string
var img;

function init(param) {
    url = param;
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    img = new Image();
    img.onload = function() {
        canvas.setAttribute("width", img.width);
        canvas.setAttribute("height", img.height);
        context.drawImage(this, 0, 0);
    };
    refresh();
}
function refresh()
{
    //img.src = url + "?t=" + new Date().getTime();
    echo '<img src="' . url . '?m=' . filemtime(url) . '">';
    setTimeout("refresh()",refreshInterval);
}

