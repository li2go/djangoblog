var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
radius = 10;
var dragging = false;
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var putPoint = function(e) {
	if(dragging){
	context.lineTo(e.clientX,e.clientY);	
	context.beginPath();
	context.arc(e.offsetX, e.offsetY, radius, 0, Math.PI * 2);
	context.fill();
	context.beginPath();
	context.moveTo(e.clientX,e.clientY);

	}
}
var engage = function(e){
	dragging = ture;
	putPoint(e);

}
var disengage = function(){
	dragging = false;
	context.beginPath();
}
canvas.
canvas.addEventListener('mosuedown',engage);
canvas.addEventListener('mousemove', putPoint);
canvas.addEventListener('mouseup',disengage);