<html>
<meta http-equiv="Cache-control" content="no-cache" charset="utf-8">
<p><font size = "4"><a href="/init">Configuration and Spectrum</a> | <a href="/sync">Sync</a> | <a href="/doa">DOA Estimation</a> | <a href="/pr">Passive Radar</a> | <a href="/stats">Stats</a></font></p>
<hr>

<b>Receiver Configuration</b>
<form action="/sync" method="post">
        <input type="hidden" name="update_sync" value="update_sync" />
	
	<input type="checkbox" name="en_sync" value="on" {{!'checked="checked"' if en_sync >= 1 else ""}}>Enable Sync Display<br>
	<input type="checkbox" name="en_noise" value="on" {{!'checked="checked"' if en_noise >= 1 else ""}}>Noise Source ON/OFF<br>

	<p><input value="Update" type="submit" /></p>
</form>
<hr>

<form action="/sync" method="post">
        <input type="hidden" name="del_hist" value="del_hist" />
	<p><input value="Delete History" type="submit" /></p>
</form>

<form action="/sync" method="post">
        <input type="hidden" name="samp_sync" value="samp_sync" />
	<p><input value="Sample Sync" type="submit" /></p>
</form>

<form action="/sync" method="post">
        <input type="hidden" name="cal_iq" value="cal_iq" />
	<p><input value="Calibrate IQ" type="submit" /></p>
</form>
<hr>

<!--<script type="text/javascript" src="/static/refresh_image.js" charset="utf-8" style="float:right"></script>

<body onload="JavaScript:init('/static/sync.jpg');">
<canvas id="canvas"/>
</body>-->

<iframe width=100% height=100% src="http://192.168.4.1:8081/sync_graph.html"></iframe>


</html>
