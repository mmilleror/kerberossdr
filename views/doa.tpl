<html>

<p><font size = "4"><a href="/init">Configuration and Spectrum</a> | <a href="/sync">Sync</a> | <a href="/doa">DOA Estimation</a> | <a href="/pr">Passive Radar</a> | <a href="/stats">Stats</a></font></p>
<hr>

<p><font size = "4"><a href="/static/compass.html">Compass</a></font></p>
<hr>

<b>Antenna Configuration</b>
<form action="/doa" method="post">
        <input type="hidden" name="ant_config" value="ant_config" />

	<p>Arrangement:
	<select name = "ant_arrangement">
		<option value="0" {{!'selected="selected"' if ant_arrangement_index == 0 else ""}}>ULA</option>
		<option value="1" {{!'selected="selected"' if ant_arrangement_index == 1 else ""}}>UCA</option>
	</select></p>

	<p>Spacing [lambda]: <input type="number" value="{{ant_spacing}}" step="0.0001" name="ant_spacing"/></p>


	<input type="checkbox" name="en_doa" value="on" {{!'checked="checked"' if en_doa >= 1 else ""}}>Enable DOA<br>

	<input type="checkbox" name="en_bartlett" value="on" {{!'checked="checked"' if en_bartlett >= 1 else ""}}>Bartlett<br>
	<input type="checkbox" name="en_capon" value="on" {{!'checked="checked"' if en_capon >= 1 else ""}}>Capon<br>
	<input type="checkbox" name="en_MEM" value="on" {{!'checked="checked"' if en_MEM >= 1 else ""}}>MEM<br>
	<input type="checkbox" name="en_MUSIC" value="on" {{!'checked="checked"' if en_MUSIC >= 1 else ""}}>MUSIC<br>

	<br>

	<input type="checkbox" name="en_fbavg" value="on" {{!'checked="checked"' if en_fbavg >= 1 else ""}}>FB Average (Do not use with UCA)<br>

	<p><input value="Update DOA" type="submit" /></p>
</form>
<hr>
<script type="text/javascript" src="/static/refresh_image.js" charset="utf-8" style="float:right"></script>

<body onload="JavaScript:init('/static/doa.jpg');">
<canvas id="canvas"/>
</body>

</html>
