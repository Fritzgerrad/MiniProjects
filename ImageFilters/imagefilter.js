var imagered = null
var imageblue = null;
var imagegreen = null;
var imagegrey = null;
var imagewin = null;
var image = null;
var imagepix = null;
var imagewpix = null;
var imagerain = null;
var imageblur = null;

function upLoad(){
var img = document.getElementById("finput");
image = new SimpleImage (img); 
imagered = new SimpleImage (img); 
imagegrey = new SimpleImage (img); 
imagegreen = new SimpleImage (img); 
imageblue = new SimpleImage (img); 
imagewin = new SimpleImage (img); 
imagepix = new SimpleImage (img); 
imagewpix = new SimpleImage (img);
imagerain = new SimpleImage (img);
imageblur = new SimpleImage (img); 
var canva = document.getElementById("can1");
image.drawTo(canva);
}


function makeRed(){
  var img = document.getElementById("finput");
  for (var pixel of imagered.values()){
   var r = pixel.getRed();
    var g = pixel.getGreen();
    var b = pixel.getBlue();
    var avg = (r+g+b)/3;
    if (avg<128){
        pixel.setRed(2*avg);
        pixel.setBlue(0);
        pixel.setBlue(0);
   }
    else{
        pixel.setRed(255);
        pixel.setGreen((2*avg)-255);
        pixel.setBlue((2*avg)-255);
    }
  }
  var canva = document.getElementById("can1");
  imagered.drawTo(canva);
}


function makeGrey(){
var img = document.getElementById("finput");
for (var pixel of imagegrey.values()){
    var red = pixel.getRed();   
    var green = pixel.getGreen();
    var blue = pixel.getBlue();
    var gray = ( red+green+blue)/3;
    
    pixel.setRed(gray);
    pixel.setGreen(gray); 
    pixel.setBlue(gray);
} 
var canvas = document.getElementById("can1");
imagegrey.drawTo(canvas);
}


function makeBlue(){
var img = document.getElementById("finput");
for (var pixel of imageblue.values()){   
   var r = pixel.getRed();
    var g = pixel.getGreen();
    var b = pixel.getBlue();
    var avg = (r+g+b)/3;
    if (avg<128){
        pixel.setRed(0);
        pixel.setBlue(2*avg);
        pixel.setGreen(0);
    
    }
    else{
        pixel.setBlue(255);
        pixel.setRed((2*avg)-255);
        pixel.setGreen((2*avg)-255);
    }
} 
var canvas = document.getElementById("can1");
imageblue.drawTo(canvas);
}


function makeGreen(){
var img = document.getElementById("finput");
for (var pixel of imagegreen.values()){   
    var r = pixel.getRed();
    var g = pixel.getGreen();
    var b = pixel.getBlue();
    var avg = (r+g+b)/3;
    if (avg<128){
        pixel.setGreen(2*avg);
        pixel.setRed(0);
        pixel.setBlue(0);
    }
    else{
        pixel.setGreen(255);
        pixel.setRed((2*avg)-255);
        pixel.setBlue((2*avg)-255);
    }} 
var canvas = document.getElementById("can1");
imagegreen.drawTo(canvas);
}


function jail(image){
var img = document.getElementById("finput");
for (var pixel of imagewin.values()){   
    var r= pixel.getRed();
    var g= pixel.getBlue();
    var b= pixel.getGreen()
    var xpix =pixel.getX();
    var ypix =pixel.getY();
    
    if (((xpix%80)<10) || ((ypix%50)<10)){
      pixel.setRed(0);
       pixel.setBlue(0);
       pixel.setGreen(0); 
   }
    else{
         pixel.setRed(r);
       pixel.setBlue(g);
       pixel.setGreen(b);
    }
       
   } 
  var canvas = document.getElementById("can1");
imagewin.drawTo(canvas);  
}


function pixelated(){
var img = document.getElementById("finput");
for (var pixel of imagepix.values()){
    var r= pixel.getRed();
    var g= pixel.getBlue();
    var b= pixel.getGreen()
   if ((Number.isInteger(pixel.getX()/2)) || (Number.isInteger(pixel.getY()/2))){
       pixel.setRed(r);
       pixel.setBlue(g);
       pixel.setGreen(b);
   }
    else{
       pixel.setRed(0);
       pixel.setBlue(0);
       pixel.setGreen(0);  
    }
       
   } 
    
 var canvas = document.getElementById("can1");
imagepix.drawTo(canvas);  
}


function pixelatedWhite(){
var img = document.getElementById("finput");
for (var pixel of imagewpix.values()){
    var r= pixel.getRed();
    var g= pixel.getBlue();
    var b= pixel.getGreen()
   if ((Number.isInteger(pixel.getX()/2)) || (Number.isInteger(pixel.getY()/2))){
       pixel.setRed(r);
       pixel.setBlue(g);
       pixel.setGreen(b);
   }
    else{
       pixel.setRed(255);
       pixel.setBlue(255);
       pixel.setGreen(255);  
    }
       
   } 
    
 var canvas = document.getElementById("can1");
imagewpix.drawTo(canvas);  
}


function makeRainbow(){
var img = document.getElementById("finput");
//var x= imagerain.getWidth()/7;
var y = imagerain.getHeight()/7;
for (var pixel of imagerain.values()){
    var c= pixel.getX();
    var a = pixel.getY();
    var avg = (pixel.getRed()+pixel.getBlue()+pixel.getGreen())/3
    //RED
    if (a<=y){
        if (avg<128){
            pixel.setRed(2*avg);
            pixel.setBlue(0);
            pixel.setGreen(0);
        }
        if (avg>=128){
          pixel.setRed(255);
          pixel.setGreen((2*avg)-255);
          pixel.setBlue((2*avg)-255);   
        }
            
    }
     //ORANGE
    if((a<=2*y) && (a>y)){
        if (avg<128){
            pixel.setRed(2*avg);
            pixel.setGreen(0.8*avg);
            pixel.setBlue(0);
        }
        if (avg>=128){
            pixel.setRed(255);
            pixel.setGreen((1.2*avg)-255);
            pixel.setBlue((2*avg)-255);
        }
    }
     //YELLOW
    if((a<=3*y) && (a>2*y)){
        if (avg<128){
            pixel.setRed(2*avg);
            pixel.setGreen(2*avg);
            pixel.setBlue(0);
        }
        if (avg>=128){
            pixel.setRed(255);
            pixel.setGreen(255);
            pixel.setBlue((2*avg)-255);
        }
    }
    //GREEN
    if((a<=4*y) && (a>3*y)){
        if (avg<128){
            pixel.setRed(0);
            pixel.setGreen(2*avg);
            pixel.setBlue(0);
        }
        if (avg>=128){
            pixel.setRed((2*avg)-255);
            pixel.setGreen(255);
            pixel.setBlue((2*avg)-255);
        }
    }
    //BLUE
    if((a<=5*y) && (a>4*y)){
        if (avg<128){
            pixel.setRed(0);
            pixel.setBlue(2*avg);
            pixel.setBlue(0);
        }
        if (avg>=128){
            pixel.setRed((2*avg)-255);
            pixel.setBlue(255);
            pixel.setGreen((2*avg)-255);
        }
    }
    //INDIGO
    if((a<=6*y) && (a>5*y)){
        if (avg<128){
            pixel.setRed(0.8*avg);
            pixel.setGreen(0);
            pixel.setBlue(2*avg);
        }
        if (avg>=128){
            pixel.setRed((1.2*avg)-51);
            pixel.setBlue(255);
            pixel.setGreen((2*avg)-255);
        }
    }
     //VIOLET
    if((a<=7*y) && (a>6*y)){
        if (avg<128){
            pixel.setRed(1.6*avg);
            pixel.setGreen(0);
            pixel.setBlue(1.6*avg);
        }
        if (avg>=128){
            pixel.setRed((0.4*avg)+153);
            pixel.setGreen((0.4*avg)+153);
            pixel.setBlue((2*avg)-255);
        }
    }
}    
var canvas = document.getElementById("can1");
imagerain.drawTo(canvas);  
}


function makeBlur() {
var img = document.getElementById("finput");
var width = imageblur.getWidth();
var height = imageblur.getHeight();
var blurimage = new SimpleImage(width, height);
  
  for (var pixel of imageblur.values()) {
    var num = Math.random();
    if (num < 0.5) {
      var x = pixel.getX();
      var y = pixel.getY();
      var pix = blurimage.getPixel(x, y);
      var red = pixel.getRed();
      var green = pixel.getGreen();
      var blue = pixel.getBlue();
      pix.setRed(red);
      pix.setGreen(green);
      pix.setBlue(blue);
    }
    else {
      var random1 = Math.floor(Math.random() * 5) + 1;
      var random2 = Math.floor(Math.random() * 5) + 1;
      var x = pixel.getX();
      var y = pixel.getY();
      var randomX = x - random1;
      var randomY = y - random2;
      if (randomX < 0) {
        randomX = 0;
      }
      if (randomY < 0) {
        randomY = 0;
      }
      var gtpix = imageblur.getPixel(randomX, randomY);
      var red = gtpix.getRed();
      var green = gtpix.getGreen();
      var blue = gtpix.getBlue();
      var stpix = blurimage.getPixel(x, y);
      stpix.setRed(red);
      stpix.setGreen(green);
      stpix.setBlue(blue);
    }
  }
var canvas = document.getElementById("can1");
blurimage.drawTo(canvas);  
}